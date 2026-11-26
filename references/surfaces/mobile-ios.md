# iOS and iPhone apps

The fastest way to make an iPhone app feel Apple-quality is to use the system structure (navigation stack, large titles, tab bar, sheets, inset grouped lists) and then make the **content** vivid: real images, big numbers, the brand color in the right places, springs and press feedback everywhere.

## Screen anatomy

```text
┌──────────────────────────────┐
│ status bar                   │  content scrolls under the bars (edge to edge)
│ Large Title          (+) (⋯) │  34pt bold, left aligned; collapses into an inline title on scroll
│ [ Search                  ]  │  search in the bar or as a tab (iOS 26 search tab role)
│                              │
│  content: hero, shelves,     │  margins 16–20pt; section gaps 24–36pt
│  grouped lists, cards        │
│                              │
│ ╭──────────────────────────╮ │  tab bar: 3–5 destinations on Liquid Glass,
│ │ ⌂ Home  ◎ Browse  ☺ You  │ │  minimizes on scroll in reading contexts
│ ╰──────────────────────────╯ │
└──────────────────────────────┘
```

- **Navigation:** `NavigationStack` with large titles at the top level, inline titles deeper. System back (swipe from edge must work). No hamburger menus, no custom web-style headers with a centered logo.
- **Tab bar** for 3–5 top-level destinations; keep each tab's navigation state. Use a toolbar for actions on the current screen, not extra tabs.
- **Sheets** for focused subtasks, with detents (`.medium`, `.large`) and a grabber; full-screen covers only for immersive or multi-step flows.
- **Menus and context menus** for secondary actions instead of action sheets full of buttons.

## The home screen is the core object

The most common generated iPhone app is a large "Today" title, a gradient hero card, two stat cards with sparklines, and a list. It fits every product, so it says nothing about yours. Make the first screen the product's core object in its own form (`../foundations/principles.md`):

```text
Transit                      Banking                       Reading
────────────────────         ────────────────────          ────────────────────
Home → Office      ⇅         ╭──────────────────╮          ▔▔▔▔▔▔▔▔▔▔▔▔▔ 38%
(M2) Central                 │ card, in its own │          CHAPTER 1
4 min                        │ finish   •• 4821 │          Loomings
━━●━━━━○━━━○━━               ╰──────────────────╯          Call me Ishmael. Some
Platform 3 · on time         Available                     years ago — never mind
Later                        Rp 12.480.500                 how long precisely…
(M2) 4 min  (M4) 9 min       [Kirim] [Minta]               (the current sentence
⚠ M4 delays ~6 min           Hari ini                      softly highlighted)
[ Plan a trip…        ]      Kopi Tuku     − 38.000        [Aa]  [☰]  [🔖]
```

Different products, different first screens — none of them a template. The recipes below are structures for the rest of the app; adapt them around the object rather than starting from them.

## Screen recipes

### Content-led home (when content is the core object)

```text
Large title only if it adds orientation; otherwise lead with the object
╭────────────────────────────╮
│  FEATURED ITEM             │  a real image, artwork, or the object itself —
│  (its own form and color)  │  not a decorative gradient; press scale 0.97
╰────────────────────────────╯
Section title            See All ›
[item][item][it…  → shelf with peek, only when browsing a set matters
Grouped list of recent items
```

### Summary dashboard (only when the user truly monitors several equal values)

Lead with the one value or sentence that answers the user's main question ("You're 1,600 steps from your goal"), large. Supporting metrics follow as quiet rows or a compact group with category colors and small charts. If one value matters most, do not give it a card of the same size as the others.

### List → detail

- List: inset grouped or plain list with leading thumbnail (concentric radius), title 17, subtitle 15 secondary, trailing value or chevron.
- Detail: a **stretchy header** image or color field that scales on overscroll, title and key facts below, a row of capsule action buttons (primary filled with accent, secondary tinted with `accentSoft`), then grouped sections.

### Settings

Inset grouped list, colored rounded-square icon tiles with white SF Symbols (one color per category), trailing current values in secondary text, toggles tinted with the accent, explanatory footers under groups.

### Onboarding / What's New

Large bold title (left-aligned or centered), 3 feature rows each with an SF Symbol in the accent or a category color, a short title and one-line description, a prominent full-width Continue button at the bottom, and a secondary text button. Ask for permissions in context, not on the first screen.

### Media / immersive

Background derived from the artwork (blurred artwork or sampled color), large artwork with a soft shadow, big rounded controls, scrubber that tracks the finger. Immersive dark is right here; elsewhere start light unless the user chose dark.

### Forms and checkout

Grouped fields with persistent labels, the right keyboard type, autofill (`textContentType`), inline validation, a sticky primary action that respects the keyboard, and Apple Pay as the express option when the product supports it.

### Empty, loading, error

`ContentUnavailableView` (or equivalent) with a symbol, a clear title, one sentence, and an action. Skeletons match the final layout; use `.redacted(reason: .placeholder)` in SwiftUI.

## Component calibration

| Element | Starting point |
| --- | --- |
| Touch target | ≥ 44×44pt |
| Primary button | 50pt tall, capsule or 14pt radius, accent fill or `.glassProminent`, title Headline |
| Secondary button | tinted: `accentSoft` fill + `link` label; or bordered / plain text |
| List row | ≥ 44pt; 11–12pt vertical padding; separator inset to text start |
| Card | 18–26pt continuous radius, 16pt padding, image concentric inside |
| Margins | 16pt (20pt for reading-heavy and larger phones) |
| Grouped background | the generated `bg` (tinted), cards/rows on `surface`; or system grouped background when the brand is neutral |
| Icons | SF Symbols at the text's weight; hierarchical or palette rendering for color |

## Color on iOS

- Set the app accent with `.tint(AppColor.accent)` (and the AccentColor asset) so system controls pick it up.
- Use the brand on the primary action, selected states, links, key icons, hero fields, and charts. Use category colors where data has categories.
- A tinted ground (`palette.py --strategy tinted`) instantly looks less like a template than default white/black.
- Dark mode: generated dark roles, not pure black, unless the app is media-first.

## Motion and touch

Apply the feel kit in `../foundations/motion.md`: press feedback on every tappable card and row, springs for movement, large-title collapse, sheet detents that track the finger, `matchedGeometryEffect` or the zoom navigation transition from card to detail, `.sensoryFeedback` on selection and success, symbol effects (`.symbolEffect(.bounce)`) for small confirmations.

## Why an iOS app feels "rigid" — and the fix

| Symptom | Fix |
| --- | --- |
| Web-style header, centered logo, hamburger | Large-title navigation stack, tab bar, toolbar items |
| Black background by default | Ask for color; use generated tinted light theme; dark only by choice |
| Gray `#F2F2F2` page with white 8px-radius boxes everywhere | Inset grouped lists, fewer cards, 20pt+ continuous radii, tinted ground |
| Every text 14–17pt | Use the full Dynamic Type range: large titles, bold metrics, secondary captions |
| Hard 1px borders around everything | Separators inset in lists; spacing and fills for grouping |
| Full-width rectangular buttons on every screen | One prominent action per screen; capsules; secondary tinted or text buttons |
| No reaction to touch | Press scale/dim, springs, haptics |
| Modals that slide in from the bottom with no gesture | Sheets with detents and swipe to dismiss |
| No images, only text and icons | Hero media, thumbnails, color fields, charts |
| Custom back button and gestures that fight the system | System back, edge swipe, standard navigation |

## Accessibility

Dynamic Type through every size (layouts reflow; nothing clips), VoiceOver labels and traits, Reduce Motion and Reduce Transparency paths, Increase Contrast, 44pt targets, no color-only meaning. Implementation details live in `../stacks/swiftui.md` and `../quality/accessibility.md`.

## Sources

Checked 2026-11-26: [HIG: Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios), [HIG: Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars), [HIG: Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets), [HIG: Lists and tables](https://developer.apple.com/design/human-interface-guidelines/lists-and-tables), [WWDC25: Build a SwiftUI app with the new design](https://developer.apple.com/videos/play/wwdc2025/323/). Screen recipes and calibration values are this skill's synthesis from Apple's apps.
