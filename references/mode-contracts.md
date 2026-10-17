# Mode contracts

## Advise

Return the recommended decision first, the reason tied to the user task second, and alternatives only when they change an important trade-off. Mention assumptions that affect the recommendation.

## Review

Return a short prioritized report. Every finding has What, Why, Fix, and Evidence or Limitation. Separate blockers from polish. Do not turn taste into a violation.

## Design

Return a platform and task summary, information hierarchy, layout/composition, semantic tokens, component decisions, interaction states, motion choreography, accessibility/localization notes, and a verification checklist. Include responsive or platform adaptations rather than duplicate screens with no rationale.

## Implement

Inspect the existing project first. Reuse its components and dependencies. Make the smallest complete change, preserve data and error handling, and do a proportionate verification pass. Report files changed, checks run, and anything unverified; do not build a testing system unless the user asks for one.

## Enforce

Use only after explicit request. Establish the scope and pass criteria, inspect the artifact, fix only in-scope issues, and re-review. Stop after a bounded number of cycles or when progress requires product decisions. Never imply certification or App Store/WCAG conformance without the required evidence.
