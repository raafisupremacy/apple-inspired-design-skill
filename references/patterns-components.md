# Patterns and components

Use these as decision patterns, not a mandatory component library.

## Page patterns

- **Home/dashboard**: one clear task or insight first, then grouped supporting content.
- **Index/detail**: list to detail on compact screens; split or side-by-side on wide screens.
- **Form/task**: one focused task per step, clear validation, preserved input, explicit completion state.
- **Settings/profile**: grouped rows and predictable hierarchy; avoid a grid of unrelated cards.
- **Marketing/landing**: a strong story arc, deliberate scroll choreography, and restrained interactive moments.
- **Data-heavy**: use tables where scanning benefits from columns; use readable grouped rows on compact screens.

## Component decisions

- Prefer one unified panel with separators for sibling settings or rows over many disconnected cards.
- Use sheets and dialogs for focused temporary work; keep escape, backdrop, back, and focus restoration predictable.
- Use segmented controls only for a small set of mutually exclusive views.
- Use a status treatment with text and a non-color cue.
- Use icons when they clarify an action or status; do not place an icon beside every heading.
- Use a signature element sparingly: one distinctive visual or motion idea can give a product a point of view.

## Platform translation

The same information architecture may use different controls: a web link, an iOS navigation item, an Android back-aware screen, or a Flutter platform-adaptive widget. Preserve intent and context, not identical markup.
