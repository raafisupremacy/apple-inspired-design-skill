"""Validate the bundled starter tokens without third-party dependencies.

Checks: colors match what palette.py generates from the stored seed and strategy,
every contrast floor passes in both themes, tokens.css is exactly what the generator
renders from tokens.json, and the non-color scales are ordered and complete.
This covers this skill's own starter files only, never a user's project.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import palette  # noqa: E402

TYPE_ROLES = {"display", "title1", "title2", "title3", "eyebrow", "headline", "body",
              "callout", "subhead", "footnote", "caption"}
DURATIONS = ("fast", "base", "slow", "max", "reduced")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    tokens = json.loads((root / "assets" / "tokens.json").read_text(encoding="utf-8"))

    built = palette.build_palette(tokens["seed"], tokens["strategy"])
    expected_color = {key: built[key] for key in ("defaultTheme", "light", "dark", "ramp")}
    if tokens["color"] != expected_color:
        raise SystemExit("color tokens differ from palette.py output; run "
                         f"python scripts/palette.py \"{tokens['seed']}\" --strategy {tokens['strategy']} --write-starter")
    problems = palette.check_palette(built)
    if problems:
        raise SystemExit("contrast floors failed: " + "; ".join(problems))

    missing_roles = TYPE_ROLES - tokens["typography"]["scale"].keys()
    if missing_roles:
        raise SystemExit("missing type roles: " + ", ".join(sorted(missing_roles)))
    spacing = list(tokens["spacing"].values())
    if spacing != sorted(spacing) or len(set(spacing)) != len(spacing):
        raise SystemExit("spacing scale must be strictly ascending")
    radius = [value for name, value in tokens["radius"].items() if name != "pill"]
    if radius != sorted(radius):
        raise SystemExit("radius scale must be ascending")

    durations = tokens["motion"]["durationMs"]
    if any(not isinstance(durations.get(name), int) or durations[name] <= 0 for name in DURATIONS):
        raise SystemExit("motion durations must be positive integers: " + ", ".join(DURATIONS))
    if not durations["fast"] <= durations["base"] <= durations["slow"] <= durations["max"]:
        raise SystemExit("motion durations must be ordered fast <= base <= slow <= max")
    if durations["reduced"] >= durations["base"]:
        raise SystemExit("reduced motion duration must be shorter than base motion")
    for name, spec in tokens["motion"]["spring"].items():
        if not (0 < spec["response"] <= 1.5 and 0.3 <= spec["damping"] <= 1.0):
            raise SystemExit(f"spring {name} needs 0 < response <= 1.5 and 0.3 <= damping <= 1")

    css = (root / "assets" / "tokens.css").read_text(encoding="utf-8")
    if css != palette.render_starter_css(tokens):
        raise SystemExit("tokens.css drifted from tokens.json; run palette.py --write-starter")

    light = built["light"]
    print(f"tokens valid; seed {built['seed']} ({built['strategy']}), "
          f"text {palette.contrast(light['text'], light['bg']):.2f}:1, all contrast floors pass in light and dark")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
