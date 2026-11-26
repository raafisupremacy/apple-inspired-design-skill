# Agent integration

When this repository is installed as an agent skill, follow `SKILL.md` as the entry point.

## Operating protocol

1. Identify the mode, surface/platform, primary user task, and the artifact or project.
2. For new work, have the user fill in the intake form (`references/foundations/intake-form.md`) before visual work: pre-fill what the project answers, ask the missing fields (structured question tool if available, otherwise the text form), and wait. Never fill color, mood, theme, or core object with your own guesses, and never silently default to black, white, gray, or system blue.
3. Read the four core foundations (`references/foundations/principles.md`, `references/foundations/color.md`, `references/foundations/typography.md`, `references/foundations/layout.md`), then only the surface, stack, and quality references the task needs, using the routing table in `SKILL.md`.
4. Keep the project's existing stack and conventions. Do not add dependencies, fetch remote material, inspect unrelated files, or make external changes without an explicit request.
5. For implementation, preserve existing data and error handling; include states, responsive/platform behavior, accessibility, and motion.
6. Report visual decisions separately from technical checks, with evidence labels; mark anything inferred or unverified.

If the request is ambiguous, ask only for information that changes the design decision. Do not enter Enforce mode unless the user explicitly asks. Do not claim official Apple design, Apple endorsement, device testing, contrast validation, or performance results without evidence.

## Maintaining this skill

- After changing `scripts/palette.py` or `assets/tokens.json`: run `python scripts/palette.py "<seed>" --strategy <s> --write-starter`, then `python scripts/validate_tokens.py` and `python -m unittest discover -s tests`.
- After adding, moving, or renaming references: run `python scripts/check_references.py` and update the routing table in `SKILL.md`.
- When improving the skill from real projects, follow the transfer process in `references/quality/review-and-evidence.md`: prefer adding craft knowledge, recipes, and examples over adding reporting rules, and update the owning reference instead of duplicating guidance.
- Use `evals/README.md` to compare outputs before and after a change.
