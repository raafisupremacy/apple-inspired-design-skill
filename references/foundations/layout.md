# Layout and composition

Generic layouts come from repeating one pattern: the same card, the same size, the same centered stack, section after section. Apple-inspired composition gives each view **one dominant element**, groups tightly, separates generously, and varies the pattern with the job of each section.

## Grid and spacing

- **Base unit:** 8pt/dp/px with a 4 half-step (`assets/tokens.json` spacing 4…128).
- **Margins:** phones 16–20pt (20 on larger phones and for reading); tablets 24–32; web gutters 20 / 32 / 48 (compact / medium / wide) with content max ~1180px and reading max ~680px.
- **Spacing ratio:** inside a group : between groups : between sections ≈ **1 : 2–3 : 6–10**. Example: 8 between title and subtitle, 24 between cards, 96–140 between marketing sections. Apple pages are generous at the section level and tight inside groups.
- **Alignment:** a few strong alignment lines. Text edges align with media edges; numbers align on the right or on the decimal.
- **Optical adjustments:** round shapes and icons sit slightly larger than squares; text in buttons is optically centered; large headlines may need a small negative left offset to align with body text.

## Shape and radius

- **Continuous corners.** Apple uses continuous (squircle-like) curvature. SwiftUI: `RoundedRectangle(cornerRadius:style: .continuous)` (the default for many shapes). Web: `border-radius`, optionally enhanced with `corner-shape: squircle` where supported. Compose/Flutter: standard rounded corners are acceptable; avoid tiny 2–4px radii on large cards.
- **Concentric nesting.** Inner radius = outer radius − padding. A 22pt card with 8pt padding holds a 14pt image. Mismatched nested radii look amateur.
- **Scale:** controls 10–14, cards 18–30, sheets and large panels 28–38, capsules for primary buttons, chips, and segmented tracks. Keep one radius per role.

## Start from the core object, not from a pattern

Compose each view around the product's core object in its own form (`principles.md`): a countdown is a huge number, a card looks like a card, reading is the page, a map is the canvas, a deploy is a live timeline. Ask what shape the object naturally has, how big it should be, and what must sit next to it. Only then look at the catalog below for supporting structure.

## Composition patterns (options, not defaults)

Each pattern below has a job and a failure mode. Overused ones are marked; when a model reaches for them by reflex, the result reads as generated.

| Pattern | Job | Shape | Avoid when |
| --- | --- | --- | --- |
| **Statement hero** *(overused)* | introduce an idea | big headline, short subhead, one action | the product can be shown instead; the headline is a generic slogan |
| **Product stage** | show the thing | the product or real UI large, minimal copy, ground from the product | there is no real product image or UI to show |
| **Split feature** | explain one capability | text beside media | used for every section in alternation |
| **Bento / tile grid** *(overused)* | survey true peers | mixed tile sizes, each tile one idea with its own visual | features are unequal, have no distinct visuals, or need explanation |
| **Shelf / carousel** | browse a set | horizontal row with a peek of the next item, snap scrolling | items need comparison side by side; there are fewer than four |
| **Sticky story** | demonstrate a sequence | media pinned while chapters scroll and change it | content is not a sequence; on small screens (stack instead) |
| **Full-bleed media** | create presence | edge-to-edge photo/video, short text with a scrim | the image is stock or illustrative |
| **Stat row** | prove | 2–4 sourced numbers with labels | numbers are invented or unsourced |
| **Comparison** | decide | aligned columns, identical row order | there is only one real option |
| **Inset grouped list** | configure, navigate | grouped rows, headers and footers | content is visual or editorial |
| **Large-title list** | browse in apps | large title collapsing on scroll | the screen has a stronger core object to lead with |
| **Metric cards** *(overused)* | monitor several equal values | a few related values with trends | the user has one main question — answer it big instead |

## Avoiding boring layouts

- **One hero per view.** Decide what is biggest. If everything is the same size, nothing leads.
- **Vary scale and rhythm.** Follow a wide section with a tight one; a bento with a full-bleed; a dark band with a light one. Do not stack identical "heading + paragraph + three cards" sections.
- **Use bleed and asymmetry.** Media can touch the edge; a shelf can overflow the margin; a large number can sit off-center.
- **Mix cards with non-cards.** Grouped lists, open typography on the ground, full-bleed media, and dividers often beat another card. Cards are for tappable objects or genuinely separate units.
- **Give content real shapes.** Use actual images, numbers, and names; uniform placeholder boxes hide the rhythm.
- **Let color mark structure.** A colored band, a tinted section, or a category color on tiles breaks monotony with meaning.

## Responsive recomposition

Recompose, do not shrink: columns become stacks, side-by-side becomes sequential, tables become prioritized rows, sticky stories become simple sequences on small screens. Check intermediate widths and the points just before and after layout changes. Details per stack are in `../stacks/web.md` and the surface playbooks.

## Sources

Checked 2026-11-26: [HIG: Layout](https://developer.apple.com/design/human-interface-guidelines/layout), [WWDC25: Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356/) (concentricity). Pattern catalog and ratios are this skill's synthesis from Apple apps and apple.com.
