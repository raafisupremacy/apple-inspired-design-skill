"""Check that every local reference linked from the skill exists."""

from pathlib import Path
import re


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    text = (root / "SKILL.md").read_text(encoding="utf-8")
    paths = re.findall(r"\]\((references/[^)]+)\)", text)
    missing = [path for path in paths if not (root / path).is_file()]
    if missing:
        raise SystemExit("missing references: " + ", ".join(missing))
    print(f"references valid; checked {len(paths)} local links")


if __name__ == "__main__":
    main()
