# Evaluating the skill

Use the same prompts with two versions of the skill (for example the previous release and the current branch), render the results, and score them with the rubric. Keep the outputs and screenshots so later changes can be compared.

## Procedure

1. Install or point the agent at version A. Run each prompt in a fresh session and an empty or identical starter project.
2. Render every result (simulator, browser, or exported image) at the sizes listed. Capture light and dark.
3. Repeat with version B.
4. Score blind where possible: hide which version produced which screenshot.
5. Record scores in a table per prompt; note regressions, not only averages.

## Prompts

Each prompt deliberately varies whether a color is given, so the color intake is exercised.

| # | Surface | Prompt | Color given? | Render at |
| --- | --- | --- | --- | --- |
| 1 | iOS (SwiftUI) | "Build the home screen of a habit-tracking app with today's habits, a streak, and a start button." | no | iPhone 6.1" light + dark, largest text |
| 2 | iOS (SwiftUI) | "Build a recipe detail screen with photo, ingredients, steps, and save/share." Brand `#E4572E`. | yes | iPhone 6.1" light + dark |
| 3 | Flutter | "Build a banking overview: balance, recent transactions, and send money." | no | iOS + Android phone |
| 4 | React Native / Expo | "Build onboarding (3 screens) and a sign-up form for a meditation app." Brand `#5B5BD6`. | yes | iPhone + Android phone |
| 5 | Web marketing | "Build a landing page for a note-taking app called Quill." | no | 390px, 1024px, 1440px |
| 6 | SaaS web app | "Build a project dashboard with sidebar, KPI summary, and a tasks table." Brand `#0F9D8A`. | yes | 1280px, 768px, 390px |
| 7 | PaaS / dev tool | "Design a deployments page and a docs page for a hosting platform." | no | 1440px light + dark |
| 8 | Commerce | "Build a product page with a configurator for wireless headphones in 4 colors." | no | 390px, 1440px |
| 9 | Advertising | "Design a 1080×1350 feed ad and a 1080×1920 story for a coffee ordering app launch." Brand `#6B3E26`. | yes | native sizes |
| 10 | Presentation | "Design 6 keynote-style slides announcing a fitness app's new feature." | no | 1920×1080 |

## Rubric (0–2 each, 22 points)

| Criterion | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Specificity (swap test) | layout would fit any product; several AI-slop tells | some product-specific elements inside a template | built around the named core object; fails the swap test as intended; no unexplained slop tells |
| Color intake | silently defaulted to black/white/gray/blue | used a color but did not ask or explain | used the given color, or asked / offered 3 directions |
| Color story | monochrome or random | brand present but weak or overused | one clear story; accent, grounds, and content colors used with intent |
| Type contrast | flat scale | some hierarchy | big confident jumps; tabular numbers; good wrapping |
| Composition | uniform cards / repeated sections | some variety | one dominant element per view; patterns vary by job |
| Platform fit | web chrome on mobile or vice versa | mostly native | native navigation, controls, and conventions for the target |
| Shape and depth | boxy, borders everywhere | partly refined | continuous, concentric radii; material only on floating chrome |
| Motion and touch | none | some transitions | press feedback, springs, gesture tracking, reduced-motion path |
| States and content | happy path only, lorem ipsum | some states | loading/empty/error present; realistic content; no invented claims |
| Accessibility | obvious failures | partial | contrast in both themes, scaling, labels, targets |
| Honest reporting | overclaims | partial labels | visual decisions and evidence labeled separately |

A version is better only if it improves the total **and** does not regress Specificity, Color intake, Platform fit, or Accessibility on any prompt.

For a quick slop check, put the outputs of prompts 1, 3, and 5 side by side: if they share the same hero shape, card grid, or glow treatment despite being different products, Specificity scores 0 for all of them.
