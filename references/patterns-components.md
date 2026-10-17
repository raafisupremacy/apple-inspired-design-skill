# Patterns and components

Use these as decision patterns, not a mandatory component library.

## Page patterns

- **Home/dashboard**: one clear task or insight first, then grouped supporting content.
- **Index/detail**: list to detail on compact screens; split or side-by-side on wide screens.
- **Form/task**: one focused task per step, clear validation, preserved input, explicit completion state.
- **Settings/profile**: grouped rows and predictable hierarchy; avoid a grid of unrelated cards.
- **Marketing/landing**: a strong story arc, deliberate scroll choreography, and restrained interactive moments.
- **Data-heavy**: use tables where scanning benefits from columns; use readable grouped rows on compact screens.

### Marketing surface composition

- Give each section one job: introduce, demonstrate, explain, prove, compare, or convert.
- Vary composition by job: product-led media, split detail, editorial statement, comparison, proof, and focused purchase—not the same centered heading and card repeated.
- Establish the product and one primary action before exposing a long specification table. Move exhaustive detail below the decision or into an expandable surface.
- Let the real asset determine the crop, scale, and background. Do not wrap every image in the same rounded card with the same shadow.
- Where it strengthens the story, use an authored scroll or interaction moment tied to the product; do not attach generic reveal animations to every section.

## Component decisions

- Prefer one unified panel with separators for sibling settings or rows over many disconnected cards.
- Use sheets and dialogs for focused temporary work; keep escape, backdrop, back, and focus restoration predictable.
- Use segmented controls only for a small set of mutually exclusive views.
- Choose tabs for associated content panels, radio groups for one value, checkboxes for independent multiple values, toggle buttons for on/off actions, and links for destinations. A filter or variant picker can use different patterns depending on its task and selection rules.
- For compact single-selection controls, a shared moving indicator can clarify continuity. Underlines, swatches, checkmarks, and native selected treatments remain valid; do not impose a pill on every control. Expose the selected state and implement the chosen pattern's keyboard behavior.
- Use a status treatment with text and a non-color cue.
- Use icons when they clarify an action or status; do not place an icon beside every heading.
- Use a signature element sparingly: one distinctive visual or motion idea can give a product a point of view.
- Do not treat rounded cards, gradients, badges, icon tiles, or drop shadows as the default answer for every content group. First ask whether spacing, alignment, a divider, or an edge-to-edge composition communicates the relationship better.

## Platform translation

The same information architecture may use different controls: a web link, an iOS navigation item, an Android back-aware screen, or a Flutter platform-adaptive widget. Preserve intent and context, not identical markup.

## Information priority within repeated components

Rank the content needed to identify, compare, decide, and act. Give the primary decision information the strongest emphasis; make metadata secondary and decoration quiet. Ratings, statuses, badges, discounts, tags, and icons do not all deserve containers or equal visual weight. Keep a badge only when its meaning helps the task.

Show the context needed to interpret a value near it: unit, time period, scope, or selected option as appropriate. Use progressive disclosure for supporting detail without hiding essential decision information. Preserve alignment and comparable positions across repeated items; let real text lengths determine wrapping rather than forcing every item to look artificially identical.

For practical instructions and comparable information, separate key parameters, units, and steps from explanatory prose when users need to scan or act. Use concise labeled values, lists, or tables as appropriate; preserve prose for narrative reading. Do not turn every parameter into a badge or card.

## Decision density on operational surfaces

- A dashboard or workspace should answer one primary question before showing supporting metrics. Give the first viewport a clear orientation, current state, and next useful action.
- Limit competing emphasis: use one dominant metric or action per region, then quiet secondary values with spacing, grouping, and typography before adding color, badges, or containers.
- Group related metrics, activity, and records into a few meaningful surfaces. If every item becomes a card, pill, or colored icon, comparison slows and the page becomes visual noise.
- Preserve scan paths at each width. On compact screens, reorder, collapse, or replace secondary regions; do not squeeze a desktop dashboard into a narrow column or rely on horizontal overflow for essential content.
- This is a decision rule, not a fixed card count. Dense tables and compact controls are appropriate when repeated comparison is the task; promotional or editorial surfaces need a different rhythm.
