# Apple-inspired design skill v2 — design

Approved by the user on 2026-11-26 (roadmap accepted in conversation; "perbaiki dan maksimalkan").

## Intent

Real use across four mobile projects and some web work produced generic, rigid, almost always black/white interfaces that did not feel Apple-like. The skill spends most of its text on reporting/evidence rules and very little on design craft. v2 makes the skill produce visibly Apple-quality work on any surface, in any color the user chooses.

## Goals

- Color is the user's choice. The skill asks for or offers color directions; it never silently defaults to neutral black/white.
- Concrete craft knowledge: type scales, layout/composition recipes, depth/material (Liquid Glass), imagery, copy voice, motion feel values.
- Surface playbooks for every project type: iOS, Android/cross-platform, marketing web, SaaS/PaaS/dev tools, commerce, advertising, presentations, email, desktop/iPad/watch/visionOS.
- Stack adapters: web (CSS/Tailwind/React), SwiftUI, Compose, Flutter/React Native.
- Progressive loading: SKILL.md routes to the few files a task needs instead of "read all 17 files".
- A palette generator (stdlib Python): one seed color → light/dark semantic tokens with contrast checks, exported to several stacks.
- Examples that show non-monochrome Apple-quality results, and an eval prompt set with a rubric for before/after comparison.

## Non-goals

- No runtime services, dependencies, network access (security posture unchanged).
- Not a replica of Apple branding, SF fonts outside Apple platforms, SF Symbols outside Apple platforms, or Apple marketing assets.
- No device lab or automated visual regression.

## Anti-goals

- Adding more defensive reporting rules instead of craft.
- A single "Apple look" (gray + blue + white cards) applied to every product.

## Approaches considered

1. **Patch the existing files** (edit color rules, lengthen web/mobile). Cheap, but keeps the rule-heavy structure and the read-everything cost.
2. **Restructure into foundations / surfaces / stacks / quality with a lean router** (chosen). Lets each task load only what matters and gives room for deep craft content.
3. **Generate a large design database (CSV of styles/palettes)**. Broad but shallow, and drifts away from a coherent Apple philosophy.

## Structure (builder's calls, made by Claude)

```
SKILL.md                    lean router + Design Direction intake
references/foundations/     principles, color, typography, layout, depth-materials, imagery-icons, copy-voice, motion
references/surfaces/        mobile-ios, mobile-android-crossplatform, web-marketing, web-app-saas, commerce, advertising, presentations-email, desktop-spatial
references/stacks/          web, swiftui, compose, flutter-react-native
references/quality/         accessibility, anti-patterns, review-and-evidence, checklist
scripts/palette.py          seed → tokens (CSS, Tailwind, JSON, SwiftUI, Compose, Flutter)
assets/                     tokens regenerated from a sample seed, clearly marked as an example
examples/                   color-strategy gallery (HTML)
evals/                      prompt set + rubric
```

Old reference files are merged into the new ones (evidence/claim rules consolidated into one quality file) and then removed.

## Left to the builder

Exact wording, token naming details, example content.
