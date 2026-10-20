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
- [ ] Composition fits the surface purpose: marketing has a clear story arc; operational and reading surfaces preserve useful repetition, scanning, and predictable task structure.
- [ ] Dense operational surfaces establish one primary question or action, keep secondary metrics visually quiet, and recompose rather than squeeze at compact widths.
- [ ] Typography uses an available or bundled font, with real copy checked for wrapping and hierarchy.
- [ ] Depth is intentional: shadows, borders, blur, and rounded surfaces are used consistently and sparingly.
- [ ] Linked states stay synchronized across visible content and accessibility text.
- [ ] Selection controls match their task and cardinality; their visible state, accessible state, keyboard behavior, and dependent content agree. Shared indicators, when used, preserve their final position under reduced motion.
- [ ] Product claims, reviews, prices, guarantees, and technical specifications are verified or clearly marked illustrative.

## Acceptance gate

- [ ] The established context or brief identifies the task and constraints relevant to the change; new surfaces also establish hierarchy, next action, content shape, and evidence limits.
- [ ] The visual treatment supports the task, brand, or intended experience; expressive choices preserve readability and operability, and familiar patterns are not changed merely to appear distinctive.
- [ ] Repeated patterns were compared across representative screens or states, while platform-specific differences remain intentional.
- [ ] Real or representative content was checked for wrapping, empty/long/error states, and the required text scale or zoom.
- [ ] Visual acceptance is based on rendered evidence when appearance is part of the request; source inspection and validators are reported separately.

Do not call a result polished, production-ready, or fully applied when this gate is incomplete. Label the missing evidence and the smallest next verification step.

Do not mark a screen complete from a screenshot alone when interaction, accessibility, performance, or responsive behavior is part of the request.

## Cross-surface design review

For a multi-screen design or implementation, compare representative related surfaces at comparable viewport and text settings, then check the relevant compact/wide and enlarged-text variants. For a one-screen task, use its important states. Use real content and the project's existing visual direction; do not invent another screen just to perform this check.

- [ ] The first emphasis, comparison groups, and next useful action match the stated task; surrounding space supports those relationships.
- [ ] Equivalent controls belong to a consistent family; differences have a task, state, input, or platform reason.
- [ ] Headers and navigation distinguish peer destinations from deeper levels consistently; back controls have a meaningful destination.
- [ ] Status text, icons, and colors agree, including neutral and unavailable-data states.
- [ ] System bars, app chrome, and content remain legible and separated where needed, including themes, overlays, insets, and keyboard changes on platforms that expose them.

When a rendered comparison exposes a concrete failure, fix its shared cause within the authorized scope and recheck the affected surfaces. In Review mode, report the fix instead of editing. Record the artifact, state, viewport/text settings when known, and remaining limitations. Static screenshots support composition findings; source checks and validator passes do not establish visual quality or interactive behavior. Without rendered evidence, label visual acceptance unverified rather than declaring the design polished.

- [ ] Brand decisions connect composition, type, imagery, density, controls, depth, and motion without sacrificing task clarity.
- [ ] Primary information outranks supporting badges and metadata; repeated components remain easy to compare.
- [ ] Images accurately represent their entity or are clearly contextual/illustrative.
- [ ] Compact navigation preserves access; important labels, actions, and selected options remain discoverable.
- [ ] Related transitions form a coherent sequence, including dismissal, focus, and reduced motion.
- [ ] Findings stay within the requested design scope; backend and business-rule correctness are not inferred from UI inspection.

- [ ] A live audit includes independent inspection beyond user-supplied screenshots and labels unobserved states.
- [ ] Interface icons form a coherent family; emoji are intentional content or brand expression, not default control assets.
- [ ] Headlines and action placement remain appropriate after reflow, including intermediate widths and long overlays.
- [ ] Reduced motion preserves closed/open visibility and selected geometry; runtime behavior is distinguished from CSS inference.
