"""Generate an accessible light/dark palette from any seed color.

Standard library only. The seed is kept exactly as the ``brand`` role; UI roles
are derived in OKLCH and adjusted only as far as needed to meet contrast floors.

Usage:
    python scripts/palette.py "#F2643A"                       # CSS + contrast report
    python scripts/palette.py "#F2643A" --strategy vivid --format swiftui
    python scripts/palette.py "#F2643A" --write-starter      # rebuild assets/tokens.*

Strategies (see references/foundations/color.md):
    neutral    quiet gray foundation, color only in accent and content
    tinted     neutrals carry a whisper of the seed hue (default)
    vivid      surfaces are visibly colored; for expressive consumer products
    immersive  dark-first, deep tinted background; for media, fitness, night use
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from pathlib import Path

ROLES = (
    "bg", "surface", "surfaceElevated", "separator",
    "text", "textSecondary", "textTertiary", "textInverse",
    "brand", "accent", "accentHover", "accentPressed", "accentSoft", "onAccent",
    "link", "focus", "success", "warning", "danger", "info",
)
STRATEGIES = ("neutral", "tinted", "vivid", "immersive")
RAMP_STEPS = ("50", "100", "200", "300", "400", "500", "600", "700", "800", "900", "950")

# (lightness, max chroma) for bg, surface, surfaceElevated, separator per theme.
_SURFACES = {
    "neutral": {
        "light": [(0.972, 0.002), (0.995, 0.001), (1.0, 0.0), (0.905, 0.003)],
        "dark": [(0.165, 0.003), (0.215, 0.003), (0.265, 0.003), (0.33, 0.004)],
    },
    "tinted": {
        "light": [(0.968, 0.014), (0.993, 0.005), (0.998, 0.002), (0.9, 0.016)],
        "dark": [(0.175, 0.014), (0.225, 0.016), (0.275, 0.018), (0.34, 0.018)],
    },
    "vivid": {
        "light": [(0.94, 0.045), (0.985, 0.014), (0.995, 0.006), (0.88, 0.05)],
        "dark": [(0.2, 0.045), (0.25, 0.05), (0.3, 0.05), (0.37, 0.05)],
    },
    "immersive": {
        "light": [(0.968, 0.014), (0.993, 0.005), (0.998, 0.002), (0.9, 0.016)],
        "dark": [(0.13, 0.025), (0.19, 0.03), (0.245, 0.032), (0.32, 0.03)],
    },
}
_SEMANTIC_HUES = {"success": (150, 0.16), "warning": (70, 0.15), "danger": (27, 0.19), "info": (245, 0.14)}
FLOORS = {"text": 7.0, "textSecondary": 4.5, "textTertiary": 3.0, "link": 4.5,
          "success": 4.5, "warning": 4.5, "danger": 4.5, "info": 4.5}
ON_ACCENT_FLOOR = 4.5


# ---------------------------------------------------------------- color math

def parse_hex(value: str) -> str:
    """Return a normalized ``#rrggbb`` string or raise ValueError."""
    if not isinstance(value, str):
        raise ValueError(f"invalid color: {value!r}")
    raw = value.strip().lstrip("#")
    if re.fullmatch(r"[0-9a-fA-F]{3}", raw):
        raw = "".join(ch * 2 for ch in raw)
    if not re.fullmatch(r"[0-9a-fA-F]{6}", raw):
        raise ValueError(f"invalid color: {value!r} (use #rrggbb or #rgb)")
    return "#" + raw.lower()


def _to_linear(channel: float) -> float:
    return channel / 12.92 if channel <= 0.04045 else ((channel + 0.055) / 1.055) ** 2.4


def _to_gamma(channel: float) -> float:
    return 12.92 * channel if channel <= 0.0031308 else 1.055 * channel ** (1 / 2.4) - 0.055


def _hex_to_linear(value: str) -> tuple[float, float, float]:
    value = parse_hex(value)
    return tuple(_to_linear(int(value[i:i + 2], 16) / 255) for i in (1, 3, 5))  # type: ignore[return-value]


def hex_to_oklch(value: str) -> tuple[float, float, float]:
    r, g, b = _hex_to_linear(value)
    l_ = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m_ = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s_ = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = (math.copysign(abs(x) ** (1 / 3), x) for x in (l_, m_, s_))
    lightness = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    chroma = math.hypot(a, bb)
    hue = math.degrees(math.atan2(bb, a)) % 360 if chroma > 1e-6 else 0.0
    return lightness, chroma, hue


def _oklch_to_linear(lightness: float, chroma: float, hue: float) -> tuple[float, float, float]:
    a = chroma * math.cos(math.radians(hue))
    b = chroma * math.sin(math.radians(hue))
    l_ = (lightness + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m_ = (lightness - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s_ = (lightness - 0.0894841775 * a - 1.2914855480 * b) ** 3
    return (
        4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
        -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
        -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_,
    )


def _in_gamut(rgb: tuple[float, float, float]) -> bool:
    return all(-1e-4 <= ch <= 1 + 1e-4 for ch in rgb)


def oklch_to_hex(lightness: float, chroma: float, hue: float) -> str:
    """Convert OKLCH to sRGB hex, reducing chroma until the color is in gamut."""
    lightness = min(max(lightness, 0.0), 1.0)
    chroma = max(chroma, 0.0)
    rgb = _oklch_to_linear(lightness, chroma, hue)
    if not _in_gamut(rgb):
        low, high = 0.0, chroma
        for _ in range(24):
            mid = (low + high) / 2
            if _in_gamut(_oklch_to_linear(lightness, mid, hue)):
                low = mid
            else:
                high = mid
        rgb = _oklch_to_linear(lightness, low, hue)
    return "#" + "".join(f"{round(min(max(_to_gamma(min(max(ch, 0.0), 1.0)), 0.0), 1.0) * 255):02x}" for ch in rgb)


def luminance(value: str) -> float:
    r, g, b = _hex_to_linear(value)
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast(first: str, second: str) -> float:
    a, b = luminance(first), luminance(second)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


# ---------------------------------------------------------------- derivation

def _fit(lightness: float, chroma: float, hue: float, against: list[str], target: float, direction: int) -> str:
    """Move lightness in ``direction`` until contrast against every color meets ``target``."""
    current = lightness
    while True:
        candidate = oklch_to_hex(current, chroma, hue)
        if min(contrast(candidate, other) for other in against) >= target:
            return candidate
        if current <= 0.0 or current >= 1.0:
            return candidate
        current = min(max(current + 0.005 * direction, 0.0), 1.0)


def _accent_set(l: float, c: float, h: float, bg: str, theme: str) -> dict[str, str]:
    accent = oklch_to_hex(l, c, h)
    # Keep the fill visible when a near-gray seed (white, black, gray) disappears into the page.
    # Chromatic seeds keep their hue and lightness; their labels carry the control.
    if (c < 0.04 and contrast(accent, bg) < 1.3) or contrast(accent, bg) < 1.1:
        accent = _fit(l, c, h, [bg], 3.0, -1 if theme == "light" else 1)
    l, c, h = hex_to_oklch(accent)
    light_text = oklch_to_hex(0.995, min(c * 0.05, 0.005), h)
    dark_text = oklch_to_hex(0.18, min(c * 0.2, 0.03), h)
    on_accent = light_text if contrast(light_text, accent) >= contrast(dark_text, accent) else dark_text
    direction = -1 if on_accent == light_text else 1
    if contrast(on_accent, accent) < ON_ACCENT_FLOOR:
        accent = _fit(l, c, h, [on_accent], ON_ACCENT_FLOOR, direction)
        l, c, h = hex_to_oklch(accent)

    # Interaction states dim in light themes and brighten in dark themes, as long as the label
    # keeps its contrast; otherwise they move the other way.
    preferred = -1 if theme == "light" else 1

    def shifted(step: float) -> str:
        for sign in (preferred, -preferred):
            for scale in (1.0, 0.8, 0.6):
                target = l + sign * step * scale
                if 0.02 <= target <= 0.99:
                    candidate = oklch_to_hex(target, c, h)
                    if contrast(on_accent, candidate) >= ON_ACCENT_FLOOR:
                        return candidate
        return _fit(l + direction * step, c, h, [on_accent], ON_ACCENT_FLOOR, direction)

    return {"accent": accent, "accentHover": shifted(0.035), "accentPressed": shifted(0.07), "onAccent": on_accent}


def _theme(seed: str, strategy: str, theme: str) -> dict[str, str]:
    sl, sc, sh = hex_to_oklch(seed)
    lighter_text = 1 if theme == "dark" else -1  # direction that increases text contrast
    surfaces = []
    for lightness, max_chroma in _SURFACES[strategy][theme]:
        surfaces.append(oklch_to_hex(lightness, min(max_chroma, sc), sh))
    bg, surface, elevated, separator = surfaces
    grounds = [bg, surface, elevated]
    text_c = min(0.02, sc * 0.15)
    starts = {"light": (0.2, 0.48, 0.6), "dark": (0.965, 0.78, 0.64)}[theme]

    roles: dict[str, str] = {"bg": bg, "surface": surface, "surfaceElevated": elevated, "separator": separator}
    roles["text"] = _fit(starts[0], text_c, sh, grounds, FLOORS["text"], lighter_text)
    roles["textSecondary"] = _fit(starts[1], text_c, sh, grounds, FLOORS["textSecondary"], lighter_text)
    roles["textTertiary"] = _fit(starts[2], text_c, sh, grounds, FLOORS["textTertiary"], lighter_text)
    roles["textInverse"] = oklch_to_hex(0.99 if theme == "light" else 0.17, min(0.005, sc), sh)
    roles["brand"] = seed

    al, ac, ah = sl, sc, sh
    if theme == "dark" and al < 0.62:
        al = 0.66
    roles.update(_accent_set(al, ac, ah, bg, theme))

    soft = (0.935, min(sc * 0.3, 0.05)) if theme == "light" else (0.3, min(sc * 0.4, 0.07))
    roles["accentSoft"] = oklch_to_hex(soft[0], soft[1], sh)
    link_start = hex_to_oklch(roles["accent"])
    roles["link"] = _fit(link_start[0], link_start[1], link_start[2], grounds + [roles["accentSoft"]],
                         FLOORS["link"], lighter_text)
    roles["focus"] = roles["link"]
    for name, (hue, chroma) in _SEMANTIC_HUES.items():
        start = 0.55 if theme == "light" else 0.76
        roles[name] = _fit(start, chroma, hue, grounds, FLOORS[name], lighter_text)
    return {role: roles[role] for role in ROLES}


def build_palette(seed: str, strategy: str = "tinted") -> dict:
    """Return seed, strategy, default theme, light/dark roles, and an 11-step brand ramp."""
    seed = parse_hex(seed)
    if strategy not in STRATEGIES:
        raise ValueError(f"unknown strategy {strategy!r}; choose one of {', '.join(STRATEGIES)}")
    sl, sc, sh = hex_to_oklch(seed)
    ramp_l = (0.97, 0.93, 0.87, 0.78, 0.69, 0.6, 0.51, 0.43, 0.35, 0.27, 0.2)
    ramp_c = (0.25, 0.4, 0.6, 0.8, 0.95, 1.0, 0.95, 0.85, 0.7, 0.55, 0.4)
    ramp = {step: oklch_to_hex(l, sc * k, sh) for step, l, k in zip(RAMP_STEPS, ramp_l, ramp_c)}
    return {
        "seed": seed,
        "strategy": strategy,
        "defaultTheme": "dark" if strategy == "immersive" else "light",
        "light": _theme(seed, strategy, "light"),
        "dark": _theme(seed, strategy, "dark"),
        "ramp": ramp,
    }


def check_palette(palette: dict) -> list[str]:
    """Return human-readable contrast failures; an empty list means every floor passes."""
    problems = []
    for theme in ("light", "dark"):
        roles = palette[theme]
        grounds = {name: roles[name] for name in ("bg", "surface", "surfaceElevated")}
        for role, floor in FLOORS.items():
            backgrounds = dict(grounds)
            if role == "link":
                backgrounds["accentSoft"] = roles["accentSoft"]
            for ground_name, ground in backgrounds.items():
                ratio = contrast(roles[role], ground)
                if ratio + 1e-9 < floor:
                    problems.append(f"{theme}: {role} on {ground_name} is {ratio:.2f}:1, needs {floor}:1")
        for fill in ("accent", "accentHover", "accentPressed"):
            ratio = contrast(roles["onAccent"], roles[fill])
            if ratio + 1e-9 < ON_ACCENT_FLOOR:
                problems.append(f"{theme}: onAccent on {fill} is {ratio:.2f}:1, needs {ON_ACCENT_FLOOR}:1")
        if roles["brand"] != palette["seed"]:
            problems.append(f"{theme}: brand role must equal the seed")
    return problems


def report(palette: dict) -> str:
    lines = [f"Palette for {palette['seed']} ({palette['strategy']}, default {palette['defaultTheme']} theme)"]
    for theme in ("light", "dark"):
        roles = palette[theme]
        lines.append(f"\n{theme}:")
        for role in ("text", "textSecondary", "textTertiary", "link", "success", "warning", "danger", "info"):
            lines.append(f"  {role:<14} {roles[role]}  {contrast(roles[role], roles['bg']):5.2f}:1 on bg")
        lines.append(f"  {'onAccent':<14} {roles['onAccent']}  {contrast(roles['onAccent'], roles['accent']):5.2f}:1 on accent {roles['accent']}")
        visibility = contrast(roles["accent"], roles["bg"])
        if visibility < 3.0:
            lines.append(f"  note: accent fill is {visibility:.2f}:1 against bg; give filled controls a label "
                         "(always) and consider a border or a darker surface behind large fills.")
    l, c, _ = hex_to_oklch(palette["seed"])
    if c < 0.03:
        lines.append("\nnote: the seed is nearly gray, so the palette is effectively neutral. "
                     "Pick a hue if the product needs a color story.")
    problems = check_palette(palette)
    lines.append("\ncontrast floors: " + ("all pass" if not problems else "; ".join(problems)))
    return "\n".join(lines)


# ---------------------------------------------------------------- renderers

def _kebab(name: str) -> str:
    return re.sub(r"([A-Z])", lambda m: "-" + m.group(1).lower(), name)


def _camel_upper(name: str) -> str:
    return name[0].upper() + name[1:]


def _css_block(selector: str, roles: dict[str, str], scheme: str, indent: str = "") -> list[str]:
    lines = [f"{indent}{selector} {{", f"{indent}  color-scheme: {scheme};"]
    lines += [f"{indent}  --color-{_kebab(role)}: {roles[role]};" for role in ROLES]
    lines.append(f"{indent}}}")
    return lines


def render_css(palette: dict) -> str:
    base_theme = palette["defaultTheme"]
    other = "light" if base_theme == "dark" else "dark"
    lines = [f"/* Generated by palette.py: seed {palette['seed']}, strategy {palette['strategy']}. */"]
    lines += _css_block(":root", palette[base_theme], "light dark" if base_theme == "light" else "dark")
    lines.insert(2, "  " + "\n  ".join(f"--brand-{step}: {value};" for step, value in palette["ramp"].items()))
    if base_theme == "light":
        lines.append("")
        lines.append("@media (prefers-color-scheme: dark) {")
        lines += _css_block(':root:not([data-theme="light"])', palette["dark"], "dark", "  ")
        lines.append("}")
    lines.append("")
    lines += _css_block(f':root[data-theme="{other}"]', palette[other], other)
    lines.append("")
    lines += _css_block(f':root[data-theme="{base_theme}"]', palette[base_theme], base_theme)
    return "\n".join(lines) + "\n"


def render_json(palette: dict) -> str:
    return json.dumps(palette, indent=2) + "\n"


def render_tailwind(palette: dict) -> str:
    colors = {role: f"var(--color-{_kebab(role)})" for role in ROLES}
    colors["brandScale"] = dict(palette["ramp"])
    body = json.dumps(colors, indent=2).replace("\n", "\n    ")
    return (
        f"// Generated by palette.py: seed {palette['seed']}, strategy {palette['strategy']}.\n"
        "// Load the CSS output first; these names resolve to its variables, so light/dark switch automatically.\n"
        "// Tailwind v4: declare the same names in `@theme inline { --color-bg: var(--color-bg); ... }` instead.\n"
        "module.exports = {\n  theme: {\n    extend: {\n      colors: " + body.replace("\n", "\n    ") +
        "\n    },\n  },\n};\n"
    )


def _hex_int(value: str) -> str:
    return "0x" + value[1:].upper()


def render_swiftui(palette: dict) -> str:
    lines = [
        f"// Generated by palette.py: seed {palette['seed']}, strategy {palette['strategy']}.",
        "// Prefer system colors for system chrome; use these for brand and content roles.",
        "// For production, the same values can live in an asset catalog with Any/Dark appearances.",
        "import SwiftUI",
        "#if canImport(UIKit)",
        "import UIKit",
        "#elseif canImport(AppKit)",
        "import AppKit",
        "#endif",
        "",
        "private extension Color {",
        "    init(hex: UInt32) {",
        "        self.init(red: Double((hex >> 16) & 0xFF) / 255,",
        "                  green: Double((hex >> 8) & 0xFF) / 255,",
        "                  blue: Double(hex & 0xFF) / 255)",
        "    }",
        "",
        "    static func dynamic(light: UInt32, dark: UInt32) -> Color {",
        "        #if canImport(UIKit)",
        "        return Color(UIColor { $0.userInterfaceStyle == .dark",
        "            ? UIColor(Color(hex: dark)) : UIColor(Color(hex: light)) })",
        "        #elseif canImport(AppKit)",
        "        return Color(NSColor(name: nil) { $0.bestMatch(from: [.darkAqua, .aqua]) == .darkAqua",
        "            ? NSColor(Color(hex: dark)) : NSColor(Color(hex: light)) })",
        "        #else",
        "        return Color(hex: light)",
        "        #endif",
        "    }",
        "}",
        "",
        "enum AppColor {",
    ]
    for role in ROLES:
        lines.append(f"    static let {role} = Color.dynamic(light: {_hex_int(palette['light'][role])}, "
                     f"dark: {_hex_int(palette['dark'][role])})")
    lines.append("}")
    return "\n".join(lines) + "\n"


def render_compose(palette: dict) -> str:
    def obj(name: str, roles: dict[str, str]) -> list[str]:
        out = [f"object {name} {{"]
        out += [f"    val {role} = Color(0xFF{roles[role][1:].upper()})" for role in ROLES]
        return out + ["}", ""]

    def scheme(fn: str, name: str, ref: str) -> list[str]:
        return [
            f"val {name} = {fn}(",
            f"    primary = {ref}.accent,", f"    onPrimary = {ref}.onAccent,",
            f"    primaryContainer = {ref}.accentSoft,", f"    onPrimaryContainer = {ref}.link,",
            f"    background = {ref}.bg,", f"    onBackground = {ref}.text,",
            f"    surface = {ref}.surface,", f"    onSurface = {ref}.text,",
            f"    surfaceVariant = {ref}.surfaceElevated,", f"    onSurfaceVariant = {ref}.textSecondary,",
            f"    outline = {ref}.separator,", f"    outlineVariant = {ref}.separator,",
            f"    error = {ref}.danger,",
            ")", "",
        ]

    lines = [
        f"// Generated by palette.py: seed {palette['seed']}, strategy {palette['strategy']}.",
        "// Replace the package name. Material roles keep platform components coherent;",
        "// the App* objects expose every semantic role for custom surfaces.",
        "package com.example.ui.theme",
        "",
        "import androidx.compose.material3.darkColorScheme",
        "import androidx.compose.material3.lightColorScheme",
        "import androidx.compose.ui.graphics.Color",
        "",
    ]
    lines += obj("AppColorsLight", palette["light"]) + obj("AppColorsDark", palette["dark"])
    lines += scheme("lightColorScheme", "AppLightColorScheme", "AppColorsLight")
    lines += scheme("darkColorScheme", "AppDarkColorScheme", "AppColorsDark")
    return "\n".join(lines)


def render_flutter(palette: dict) -> str:
    def on_color(fill: str) -> str:
        return "0xFFFFFFFF" if contrast("#ffffff", fill) >= contrast("#111111", fill) else "0xFF111111"

    def block(theme: str) -> list[str]:
        roles = palette[theme]
        cls = "AppColors" + _camel_upper(theme)
        out = [f"abstract final class {cls} {{"]
        out += [f"  static const {role} = Color(0xFF{roles[role][1:].upper()});" for role in ROLES]
        out += ["}", ""]
        out += [
            f"const {theme}ColorScheme = ColorScheme(",
            f"  brightness: Brightness.{theme},",
            f"  primary: {cls}.accent,", f"  onPrimary: {cls}.onAccent,",
            f"  secondary: {cls}.accentSoft,", f"  onSecondary: {cls}.link,",
            f"  error: {cls}.danger,", f"  onError: Color({on_color(roles['danger'])}),",
            f"  surface: {cls}.surface,", f"  onSurface: {cls}.text,",
            f"  outline: {cls}.separator,",
            ");", "",
        ]
        return out

    lines = [
        f"// Generated by palette.py: seed {palette['seed']}, strategy {palette['strategy']}.",
        "// Use with ThemeData(colorScheme: lightColorScheme) and darkTheme: ThemeData(colorScheme: darkColorScheme).",
        "import 'package:flutter/material.dart';",
        "",
    ]
    return "\n".join(lines + block("light") + block("dark"))


# ---------------------------------------------------------------- starter tokens

def spring_curve(response: float, damping: float, samples: int = 32) -> tuple[str, int]:
    """Approximate a spring step response as a CSS ``linear()`` easing plus its settle duration (ms).

    ``response`` and ``damping`` follow the common response/damping-fraction parameterization.
    This is a calibrated approximation for the web, not Apple's internal curve.
    """
    omega = 2 * math.pi / response

    def position(t: float) -> float:
        if damping >= 1:
            return 1 - math.exp(-omega * t) * (1 + omega * t)
        damped = omega * math.sqrt(1 - damping ** 2)
        return 1 - math.exp(-damping * omega * t) * (
            math.cos(damped * t) + (damping * omega / damped) * math.sin(damped * t))

    settle, t = 0.0, 0.0
    while t < 3.0:
        if abs(1 - position(t)) > 0.002:
            settle = t
        t += 0.001
    settle = max(settle, 0.05)
    points = []
    for i in range(samples + 1):
        progress = i / samples
        points.append(f"{round(position(progress * settle), 3):g}")
    points[-1] = "1"
    return f"linear({', '.join(points)})", round(settle * 1000)


def render_starter_css(tokens: dict) -> str:
    """Render assets/tokens.css from assets/tokens.json (colors plus non-color tokens)."""
    palette = {key: tokens[key] for key in ("seed", "strategy")}
    palette.update(tokens["color"])
    lines = [
        "/* Starter tokens. Generated from assets/tokens.json by scripts/palette.py --write-starter. */",
        f"/* The sample seed {tokens['seed']} is an example, not a default brand: replace it with the user's color. */",
        "",
        render_css(palette).rstrip("\n").split("\n", 1)[1],
        "",
        ":root {",
    ]
    for name, value in tokens["radius"].items():
        lines.append(f"  --radius-{name}: {value}px;")
    for name, value in tokens["spacing"].items():
        lines.append(f"  --space-{name}: {value}px;")
    type_tokens = tokens["typography"]
    for name in ("sans", "display", "rounded", "mono"):
        lines.append(f"  --font-{name}: {type_tokens['font'][name]};")
    for role, spec in type_tokens["scale"].items():
        for prop in ("size", "leading", "tracking", "weight"):
            lines.append(f"  --text-{_kebab(role)}-{prop}: {spec[prop]};")
    for name, value in tokens["layout"].items():
        lines.append(f"  --layout-{_kebab(name)}: {value}px;")
    for name, value in tokens["elevation"].items():
        lines.append(f"  --elevation-{name}: {value};")
    motion = tokens["motion"]
    for name, value in motion["durationMs"].items():
        lines.append(f"  --motion-{name}: {value}ms;")
    for name, value in motion["easing"].items():
        lines.append(f"  --ease-{name}: {value};")
    for name, spec in motion["spring"].items():
        curve, duration = spring_curve(spec["response"], spec["damping"])
        lines.append(f"  --spring-{name}: {curve};")
        lines.append(f"  --spring-{name}-duration: {duration}ms;")
    for name, value in motion.get("press", {}).items():
        lines.append(f"  --press-{name}: {value};")
    lines.append("}")
    return "\n".join(lines) + "\n"


def write_starter(seed: str, strategy: str, root: Path) -> None:
    path = root / "assets" / "tokens.json"
    tokens = json.loads(path.read_text(encoding="utf-8"))
    built = build_palette(seed, strategy)
    tokens["seed"], tokens["strategy"] = built["seed"], built["strategy"]
    tokens["color"] = {key: built[key] for key in ("defaultTheme", "light", "dark", "ramp")}
    path.write_text(json.dumps(tokens, indent=2) + "\n", encoding="utf-8")
    (root / "assets" / "tokens.css").write_text(render_starter_css(tokens), encoding="utf-8")


RENDERERS = {
    "css": render_css, "json": render_json, "tailwind": render_tailwind,
    "swiftui": render_swiftui, "compose": render_compose, "flutter": render_flutter, "report": report,
}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Generate accessible light/dark tokens from a seed color.")
    parser.add_argument("seed", help="brand or chosen color, e.g. #F2643A")
    parser.add_argument("--strategy", choices=STRATEGIES, default="tinted")
    parser.add_argument("--format", choices=tuple(RENDERERS), default=None,
                        help="output format; default prints CSS followed by the contrast report")
    parser.add_argument("--write-starter", action="store_true",
                        help="rewrite this skill's assets/tokens.json and tokens.css (skill maintenance only)")
    args = parser.parse_args(argv)
    try:
        built = build_palette(args.seed, args.strategy)
    except ValueError as error:
        parser.error(str(error))
    if args.write_starter:
        write_starter(args.seed, args.strategy, Path(__file__).resolve().parents[1])
        print("wrote assets/tokens.json and assets/tokens.css")
        return 0
    if args.format:
        sys.stdout.write(RENDERERS[args.format](built))
        if args.format == "report":
            sys.stdout.write("\n")
    else:
        sys.stdout.write(render_css(built) + "\n" + report(built) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
