# Changelog

All notable changes to this skill. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the project uses [Semantic Versioning](https://semver.org/).

## [2.0.0] - 2026-11-26

Version 2 rebuilds the skill around design craft instead of reporting rules. Real use showed v1 producing generic, rigid, mostly black-and-white interfaces; v2 targets that directly.

### Breaking

- **References restructured.** The 17 flat files in `references/` are replaced by `foundations/`, `surfaces/`, `stacks/`, and `quality/`. Agents now read the core foundations plus what the task needs, through the routing table in `SKILL.md`, instead of every file. See the migration table below.
- **Starter tokens changed.** Color role names are kept and `brand`, `on-accent`, `link`, and `info` are added. Radius, spacing, typography, and layout tokens use new names and values. Projects that copied v1 tokens must remap them (see below).
- **Sample colors.** The starter colors now come from a sample coral seed, not an Apple-like gray/blue palette. They are an example to replace, not a default brand.

### Added

- **Design intake form** (`references/foundations/intake-form.md`): before new work the agent pre-fills what the project answers and asks for product and audience, surface, color, mood, theme, and core object — as a multiple-choice form where the host supports it, otherwise as a text form in the user's language.
- **Core object step and swap test**: each design is built around the one thing only that product has; a layout that would fit another product is rejected as a template.
- **AI-slop tells**: an explicit list of overproduced patterns (recolored templates, glow blobs, purple gradients, centered slogan heroes, stat-card grids, default bento, glass everywhere, generic slogans, invented data).
- **Palette generator** (`scripts/palette.py`): any seed color → accessible light/dark semantic tokens in OKLCH with contrast floors, four strategies (`neutral`, `tinted`, `vivid`, `immersive`), and CSS, Tailwind, JSON, SwiftUI, Compose, and Flutter output.
- **Palette library** (`references/foundations/palette-library.md`): precomputed palettes for agents that cannot run Python, with fallback steps in `color.md`.
- **Foundations**: principles (eight Apple signals), color strategies, typography scales and font licensing, layout patterns with "avoid when" guidance, depth and Liquid Glass, imagery and icons, copy and voice, and a motion feel kit with spring presets per stack.
- **Surface playbooks**: iOS, Android and cross-platform, marketing websites, web apps/SaaS/PaaS/developer tools, commerce, advertising and App Store assets, presentations and email, desktop/iPad/watch/TV/visionOS/widgets, and domain patterns.
- **Stack adapters**: web (CSS/Tailwind/React), SwiftUI/UIKit, Jetpack Compose, Flutter and React Native.
- **Starter motion tokens**: CSS `linear()` spring curves (`--spring-smooth|snappy|bouncy`) with durations, and press feedback tokens.
- **Example**: `examples/core-object-gallery.html` — transit, banking, and reading apps, each built around its own core object.
- **Evals**: `evals/README.md` with ten prompts across surfaces and a 22-point rubric.
- **Tests**: `tests/test_palette.py` (standard library `unittest`).

### Changed

- Color guidance no longer starts from a neutral palette; the user's color is always resolved first, and the agent never silently defaults to black, white, gray, or system blue.
- Evidence and reporting rules, previously repeated across five files, are consolidated into `references/quality/review-and-evidence.md`.
- `scripts/validate_tokens.py` now checks that starter colors match the generator, that every contrast floor passes in both themes, and that `tokens.css` is exactly what the generator renders.
- `scripts/check_references.py` also checks code-formatted file paths, not only Markdown links.

### Fixed

- React Navigation 7 uses `headerLargeTitleEnabled` (`headerLargeTitle` is v6).
- Compose reduced motion reads `ANIMATOR_DURATION_SCALE`; `LocalAccessibilityManager` has no reduce-motion API.

### Migration from 1.x

| v1 reference | v2 location |
| --- | --- |
| `core-principles.md`, `design-reasoning.md`, `brand-adaptation.md` | `foundations/principles.md` |
| `color-system.md` | `foundations/color.md`, `foundations/depth-materials.md` |
| `motion.md` | `foundations/motion.md` |
| `user-assets.md` | `foundations/imagery-icons.md` |
| `mobile.md` | `surfaces/mobile-ios.md`, `surfaces/mobile-android-crossplatform.md` |
| `web.md`, `responsive-web.md`, `compatibility-testing.md` | `stacks/web.md`, `surfaces/web-marketing.md`, `quality/review-and-evidence.md` |
| `patterns-components.md`, `domain-recipes.md` | `foundations/layout.md`, `surfaces/*`, `surfaces/domain-patterns.md` |
| `accessibility-content.md` | `quality/accessibility.md`, `foundations/copy-voice.md` |
| `agent-guidelines.md`, `mode-contracts.md` | `quality/review-and-evidence.md`, `SKILL.md` |
| `quality-checklist.md` | `quality/checklist.md` |
| `anti-patterns.md` | `quality/anti-patterns.md` |

| v1 token | v2 token |
| --- | --- |
| `--color-*` (16 roles) | same names; new `--color-brand`, `--color-on-accent`, `--color-link`, `--color-info` |
| `--radius-control`, `--radius-panel`, `--radius-pill` | `--radius-xs` … `--radius-xl`, `--radius-pill` |
| `--space-1` … `--space-7` | `--space-1` … `--space-12` (values from 5 upward differ) |
| `--text-body`, `--text-caption`, `--text-title`, `--text-hero`, `--leading-*` | `--text-<role>-size`, `-leading`, `-tracking`, `-weight` for 11 roles |
| `--content-max`, `--reading-max`, `--page-padding` | `--layout-content-max`, `--layout-reading-max`, `--layout-gutter-*` |
| `--elevation-floating` | `--elevation-low`, `--elevation-mid`, `--elevation-floating` |
| `--motion-*`, `--ease-*` | same names; new `--ease-sheet`, `--spring-*`, `--press-*` |

Updating the installed skill does not change existing project code. Ask the agent to apply v2 to a project to adopt the new guidance.

## [1.0.0] - 2026-10-20

First release: Apple-inspired design guidance for web and mobile with Advise, Review, Design, Implement, and Enforce modes; motion system guidance; accessibility, responsive, and dark-mode contrast gates; evidence-labeling rules; starter CSS/JSON tokens; and local validators.

[2.0.0]: https://github.com/raafisupremacy/apple-inspired-design-skill/compare/v1.0.0...v2.0.0
[1.0.0]: https://github.com/raafisupremacy/apple-inspired-design-skill/releases/tag/v1.0.0
