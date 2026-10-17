"""Validate the bundled starter tokens without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path

REQUIRED = {
    "bg", "surface", "surfaceElevated", "separator", "text", "textSecondary",
    "textTertiary", "textInverse", "accent", "accentHover", "accentPressed", "accentSoft",
    "focus", "success", "warning", "danger",
}
MOTION_REQUIRED = {"fastMs", "baseMs", "slowMs", "maxMs", "reducedMs"}


def luminance(hex_color: str) -> float:
    value = hex_color.lstrip("#")
    if len(value) != 6 or not re.fullmatch(r"[0-9a-fA-F]{6}", value):
        raise ValueError(f"invalid color: {hex_color}")
    channels = [int(value[i:i + 2], 16) / 255 for i in (0, 2, 4)]
    channels = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4 for c in channels]
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]


def contrast(first: str, second: str) -> float:
    a, b = luminance(first), luminance(second)
    return (max(a, b) + 0.05) / (min(a, b) + 0.05)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    colors = json.loads((root / "assets" / "tokens.json").read_text(encoding="utf-8"))["color"]
    missing = REQUIRED - colors.keys()
    if missing:
        raise SystemExit(f"missing color tokens: {', '.join(sorted(missing))}")
    for name, value in colors.items():
        if not isinstance(value, str):
            raise SystemExit(f"color token is not a string: {name}")
        luminance(value)
    motion = json.loads((root / "assets" / "tokens.json").read_text(encoding="utf-8"))["motion"]
    missing_motion = MOTION_REQUIRED - motion.keys()
    if missing_motion:
        raise SystemExit(f"missing motion tokens: {', '.join(sorted(missing_motion))}")
    if any(not isinstance(motion[name], int) or motion[name] <= 0 for name in MOTION_REQUIRED):
        raise SystemExit("motion tokens must be positive integers")
    if not motion["fastMs"] <= motion["baseMs"] <= motion["slowMs"] <= motion["maxMs"]:
        raise SystemExit("motion durations must be ordered fast <= base <= slow <= max")
    if motion["reducedMs"] >= motion["baseMs"]:
        raise SystemExit("reduced motion duration must be shorter than base motion")
    css = (root / "assets" / "tokens.css").read_text(encoding="utf-8")
    css_colors = set(re.findall(r"--color-([a-z-]+):", css))
    expected_css_colors = {
        re.sub(r"([A-Z])", lambda match: "-" + match.group(1).lower(), name)
        for name in colors
    }
    if css_colors != expected_css_colors:
        missing_css = sorted(expected_css_colors - css_colors)
        extra_css = sorted(css_colors - expected_css_colors)
        details = []
        if missing_css:
            details.append("missing CSS colors: " + ", ".join(missing_css))
        if extra_css:
            details.append("extra CSS colors: " + ", ".join(extra_css))
        raise SystemExit("color token parity failed; " + "; ".join(details))
    for name in REQUIRED:
        kebab = re.sub(r"([A-Z])", lambda match: "-" + match.group(1).lower(), name)
        if f"--color-{kebab}:" not in css:
            raise SystemExit(f"missing CSS token: {name}")
    for name in ("motion-fast", "motion-base", "motion-slow", "motion-max", "motion-reduced"):
        if f"--{name}:" not in css:
            raise SystemExit(f"missing CSS motion token: {name}")
    ratio = contrast(colors["text"], colors["bg"])
    if ratio < 4.5:
        raise SystemExit(f"primary text contrast is {ratio:.2f}:1; need at least 4.5:1")
    print(f"tokens valid; primary text contrast {ratio:.2f}:1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
