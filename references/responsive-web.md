# Responsive web quality

Responsive design is a change in composition, interaction, and content priority, not merely a smaller desktop layout.

## Layout

- Start with the narrowest useful layout, then add columns, panes, and navigation space as the viewport allows.
- Prefer fluid constraints such as `max-width`, `min()`, `max()`, `clamp()`, flexible grids, and container queries over a long list of device-specific breakpoints.
- Keep reading measure, touch targets, and hierarchy stable while changing composition.
- Let tables, media, code, and other exceptional content have an intentional overflow strategy. Never make the whole page scroll sideways.
- Test real content at narrow mobile, larger mobile, tablet, desktop, and zoomed browser sizes. Include long labels, translated text, empty data, and user-provided media.
- Prefer container queries for reusable components whose layout depends on their parent, and viewport queries for page-level composition. Components should remain usable when placed in an unexpected container.

## Navigation and interaction

- A mobile menu is a real focus-managed surface: it has a clear trigger, enter/exit motion, escape/back behavior, focus restoration, and a reduced-motion path.
- Preserve the user’s position and context when navigation collapses or expands.
- Use hover only as an enhancement. Every important action works with touch, keyboard, and a coarse pointer.
- Infinite scroll is appropriate for content discovery, not for workflows that need a reachable footer, stable URLs, or deliberate pagination. Provide loading, end-of-list, retry, and keyboard-accessible alternatives.

## Theme and offline behavior

- Define semantic tokens once and support system preference plus an explicit user override when the product needs it.
- Theme switching changes roles, not component-specific hard-coded colors. Recheck contrast in every theme and state.
- For a PWA or offline-capable app, distinguish cached content, stale content, unavailable content, and a failed mutation. Keep the user’s work recoverable.

## Performance and discoverability

- Prevent layout shift with intrinsic media dimensions, stable skeletons, and reserved regions.
- Lazy-load below-the-fold media and expensive content, but do not lazy-load the first meaningful content without reason.
- Use Intersection Observer or native view-timeline features for visibility-based work, with a non-animated fallback. Do not attach scroll handlers that repeatedly force layout.
- Use a capability or Baseline check before shipping a newer CSS or browser API as a requirement. Treat unsupported behavior as a graceful fallback, not an error screen.
- Treat Lighthouse, Web Vitals, semantic HTML, metadata, and share previews as quality checks. A high score does not prove good hierarchy, accessibility, or platform fit.

## Progressive enhancement

The essential page must work without JavaScript-heavy motion, unsupported browser APIs, or a service worker. Add View Transitions, scroll-driven effects, PWA caching, and richer gestures when support and product value justify them.

For narrow controls, inspect the real labels and target sizes, not just page overflow. Adapt navigation priority, label wording, and control composition when wrapping makes the interface harder to operate. Keep accessible names meaningful after shortening visible labels. Aim for comfortable touch targets (commonly about 44 CSS px on web); evaluate spacing and input context rather than confusing that comfort target with every platform's conformance minimum.
