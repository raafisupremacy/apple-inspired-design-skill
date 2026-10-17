---
name: apple-inspired-design
description: Design, review, or implement calm, precise web and mobile interfaces with Apple-inspired clarity and motion. Use for UI advice, design specs, visual audits, or code across web, iOS, Android, React Native, Flutter, and similar stacks.
metadata:
  short-description: Apple-inspired web and mobile UI design
---

# Apple-inspired design

Use Apple’s design principles as guidance, not as a literal copy of Apple’s branding or components. Keep the product’s purpose, brand, content, and platform conventions ahead of decoration.

This is an agent skill for design intelligence: inspect the real artifact, route to the smallest relevant reference set, make evidence-based design decisions, and report what was checked. It is not a testing framework or device-lab automation tool. Do not give a generic “make it more Apple” answer.

## Choose the mode

- **Advise**: explain design decisions and alternatives.
- **Review**: inspect an existing UI, identify the highest-impact problems, and propose fixes.
- **Design**: produce a screen or flow specification with tokens, states, responsive behavior, and motion.
- **Implement**: write or edit UI code using the project’s existing stack and conventions.
- **Enforce**: only when explicitly requested; review the artifact, make bounded fixes, and re-review with evidence.

Infer the mode from the request. Ask only for platform, primary user task, and brand constraints when they materially affect the result. Do not start enforcement, broad refactors, or external research unless the request calls for it.

## Route by platform

Read only the relevant references:

- [Core principles](references/core-principles.md) for every task.
- [Motion](references/motion.md) whenever an interaction, transition, scroll effect, or animation is involved.
- [Web](references/web.md) for websites, web apps, PWAs, or responsive browser UI.
- [Responsive web](references/responsive-web.md) for fluid layout, theme switching, PWA/offline behavior, performance, SEO, or scroll-triggered loading.
- [Compatibility and testing](references/compatibility-testing.md) when browser support, device testing, performance, or production readiness matters.
- [Mobile](references/mobile.md) for native or cross-platform mobile UI.
- [Color and tokens](references/color-system.md) when choosing colors, themes, or tokens.
- [Accessibility and content](references/accessibility-content.md) for copy, forms, states, localization, or accessibility.
- [User-provided assets](references/user-assets.md) when the user supplies images, icons, screenshots, video, or logos.
- [Agent guidelines](references/agent-guidelines.md) for review structure, evidence, routing, and implementation behavior.
- [Patterns and components](references/patterns-components.md) when creating a page, flow, or reusable UI.
- [Mode contracts](references/mode-contracts.md) when deciding what a complete answer or artifact must contain.
- [Design reasoning](references/design-reasoning.md) when the product, audience, task, or trade-offs are still unclear.
- [Brand adaptation](references/brand-adaptation.md) when the user supplies a brand, color, tone, or visual identity.
- [Anti-patterns](references/anti-patterns.md) when auditing generic, overdecorated, or AI-generated UI.
- [Domain recipes](references/domain-recipes.md) when the product type is a dashboard, ecommerce flow, onboarding, settings, social app, or SaaS workspace.

## Non-negotiable behavior

- Make the main task obvious and keep hierarchy strong.
- Prefer familiar platform patterns over invented controls.
- Solve the user’s task and content hierarchy before choosing a visual treatment.
- Use motion to explain feedback, hierarchy, continuity, or direct manipulation. Remove decorative motion.
- Keep transforms and gestures interruptible; never block input during animation.
- Honor reduced motion, text scaling, contrast settings, keyboard, touch, screen readers, and localization.
- Treat user-provided assets as authoritative content. Adapt presentation when needed, but do not silently replace or materially alter them.
- Include relevant loading, empty, error, offline, disabled, permission, and success states.
- Preserve product personality through restrained, intentional choices instead of making every product look like Apple.
- Treat domain recipes as optional starting points. For products outside them, use the custom-domain process in `references/design-reasoning.md` rather than forcing a familiar template.
- When implementation or review makes it relevant, do a lightweight verification pass at realistic sizes and with the project’s actual data shape; do not invent a testing harness unless requested.
- When tokens are added or changed, run `scripts/validate_tokens.py` before claiming they are ready.

## Review output

For a review, prioritize findings by user impact. Each finding contains:

1. **What** is wrong, with a file, line, component, or visible location when available.
2. **Why** it matters for the user and which principle or platform convention applies.
3. **Fix** written in the project’s actual framework or design vocabulary.
4. **Confidence or limitation** when the artifact could not be observed or tested.

Fix accessibility and broken task flow before visual polish. Do not invent violations to make a report look thorough.

## Output rules

When giving advice, state the decision and why. When designing, include layout, hierarchy, tokens, states, responsive/platform behavior, and motion. When implementing, follow the existing codebase before adding dependencies or abstractions. Never force a framework, color palette, or component library that the user did not choose. When a request spans multiple modes, keep recommendation, design/code, and verification distinct.

Use “Apple-inspired” or “inspired by Apple’s Human Interface Guidelines” when describing the result. Do not claim the result is official Apple design.
