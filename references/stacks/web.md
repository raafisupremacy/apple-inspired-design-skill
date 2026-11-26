# Web implementation (HTML, CSS, Tailwind, React and similar)

Use the project's existing framework, component library, and styling approach. These recipes show how to express the foundations in that stack.

## Tokens

1. Generate colors: `python scripts/palette.py "<seed>" --strategy <s> --format css` (and `--format tailwind` for a Tailwind config mapping).
2. Put the CSS variables in the project's global stylesheet or theme layer; map them into the existing theme (Tailwind config, CSS-in-JS theme, design-token pipeline) instead of creating a parallel system.
3. Copy only the non-color tokens you use from `assets/tokens.css` (type scale, spacing, radius, elevation, motion, springs).
4. Theme switching: system preference by default, explicit override with `data-theme="light|dark"` on `<html>` (the generated CSS supports both). Persist the user's override if the product has a theme toggle.

## Base styles that set the tone

```css
html { color-scheme: light dark; -webkit-text-size-adjust: 100%; }
body {
  margin: 0;
  background: var(--color-bg);
  color: var(--color-text);
  font: var(--text-body-weight) var(--text-body-size)/var(--text-body-leading) var(--font-sans);
  -webkit-font-smoothing: antialiased;
  text-rendering: optimizeLegibility;
}
h1, h2, h3 { text-wrap: balance; letter-spacing: var(--text-title1-tracking); }
p { text-wrap: pretty; max-width: 68ch; }
.num { font-variant-numeric: tabular-nums; }
:focus-visible { outline: 3px solid var(--color-focus); outline-offset: 2px; border-radius: inherit; }
```

## Components

```css
.button {
  display: inline-flex; align-items: center; justify-content: center; gap: 8px;
  min-height: 44px; padding: 0 22px; border: 0; border-radius: var(--radius-pill);
  background: var(--color-accent); color: var(--color-on-accent);
  font: 600 1.0625rem/1 var(--font-sans);
  transition: transform var(--spring-snappy-duration) var(--spring-snappy),
              background-color var(--motion-fast) var(--ease-enter);
}
.button:hover { background: var(--color-accent-hover); }
.button:active { transform: scale(var(--press-scale)); background: var(--color-accent-pressed); }
.button--tinted { background: var(--color-accent-soft); color: var(--color-link); }

.card {
  background: var(--color-surface); border-radius: var(--radius-lg); padding: var(--space-5);
  box-shadow: var(--elevation-low);
  transition: transform var(--spring-snappy-duration) var(--spring-snappy);
}
.card:active { transform: scale(var(--press-scale)); }
@supports (corner-shape: squircle) { .card, .button { corner-shape: squircle; } }

@media (prefers-reduced-motion: reduce) {
  .button, .card { transition: background-color var(--motion-reduced) linear; }
  .button:active, .card:active { transform: none; }
}
```

Use `linear()` spring tokens only where supported (all current evergreen browsers support `linear()`; older ones fall back to the browser default easing if you add a plain `ease-out` declaration before it).

## Layout recipes

- Container: `width: min(100% - 2 * var(--layout-gutter-compact), var(--layout-content-max)); margin-inline: auto;` with larger gutters via media queries or `clamp()`.
- Bento: CSS Grid with `grid-template-columns: repeat(6, 1fr)` and tiles spanning 2/3/6 columns; collapse to one column on compact widths.
- Shelf: `display: grid; grid-auto-flow: column; grid-auto-columns: min(80%, 360px); overflow-x: auto; scroll-snap-type: x mandatory;` with `scroll-padding` equal to the gutter and visible previous/next buttons on pointer devices.
- Sticky story: a two-column grid where the media column is `position: sticky; top: <nav height>`; on compact widths stack chapters with their own media.
- Container queries for reusable components; viewport queries for page composition. Never let the page scroll sideways.

## Motion on the web

- View Transitions (`document.startViewTransition`, cross-document `@view-transition`) for shared elements and page changes, with no-op fallback.
- Scroll-driven animations (`animation-timeline: view()/scroll()`) behind `@supports`, Intersection Observer otherwise, static content without either.
- Framer Motion / Motion One / GSAP only if already in the project; map the spring presets from `../foundations/motion.md`.

## Quality

Semantic HTML, keyboard support, visible focus, `prefers-reduced-motion`, `prefers-reduced-transparency`, `prefers-contrast`, zoom to 200%, responsive images with dimensions, no layout shift, works without JavaScript for essential content. Check narrow, intermediate, and wide widths; touch and pointer; light and dark.

## Browser support

Feature-detect optional APIs (`@supports`, `CSS.supports`, `'startViewTransition' in document`). Treat unsupported features as graceful fallbacks, not errors. Prefer viewport, container, input, and preference signals over user-agent sniffing.
