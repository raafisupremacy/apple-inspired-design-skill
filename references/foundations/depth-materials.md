# Depth and materials

Depth tells the user what floats above what. Apple's current design separates two layers:

- **Content layer:** lists, media, documents, cards. Mostly opaque, using standard materials, fills, and spacing for grouping.
- **Functional layer:** navigation bars, tab bars, toolbars, sidebars, sheets, menus, floating buttons. This layer floats above content on **Liquid Glass**.

## Liquid Glass on Apple platforms (iOS/iPadOS/macOS/watchOS/tvOS 26 and later)

Characteristics: it refracts and reflects the content beneath, adapts its tint and shadow to that content and to light/dark, uses specular highlights, and morphs fluidly between shapes (a button expanding into a menu, a tab bar minimizing on scroll). It comes in **regular** (adaptive, most uses) and **clear** (more transparent, for controls over rich media, with a dimming layer behind).

Use it like Apple does:

- Prefer system components; they adopt Liquid Glass automatically (tab bars, toolbars, sheets, navigation).
- Reserve custom glass for the functional layer; do not put content cards on glass. Transient interactive states (an activated slider or toggle) are an exception Apple documents.
- Do not stack glass on glass. Group nearby glass elements so they blend and morph together.
- Let content scroll under bars edge to edge; use scroll edge effects rather than opaque bars.
- Tint glass sparingly — a tinted primary action, not every button.

SwiftUI essentials (iOS 26+): `.glassEffect()` / `.glassEffect(.regular.tint(color).interactive(), in: .capsule)`, `GlassEffectContainer` for groups that blend, `.glassEffectID(_:in:)` for morphing, `.buttonStyle(.glass)` and `.buttonStyle(.glassProminent)`. UIKit: `UIGlassEffect` in a `UIVisualEffectView`. Check the deployment target and provide the earlier material (`.ultraThinMaterial`, `.regularMaterial`) on older OS versions.

## Material outside Apple platforms

A CSS or Flutter blur is not Liquid Glass. Recreate the hierarchy, not the optics:

```css
.glass {
  background: color-mix(in oklch, var(--color-surface) 72%, transparent);
  backdrop-filter: blur(24px) saturate(1.6);
  -webkit-backdrop-filter: blur(24px) saturate(1.6);
  border: 1px solid color-mix(in oklch, white 35%, transparent);   /* top highlight */
  box-shadow: var(--elevation-mid), inset 0 1px 0 rgb(255 255 255 / 0.25);
  border-radius: var(--radius-pill);
}
@media (prefers-reduced-transparency: reduce) {
  .glass { background: var(--color-surface-elevated); backdrop-filter: none; }
}
@supports not (backdrop-filter: blur(1px)) {
  .glass { background: var(--color-surface-elevated); }
}
```

- Flutter: `ClipRRect` + `BackdropFilter(filter: ImageFilter.blur(...))` + translucent fill; keep it to bars and sheets for performance.
- React Native: use a blur component already in the project (for example `expo-blur`); otherwise a translucent fill.
- Android/Compose: follow Material tonal elevation (surface containers) instead of faking glass; blur behind content is not a platform convention there.
- Always check text legibility over light, dark, and busy content scrolling beneath, and honor Reduce Transparency / Increase Contrast.

## Shadows and elevation

- Shadows are soft, layered, and low-opacity: a tight contact shadow plus a large diffuse one (`elevation.low/mid/floating` tokens). Never a hard dark offset.
- Tint large shadows slightly toward the brand or surface hue on colored grounds; pure black shadows on warm grounds look dirty.
- In dark mode, show elevation with lighter surfaces (`surface` → `surfaceElevated`) rather than shadows.
- Use one depth language per product: flat ground, grouped surfaces, and one floating level is usually enough.

## Borders and separators

- Hairline separators (1px at low contrast, or 0.5px on high-density screens where supported) inset to the text start in lists.
- A faint inner stroke helps glass and media edges on similar grounds. Do not outline every card.

## Sources

Checked 2026-11-26: [HIG: Materials](https://developer.apple.com/design/human-interface-guidelines/materials), [Liquid Glass technology overview](https://developer.apple.com/documentation/technologyoverviews/liquid-glass), [WWDC25: Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/), [WWDC25: Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/323/). Web and cross-platform recipes are this skill's approximations, not Apple behavior.
