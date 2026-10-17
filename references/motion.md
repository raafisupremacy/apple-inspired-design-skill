# Motion system

Motion must communicate one of four things: feedback, orientation, continuity, or direct manipulation. If it communicates none of them, remove it.

## Behavior

- Use spring-like motion for transforms, sheets, controls, shared elements, and layout changes.
- Use short easing for opacity, color, and blur.
- Gestures follow the pointer or finger directly and carry release velocity into the settling motion.
- Animations are interruptible. A new action starts from the current position and velocity.
- Keep navigation chrome stable while the related content changes.
- Do not animate layout properties directly when transform, opacity, FLIP, or platform layout animation can express the change.
- Keep entrances short and purposeful. Avoid repeated motion on every tab switch or every scroll.

## Patterns

- Detail navigation: push on mobile; pane replacement or subtle cross-fade on wide layouts.
- Top-level navigation: cross-fade or immediate state change; preserve each destination’s context.
- Modal work: sheet on compact touch layouts, dialog or popover where platform conventions call for it.
- Related content: shared-element transition when the destination visibly contains the source object.
- Lists: animate insertion, removal, reorder, and filtering so the user can follow identity.
- Scroll effects: tie meaningful title, header, and reveal changes directly to scroll progress; keep parallax subtle.

## Accessibility and performance

Honor `prefers-reduced-motion` and native Reduce Motion by replacing travel, bounce, shimmer, parallax, and count-up effects with an immediate or short fade plus a clear state change. Never hide important information behind animation. Keep input responsive and test long lists, low-power devices, and high-refresh displays.

Implementation values are starting points, not claims of Apple’s private timings. Map the behavior to CSS/View Transitions, SwiftUI, React Native Reanimated, Flutter, or the project’s existing motion system.
