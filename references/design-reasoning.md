# Design reasoning

Apple-inspired quality comes from the chain of decisions, not from a fixed look.

## Frame the problem

Before choosing components, identify:

- who is acting and what they are trying to accomplish
- the most important content or decision on the screen
- frequency, urgency, risk, and reversibility of the task
- platform, input methods, environment, and interruption level
- brand constraints, localization, privacy, and technical constraints

If a missing answer changes the design materially, ask one focused question. Otherwise state an assumption and proceed.

## Decide in order

1. **Purpose**: define the user outcome in one sentence.
2. **Hierarchy**: rank content and actions; remove items that do not support the outcome.
3. **Information architecture**: choose the smallest clear set of screens, sections, and destinations.
4. **Interaction model**: choose familiar platform patterns for navigation, input, feedback, and recovery.
5. **Composition**: place content using alignment, grouping, whitespace, scale, and contrast.
6. **Identity**: add brand color, imagery, type personality, or one signature moment where it reinforces the product.
7. **Motion**: explain state, relationship, or manipulation; allow deliberate brand expression when it supports the intended experience without impairing readability, control, or accessibility.
8. **Verification**: check states, accessibility, content length, and the real task.

Do not reverse this order by starting with gradients, glass, cards, animations, or a component library.

## Calibrate composition to the task

Before propagating a visual treatment, describe what the user should notice first, which information they must compare together, and the next useful action. Apply that hierarchy to a representative surface with real content. For multi-screen work, compare a related screen or state before spreading the same decisions across the product.

Calibrate spacing at three levels: within a related group, between groups, and around the page or surface. Related content should read as a group before borders or cards are added. If users must scroll back and forth to compare short related values, regroup them; if dense content loses legibility or operability, give it more space or progressive disclosure. Preserve readable type, focus indicators, and input targets rather than shrinking everything to fit.

Judge density by task, not by how much of the viewport is filled. A repeated-work table benefits from aligned, compact comparisons; an editorial story may need generous pauses; a form with enlarged text may need more scrolling. Empty space is a defect only when it breaks grouping, obscures priority, or makes the task needlessly harder. Do not force every action above the fold or stretch sparse content merely to fill a screen.

Translate visual intent through the target platform's layout units, text scaling, input methods, and navigation conventions. Screenshot pixels do not establish CSS pixels, dp, pt, hit areas, or device font settings. Starter token values are inputs to calibration, not universal dimensions to copy across platforms.

## Reveal complexity without hiding the task

Keep frequent actions and information required for the current decision visible. Move rarely used options behind a clearly labeled, discoverable control; do not hide the primary action in an overflow menu solely to make the screen look minimal. When a collapsed setting affects the current result, keep its active value or effect apparent.

Distinguish progressive disclosure (optional advanced detail) from staged disclosure (steps everyone must complete). A wizard can suit separable stages, but keep interdependent choices and their consequences together when users need repeated comparison. For example, comparing options and prices benefits from shared context; entering delivery details can be a later stage. Do not apply a fixed maximum number of visible controls or steps across products. If usage evidence is unavailable, label frequency assumptions and verify the common task before propagating the pattern.

## Resolve trade-offs

When values conflict, prefer in this order unless the product has a strong reason otherwise:

1. safety, accessibility, and data integrity
2. task clarity and recoverability
3. platform familiarity and input comfort
4. performance and resilience
5. brand expression and visual polish

Record the trade-off in one sentence when a deliberate exception is necessary.

## Custom domain

When no domain recipe applies, do not invent a generic template. Derive the structure from the product’s vocabulary, user mental model, task frequency, risk, collaboration model, and recovery path. Name the new pattern in plain language, explain why it fits the domain, and keep it local to the product instead of promoting it to a universal rule.

## Transfer across products

Choose the purpose of each surface, not a template for the entire product: efficient repeated work, comparison and purchase, persuasion, reading, or exploration. These can coexist in one product. Dense operational screens may need stable tables and compact controls; editorial or promotional screens may need a different rhythm. Derive density, navigation, imagery, copy, and motion from that purpose. No recipe is required for a supported web or mobile task.

When improving this skill from a real project audit, separate:
1. A missing, ambiguous, conflicting, or overbroad instruction.
2. An implementation that did not follow an adequate instruction.
3. A deliberate product-specific choice or an unverified observation.

Check the instructions actually used before assigning the cause. Generalize the decision criterion, not the audited project's layout, wording, icons, or effects. Check a proposed rule against a contrasting use case and state when it does not apply. Update the existing owning reference rather than accumulating overlapping rules. An audit does not authorize editing either the project or this skill unless the user requested that work.
