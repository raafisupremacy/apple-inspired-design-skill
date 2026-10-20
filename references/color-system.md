# Color and tokens

Ask for a brand color when one exists. Otherwise start with a neutral surface/content palette and one restrained accent. Never hard-code component colors when tokens can express the role.

## Token roles

Define roles rather than a fixed hue:

- surfaces: background, surface, elevated surface, separator, overlay
- content: primary, secondary, tertiary, inverse, link
- accent: default, hover, pressed, soft, on-accent, focus
- semantic: success, warning, danger, info, disabled

Derive variants in a perceptual color space such as OKLCH, then validate them. Do not derive success, warning, or danger from the brand accent. Dark mode is a separate accessible palette, not simply an opacity or brightness inversion.

## Materials and content layers

For Apple platforms that support Liquid Glass, prefer the system component's material behavior. Apple's Materials guidance reserves Liquid Glass for the functional controls/navigation layer, not content cards; transient interactive elements such as activated sliders and toggles are a documented exception. Standard materials may differentiate regions within content. Choose materials by semantic purpose, not a screenshot's apparent tint.

For custom translucent surfaces, check foreground legibility over representative light, dark, and busy backgrounds while content scrolls beneath them. Honor available Reduce Transparency and Increase Contrast settings. On web or Android, preserve the hierarchy using the project's platform components and an opaque fallback where needed; a CSS blur is not equivalent to Apple's adaptive material. Do not introduce glass just to signal Apple inspiration.

## Validation

- Check text and essential icons against their actual background.
- Target WCAG AA contrast for web text: 4.5:1 for normal text and 3:1 for large text; use platform guidance as an additional check for native UI.
- Pair color with text, shape, iconography, or position for status and charts.
- Test light, dark, increased contrast, disabled, focus, hover, pressed, and selected states.

When producing tokens, use the selected project's existing theme format and semantic roles: for example CSS custom properties on web, theme resources or Compose tokens on Android, and the existing native or framework theme on other platforms. Supply framework-neutral JSON or additional mappings only when requested or needed by the project's shared-token workflow. Do not create unused parallel token files.

## Dark-mode gate

Dark mode is not complete when the background changes. Recalculate the rendered foreground/background pair for every important role and state in the dark theme, including headings, primary/secondary/tertiary text, links, icons, badges, borders that convey state, on-accent labels, buttons, overlays, focus, hover, pressed, selected, disabled, and error/success/warning treatments. A light-theme pass does not carry over to dark mode.

Reject the result when important text or a control label becomes low contrast, even if the color is part of the brand palette or resembles a familiar platform color. Prefer a dark-theme role with enough separation over darkening text until hierarchy disappears. Check the actual composited color when opacity, blur, gradients, photos, or overlays are involved. Also check that the chosen text role still communicates hierarchy; a technically passing ratio can remain too weak for primary content if adjacent roles are indistinguishable.

## Check the rendered pair

Measure foreground against the actual rendered background in each relevant theme and interaction state, including on-accent button labels, secondary text, and overlays. Account for transparency and image backgrounds. Essential non-text indicators need appropriate contrast (generally 3:1 against adjacent colors under WCAG); distinguish these from decorative borders and exempt inactive controls.

The bundled validator checks starter token structure, directly mapped light-theme CSS/JSON value parity, and primary text/background contrast. It does not validate all foreground/background pairs, theme states, or composited pixels; do not use its success as evidence that a project's palette passes. Record the specific pairs checked and label unmeasured states as unverified.
