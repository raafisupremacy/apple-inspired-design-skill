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
7. **Motion**: add only motion that explains state, relationship, or manipulation.
8. **Verification**: check states, accessibility, content length, and the real task.

Do not reverse this order by starting with gradients, glass, cards, animations, or a component library.

## Trade-offs

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
