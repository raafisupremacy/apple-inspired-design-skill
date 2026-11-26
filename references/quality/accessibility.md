# Accessibility, states, and controls

Accessibility is part of the craft, not a final filter. These requirements hold on every surface.

## Perception

- Contrast: text 4.5:1 (3:1 for large text), essential icons and state-conveying borders 3:1, in every theme and state (`../foundations/color.md`).
- Never use color, motion, sound, or position alone to convey meaning; pair with text, shape, or icon.
- Support system text scaling (Dynamic Type, Android font scale, browser zoom 200%): rows grow, metadata stacks, columns reduce before essential text truncates.
- Honor Reduce Motion, Reduce Transparency, Increase Contrast, and dark mode.

## Operation

- Touch targets ≥ 44pt (iOS/web) or 48dp (Android); adequate spacing between targets.
- Every gesture has a visible alternative (button, menu, keyboard action, back).
- Full keyboard operation on web and desktop: logical order, visible focus, Escape closes overlays, focus returns to the trigger.
- Time-limited messages have an accessible alternative; critical messages do not auto-dismiss.

## Controls: choose by purpose, then style

- **Tabs** for associated content panels (tab/panel association, arrow keys, explicit activation policy).
- **Segmented control** for 2–5 mutually exclusive views or modes.
- **Radio group** for one value; **checkboxes** for independent choices; **toggle/switch** for on/off settings; **toggle button** (pressed state) for actions; **links** for destinations.
- **Sliders** announce meaningful values and units (`aria-valuetext` or native equivalent).
- Every input has a persistent label; placeholders are hints only. Swatches and thumbnails expose their name and selected state.
- Prefer native or established accessible components. An ARIA attribute is not evidence that behavior works; walk through entry, movement, activation, and exit.

## Screen readers

Name icon-only actions; hide decorative images and icons; describe informative images by what they show; group related elements into one meaningful element; announce state changes and errors; keep visible text and accessible text in sync when selections change.

## States every flow considers

Loading, empty, error, offline, partial failure, disabled, permission denied, validation, success, destructive confirmation, undo. Distinguish pending work from completed work and keep the user's input recoverable.

## Localization

Long strings and text expansion, right-to-left layouts, plurals, local date/number/currency formats, user-entered names and content.

## Data and estimates

For charts, calculators, and forecasts, separate measured data from estimates and illustrative output; place units, assumptions, and uncertainty near the value. Provide a text or table alternative for charts.
