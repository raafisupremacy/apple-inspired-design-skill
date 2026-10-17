# Motion system

Motion is part of the interface's information architecture. It should explain feedback, orientation, continuity, or direct manipulation. If an animation communicates none of those, remove it.

For a page or product surface, choose one authored motion moment that expresses the product or clarifies its key relationship. Use small state transitions elsewhere only as feedback. A scroll reveal on every section, a generic fade-in, or a hover lift on every card is not a motion system.

## Start with a motion brief

Before writing code, describe each meaningful transition in this form:

```text
Trigger → source → destination/state → property → timing/curve → interruption → reduced-motion fallback
```

Example:

```text
Tap product card → card image/title → detail header → shared position/scale → 280ms spring → reverse from current progress → cross-fade and preserve focus
```

This prevents “make it smoother” from becoming arbitrary animation. Keep the task, hierarchy, and state change correct before adding choreography.

## Motion grammar

Use the smallest property set that explains the change:

- **Feedback:** opacity, color, scale, or a small elevation change confirms an action. Keep it fast and never delay the action itself.
- **Orientation:** a sheet, popover, or navigation transition shows where the new surface came from and how to return.
- **Continuity:** shared content, stable chrome, and matched geometry preserve object identity between states.
- **Direct manipulation:** the finger or pointer leads the object. The release velocity informs the settling motion.

Prefer transforms and opacity over animating layout, width, height, top, left, or box-shadow on large surfaces. Use FLIP, View Transitions, native layout animation, or the project’s existing layout system when the layout itself must change. Do not use scale as a substitute for a real reflow when text or controls must remain readable.

## Tokens and calibration

Use semantic tokens rather than scattering durations. The bundled starter values are deliberately approximate:

| Role | Starting value | Use |
| --- | ---: | --- |
| `fast` | 180ms | press feedback, focus, small opacity/color changes |
| `base` | 280ms | control state, compact navigation, list updates |
| `slow` | 480ms | sheets, large content continuity, deliberate reveals |
| maximum | 650ms | upper bound for ordinary UI; avoid making users wait |

For CSS, pair durations with curves such as `ease-out` for entering, `ease-in` for leaving, and a custom cubic-bezier only when the product has calibrated it. For spring-capable platforms, specify mass/stiffness/damping or the named platform preset rather than pretending a cubic-bezier is a spring. These are starting points, not Apple’s private timings; calibrate against the actual content, refresh rate, and input device.

Use this calibration order:

1. Make the end state immediate and correct.
2. Add the shortest duration that preserves identity and direction.
3. Tune overshoot only for physical objects, sheets, and direct manipulation; never bounce text or critical feedback.
4. Interrupt midway, reverse direction, and trigger a second action. If the motion jumps, restarts, or blocks input, fix the state model before tuning values.

## Choreography rules

- Animate one hierarchy at a time. Parent movement establishes context; child reveals follow only when they add orientation.
- Use a small stagger (roughly 20–40ms) only for a short, related group. Never stagger a long list or essential content.
- Keep navigation chrome stable while the destination content changes unless the chrome itself is the subject of the transition.
- Preserve scroll position and focus when switching between sibling states.
- Start from the current visual state and velocity. Do not reset to the initial keyframe when a user reverses a gesture.
- Do not make a user wait for a decorative reveal, shimmer, count-up, or parallax effect.
- Avoid looping motion except for ongoing system activity, and pair it with a static label/state.

## Platform patterns

### Navigation and shared content

- Push detail on compact mobile layouts; use pane replacement or a restrained cross-fade on wide layouts.
- Use a shared-element transition only when the destination visibly contains the same object. Match identity using the image, title, or container—not unrelated decoration.
- Top-level tab changes should preserve each tab’s context. Prefer an immediate state change or short cross-fade over a directional slide that implies a hierarchy that does not exist.
- If navigation can occur during a transition, let the latest intent win and settle from the current state.

### Sheets, dialogs, and menus

- A compact touch sheet follows the drag directly, applies a velocity-aware settle/dismiss decision, and has a visible dismissal affordance.
- A desktop dialog or popover should not pretend to be a full-screen page. Anchor it to its trigger when spatial context helps.
- Back, escape, scrim tap, and the close control should resolve to the same state machine. Restore focus to the trigger after dismissal.
- Never hide destructive terms or confirmation controls behind a delayed animation.

### Lists and layout changes

- Animate insertion, removal, filtering, and reorder so item identity remains trackable. Keep stable items stable.
- Prefer cross-fade plus small translation for a filter result; avoid moving every row across the screen for a minor query change.
- Reserve image and text space before loading to prevent layout jumps. A skeleton is useful only when it represents the final geometry and does not pulse unnecessarily.

### Scroll-linked effects

- Tie title collapse, header treatment, and reveal to scroll progress, not to arbitrary timers.
- Clamp the effect, keep content readable, and avoid parallax that changes the apparent position of an actionable control.
- Provide a static layout when scroll-driven APIs or JavaScript are unavailable. Scroll-linked motion must never be required to discover or operate content.

## Gesture contract

For every drag, swipe, pinch, or interactive transition define:

1. **Start:** what region and gesture begins it, and what happens to competing scroll or controls?
2. **Mapping:** which input distance maps to which visual property, with a bounded range.
3. **Release:** how velocity, distance, and intent choose settle versus cancel.
4. **Interrupt:** how a new pointer, back action, rotation, or navigation changes it.
5. **Alternative:** an accessible button, keyboard action, or platform back path.

Use a resistance curve after the useful range rather than a hard wall. Keep hit targets comfortable and do not require a precise edge swipe when the same action can be invoked visibly.

## Reduced motion and other preferences

Honor `prefers-reduced-motion` on web and native Reduce Motion settings on mobile. Replace travel, bounce, shimmer, count-up, and parallax with an immediate state change or a short opacity change. Keep focus, hierarchy, and status information visible; do not merely set every duration to `1ms` if that causes content to flash or disappear. The starter token `--motion-reduced` is a short timing hint; it does not replace the alternate choreography.

Also account for reduced transparency, increased contrast, text scaling, keyboard focus, touch, screen readers, and localization. Never use motion, color, sound, or position as the only signal.

Example CSS fallback:

```css
.surface {
  transition: transform var(--motion-base) ease-out,
              opacity var(--motion-fast) ease-out;
}

@media (prefers-reduced-motion: reduce) {
  .surface {
    transition: opacity 120ms linear;
    transform: none !important;
  }
}
```

The important behavior is the alternate choreography, not the exact CSS snippet. Native and cross-platform implementations should map the same contract to SwiftUI/UIKit, Android, React Native Reanimated, Flutter, or the project’s existing motion system.

## Motion review checklist

- [ ] The trigger and state change are clear without motion.
- [ ] Motion has one primary purpose: feedback, orientation, continuity, or manipulation.
- [ ] The end state is correct before animation starts.
- [ ] The motion can be interrupted, reversed, and followed by another action.
- [ ] Focus, scroll position, back behavior, and input remain predictable.
- [ ] The gesture has a non-gesture alternative.
- [ ] Reduced motion, reduced transparency, text scaling, and localization remain usable.
- [ ] Long lists, low-power devices, and high-refresh displays do not expose avoidable jank.
- [ ] Values are labeled as calibrated project values, not claims about Apple internals.
