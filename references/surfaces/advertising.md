# Advertising, social, and store assets

Apple's advertising is famous for reduction: one subject, one message, a handful of words, a small logo, and either a stunning image or a bold color field. "Shot on iPhone" put the user's photograph as the entire ad with a one-line credit; the silhouette campaigns used flat saturated color and a single figure; the "Colors" series hand-picked locations so color would pop.

## Principles

1. **One subject.** The product, the person's photo, or the outcome — not a feature list.
2. **One message, few words.** Headline 2–6 words; billboards ≤ 7 words total because people read them in seconds.
3. **Image or color does the talking.** Full-bleed photography or a flat brand-color field; no clutter.
4. **Small, confident brand mark.** Logo or product name small, usually at the bottom or top center; generous clear space.
5. **Consistent system.** A campaign is a family: same grid, type, logo placement, and color logic across formats.
6. **Truthful.** Real product, real photos, real claims with sources. Mark simulated screens as such where required.

Do not imitate Apple's ads one-to-one, use Apple's trademarks or campaign names, or imply Apple endorsement.

## Formats (check each network's current spec)

| Format | Size | Notes |
| --- | --- | --- |
| Feed square / portrait | 1080×1080, 1080×1350 | Headline readable at thumbnail size; subject centered |
| Stories / Reels / TikTok | 1080×1920 | Keep text and logos out of roughly the top and bottom 250px (UI overlays) |
| Landscape video / YouTube | 1920×1080 | Message in the first 3 seconds; captions on |
| Display banners | 300×250, 728×90, 160×600, 320×50, 300×600 | Logo, 3–5 word line, one CTA; animation short and stopping; under the network's file-size limit |
| Billboard / OOH | ratio per site | ≤ 7 words, huge type, extreme contrast, legible at distance |
| App Store screenshots | per App Store Connect's required device sizes (6.9" iPhone first) | First 2–3 tell the story; caption 3–6 words above the screen; consistent background system |
| Google Play graphics | feature graphic 1024×500 + screenshots | Same story, Android device frames |

## Layout systems

```text
Product hero          Color field             Photo-led             Store screenshot
┌──────────┐          ┌──────────┐            ┌──────────┐          ┌──────────┐
│ Headline │          │          │            │          │          │ Caption  │
│          │          │  figure  │            │  photo   │          │ ┌──────┐ │
│ [product]│          │          │            │          │          │ │screen│ │
│          │          │ headline │            │ credit   │          │ │      │ │
│   logo   │          │   logo   │            │   logo   │          │ └──────┘ │
└──────────┘          └──────────┘            └──────────┘          └──────────┘
```

- Use the brand palette from `scripts/palette.py`; color-field ads use the exact `brand` seed or a ramp step as ground, with text roles checked for contrast.
- Type: one family, bold headline with tight tracking, small regular supporting line.
- Motion ads: one movement that reveals the product or message, then hold on the end frame with the logo. Respect reduced motion where the platform exposes it.

## Workflow

1. Define the single message and the audience.
2. Pick the hero (photo, product, color field, UI) and the format list.
3. Design the master (usually 1080×1350 or 1080×1920), then adapt per format — recompose, don't just scale.
4. Check legibility at thumbnail size and at distance, safe zones, contrast, and claim sources.
5. Export per network spec; keep originals of supplied assets untouched.

## Sources

[PhoneArena: How "Shot on iPhone" became iconic](https://www.phonearena.com/news/how-shot-on-iphone-became-a-thing_id136380), [Cannes Lions: Shot on iPhone – Colors](https://www.lovethework.com/work-awards/campaigns/shot-on-iphone-colors-31508), [App Store Connect screenshot specifications](https://developer.apple.com/help/app-store-connect/reference/screenshot-specifications/). Formats change often; verify against each platform before export.
