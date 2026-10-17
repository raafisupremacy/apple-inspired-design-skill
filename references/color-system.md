# Color and tokens

Ask for a brand color when one exists. Otherwise start with a neutral surface/content palette and one restrained accent. Never hard-code component colors when tokens can express the role.

## Token roles

Define roles rather than a fixed hue:

- surfaces: background, surface, elevated surface, separator, overlay
- content: primary, secondary, tertiary, inverse, link
- accent: default, hover, pressed, soft, on-accent, focus
- semantic: success, warning, danger, info, disabled

Derive variants in a perceptual color space such as OKLCH, then validate them. Do not derive success, warning, or danger from the brand accent. Dark mode is a separate accessible palette, not simply an opacity or brightness inversion.

## Validation

- Check text and essential icons against their actual background.
- Target WCAG AA contrast for web text: 4.5:1 for normal text and 3:1 for large text; use platform guidance as an additional check for native UI.
- Pair color with text, shape, iconography, or position for status and charts.
- Test light, dark, increased contrast, disabled, focus, hover, pressed, and selected states.

When producing tokens, offer CSS custom properties and JSON. Add SwiftUI, React Native, or Flutter mappings only when that stack is relevant.
