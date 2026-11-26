# Color

Color belongs to the user and the product. This skill never decides on its own that a product is black, white, or gray.

## Rule zero: get the color decision

1. If the user or project already has a brand color, palette, or theme, use it.
2. If not, **ask** through the intake form (`intake-form.md`): their brand color, a color they like, or "show me 3 options". For options, offer three concrete directions (seed hex + strategy + mood + one-line reason) and let them pick.
3. If they say "you decide", choose the direction that best fits the product and audience, state it in one line, and proceed.
4. Monochrome or dark is a valid choice when the user or product calls for it (a pro photo tool, a cinema app). It is never the silent default.

Never copy the bundled sample seed (`assets/tokens.json`) into a project as if it were the brand.

## How Apple actually uses color

Apple's restraint is in system chrome, not in the product:

- **System chrome is neutral, content is colorful.** Navigation bars, lists, and controls stay quiet so photos, artwork, maps, and the user's data carry the color.
- **First-party apps color-code meaning.** Health uses category colors, Fitness uses bright activity rings on black, Weather paints the sky condition, Music derives color from album art, Notes and Reminders use a signature or user-chosen list color, Wallet shows each card's own color, Calendar colors by calendar.
- **apple.com takes color from the product.** Each product page borrows its palette from the hardware finishes (for example Cosmic Orange for iPhone 17 Pro, Sky Blue for MacBook Air) and changes ground color section by section.
- **Marketing goes bold.** Flat color fields with silhouettes, campaign color series, and saturated product backdrops.
- **HIG Branding:** use the accent color judiciously; using the brand color too broadly overwhelms the interface and dilutes its impact. That is a rule about proportion, not about avoiding color.

## Choose a color strategy

| Strategy | Feels | Use for | Generator |
| --- | --- | --- | --- |
| **Quiet neutral + accent** | precise, utilitarian | finance, pro tools, settings-heavy apps, dev tools | `--strategy neutral` |
| **Tinted neutrals** | warm, premium, cohesive | most products; the best default when unsure | `--strategy tinted` |
| **Vivid surfaces** | friendly, energetic | consumer, kids, food, lifestyle, onboarding | `--strategy vivid` |
| **Immersive dark** | cinematic, focused | media, fitness, music, camera, night use | `--strategy immersive` |
| **Content / category color** | informative, alive | health, calendars, lists, analytics, multi-category data | any strategy + a category palette |
| **Product-led / color field** | iconic, campaign-like | marketing pages, ads, launches, App Store screenshots | any strategy + full-bleed brand or product color sections |

The last two are composition strategies layered on top of a generated palette: you still need accessible roles for text and controls.

### Color budget

- **App UI:** neutral or tinted ground; accent on the primary action, selection, links, and key highlights; content and category colors where they carry meaning. One screen should have one dominant accent moment.
- **Marketing:** whole sections may take the brand or product color as ground. Alternate grounds with the story (light → product color → dark → light), not randomly.
- **Data:** color encodes category or status, paired with labels or shapes. Keep the brand accent out of semantic success/warning/danger.

## Generate the palette

Use `scripts/palette.py` (standard library only) from the skill directory:

```bash
python scripts/palette.py "#F2643A"                          # CSS variables + contrast report
python scripts/palette.py "#F2643A" --strategy vivid --format report
python scripts/palette.py "#0A84FF" --strategy immersive --format swiftui
python scripts/palette.py "#2EBD85" --format compose          # also: tailwind, flutter, json
```

It preserves the seed exactly as `brand`, derives every role in OKLCH, and adjusts lightness only as far as needed so that, in both themes and against `bg`, `surface`, and `surfaceElevated`: text ≥ 7:1, secondary text ≥ 4.5:1, tertiary ≥ 3:1, link ≥ 4.5:1, label on accent ≥ 4.5:1, semantic colors ≥ 4.5:1. It also emits an 11-step `brand-50…950` ramp for gradients, illustrations, and charts.

Roles:

- surfaces: `bg`, `surface`, `surfaceElevated`, `separator`
- content: `text`, `textSecondary`, `textTertiary` (non-essential or large text only), `textInverse`
- brand: `brand` (exact seed, for hero fields and illustration), `accent`, `accentHover`, `accentPressed`, `accentSoft`, `onAccent`, `link`, `focus`
- semantic: `success`, `warning`, `danger`, `info` (independent of the brand hue)

A light brand color (yellow, mint) gets a dark `onAccent` label instead of being darkened into mud; a very dark seed is brightened for dark mode. Map the output into the project's existing theme system rather than adding a parallel token file. If the project already has tokens, validate its pairs instead of replacing them.

### When `scripts/palette.py` cannot run

Some agents have no terminal or Python (sandboxed chats, restricted IDEs). Do not fall back to black, white, or gray because of that. Use the precomputed [palette library](palette-library.md) — 14 hue families × 4 strategies, light and dark, all passing the same contrast floors:

1. **Pick the nearest entry.** Choose the library hue closest to the user's color (red, coral, orange, amber, lime, green, teal, sky, blue, indigo, violet, pink, brown, graphite) and the strategy from the intake form. Copy its `light` and `dark` lines as the role values, and its brand ramp if you need gradients or chart steps.
2. **Keep the user's color exact.** Set `brand` to the user's color in both themes.
3. **Adjust the accent only if needed.** If the user's color is close to the library seed (same family, similar brightness), keep the library's accent roles. If it is noticeably different (a deep navy versus the library blue, a pastel versus a saturated seed), set `accent` to the user's color and choose `onAccent`: near-white for mid-to-dark colors (OKLCH lightness below about 0.68), near-black for light ones (yellow, mint, pastels). Derive `accentHover` / `accentPressed` by lowering OKLCH lightness about 0.035 / 0.07 in the light theme and raising it in the dark theme. Keep the library's surfaces, text, link, and semantic roles — they are already validated.
4. **On the web, let CSS derive variants.** Relative color syntax works in current evergreen browsers, with a plain value first as a fallback:

   ```css
   --color-accent-hover: #e5582e;
   --color-accent-hover: oklch(from var(--color-accent) calc(l - 0.035) c h);
   ```

5. **Report honestly.** Library roles are measured by the generator; any role you changed is unverified until checked with a contrast tool (browser DevTools color picker, Xcode Accessibility Inspector, Android Accessibility Scanner). Say which roles you changed.

## Craft details

- **Tint the neutrals.** Pure `#FFFFFF`/`#000000` grounds with `#888` grays read as unfinished. A ground with a trace of the brand hue (chroma ≈ 0.005–0.02) feels designed.
- **Dark mode is its own palette.** Use a tinted near-black ground, lighter surfaces for elevation instead of shadows, and slightly brighter accents. Reserve pure black for OLED media, camera, and immersive watch faces.
- **Gradients only when they depict something:** the sky in a weather app, light falling on a product, a material's sheen, artwork-derived color. Use analogous ramp steps at low contrast. Decorative radial glows, color blobs, and purple-to-blue "tech" gradients are AI-slop tells (`../quality/anti-patterns.md`); flat brand color usually has more presence.
- **Color from the core object:** a transit line's color, a card's finish, a dish's tones, a book cover — let the product's own object set the accent and the hero ground when it has a color.
- **Content-derived color:** for media, sample a dominant color from the artwork, then darken or lighten it in OKLCH until text on it meets contrast. Add a scrim when text sits on photos.
- **Category palettes:** pick 5–8 hues spaced around the wheel at similar lightness and chroma (OKLCH makes this easy), then check each against both themes. Pair every color with a label or icon.
- **Selection and state:** selected = accent or `accentSoft` fill with `link` text; disabled = reduced contrast plus a non-color cue; never use only a color change to show state.
- **Hairlines:** separators are low-contrast on purpose; anything that conveys state needs ≥ 3:1.

## Validation

- Measure each rendered text/icon color against its actual background in light, dark, increased contrast, and every interaction state (hover, pressed, selected, focus, disabled, error).
- Check composited colors when opacity, blur, gradients, photos, or overlays are involved.
- Dark mode is not done when the background changes: recheck headings, secondary text, links, badges, on-accent labels, focus rings, and status colors.
- `scripts/palette.py` checks its own generated roles only. It does not see the user's rendered UI; report which pairs you actually measured.

## Sources

Checked 2026-11-26: [HIG: Color](https://developer.apple.com/design/human-interface-guidelines/color), [HIG: Branding](https://developer.apple.com/design/human-interface-guidelines/branding), [HIG: Dark Mode](https://developer.apple.com/design/human-interface-guidelines/dark-mode), Apple's regional store pages for current product finishes. Descriptions of first-party apps and campaigns are observations, not Apple rules.
