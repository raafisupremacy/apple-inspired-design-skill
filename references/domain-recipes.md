# Domain recipes

These are starting structures, not templates. Keep the product’s actual task, audience, data, and platform conventions in control.

## Dashboard and operations

- Lead with one decision or exception that deserves attention now.
- Use a readable summary before detail; group related metrics instead of making a wall of statistic cards.
- Let users move from summary to source records without losing filters or context.
- Include stale data, no data, partial failure, permissions, and export states.
- On compact screens, turn wide tables into prioritized rows or a detail flow; do not shrink columns until they are unreadable.

## Ecommerce and checkout

- Make product identity, price, availability, and the next action obvious.
- Keep browsing, comparison, cart, checkout, and confirmation distinct; preserve selections across navigation.
- Show totals, fees, delivery, payment state, and recovery paths before commitment.
- Treat destructive or irreversible actions carefully and never hide important terms in motion or a sheet.
- Use product imagery as content: preserve focal points, variants, zoom, loading, and failed-media states.

## Onboarding and first run

- Start with the value and let people reach the useful experience quickly.
- Ask only for information or permission when it is needed; explain why before requesting access.
- Break complex setup into focused steps with progress, skip/back, persistence, and recovery.
- Prefer a small first success over a tour of every feature.
- Respect reduced motion and do not make the user wait for decorative reveals.

## Settings and account

- Organize by user mental model and task, not by internal implementation.
- Use grouped rows, clear current values, predictable navigation, and explicit destructive recovery.
- Distinguish local preferences, account changes, privacy, security, billing, and help.
- Make unsaved changes, session state, permission state, and sign-out consequences clear.

## Social and community

- Prioritize reading, identity, context, and safe participation.
- Keep actions near the content they affect and make privacy, audience, edit, undo, report, and block states understandable.
- Handle empty feeds, moderation, loading gaps, optimistic updates, failures, and notification overload.
- Avoid using engagement motion or badges as decoration; motion should clarify new, changed, or acknowledged content.

## SaaS workspace

- Establish a stable shell, predictable navigation, and a clear current location.
- Support progressive complexity: a useful default view first, advanced filters and configuration when needed.
- Preserve context across search, filters, saved views, bulk actions, and deep links.
- Account for roles, permissions, collaboration, audit history, imports, exports, and partial failures.
- Keep dense information scannable through grouping, alignment, type, and whitespace before adding color.

## Choosing a recipe

If a product fits more than one recipe, choose the one that matches the user’s primary task, then borrow only the supporting pattern needed from the others. Do not combine every recipe into a universal dashboard.

If no recipe fits, use the custom-domain process: identify the primary task, user mental model, risk, frequency, content structure, platform constraints, and recovery needs; then create the smallest domain-specific information architecture and interaction model. Do not label an unfamiliar product as a dashboard, SaaS, or social app merely because those patterns are available.
