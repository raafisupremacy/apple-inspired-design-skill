# Quality checklist

Run the relevant sections before calling work done. Do not report an unchecked item as passing.

## Specificity check (do this first)

- [ ] The core object is named, and the hero of each main view is that object in its own form (a countdown, a card, the text, the dish, the deploy) — not a generic card.
- [ ] **Swap test passed:** with the logo and content replaced by another product, the design would no longer fit.
- [ ] None of the AI-slop tells in `anti-patterns.md` appear without a product-specific reason you can state in one sentence.
- [ ] Copy and data are the product's own or labeled placeholders; no invented brand name, slogan, or numbers presented as real.

## Apple-ness check (visual direction)

- [ ] The color direction came from the user or was offered and chosen — not a silent black/white default.
- [ ] One dominant element per view; the type scale has big, clear jumps.
- [ ] Content (images, numbers, the user's data) leads; chrome is quiet.
- [ ] Grouping is tight, section spacing generous; sections vary by job.
- [ ] Continuous, consistent radii; nested corners are concentric.
- [ ] Depth is meaningful: floating chrome on a material, content opaque, one depth language.
- [ ] Every tappable element responds to touch; movement uses springs; gestures track input.
- [ ] Details: tabular numbers, optical alignment, consistent icon family, real copy.
- [ ] Platform conventions respected for the target (iOS, Android, web, desktop).
- [ ] At most one or two signature moves, and they serve the product.

## States and content

- [ ] Loading, empty, error, offline, permission, success, and destructive recovery where relevant.
- [ ] Real or realistic content shapes; long strings and translations considered.
- [ ] Claims, prices, reviews, and specs are supplied or clearly marked as placeholders.
- [ ] Supplied assets are intact and presented with intent.

## Accessibility

- [ ] Contrast measured for important pairs in light and dark and in interaction states.
- [ ] Text scaling to the largest setting / 200% zoom without clipping essential content.
- [ ] Keyboard, focus, screen reader labels, touch targets.
- [ ] Reduced motion and reduced transparency paths.

## Responsive and platform

- [ ] Narrow, intermediate, and wide compositions recomposed, not squeezed; no page-level horizontal scroll.
- [ ] Safe areas, keyboard, rotation/resizing, system back.
- [ ] Optional browser APIs feature-detected with fallbacks.

## Acceptance

- [ ] Visual acceptance is based on rendered evidence when appearance was the request; otherwise labeled unverified.
- [ ] Each targeted visual problem has a concrete change or an evidenced reason to keep it.
- [ ] The requested scope is accounted for; nothing is called "polished" or "complete" with gaps unlabeled.
