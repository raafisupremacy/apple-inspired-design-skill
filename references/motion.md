# Motion system

Motion is part of the interface's information architecture. It should explain feedback, orientation, continuity, or direct manipulation. If an animation communicates none of those, remove it.

When a page or product surface benefits from a signature motion moment, choose one that expresses the product or clarifies its key relationship. Do not require a showcase animation for routine operational or reading tasks. Use small state transitions elsewhere only as feedback. A scroll reveal on every section, a generic fade-in, or a hover lift on every card is not a motion system.

## Start with a motion brief

Before writing code, describe each meaningful transition in this form:

```text
Trigger → source → destination/state → property → timing/curve → interruption → reduced-motion fallback
```

Example:

```text
Tap product card → card image/title → detail header → shared position/scale → calibrated spring preset → reverse from current progress → cross-fade and preserve focus
```

This prevents “make it smoother” from becoming arbitrary animation. Keep the task, hierarchy, and state change correct before adding choreography.

## Motion grammar

Use the smallest property set that explains the change:

- **Feedback:** opacity, color, scale, or a small elevation change confirms an action. Keep it fast and never delay the action itself.
- **Orientation:** a sheet, popover, or navigation transition shows where the new surface came from and how to return.
- **Continuity:** shared content, stable chrome, and matched geometry preserve object identity between states.
- **Direct manipulation:** the finger or pointer leads the object. The release velocity informs the settling motion.

Prefer transforms and opacity over animating layout, width, height, top, left, or box-shadow on large surfaces. Use FLIP, View Transitions, native layout animation, or the project’s existing layout system when the layout itself must change. Do not use scale as a substitute for a real reflow when text or controls must remain readable.

## Motion primitives and state modeling

Treat animation as a rendering of state, not a separate event layer. Define a small set of visual states (`rest`, `pressed`, `entered`, `exited`, `dragging`, `settling`, `disabled`) and derive the animation from the state change. This keeps the latest user intent authoritative when an animation is interrupted or a second action arrives.

Use these primitives when they map to the product task:

- **Variants/state recipes:** name states and their transition rules once, then reuse them for related components. Do not create a variant for every visual tweak.
- **Layout transition:** animate a real change of position or size when preserving object identity helps orientation. Measure the destination; never guess dimensions from label length.
- **Shared identity:** carry an image, title, or container into the next surface only when it is the same object. A shared transition is an orientation cue, not a decorative effect.
- **Presence:** distinguish semantic dismissal from visual removal. Transfer focus before making outgoing content inert or hiding it from assistive technology; apply the enter–exit contract below.
- **Timeline/scroll progress:** bind progress to a bounded range of scroll or media state. Provide a static end state when the API is unavailable.

The primitive is a means, not a style requirement. A native transition, CSS transition, View Transition, SwiftUI animation, UIKit animator, Android motion system, React Native Reanimated, Flutter animation, or an existing project utility can satisfy the same contract.

Framework-neutral state shape:

```text
state = { status, selectedKey, layoutBounds, progress, velocity }
transition(previous, next):
  preserve semantic state immediately
  animate only the visual delta
  sample current rendered value on interruption
```

Do not model motion as `onClick → play animation → update state`. That ordering creates stale content, broken reversal, and focus races.

## Choosing the right transition

Use this order before choosing an API:

1. Is the task feedback, orientation, continuity, or direct manipulation?
2. Does the layout or object identity actually change?
3. Can the interaction be completed without motion, gesture, or JavaScript?
4. What is the smallest property set and shortest duration that preserves meaning?
5. What is the reduced-motion choreography and what remains interactive during it?

If the answer to the first question is unclear, remove the animation. If only a value changes, prefer opacity/color or a brief numeric replacement over moving the whole region. If a surface changes hierarchy, use position and scale only when they explain where it came from and where it will return.

### Property ownership and handoff

For overlapping effects, identify the owner of each rendered property. Independent CSS transitions, keyframes, gesture handlers, and layout engines must not overwrite the same `transform` or opacity without an explicit composition rule. Separate transform components are safe only when the renderer actually composes them; separate API names alone do not establish ownership.

- Prefer the project's existing animation compositor. During drag, input owns translation; suspend competing positional motion or compose it in a coordinate system that keeps the object under the pointer. Decorative hover motion must yield when it interferes with manipulation.
- On release or cancellation, hand the current position and supported velocity to the settling transition. Stop the old writer and invalidate its completion before the next owner takes over; do not snap back to the previous target first.
- Use separate visual layers only when simultaneous effects are necessary, such as layout positioning on an outer layer and press scale on an inner layer. Check transform order, measured bounds, clipping, focus outlines, and hit testing; an extra wrapper is not automatically a fix.
- Reduced motion removes animation, not ownership of destination geometry. Keep the selected position, drag result, and open/closed state correct.

Check a layout update while the pointer hovers and drags, then release, cancel, and resize. The object should remain attached to input and settle at the latest valid destination without a jump or an old effect restoring stale geometry.

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

### Spring or duration-based easing

| Need | Starting choice | Calibration criterion |
| --- | --- | --- |
| Short opacity/color feedback or a deliberately timed sequence | Duration and easing | The result is readable promptly; timing does not delay the action. |
| Retargetable position, shared geometry, or settling after direct manipulation | Spring supported by the existing platform | Position remains continuous on interruption; preserve velocity when the engine supports it. A spring need not bounce. |
| A visual property that represents exact scroll progress | Direct bounded progress mapping | Reversing scroll reverses the effect without lag; smoothing must not misrepresent progress. |

While dragging, follow input directly; apply a spring to settling after release rather than making the object chase the pointer. Duration-based animation can also be interrupted, but restarting from the current value does not by itself preserve velocity.

For a physics spring, calibrate stiffness and damping with mass held stable initially. Unwanted repeated overshoot calls for more damping toward a nonoscillating response. A slow nonoscillating tail may instead be excessive damping: reduce it or increase stiffness while recalibrating damping. More damping is not always faster. Prefer an established platform preset before tuning raw parameters.

Inspect short and long travel, slow and fast releases, and reversal midway. Use the engine's documented rest thresholds; thresholds that are too loose can produce a visible final snap, while overly strict ones can prolong tiny updates. Completion still must not gate focus, semantic state, or user input.

Duration/bounce spring controls and physical mass/stiffness/damping controls are different parameterizations. Check the installed engine's precedence and units before combining options; do not assume a physics spring has a fixed duration or copy constants between engines. The timing tokens above are calibration targets for perceived responsiveness, not guaranteed spring completion times or Apple specifications.

## Choreography rules

- Animate one hierarchy at a time. Parent movement establishes context; child reveals follow only when they add orientation.
- Use a small stagger (roughly 20–40ms) only for a short, related group. Never stagger a long list or essential content.
- Keep navigation chrome stable while the destination content changes unless the chrome itself is the subject of the transition.
- Preserve scroll position and focus when switching between sibling states.
- Start from the current visual state and velocity. Do not reset to the initial keyframe when a user reverses a gesture.
- Do not make a user wait for a decorative reveal, shimmer, count-up, or parallax effect.
- Avoid looping motion except for ongoing system activity, and pair it with a static label/state.

## Enter–exit contract

Define which surface owns focus and interaction throughout the transition. Prefer the platform or project's established dialog/navigation lifecycle; animation completion must not decide whether a user action took effect.

- **Enter:** establish the destination's semantics, focus policy, and usable controls when it becomes active. Avoid focusing content that is still invisible or offscreen; reveal the focus target immediately or simplify its entry motion. For a modal, coordinate focus containment and background inertness with activation.
- **Replace:** use simultaneous movement or a short cross-fade when it preserves context. An outgoing visual copy must not duplicate active controls, accessible content, or IDs. Use exit-before-enter only when the sequence explains a meaningful relationship; show a real loading state if the destination is unavailable rather than extending an exit animation.
- **Dismiss:** resolve the close action through the existing state model. Transfer focus to an available trigger or a logical target in the surviving view before making the outgoing surface inert or accessibility-hidden. Coordinate release of background inertness with that transfer. A visual exit may finish afterward without trapping focus or blocking input. `aria-hidden` alone does not prevent keyboard or pointer interaction.
- **Interrupt:** when reopened during exit, continue from current geometry and restore active semantics. Cancel or invalidate obsolete completion callbacks so an earlier exit cannot remove the reopened surface, move its focus, or clear its scroll lock.
- **Finish:** remove only the outgoing instance that is still meant to leave. Cleanup also needs to work when motion is skipped, cancelled, or reduced; do not depend solely on a duration timer or a transition event that may never fire.

This contract governs visual lifecycle, not authorization or persistence: keep the project's existing validation, pending, failure, and recovery behavior. A cancelled dismissal must leave the surface usable.

## Interaction recipes and acceptance checks

These recipes apply the platform patterns below; they are optional starting points, not required effects. Use the existing platform behavior when it already satisfies the task.

| Interaction and purpose | Motion and interruption | Reduced motion | Check the outcome |
| --- | --- | --- | --- |
| Segmented selection: track one active choice | Move one measured indicator; retarget from its current position on rapid selection. Keep labels and hit targets stable. | Place the indicator at the selected option immediately. | Select A → B → C rapidly, then resize or load a longer label: indicator, panel, focus, and semantic selection agree with the latest choice. |
| Sheet: explain a temporary layer and return | Follow the drag directly, then settle or dismiss from release intent. Reopening during exit invalidates old cleanup. Keep a visible close alternative. | Preserve direct input tracking when needed for manipulation; remove autonomous travel and bounce on release or button activation. | Close with focus inside, reopen before exit ends, and remove the original trigger: no stale unmount, hidden focus, or stranded background lock. |
| List reorder: preserve item identity | Track items by stable identity rather than position; move affected neighbors only. Reconcile a drop with current data using the product's existing update policy. | Update order without animated rearrangement; retain focus and announce the resulting position where appropriate. | Reorder by keyboard as well as drag. Insert or remove an item during drag: no duplicated/lost items, stale target, or unexplained focus loss. |
| Card to detail: connect the same object across hierarchy | Match the same object and current geometry on entry and return. If its counterpart disappears, use a simple replacement or fade. | Preserve navigation and context with immediate replacement or a short fade. | Return after filtering out the source card: keep the filter, choose a logical focus target, and never invent a shared destination just to complete the effect. |

For reorder, define what happens when the dragged item or drop target disappears: resolve against current eligible items or cancel visibly under the existing product policy. Do not restore stale data to preserve an animation. For shared content, an unmounted, filtered, or unavailable counterpart is a fallback case, not permission to change the user's filters or selection.

Repeat relevant checks with reduced motion active and with the preference changed mid-transition. Verify the final state and operability even if no animation completion fires. Record viewport, input, sequence, and observed outcome using compatibility-testing.md; these recipes alone are not evidence of working runtime behavior.

## Platform patterns

### Segmented controls and selection surfaces

For a compact single-selection control whose design uses a moving background or underline, treat that indicator as one shared surface. Choose the semantic control first using patterns-components.md. Native controls, static swatches, and independent multi-select filters do not require a shared pill.

- Keep the option labels and icons stationary; move or resize one selection layer using measured bounds, a layout animation, or a transform.
- Animate the selection layer with a short spring or calibrated ease-out (roughly `180–280ms` for a compact control). Let the label color and icon treatment follow with a shorter fade or color transition.
- Preserve the control’s outer track, hit targets, and focus ring while the inner selection surface moves. Do not animate width from guessed text lengths.
- Match semantics to behavior: tabs use aria-selected, radio choices use checked/aria-checked, and toggle buttons use aria-pressed. Native platform controls keep their platform semantics. Implement the matching keyboard pattern; adding a role alone does not add arrow-key behavior.
- When the content panel changes, update selection, panel content, accessible name, and any dependent summary from one source of truth. Do not leave the old panel or stale label visible during the transition.
- Under reduced motion, keep the selected surface in the new position immediately or use a short fade; never hide the selected state.

Framework-neutral shape:

```text
selection = { key, bounds }
onSelect(next):
  update state and content immediately
  animate shared selection layer from previous bounds to next bounds
  fade or color-transition labels only as supporting feedback
```

Use this motion only when one indicator meaningfully represents one active choice. For wrapped options, unequal labels, RTL, font loading, and resizing, measure the actual destination geometry again; do not assume equal widths or horizontal-only travel. For interruption, animate from the current rendered position rather than restarting at the previous option.

### Navigation and shared content

- Push detail on compact mobile layouts; use pane replacement or a restrained cross-fade on wide layouts.
- Use a shared-element transition only when the destination visibly contains the same object. Match identity using the image, title, or container—not unrelated decoration.
- Top-level tab changes should preserve each tab’s context. Prefer an immediate state change or short cross-fade over a directional slide that implies a hierarchy that does not exist.
- If navigation can occur during a transition, let the latest intent win and settle from the current state.

### Sheets, dialogs, and menus

- A compact touch sheet follows the drag directly, applies a velocity-aware settle/dismiss decision, and has a visible dismissal affordance.
- A desktop dialog or popover should not pretend to be a full-screen page. Anchor it to its trigger when spatial context helps.
- Back, escape, scrim tap, and the close control should resolve to the same state machine. Transfer focus on semantic dismissal using the enter–exit contract, with a logical fallback when the trigger is unavailable.
- Never hide destructive terms or confirmation controls behind a delayed animation.

### Lists and layout changes

- Animate insertion, removal, filtering, and reorder so item identity remains trackable. Keep stable items stable.
- Prefer cross-fade plus small translation for a filter result; avoid moving every row across the screen for a minor query change.
- Reserve image and text space before loading to prevent layout jumps. A skeleton is useful only when it represents the final geometry and does not pulse unnecessarily.

### Scroll-triggered and scroll-linked effects

- **Triggered:** entering a viewport threshold starts a time-based transition. Define once versus replay explicitly; a reading reveal usually remains visible after its first entry rather than repeatedly hiding on small scroll reversals. Use visibility observation instead of per-frame layout polling. Reveal focused or anchor-targeted content immediately.
- **Linked:** a property follows progress between defined start and end offsets in the actual scroll container. Use this for a collapsing title or meaningful progress treatment; clamp the range and reverse naturally with scroll. Recompute bounds after resize or content changes, and handle a zero-length range with a stable static state.
- Keep native scrolling, keyboard navigation, and reading position under user control. Do not intercept wheel or touch input to force a timeline. Avoid parallax that displaces actionable controls or smoothing that makes a progress indicator lag behind its meaning.
- Essential content is visible in the base layout. Add hidden reveal states only when enhancement is ready; an unavailable observer, scroll API, or JavaScript must leave readable content. With reduced motion, show reveals immediately and use a static layout for decorative travel/parallax; retain useful progress information without spatial animation.

Check initial load in the middle of the page, anchor navigation, fast forward/back scroll across a threshold, resize, and late-loading media. Triggered effects follow their once/replay policy; linked effects match current progress. Neither leaves content hidden, restarts the reading flow, or requires finishing an animation to reach an action.

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

Reduced motion must preserve open/closed visibility, selected position, focus, and operability. Do not apply blanket transform: none rules to components whose transforms encode positioning or hidden state. Remove travel transitions or define state-specific alternatives while keeping closed surfaces hidden and non-interactive. Check both open and closed states, including changing the preference while a surface is open. Replace smooth scrolling with immediate scrolling where appropriate.

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
    /* Keep the destination transform; remove animated travel, not positioning. */
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

## Coherence across an interaction sequence

Review trigger feedback, selection, content change, surface entry, dismissal, and return as one sequence where relevant. Give related transitions a consistent spatial relationship and timing vocabulary, while allowing different distances and tasks to require different durations. One animated indicator does not establish a complete motion system.

Keep outgoing and incoming content coordinated so transitions do not flash an unexplained empty region or compete for attention. Preserve the user's reading position and focus unless the next task requires a deliberate move. Surface dismissal should have a comprehensible return path; hidden surfaces must not remain interactive or exposed as active content to assistive technology. Reduced motion must preserve the same state and orientation cues without requiring travel.
