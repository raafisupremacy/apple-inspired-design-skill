# Typography

Type does most of the work in an Apple-inspired design. The signature is **contrast between levels**: large, tight, heavy headlines over calm, readable body text, with clear secondary and caption roles.

## Choose the typeface

| Target | Use | Notes |
| --- | --- | --- |
| iOS, iPadOS, macOS, watchOS, visionOS | The system font through system text styles (SF Pro, SF Compact, SF Pro Rounded, New York) | Use `Font.title`, `.body`, `UIFont.preferredFont(forTextStyle:)` so Dynamic Type works. Add `.fontDesign(.rounded)` or `.serif` for personality. |
| Web | `-apple-system, BlinkMacSystemFont, …` stack (in `assets/tokens.json`) | Shows SF on Apple devices, Segoe UI Variable on Windows, Roboto on Android. **Do not self-host SF font files**: Apple licenses them for designing and developing for Apple platforms. |
| Web needing one consistent face on every OS | A licensed font with similar qualities: Inter (use Inter Display for large sizes), Geist, or the brand's font | Only add a font when the project allows it; bundle or load it per the project's conventions. |
| Android / Compose | Roboto/Roboto Flex or the brand font via Material type roles | Do not force SF on Android. |
| Editorial or premium accents | A serif for display or long reading (New York on Apple platforms; Newsreader, Source Serif, or the brand serif elsewhere) | Use for one role, not everything. |

Verify a font is actually available before tuning metrics to it; if it falls back, recalibrate size, weight, and tracking.

## Scales

### Apple platforms — Dynamic Type defaults (Large content size)

| Style | Size / leading (pt) | Weight |
| --- | --- | --- |
| Large Title | 34 / 41 | Regular (Bold when emphasized) |
| Title 1 | 28 / 34 | Regular |
| Title 2 | 22 / 28 | Regular |
| Title 3 | 20 / 25 | Regular |
| Headline | 17 / 22 | Semibold |
| Body | 17 / 22 | Regular |
| Callout | 16 / 21 | Regular |
| Subheadline | 15 / 20 | Regular |
| Footnote | 13 / 18 | Regular |
| Caption 1 | 12 / 16 | Regular |
| Caption 2 | 11 / 13 | Regular |

Use the styles, not these numbers: they scale with the user's text size. Apply `.bold()` / emphasized weights to create stronger titles — current Apple apps use bolder titles and left alignment in key moments like onboarding and alerts.

### Android — Material 3 roles

Display L/M/S 57/45/36, Headline L/M/S 32/28/24, Title L/M/S 22/16/14, Body L/M/S 16/14/12, Label L/M/S 14/12/11 (sp). Map: Large Title → Headline L or Display S; Headline → Title M (semibold); Body → Body L; Footnote → Body S; Caption → Label M.

### Web — fluid scale

The starter tokens define `display`, `title1`, `title2`, `title3`, `eyebrow`, `headline`, `body`, `callout`, `subhead`, `footnote`, `caption` with `clamp()` sizes. Marketing calibration that reads as apple.com-like:

- Hero headline: 48–96px, weight 600–700, leading 1.0–1.08, tracking −0.02 to −0.035em.
- Intro / subhead paragraph: 21–28px, weight 400–500, leading 1.3–1.4, often in `textSecondary` with a key phrase in `text` or `brand`.
- Section headline: 40–64px. Body: 17–19px at leading 1.45–1.55, max ~68ch.
- Eyebrow (product name, "New"): 17–21px semibold, sometimes in `brand`/`link` color. Avoid all-caps tracking-heavy eyebrows unless the brand uses them.

## Rules that create the look

- **Make the jump big.** Adjacent levels should differ by at least 1.25× in size or a clear weight step. A page where everything is 14–20px looks generic.
- **Tighten large type, loosen tiny type.** Negative tracking above ~28px; neutral body; slight positive tracking at 12px and below. (System SF applies optical tracking automatically; apply it manually for Inter and others.)
- **Weight carries hierarchy.** Semibold/bold for titles and key numbers, regular for reading, medium for small labels. Avoid thin weights below 20px.
- **Numbers are design elements.** Big numerals for the key metric (Fitness/Health style) with a small unit label beside them; `font-variant-numeric: tabular-nums` (or `.monospacedDigit()`) where numbers update or align.
- **Wrap with intent.** `text-wrap: balance` for headings, `text-wrap: pretty` for paragraphs; control line breaks in heroes so a single word never dangles.
- **Alignment:** left-aligned in apps and reading; centered is fine for short marketing heroes and statement sections.
- **Color for hierarchy:** `text` for primary, `textSecondary` for supporting, accent only for links or one emphasized phrase.

## Hierarchy recipes

```text
Product hero:     Product name (19 semibold) / one specific claim (80 bold, −0.03em) / supporting line (24, secondary) / one action — beside or above the product itself
Core-object hero: the object's own number or text at display size (a 112pt countdown, a 34pt balance, the page in a reading face) / one line of context
List row:         Title (17 regular or semibold) / Subtitle (15 secondary) / trailing value (17 secondary, tabular)
Metric card:      Label (13 semibold, secondary) / Value (34–48 bold, tabular) + unit (17 secondary) / delta (13, semantic + icon)
Detail header:    Large title (34 bold) / meta line (15 secondary) / primary action
Card in a shelf:  Category (12 semibold, accent or secondary) / Title (20–22 bold) / one-line description (15 secondary)
```

## Accessibility and scaling

- Use semantic text roles so sizes follow system settings (Dynamic Type, Android font scale, browser zoom to 200%).
- At large sizes let rows grow, stack metadata, and reduce columns before truncating. Never disable scaling to protect a layout.
- Truncate only previews, with a way to read the full text. Keep comfortable leading for multiline text.
- Custom fonts must still scale (`UIFontMetrics`, `relativeTo:` in SwiftUI, `sp` units, `rem` on web).

## Sources

Checked 2026-11-26: [HIG: Typography](https://developer.apple.com/design/human-interface-guidelines/typography), [Apple Fonts](https://developer.apple.com/fonts/) (license terms accompany the downloads), [Material 3 type scale](https://m3.material.io/styles/typography/type-scale-tokens). Marketing calibration values are this skill's starting points from observing apple.com, not Apple specifications.
