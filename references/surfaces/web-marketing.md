# Marketing websites, landing pages, and company sites

Apple's product pages read as a guided story: one idea per viewport, big type, the product as the hero, and color taken from the product. The same structure works for a SaaS landing page, an app launch, a company profile, or a campaign.

## Start from the core object

Ask what the visitor should see first that only this product can show: the device itself, the app doing its one magic thing, the dish, the place, the result a customer gets. The hero shows that, as large and as real as possible. A page that opens with a centered slogan over a glow could belong to anyone — it fails the swap test (`../foundations/principles.md`).

## Story arc

Give every section one job and a composition that fits that job (`../foundations/layout.md`). The jobs below are a menu; most pages need four or five of them, not all.

1. **Hero — show.** The product or its key moment, the product name, one specific claim, one action.
2. **Demonstrate.** Each chapter one claim with visual proof: a sticky story, a split, or a live UI fragment.
3. **Survey (optional).** Remaining features only if they are true peers with distinct visuals; otherwise cut them or list them plainly.
4. **Proof — trust.** Sourced numbers, real customer logos or quotes the user supplied, awards with sources.
5. **Compare / pricing — decide.** Aligned comparison or plan cards with one recommended plan.
6. **Final action.** One short, concrete section with one action.
7. **Footer — reference.** Footnotes for claims, legal, navigation.

The first viewport must establish product, audience, value, and action. Later sections must each earn their place; do not repeat "centered heading + paragraph + three white cards", and do not add a highlights shelf or bento just because pages often have one.

## Page chrome

- **Local nav bar:** product name on the left, 3–6 section links, and a small capsule "Buy"/"Get started" button on the right; sticky, on a glass-like translucent bar (`../foundations/depth-materials.md`), with a solid fallback.
- Keep the global nav light. On mobile, collapse into a focus-managed menu with Escape/back and focus restore.

## Hero recipes

```text
Product stage                 Live moment                     Split
──────────────                ──────────────────────          ──────────────────────
Name                          Name — one specific claim       Name        ┌────────┐
ONE SPECIFIC CLAIM            ┌──────────────────────────┐    CLAIM       │ real   │
[Action]                      │ the app doing its one    │    one line    │ media  │
┌──────────────────┐          │ thing, animated or live  │    [Action]    └────────┘
│ product / real UI│          └──────────────────────────┘
└──────────────────┘          [Action]
```

- Prefer the product stage or a live moment. Use a text-only statement hero only when the idea itself is the product (a manifesto, an event) and the line is specific.
- Headline 56–96px bold, tight tracking; supporting line 21–28px in secondary text; generous top padding. Left-aligned heroes often feel less templated than centered ones.
- The ground comes from the product: its finish, its screenshot's colors, the brand color, or plain tinted light/dark. No decorative glow blobs.

## Scroll choreography

- **Sticky story:** media pinned (`position: sticky`) while text chapters scroll; each chapter swaps or transforms the media.
- **Scroll-linked:** scale or fade the hero product slightly as it leaves; reveal a UI screenshot as it enters — bound to scroll progress with `animation-timeline: view()` where supported, Intersection Observer otherwise, static without either.
- **Video:** short, muted, looping only when it explains; poster image, pause control, no autoplay with sound, reduced-motion shows the poster.
- Animate transform and opacity only. Content must be readable with JavaScript off and with reduced motion.
- One signature motion moment per page is enough; do not fade-in every block.

## Color through the page

Alternate section grounds with the story — light, brand color, dark, light — rather than one white canvas. Use the generated palette for text roles on each ground; the brand ramp for gradients and tiles. Product pages can borrow colors from product finishes or app screenshots.

## Variants

- **SaaS / app landing:** product UI screenshot as the hero (real, crisp, in a window or device frame), logo cloud only with real customers, features demonstrated with real UI fragments (a bento only if they are true peers), pricing with a recommended plan, FAQ.
- **Company profile / agency:** statement hero, selected work as full-bleed case cards, capabilities as a calm list, people with real photos, contact.
- **Event / campaign:** a color field and one bold line, date and CTA, minimal sections.
- **Portfolio:** large media, minimal chrome, project pages as sticky stories.

## Performance and quality

- The hero image or video poster is the LCP element: preload it, size it, never lazy-load it. Lazy-load below-the-fold media with reserved space.
- Responsive images (`srcset`/`sizes`, AVIF/WebP), font loading without layout shift.
- Semantic headings in story order, descriptive link text, metadata and share images.
- Check narrow mobile, tablet, laptop, and wide desktop; long headlines in other languages; 200% zoom.

## Sources

Observed apple.com product pages (November 2026) and third-party teardowns: [UX Collective: The autopsy of an Apple webpage](https://uxdesign.cc/autopsy-of-an-apple-webpage-cbfebed98b6c), [Baymard: Apple product page](https://baymard.com/ecommerce-design-examples/41-product-page/15798-apple). These are interpretations, not Apple documentation.
