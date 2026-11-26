# Modes, reviews, and evidence

## What each mode delivers

- **Advise:** the recommended decision first, the reason tied to the user's task, and alternatives only when they change an important trade-off.
- **Design:** the brief (with the color direction), hierarchy, layout/composition, tokens, component decisions, states, motion, accessibility notes, and responsive/platform adaptation.
- **Implement:** inspect the project first, reuse its stack and components, make the smallest complete change that achieves the visual goal (which may recompose a layout), preserve data and error handling, verify proportionately, report files changed and what was checked.
- **Review:** a short prioritized list of findings (below).
- **Enforce:** only when explicitly requested; agree on scope and pass criteria, fix in-scope issues, re-review, stop after a bounded number of cycles.

Keep the response proportional. Completeness means covering the decisions that change the outcome, not listing every component.

## Visual redesign

A visual redesign must produce visible decisions — composition, type scale, color, spacing, shape, depth, or motion — tied to the problems found:

1. **Baseline:** inspect the current artifact; name the highest-impact visual problems with location.
2. **Intent:** what should be noticed first, what belongs together, what the next action is.
3. **Decisions:** connect each problem to a concrete change, using the foundations and surface playbook.
4. **Implement** (Implement mode) or **specify** (Design/Review mode).
5. **Compare** before and after at the same content, viewport, theme, and text size when rendering is available.

A build, lint, or token check is not visual evidence. Technical-only repairs do not complete a redesign. A representative screen calibrates a multi-screen redesign; track the rest of the requested scope.

## Review format

Scope: UI, UX, visual design, motion, design systems, responsive/platform adaptation, and interface accessibility. Do not expand into backend, business logic, payments, or security auditing unless asked.

Order: task clarity → accessibility → platform conventions → content and states → hierarchy and layout → color and type → motion → polish. For each finding:

1. **What** — with file:line, component, screenshot region, or viewport.
2. **Why** — the user impact and the principle or convention.
3. **Fix** — in the project's framework vocabulary.
4. **Evidence / limit** — how it was observed, or what could not be checked.

Separate blockers from polish. Do not invent findings to look thorough; do not turn taste into a violation.

## Evidence labels

- **Source:** seen in code or files (does not prove runtime behavior).
- **Screenshot:** seen in a still image (does not prove interaction or unshown states).
- **Observed:** exercised in a running browser, simulator, or device, with input and viewport named.
- **Measured:** calculated (contrast ratio, layout size, performance trace).
- **Inferred:** likely from source, not executed.
- **Unverified:** needs a device, assistive technology, or data that was unavailable.

Use the narrowest true verb: "declared", "measured", "observed", "verified". Never call motion smooth from a duration value or reduced motion working from the presence of a media query. When asked whether this skill was applied, answer with what was read, changed, observed, measured, and left unverified — not with reassurance.

## Runtime checks when a UI is running

Within the requested scope: narrow, intermediate, and wide sizes; largest text; light and dark; keyboard and touch; representative interactions (open, close, select, interrupt, reverse); reduced motion; loading, empty, and error states. For motion record purpose, continuity, physical response, interruption, state integrity, and the reduced-motion result.

## Improving this skill from real projects

When the user asks to improve the skill from a project audit, classify each finding as (1) a missing or wrong instruction, (2) an implementation that ignored adequate guidance, or (3) a deliberate product choice. Generalize the decision criterion, not the project's layout; test the rule against a contrasting product; update the owning reference instead of adding overlapping rules. Prefer adding craft knowledge and examples over adding reporting rules.

## Claims

Do not claim official Apple design, Apple endorsement, device testing, WCAG conformance, App Store approval, or performance results without evidence.
