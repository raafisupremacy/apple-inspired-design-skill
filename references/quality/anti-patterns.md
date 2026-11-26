# Anti-patterns

Use this to diagnose why a result looks generic, rigid, or overdecorated. Name the underlying cause and apply the smallest change that fixes it.

## AI-slop tells

These are the patterns language models and UI generators overproduce. Each one is legitimate in some product; together, or without a product-specific reason, they make a result read as machine-made. Before keeping any of them, state in one sentence why this product needs it. If the reason would apply to any product, remove or replace it.

| Tell | Why it reads as slop | Do instead |
| --- | --- | --- |
| **Recolored template** — the same layout with a different color | identity reduced to a palette swap; fails the swap test | build the composition around the core object (`../foundations/principles.md`) |
| **Radial glow / blurred color blob** behind a hero, card, or product | decoration standing in for an idea | light, color, or imagery that depicts something real about the product — or nothing |
| **Purple-to-blue or neon gradient** unrelated to the brand | the default "tech" look of generated UI | the brand's own color story; flat color often has more presence |
| **Centered hero:** eyebrow + two-line headline + subhead + two buttons | the most generated landing layout | a hero shaped by the product: the product itself, a live UI moment, a real photo, a demonstration |
| **Stat-card grid with sparklines** as a home screen | a dashboard template, not a product | one dominant answer to the user's main question; secondary values quiet and inline |
| **Bento grid by default** | fashionable filler for "many features" | fewer, deeper sections; bento only when features are truly peers with distinct visuals |
| **Glass on everything** | material as costume | material only on the functional layer that floats over content |
| **Gradient hero card on mobile home** ("Today" + big colored card) | the generic wellness/fitness app | the product's own object in its own form |
| **Rhyming or parallel slogan** ("Move more. Stress less.", "Work smarter, not harder") | sounds like every generated tagline | a specific, concrete claim the product can back up |
| **Invented brand name, metrics, or testimonials** | fake specificity | the user's real content, or clearly labeled placeholders |
| **Icon in a tinted circle above every heading** | uniform decoration with no meaning | icons only where they clarify an action, object, or status |
| **Everything rounded, shadowed, and floating equally** | no hierarchy of depth | one depth language: flat ground, grouped surfaces, one floating level |
| **Uniform card sizes in a perfect grid** | nothing leads | one dominant element; vary scale by importance |

This list includes patterns that appear elsewhere in this skill as options (bento, statement hero, metric cards, glass). Options are not defaults: use them when the core object and the task call for them.

## The generic-template look

| Anti-pattern | Looks like | Fix |
| --- | --- | --- |
| **Silent monochrome** | black or white ground, gray text, default blue, no color story | Run the color intake; generate a palette from the user's color (`../foundations/color.md`) |
| **Flat type scale** | every text between 14 and 20px, same weight | Use the full scale: big bold titles, calm body, small secondary captions |
| **Card soup** | every element in a white rounded box with a border and shadow | Grouped lists, open typography on the ground, full-bleed media; cards only for tappable units |
| **Same-section syndrome** | heading + paragraph + three cards, repeated | Give each section one job and a different composition (`../foundations/layout.md`) |
| **No hero** | nothing is bigger than anything else | Decide the one dominant element per view |
| **Boxy geometry** | 4–8px radii on large cards, mismatched nested corners | Continuous corners, larger radii, concentric nesting, capsules |
| **Dead touch** | no press state, instant jumps, linear motion | Feel kit: press feedback, springs, gesture tracking, continuity |
| **Web chrome on mobile** | centered-logo header, hamburger, custom bottom bar | Native navigation stack, large titles, tab bar, sheets |
| **Placeholder blindness** | lorem ipsum, gray image boxes, round fake numbers | Real or realistic content shapes, labeled placeholders, real images when supplied |
| **Emoji icons** | emoji standing in for interface icons | One coherent icon family |

## Overdecoration

- **Decoration-first hierarchy:** gradients, glass, glow, icons, or illustrations before the task and content are clear.
- **Glass everywhere:** translucent content cards, glass stacked on glass, glass with unreadable text.
- **AI gradient:** generic purple-to-blue blobs unrelated to the brand.
- **Animation wallpaper:** reveals on every section, looping motion, delays before content.
- **Badge confetti:** tags, pills, and colored icons on every item so nothing stands out.

## Platform and system errors

- **Platform cosplay:** web controls dressed as iOS, or iOS chrome on Android.
- **Token theater:** many tokens that do not map to roles or are used inconsistently.
- **Color semantics drift:** the same color means different states, or status shown only by color.
- **Selection discontinuity:** an indicator that jumps or swaps unrelated fills where a shared moving indicator was intended.
- **Screenshot success:** polished in one static viewport, broken with real content, keyboard, text scaling, or interaction.
- **Accessibility afterthought:** tiny text, missing focus, gesture-only actions, contrast fixes that flatten hierarchy.
- **Asset disrespect:** replacing, over-cropping, filtering, or fabricating supplied media.
- **Invented proof:** made-up reviews, ratings, prices, or specs to fill a layout.
