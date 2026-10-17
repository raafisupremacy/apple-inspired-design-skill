# Accessibility, content, and states

Write short, concrete labels. Error messages explain what happened and the next action. Permission requests explain why access is needed before the system prompt. Do not use exclamation marks or vague success messages when a precise status is possible.

Support localization, long strings, pluralization, dates, currencies, RTL layouts, and user-entered content. Never rely on color, animation, sound, or position alone to convey meaning.

Every important flow considers loading, empty, error, offline, disabled, permission denied, validation, success, and destructive confirmation. Time-limited messages need an accessible alternative; focus and announcements must move predictably.

## Content truth and state consistency

Keep one source of truth for any user-selected entity or value. When a user changes a variant, account, date, filter, quantity, or theme, synchronize every dependent image, label, price, summary, alt text, and action—or clearly mark a deliberately fixed reference state. Review visible content and accessibility text together; a correct visual state with stale alt text is still a bug.

Separate supplied facts from illustrative copy. Do not invent reviews, ratings, certifications, medical claims, guarantees, inventory, prices, or performance numbers to make a surface feel complete. Mark placeholders as placeholders and request verification before publishing them.

## Operable controls, not attributes alone

Prefer native controls or established accessible project components. For custom controls:
- Tabs need tab/panel associations, a reachable active tab, arrow-key movement appropriate to orientation, and an explicit automatic or manual activation policy. With manual activation, Enter/Space selects the focused tab. Do not remove inactive tabs from the Tab order without implementing navigation within the group.
- Radio groups expose one checked value and support the platform's group navigation. Checkboxes permit independent choices; toggle buttons expose pressed state. Focus and selection are distinct.
- Sliders announce meaningful values and units, not implementation indexes. Use aria-valuetext or the native equivalent when numeric storage differs from the displayed meaning.
- Every input has a persistent associated label; a placeholder is supplementary. Every selected swatch or thumbnail exposes its state as well as its name.
- Check icons against the action or concept they depict. Hide decorative icons from assistive technology; name icon-only actions.

Walk through keyboard entry, movement, activation, and exit. Check touch and pointer selection, then confirm that visible content and accessible state agree. An ARIA attribute is not evidence that this behavior works.

For calculators, simulations, charts, and forecasts, distinguish measured data from estimates and illustrative output. Put units, assumptions, relevant conditions, and uncertainty near the result; precision must not imply evidence the product does not have.
