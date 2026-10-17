# Web adapter

- Start mobile-first, then adapt layout for larger viewports without inventing a separate visual language.
- Use semantic HTML, logical focus order, visible focus indicators, keyboard support, and appropriate ARIA only where native semantics are insufficient.
- Preserve browser conventions: links should behave like links, back should work, and hover must never be the only feedback.
- Use responsive images, explicit dimensions, lazy loading where appropriate, and a stable placeholder to prevent layout shift.
- Use CSS/View Transitions or the project’s existing motion library progressively; provide a no-JavaScript and reduced-motion path for essential content.
- Test narrow screens, wide screens, zoom to 200%, long text, slow loading, offline failure, and pointer plus touch input.
