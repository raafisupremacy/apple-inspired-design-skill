"""Validate the bundled starter tokens without third-party dependencies."""

from __future__ import annotations

import json
import re
from pathlib import Path

REQUIRED = {
    "bg", "surface", "surfaceElevated", "separator", "text", "textSecondary",
    "textTertiary", "accent", "accentHover", "accentPressed", "accentSoft",
    "success", "warning", "danger",
}


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
    css = (root / "assets" / "tokens.css").read_text(encoding="utf-8")
    for name in REQUIRED:
        kebab = re.sub(r"([A-Z])", lambda match: "-" + match.group(1).lower(), name)
        if f"--color-{kebab}:" not in css:
            raise SystemExit(f"missing CSS token: {name}")
    ratio = contrast(colors["text"], colors["bg"])
    if ratio < 4.5:
        raise SystemExit(f"primary text contrast is {ratio:.2f}:1; need at least 4.5:1")
    print(f"tokens valid; primary text contrast {ratio:.2f}:1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
