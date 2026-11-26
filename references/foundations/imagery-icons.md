# Imagery, icons, and user assets

## Imagery leads

- Let the real subject fill the frame: the product, a real screenshot, the user's photo, a meaningful map or chart. Crop with intent and pick the background to match the image.
- One strong image beats a grid of small ones. Give hero media enough size to be the first thing seen.
- Match the image to its claim: entity-specific images for specific items; contextual images only when they truly describe the shared context.
- Photography direction for marketing: clean ground, controlled light, real use in real places, diverse people only when the product is about people. No generic stock handshakes.
- Showing an app: real screenshots in a device or window frame, or full-bleed UI crops. Apple's official device bezels come from Apple Design Resources under Apple's terms; for non-Apple platforms use neutral generic frames.

## When there are no assets

Do not invent fake product photos or fake people. Instead:

- **Typography-led composition:** let a big headline or number be the hero.
- **Color field:** a full-bleed brand or ramp color with a single crisp element.
- **Abstract product-derived art:** soft gradients from the brand ramp, simple geometric forms, or a stylized UI fragment built from real components.
- **Labeled placeholders:** if a slot needs a real photo, mark it as a placeholder with its intended content and aspect ratio.

## Icons

| Platform | Use | Notes |
| --- | --- | --- |
| Apple platforms | SF Symbols | Match symbol weight and scale to adjacent text; use rendering modes (monochrome, hierarchical, palette, multicolor) and symbol effects for feedback. Licensed for use in apps on Apple platforms. |
| Android | Material Symbols | Choose one style (outlined/rounded) and weight across the app. |
| Web / cross-platform | The project's existing icon set; otherwise one coherent open-license family (for example Lucide or Phosphor) or a few inline SVGs | Do not use SF Symbols on the web or Android. Do not add a dependency for three icons. |

- One family, one stroke weight (≈1.5–2px at 24px), one corner style. Size icons optically with text (an icon next to 17pt text is ~17–22pt).
- Icons clarify actions and status; do not decorate every heading. Icon-only actions need accessible names.
- Do not use emoji as interface icons. Emoji are fine in user content or a deliberately playful brand voice.
- Colored icon tiles (rounded square, white glyph on a color fill) work for settings rows and categories — Apple's Settings pattern — when each color means something.

## App icons

Simple single concept, no text, strong silhouette, layered foreground on a color or gradient background. On Apple platforms design layers in Icon Composer so the system can render default, dark, clear, and tinted appearances; check legibility at small sizes and in tinted mode. For Android provide an adaptive icon with a themed monochrome layer.

## User-provided assets

Treat supplied images, logos, screenshots, video, and icons as authoritative.

- Do not silently replace, fabricate, filter, or materially alter them; keep originals and create derived crops or sizes separately.
- Inspect dimensions, aspect ratio, transparency, focal point, and quality before choosing `cover`/`contain`, crop, and placement.
- Keep logos undistorted and unfiltered; keep important screenshot content visible.
- Write alt text from what the image actually shows; mark decorative media as decorative.
- Do not send private images to external services or generators without explicit permission.
- If an asset is unsuitable, say why and offer a presentation or conversion path.

## Sources

Checked 2026-11-26: [HIG: SF Symbols](https://developer.apple.com/design/human-interface-guidelines/sf-symbols), [HIG: App icons](https://developer.apple.com/design/human-interface-guidelines/app-icons), [Apple Design Resources](https://developer.apple.com/design/resources/), [Material Symbols](https://fonts.google.com/icons).
