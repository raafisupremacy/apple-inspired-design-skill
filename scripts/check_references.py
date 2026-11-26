"""Check that every local file reference in the skill's Markdown exists.

Covers Markdown links ``[text](path)`` and code-formatted paths such as
``../foundations/color.md`` or ``scripts/palette.py``. A code-formatted path is
valid when it exists relative to the document or to the repository root.
CHANGELOG.md is skipped: it records files and paths from earlier versions.
"""

from pathlib import Path
import re

CODE_PATH = re.compile(r"`((?:\.\./|[\w-]+/)*[\w.-]+\.(?:md|py|json|css|html|yaml))`")


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    missing = []
    checked = 0
    for document in root.rglob("*.md"):
        parts = document.relative_to(root).parts
        if ".git" in parts or parts == ("CHANGELOG.md",):
            continue
        text = document.read_text(encoding="utf-8")
        for target in re.findall(r"\]\(([^)]+)\)", text):
            target = target.split("#", 1)[0].strip()
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target):
                continue
            checked += 1
            if not (document.parent / target).is_file():
                missing.append(f"{document.relative_to(root)} -> {target}")
        for target in CODE_PATH.findall(text):
            checked += 1
            if not ((document.parent / target).is_file() or (root / target).is_file()):
                missing.append(f"{document.relative_to(root)} -> `{target}`")
    if missing:
        raise SystemExit("missing references:\n  " + "\n  ".join(missing))
    print(f"references valid; checked {checked} local references")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
