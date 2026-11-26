# Apple-inspired design

An agent skill that brings Apple-level craft to any product, platform, and brand — in **your** colors.

Confident typography, content-first composition, one clear color story, generous space, soft continuous shapes, meaningful depth (including Liquid Glass where the platform has it), and physical, responsive motion. The skill adapts these to the product instead of making everything look gray, black, and Apple-blue.

**Version 2.0.0** — see [CHANGELOG.md](CHANGELOG.md).

## What's new in 2.0

- **Intake form before new work:** the agent asks for color, mood, theme, and the product's core object instead of guessing.
- **Your colors:** a generator turns any color into accessible light/dark tokens for CSS, Tailwind, SwiftUI, Compose, and Flutter, with a precomputed library for agents that cannot run Python.
- **Built around the core object, not a template:** a swap test and an explicit list of AI-slop tells keep results specific to the product.
- **Craft over rules:** typography scales, layout patterns, Liquid Glass, motion springs, and playbooks for mobile, web, SaaS/PaaS, commerce, ads, decks, and more.
- **Breaking:** references and starter tokens were restructured; the changelog has a migration table.

## What it covers

| Area | Surfaces |
| --- | --- |
| Mobile | iOS (SwiftUI/UIKit), Android (Compose), Flutter, React Native / Expo |
| Web | landing and product pages, company profiles, portfolios, commerce, SaaS and PaaS apps, dashboards, docs and developer tools |
| Marketing | social posts, stories, display banners, billboards, App Store screenshots, launch visuals |
| Communication | keynote-style presentations, email |
| More platforms | macOS, iPadOS, watchOS, tvOS, visionOS, widgets |

Modes: **Advise**, **Design** (spec), **Implement** (code), **Review**, and **Enforce** (only when asked).

## Install

```bash
npx skills add raafisupremacy/apple-inspired-design-skill
```

Restart or refresh the agent if it does not discover the skill. Run the same command again to update.

The skill uses the open `SKILL.md` format, so it works with Claude Code and other agents that read skills (for example Codex, GitHub Copilot, Cursor, and Gemini CLI); the installer places it in the right folder for each detected agent. Agents with a multiple-choice question tool show the intake form as a form; others ask it as a numbered list. Agents without Python use the bundled palette library instead of the generator.

## Use it

Tell the agent what you are making. Before designing anything new, the agent asks you a short intake form — product and audience, platform, color, mood, light/dark, and the one thing users come for — pre-filling whatever it can detect from your project. Agents with a multiple-choice question tool show it as a form; others send it as a numbered list. Answer briefly or say "you decide" for any item. It never silently picks black and white.

```text
1. What is it and who is it for?        5. Theme: light first / dark first / both
2. Surface: iOS / Android / web / ...   6. The one thing users come for: (a) … (b) …
3. Color: brand color, a color you like, "show me 3 options", or "you decide"
4. Mood: calm & premium / warm & friendly / bold & energetic / precise / cinematic
```

```text
Use apple-inspired-design to build the home screen of my habit-tracking iOS app in SwiftUI.
Brand color #2EBD85, friendly and energetic.
```

```text
Use apple-inspired-design to redesign this React landing page for our PaaS product.
Keep the logo; I don't have a color yet — suggest three directions first.
```

```text
Use apple-inspired-design to design a set of Instagram and story ads for our coffee app launch.
Color #6B3E26, warm and premium. Message: "Order ahead. Skip the line."
```

```text
Use apple-inspired-design in Review mode on this Flutter checkout flow.
Report What / Why / Fix / Evidence.
```

## Generate a palette from any color

```bash
python scripts/palette.py "#2EBD85"                               # CSS variables + contrast report
python scripts/palette.py "#2EBD85" --strategy vivid --format swiftui
python scripts/palette.py "#6B3E26" --strategy immersive --format compose
python scripts/palette.py "#7B61FF" --format tailwind              # also: json, flutter, report
```

Strategies: `neutral` (quiet gray foundation), `tinted` (default; neutrals carry the brand hue), `vivid` (colored surfaces), `immersive` (dark-first). Your color is kept exactly as `brand`; text, link, label-on-accent, and status colors are adjusted only as much as needed to meet contrast in light and dark themes.

Open `examples/core-object-gallery.html` in a browser: a transit, a banking, and a reading app, each first screen built around its own core object instead of a shared template.

## Package contents

- `SKILL.md` — entry point: intake form gate, routing table, build order, boundaries
- `CHANGELOG.md` — release notes and migration from 1.x
- `references/foundations/` — intake form, principles, color, palette library, typography, layout, depth and materials, imagery and icons, copy and voice, motion
- `references/surfaces/` — iOS, Android and cross-platform, marketing web, SaaS/PaaS, commerce, advertising, presentations and email, desktop and spatial, domain patterns
- `references/stacks/` — web, SwiftUI, Compose, Flutter and React Native
- `references/quality/` — accessibility, anti-patterns, modes/reviews/evidence, checklist
- `assets/` — starter tokens (type, spacing, radius, elevation, motion, CSS spring curves); colors from a sample seed
- `scripts/` — `scripts/palette.py`, `scripts/validate_tokens.py`, `scripts/check_references.py` (Python standard library only)
- `examples/` — core object gallery (three products, no shared template)
- `evals/` — prompts and rubric for comparing skill versions

## Maintain

```bash
python -m unittest discover -s tests
python scripts/validate_tokens.py
python scripts/check_references.py
```

After changing the generator or starter tokens, regenerate with `python scripts/palette.py "#F2643A" --strategy tinted --write-starter` and `python scripts/palette.py --write-library`. Record user-facing changes in `CHANGELOG.md` and bump `metadata.version` in `SKILL.md`.

## Scope and honesty

The skill is design guidance plus local scripts, not an automated test lab. It labels what it observed, measured, inferred, or could not verify. Reviews cover interface design and experience, not backend or business logic.

It is Apple-inspired, not Apple's official design system, and does not imply Apple endorsement. It does not bundle Apple fonts, SF Symbols, logos, or imagery.

See [SECURITY.md](SECURITY.md) for trust boundaries.
