# Agent integration

When this repository is installed as an agent skill, follow `SKILL.md` as the entry point.

- Load `references/core-principles.md` first.
- Use `references/design-reasoning.md` to resolve product and interaction trade-offs before visual polish.
- Use `references/brand-adaptation.md` for brand colors, assets, type, tone, and signature choices.
- Use `references/anti-patterns.md` when auditing generic or overdecorated UI.
- Use the matching section of `references/domain-recipes.md` when the product domain is explicit.
- Route to the smallest relevant set of platform and topic references.
- For reviews, report What / Why / Fix / Evidence and prioritize by user impact.
- For builds, define hierarchy and tokens before composing components, then add states, motion, and verification.
- Use `references/motion.md` for any animation or gesture request.
- Use `references/user-assets.md` for supplied media and keep original assets intact.
- Run `scripts/validate_tokens.py` after token changes and `scripts/check_references.py` after routing changes.
- Do not claim Apple endorsement, device testing, contrast validation, or performance results without evidence.
- Do not enter Enforce mode unless the user explicitly asks for it.
