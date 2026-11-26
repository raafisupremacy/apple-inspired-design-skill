# Principles and design direction

Apple-inspired quality comes from a chain of confident decisions, not from a gray-and-blue look. Apple's own products range from the quiet utility of Settings to the neon of Fitness, the sky gradients of Weather, and the product-colored pages of apple.com. What they share is craft.

## What makes an interface feel Apple

Use these eight signals to judge a direction and to diagnose "it looks generic":

1. **Confident type contrast.** Big, tight headlines next to calm body text. The jump between levels is large; mid-sized everything reads as generic.
2. **Content is the hero.** The photo, the product, the number, the map, the user's data leads; chrome steps back.
3. **One clear color story.** A deliberate palette tied to the product: a brand hue, content colors, or a product finish. Not "no color", and not every color.
4. **Generous, purposeful space.** Large section spacing, tight related groups. Space shows what belongs together.
5. **Soft, continuous geometry.** Continuous (squircle-like) corners, concentric nesting, capsule buttons, consistent radii.
6. **Layered depth with meaning.** Content below; controls and navigation float above on a material. Depth explains relationships.
7. **Physical, responsive motion.** Springs, press feedback, gestures that track the finger, transitions that keep object identity.
8. **Obsessive detail.** Optical alignment, tabular numbers, real states, precise copy, nothing left as a default.

A design that hits one or two signals feels "clean". One that hits most of them feels Apple-inspired. Rigid, boxy, monochrome, and uniform layouts miss 1, 3, 4, 5, and 7 at once — the most common failure.

The signals are qualities, not ingredients. Adding a glow, a glass bar, a bento grid, and big type to a generic layout produces a familiar AI look, not an Apple-inspired one. Specificity comes first: see the core object below.

## Apple's stated foundations

Apple's HIG frames current design around **hierarchy** (controls and interface elevate and distinguish the content beneath them), **harmony** (align with the concentric design of hardware and software), and **consistency** (adopt platform conventions so a design adapts across window sizes and displays). Earlier and still useful: clarity, deference, depth. Translate them:

- **Hierarchy:** rank content and actions; make the primary one unmistakable through size, weight, position, and color — in that order.
- **Harmony:** shapes, radii, and spacing relate to each other and to the device; nested corners stay concentric.
- **Consistency:** familiar patterns for navigation, input, and feedback; equivalent controls look and behave alike.
- **Deference:** quiet does not mean low contrast or empty. It means chrome yields to content.
- **Agency and responsibility:** show what is happening, keep the user in control, make recovery easy, collect less data, explain permissions.

## Find the core object (the anti-template step)

Apple's designs are not memorable because of a style. They are memorable because each one is built around the one thing only that product has: Weather is the sky, Wallet is the stack of cards, Fitness is the rings, Camera is the viewfinder, an iPhone product page is the phone itself. Generic, "AI-generated" design is the opposite: a layout that would fit any product.

Before choosing any layout pattern, name the **core object**:

1. **What does this product have that no other product has?** A specific piece of data (the next departure in 4 minutes, today's balance, the page you are reading), a physical object (the card, the dish, the plant), or a moment (the countdown, the delivery arriving, the streak continuing).
2. **Make it the hero, in its own form.** A countdown is a huge number, a card looks like a card, reading is the text itself, a map is the canvas. Do not put the core object in a generic card next to other generic cards.
3. **Derive the rest from it.** Its color, shape, and motion inform the palette, the radii, and the signature transition. Secondary content gets quieter, simpler treatments.

Examples:

| Product | Core object | Hero becomes | Avoid |
| --- | --- | --- | --- |
| Transit | next departure | giant countdown with the line color, live track below | a "Today" title with stat cards |
| Banking | the card and available balance | a physical-looking card stack and one big tabular number | a gradient hero card with a glow |
| Reading | the text | the page itself in a reading face, progress as a hairline | a "Continue reading" card with a cover thumbnail |
| Recipe | the dish and the current step | full-bleed dish photo, then one step at a time with its timer | a grid of identical recipe cards |
| Dev platform | the deploy state | a live timeline of the current deploy | four KPI tiles |

### The swap test

Before accepting a direction, mentally replace the logo, name, and content with a different product. If the design still works unchanged, it is a template — redo the composition around the core object. Color alone never passes the swap test: a recolored template is still a template.

## Design Direction intake (do this before visual work)

Before a new surface or a change of visual direction, settle these with the user. Reuse anything already decided in the project; ask only what is unknown and changes the result.

| Decision | Ask / propose |
| --- | --- |
| Surface | iOS app, Android, cross-platform, marketing site, web app/SaaS, dev tool, commerce, ad, deck, email, desktop, watch, spatial |
| Audience and primary task | Who, doing what, how often, under what risk |
| **Core object** | The one thing only this product has; the composition is built around it (see above) |
| **Color** | The user's brand or chosen color and a strategy (`color.md`). **If none is given, ask, or offer three concrete directions. Never silently fall back to black/white/gray + system blue.** |
| Mood | A point on the quiet ↔ expressive dial: utility, calm premium, warm friendly, bold energetic, cinematic |
| Density | Spacious editorial, balanced, or dense operational |
| Type voice | System font, a licensed brand font, or a pairing (`typography.md`) |
| Signature | One or two memorable moves: a hero composition, a motion moment, a shape, an image treatment |

When offering three directions, make them genuinely different (for example: warm tinted neutrals with a coral accent; vivid content colors on light ground; immersive deep-blue dark). For each give the seed, strategy, mood, and why it fits the product. If the user says "you choose", pick one, state it in one line, and proceed.

Summarize the brief compactly:

```text
surface/input → audience + primary task → core object → next action
→ color (seed + strategy) → mood → density → type → signature → assumptions
```

## Decide in order

1. **Purpose:** the user outcome in one sentence.
2. **Core object:** what only this product has, and how it becomes the hero.
3. **Hierarchy:** rank content and actions; cut what does not serve the outcome.
4. **Structure:** the smallest clear set of screens, sections, and destinations.
5. **Interaction model:** platform-native navigation, input, feedback, recovery.
6. **Composition:** shape the layout around the core object; borrow a pattern from `layout.md` only when it serves it.
7. **Identity:** color story, type voice, imagery, signature — derived from the core object where possible.
8. **Depth and motion:** materials for floating chrome, springs and transitions with purpose.
9. **States and verification:** loading, empty, error, offline, permission, success; accessibility; real content; the swap test.

Identity is not optional: a correct but colorless, motionless, uniform result is unfinished work, not restraint. Neither is specificity: a polished layout that fails the swap test is unfinished too.

## Resolve trade-offs

When values conflict, prefer in this order unless the user chooses otherwise:

1. Safety, accessibility, privacy, data integrity, recoverability.
2. The user's stated goal, content, brand, and technical constraints.
3. Platform conventions and input comfort.
4. Performance and resilience.
5. Visual polish.

Never use "Apple style" to override accessibility, platform behavior, or the product's own identity. State a deliberate exception in one sentence.

## Brand adaptation

Apple-inspired means borrowing clarity, craft, and care — not Apple's identity.

- Map the brand to semantic roles (`color.md`); do not paint every component in the brand hue, and do not hide it either.
- Express personality through a small set of related decisions: composition, type scale and weight, density, imagery, control shape, depth, motion. A font and accent swap alone is not identity.
- Choose at most one or two signature moves per surface and let the rest support them.
- Distinguish three things the user might mean: Apple's **principles** (default), an explicitly requested **apple.com-like look** (translate its composition, type roles, imagery, and motion while keeping the product's identity), and **native platform conventions** (required on Apple platforms, not on Android).

## Custom domains

Domain playbooks are starting points. When none fits, derive structure from the product's vocabulary, the user's mental model, task frequency, risk, collaboration, and recovery path. Name the new pattern in plain language and keep it local to the product.

## Boundaries

- Do not copy Apple logos, product imagery, proprietary UI artwork, or marketing text. Do not imply Apple endorsement.
- SF fonts and SF Symbols are licensed for Apple-platform use; see `typography.md` and `imagery-icons.md` for web and Android alternatives.
- Describe results as "Apple-inspired" or "inspired by Apple's Human Interface Guidelines", never as official Apple design.

## Sources

Checked 2026-11-26: [HIG overview](https://developer.apple.com/design/human-interface-guidelines/), [HIG: Branding](https://developer.apple.com/design/human-interface-guidelines/branding), [WWDC25: Meet Liquid Glass](https://developer.apple.com/videos/play/wwdc2025/219/), [WWDC25: Get to know the new design system](https://developer.apple.com/videos/play/wwdc2025/356/). The eight signals are this skill's synthesis, not an Apple checklist.
