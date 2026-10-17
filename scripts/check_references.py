"""Check that every local Markdown reference in the skill exists."""

from pathlib import Path
import re


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []
    checked = 0
    for document in root.rglob("*.md"):
        if ".git" in document.parts:
            continue
        text = document.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            checked += 1
            if not (document.parent / target).is_file():
                missing.append(f"{document.relative_to(root)} -> {target}")
    if missing:
        raise SystemExit("missing references: " + ", ".join(missing))
    print(f"references valid; checked {checked} local links")


if __name__ == "__main__":
    main()
