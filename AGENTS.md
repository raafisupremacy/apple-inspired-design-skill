# Agent integration

When this repository is installed as an agent skill, follow `SKILL.md` as the entry point.

## Operating protocol

1. Identify the mode, platform, primary user task, and the artifact or project being discussed.
2. Read `references/core-principles.md`, then route only the references needed for that task.
3. Resolve product, audience, content, brand, and platform trade-offs before visual polish.
4. Keep the project’s existing stack and conventions. Do not add dependencies, fetch remote material, inspect unrelated files, or make external changes without an explicit request.
5. For implementation, preserve existing data and error handling; include relevant states, responsive/platform behavior, accessibility, and motion.
6. Report changes or recommendations with evidence and clearly label anything inferred or unverified.

If the request is ambiguous, ask only for information that changes the design decision. If the request is outside the available artifact or selected project, state the boundary instead of guessing.

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
- Treat domain recipes as optional starting points; use the custom-domain reasoning path when none fits.
- Do not claim the result is official Apple design, device-tested, performance-tested, or accessibility-certified without evidence.
