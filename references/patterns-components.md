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
