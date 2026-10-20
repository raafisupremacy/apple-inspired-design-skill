# Mode contracts

Every mode must identify the platform and primary user task, state assumptions that affect the decision, and separate source evidence, screenshot evidence, runtime observation, measured evidence, inference, and unverified limits. Keep the response proportional to the request; completeness means covering the decisions that can change the outcome, not listing every possible component.

For each major design choice, keep a short decision trace: **choice → task or platform reason → adaptation or trade-off → evidence/limit**. Use it for hierarchy, control pattern, material, type, and motion when those choices are consequential; skip it for routine implementation details. Stop when the requested scope and acceptance conditions are covered, rather than inventing extra screens or polish work.

## Advise

Return the recommended decision first, the reason tied to the user task second, and alternatives only when they change an important trade-off. Mention assumptions that affect the recommendation.

## Review

Return a short prioritized report. Every finding has What, Why, Fix, and Evidence or Limitation. Separate blockers from polish. When improving a skill from a project review, distinguish guidance gaps, implementation deviations, and product-specific choices only where the evidence supports the cause; otherwise label it unverified. Do not turn taste into a violation.

## Design

Return a platform and task summary, information hierarchy, layout/composition, semantic tokens, component decisions, interaction states, motion choreography, accessibility/localization notes, rationale tied to the task and brand, and a verification checklist. Include responsive or platform adaptations rather than duplicate screens with no rationale.

## Implement

Inspect the existing project first. Reuse its components and dependencies. Make the smallest complete change, preserve data and error handling, and do a proportionate verification pass. Report files changed, checks run, and anything unverified; do not build a testing system unless the user asks for one.

## Enforce

Use only after explicit request. Establish the scope and pass criteria, inspect the artifact, fix only in-scope issues, and re-review. Stop after a bounded number of cycles or when progress requires product decisions. Never imply certification or App Store/WCAG conformance without the required evidence.

## Claim discipline

A complete implementation or review report distinguishes **Applied** (a documented change exists), **Source evidence** (files or declarations inspected), **Screenshot evidence** (a still image inspected), **Observed** (behavior exercised in a running artifact), **Measured** (a calculation produced it), **Inferred** (source suggests it but it was not run), and **Unverified** (evidence is unavailable). Do not turn a validator pass into a whole-skill pass, or plausible data into verified production content. When asked whether the skill was used, answer the evidence matrix and limits before any summary.
