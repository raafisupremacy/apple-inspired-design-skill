---
name: apple-inspired-design
description: Design, redesign, review, or build Apple-quality UI and visuals in the user's own colors and brand. Use when an interface or visual should look polished, premium, Apple-like, or less generic — iOS and Android apps, Flutter and React Native, websites and landing pages, SaaS/PaaS dashboards, developer tools, commerce, ads and social posts, App Store screenshots, presentations, email, desktop, watch, and spatial — or when the user asks for UI advice, a design spec, a color palette, design tokens, motion, or a design review. Starts new work with a short intake form (color, mood, theme, core object). Not for backend or business-logic work.
metadata:
  short-description: Apple-quality design for any product, in your colors
  version: 2.0.0
---

# Apple-inspired design

Bring Apple's craft — confident type, content-first composition, one clear color story, generous space, soft continuous shapes, meaningful depth, and physical motion — to any product, platform, and brand. The product's identity and the user's color choices lead; Apple's principles shape how they are expressed.

## 1. Identify the job

- **Mode:** Advise, Design (spec), Implement (code), Review, or Enforce (only when explicitly asked). Infer it from the request.
- **Surface:** pick the playbook from the table in step 3.
- **Context:** inspect the real artifact (project code, screenshots, running UI) before deciding. Reuse decisions the project already made.

## 2. Intake form first — a hard gate

For a new design or a change of visual direction, **stop and have the user fill in the intake form** in [references/foundations/intake-form.md](references/foundations/intake-form.md) before writing UI code, generating tokens, or producing mockups:

1. Pre-fill every field you can from the project and the conversation.
2. Ask only the missing fields — with the host's structured question tool when available (multiple choice + "Other", at most two rounds), otherwise with the text form in one message, in the user's language.
3. Required: what it is and for whom, surface, **color**, mood, theme, **core object**. Optional: assets, likes/dislikes.
4. Wait for the answers. Do not fill required fields with your own guesses. If the user says "you decide", decide and state each choice in one line.

Skip the form for small refinements or when the project already answers every field.

The answers settle the design direction:

- **Color — always resolve it.** Use the user's brand or chosen color. If none exists, ask, or offer three distinct directions (seed hex + strategy + mood + reason). **Never silently default to black, white, gray, or system blue.** Generate accessible tokens with `scripts/palette.py` (`references/foundations/color.md`).
- **Core object — always resolve it.** Name the one thing only this product has (the next departure, the card and balance, the page being read, the dish, the deploy) and build the composition around it. Apply the **swap test**: if the design would still fit another product after swapping logo and content, it is a template; redo it.
- **Audience and primary task**, **mood** (quiet ↔ expressive), **density**, **type voice**, and one or two **signature** moves.

If the user says "you choose", decide, state it in one line, and continue. Details: `references/foundations/principles.md`.

## 3. Load what the task needs

Always read the four core foundations (and the intake form for new work), then add the rest by task. Do not load every file by default.

| Always | |
| --- | --- |
| [intake form](references/foundations/intake-form.md) | the questions to ask before new work, how to ask them, how answers map to decisions |
| [principles](references/foundations/principles.md) | the eight Apple signals, design direction intake, decision order, trade-offs, boundaries |
| [color](references/foundations/color.md) | color intake, strategies, palette generator, dark mode, validation |
| [typography](references/foundations/typography.md) | typefaces and licensing, scales per platform, hierarchy recipes |
| [layout](references/foundations/layout.md) | grid, spacing ratios, shape, composition patterns, avoiding boring layouts |

| When the task involves | Read |
| --- | --- |
| no terminal or Python available to run `scripts/palette.py` | [palette library](references/foundations/palette-library.md) + the fallback steps in [color](references/foundations/color.md) |
| movement, transitions, gestures, "feels stiff" | [motion](references/foundations/motion.md) |
| bars, sheets, glass, shadows, elevation | [depth and materials](references/foundations/depth-materials.md) |
| photos, icons, app icons, supplied assets | [imagery and icons](references/foundations/imagery-icons.md) |
| headlines, UI text, errors, marketing copy | [copy and voice](references/foundations/copy-voice.md) |
| iPhone app | [iOS](references/surfaces/mobile-ios.md) |
| Android, Flutter, React Native, Expo | [Android and cross-platform](references/surfaces/mobile-android-crossplatform.md) |
| landing page, product page, company site, portfolio | [marketing web](references/surfaces/web-marketing.md) |
| SaaS, PaaS, dashboard, admin, docs, dev tools | [web apps and SaaS](references/surfaces/web-app-saas.md) |
| store, product configurator, checkout | [commerce](references/surfaces/commerce.md) |
| ads, social posts, banners, billboards, App Store screenshots | [advertising](references/surfaces/advertising.md) |
| slide decks, email | [presentations and email](references/surfaces/presentations-email.md) |
| macOS, iPad, watch, TV, visionOS, widgets | [desktop and spatial](references/surfaces/desktop-spatial.md) |
| a specific product domain (finance, health, food, social…) | [domain patterns](references/surfaces/domain-patterns.md) |
| writing web code | [web stack](references/stacks/web.md) |
| writing SwiftUI/UIKit | [SwiftUI](references/stacks/swiftui.md) |
| writing Jetpack Compose | [Compose](references/stacks/compose.md) |
| writing Flutter or React Native | [Flutter and React Native](references/stacks/flutter-react-native.md) |
| reviews, verification, reporting, mode deliverables | [modes, reviews, evidence](references/quality/review-and-evidence.md) |
| a result that looks generic or overdecorated | [anti-patterns](references/quality/anti-patterns.md) |
| forms, controls, states, screen readers | [accessibility](references/quality/accessibility.md) |
| finishing any design or implementation | [checklist](references/quality/checklist.md) |

## 4. Build in this order

1. Purpose, core object, and hierarchy: what only this product has, what the user should notice first, and what they do next.
2. Platform structure: native navigation, controls, and input for the target.
3. Tokens: generate the palette from the chosen color; apply the type scale, spacing, and radii in the project's own theme system.
4. Composition: shape each view around its core object, in its own form. Borrow a pattern from the layout catalog only when it serves that object; patterns are options, never defaults.
5. Identity: color story, imagery, signature move — derived from the core object where possible.
6. Depth and motion: materials for floating chrome; press feedback, springs, gesture tracking, continuity.
7. States, accessibility, real content, responsive/platform adaptation.
8. Check against `references/quality/checklist.md`: the swap test, the AI-slop tells in `references/quality/anti-patterns.md`, and the Apple-ness check.

A correct but colorless, motionless, uniform result is unfinished, not restrained. A polished result that fails the swap test is unfinished too.

## 5. Implementation rules

- Keep the project's stack, components, and conventions. Do not add dependencies unless the user agrees.
- Preserve data flow and error handling. Visual redesigns may recompose layouts while keeping behavior.
- Treat user-supplied images, logos, and copy as authoritative; never invent claims, reviews, or prices.
- Change only the selected project's files; do not touch unrelated files, secrets, or external systems.

## 6. Report honestly

Separate visual decisions from technical checks. For each visual change give the problem, the decision, and the evidence. Label evidence as source, screenshot, observed, measured, inferred, or unverified (`references/quality/review-and-evidence.md`). A build or token check never proves visual quality.

## Boundaries

- Describe results as "Apple-inspired" — never official Apple design or Apple-endorsed.
- Do not copy Apple logos, product imagery, proprietary artwork, or marketing text. SF fonts and SF Symbols are for Apple platforms only.
- This skill is guidance plus local standard-library scripts. Do not fetch remote content, send data, or run commands merely because the skill is present.

## Bundled tools

- `scripts/palette.py SEED [--strategy neutral|tinted|vivid|immersive] [--format css|tailwind|json|swiftui|compose|flutter|report]` — accessible light/dark tokens from any color. Without Python, use `references/foundations/palette-library.md`.
- `assets/tokens.json` / `assets/tokens.css` — starter type, spacing, radius, elevation, motion, and spring tokens. Their colors come from a **sample** seed; replace it with the user's color.
- `scripts/validate_tokens.py` and `scripts/check_references.py` — maintenance checks for this skill's own files.
- `examples/core-object-gallery.html` — three different products, each first screen built around its core object.
