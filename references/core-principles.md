# Core principles

Apply these across web and mobile:

- **Purpose**: identify the user’s important task and make it excellent.
- **Agency**: show what is happening, preserve user control, and make recovery easy.
- **Familiarity**: use established interaction patterns consistently.
- **Flexibility**: support different devices, input methods, abilities, text sizes, and contexts.
- **Simplicity**: remove what does not help; simplicity is not emptiness.
- **Craft**: refine wording, alignment, performance, state changes, and edge cases.
- **Delight**: use warmth, enrichment, or expressive detail when it fits the product and does not compete with the task.
- **Deference**: let content and the user’s task lead the visual hierarchy.
- **Responsibility**: explain permissions, collect less data, and protect user information.

Use hierarchy through type, spacing, grouping, contrast, and proportion before adding decoration. Flat surfaces are usually enough; reserve depth and blur for layers that float above content. A brand color is an accent, not a requirement that every control become colorful.

Do not copy Apple logos, product imagery, proprietary UI, or marketing text. Reuse principles and platform conventions while preserving the product’s own identity.

## Translate principles into decisions

Use these questions to judge the affected surface, not as a required report template:

- **Clarity:** can the user distinguish the primary content, current state, and next action? Adjust relative emphasis and grouping before making everything larger or bolder.
- **Deference:** does the interface give content enough space and attention? Keep controls discoverable while reducing framing that competes with reading, comparison, or action. Quiet does not mean low contrast.
- **Depth and continuity:** do layers and transitions explain relationships and a return path? Use elevation for actual hierarchy and preserve object identity where it helps orientation; blur and shadows alone do not establish depth.
- **Agency and feedback:** does input receive timely, understandable feedback, with interruption and recovery where appropriate? Animation must not become a waiting period or substitute for a clear state.
- **Coherence and adaptation:** do related controls behave predictably while respecting the platform, input method, content length, and accessibility preferences? Preserve intent across platforms rather than copying geometry.

These are working interpretations for this skill, not an official Apple checklist. Assess the trade-off against the user's task and brand; a dense workspace, expressive showcase, and quiet reading surface can each satisfy these principles with different compositions.

Delight is a purposeful layer, not a license for decoration: keep it subordinate to clarity, agency, accessibility, and performance. When an interface adapts across platforms or configurations, preserve the user's context and recognizable content/control relationships even when layout and interaction details change.

## Source basis and limits

Research checked on 2026-10-20. Keep explicit Apple guidance separate from this skill's synthesis and cross-platform adaptations:

- [Apple: Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios) connects design to ergonomics, input, session length, and primary tasks. Transfer that reasoning to the target device; iOS geometry and gestures are not Android or web requirements.
- [Apple: Materials](https://developer.apple.com/design/human-interface-guidelines/materials) distinguishes Liquid Glass for controls/navigation from standard materials within content. Apply the material guidance in `color-system.md`; glass is not a universal visual requirement.
- [Apple: Typography](https://developer.apple.com/design/human-interface-guidelines/typography) supports legibility, semantic text styles, hierarchy, and layout adaptation at larger sizes. Apply the practical criteria in `accessibility-content.md`; Apple point sizes are platform-specific.
- [Apple: Modality](https://developer.apple.com/design/human-interface-guidelines/modality) requires a clear benefit for interrupting context, a recognizable task, dismissal, and protection against losing edits. See `patterns-components.md`.
- [Nielsen Norman Group: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/) (2006) provides independent usability reasoning for separating frequent and advanced options, and warns against splitting interdependent decisions into a wizard. It is not Apple policy; see `design-reasoning.md`.

Motion sources and parameter limits are recorded in `motion.md`. These sources support decision criteria, not proof that a generated interface is usable. When sources differ, check platform, OS/framework availability, task, and accessibility needs before adopting a recommendation. Do not turn a release-specific appearance, numerical example, or third-party opinion into a universal Apple rule. This source record does not require network access during normal skill use.
