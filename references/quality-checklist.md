# Quality checklist

Use the relevant sections as a final gate after reading the complete reference set. Do not report an unchecked item as passing.

## Responsive web

- [ ] Narrow and wide compositions preserve task priority.
- [ ] No accidental page-level horizontal scroll.
- [ ] Navigation, menu focus, back behavior, and scroll position are predictable.
- [ ] Images reserve space and have appropriate responsive variants.
- [ ] Loading, retry, end-of-content, offline, and empty states are present where relevant.
- [ ] Light, dark, increased contrast, reduced motion, keyboard, touch, and zoom states work.
- [ ] Semantic HTML and metadata are present where relevant.
- [ ] Optional browser APIs have a tested fallback or are gated by actual capability support.

## Mobile

- [ ] Native back behavior and safe areas are respected.
- [ ] Touch targets and spacing are comfortable.
- [ ] Text scaling does not clip content.
- [ ] Gestures have accessible alternatives.
- [ ] Haptics are optional feedback, never the only feedback.

## Visual and motion

- [ ] Hierarchy is clear before decoration is added.
- [ ] Tokens are semantic and derived colors pass contrast checks.
- [ ] Motion has a purpose, is interruptible, and has a reduced-motion alternative.
- [ ] Real content, long strings, and user-provided assets were considered.
- [ ] The chosen domain pattern supports the product’s actual primary task instead of adding unrelated screens or components.
- [ ] Claims about support, performance, accessibility, or device behavior have evidence labels.

Do not mark a screen complete from a screenshot alone when interaction, accessibility, performance, or responsive behavior is part of the request.
