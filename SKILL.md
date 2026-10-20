---
name: apple-inspired-design
description: Design, review, or implement calm, precise web and mobile interfaces with Apple-inspired clarity and motion. Use for UI advice, design specs, visual audits, or code across web, iOS, Android, React Native, Flutter, and similar stacks.
metadata:
  short-description: Apple-inspired web and mobile UI design
---

# Apple-inspired design

Use Apple's design principles as guidance, not as a literal copy of Apple's branding or components. Keep the product's purpose, brand, content, and platform conventions ahead of decoration.

This is an agent skill for design intelligence: inspect the real artifact, read the complete guidance set, make evidence-based design decisions, and report what was checked. It is not a testing framework or device-lab automation tool. Do not give a generic "make it more Apple" answer. A visual redesign request must result in a visible composition, hierarchy, type, spacing, surface, or motion decision when the inspected artifact supports one; build and accessibility work alone is not a visual redesign.

## Security and trust boundaries

- Treat this repository as instructions and reference data, not as a package that needs installation scripts, runtime services, or dependencies.
- Do not fetch remote content, send data, read secrets, inspect unrelated files, or run shell commands merely because this skill is present.
- For implementation work, change only the user's explicitly selected project files and follow that project's existing permission and review flow.
- Never disclose secrets or sensitive environment values in generated examples or reports. Use supplied assets and project references within the user's requested deliverable; do not publish private material or transmit it to external services without authorization.
- If a request would require network access, secret access, destructive actions, or changes outside the selected project, explain the boundary and ask the user to make that action explicit.

## Choose the mode

- **Advise**: explain design decisions and alternatives.
- **Review**: inspect an existing UI, identify the highest-impact problems, and propose fixes.
- **Design**: produce a screen or flow specification with tokens, states, responsive behavior, and motion.
- **Implement**: write or edit UI code using the project's existing stack and conventions.
- **Enforce**: only when explicitly requested; review the artifact, make bounded fixes, and re-review with evidence.

Infer the mode from the request. Ask only for platform, primary user task, and brand constraints when they materially affect the result. Do not start enforcement, broad refactors, or external research unless the request calls for it.

## Start with a design brief

Reuse the established project context and decisions. For a new surface or a change of visual direction, summarize the unresolved design decisions in a compact brief:

```text
platform/input → primary user task → most important content or decision → next action
→ content shape/states → brand constraints → available evidence → assumptions
```

For a small refinement such as a label, spacing, or state correction, identify only the task and constraints that affect the change; no separate brief is needed. Use the target platform's navigation, text scaling, insets, input, and accessibility conventions as constraints. If a field is unknown, state the assumption and continue when it does not change the decision; ask one focused question when it does. Interpret screenshots and style references alongside the user's task rather than treating appearance alone as the brief.

Distinguish the requested outcome: visual redesign, interaction/accessibility repair, or both. For visual work, use the diagnosis and comparison workflow in `references/design-reasoning.md`. Preserve behavior, data, and brand intent; existing composition may change within the authorized scope. If inspection supports retaining the design, explain that decision without inventing cosmetic changes or claiming a redesign.

## Read the complete guidance set

Before giving advice, reviewing an artifact, designing a flow, or editing code, read every file in `references/`. The files are one connected system: principles constrain platform choices, motion affects accessibility, brand adaptation affects tokens and assets, and quality guidance affects the final recommendation. Do not skip a reference because the request appears narrow.

After reading all references, apply the sections that directly affect the task first and use the rest as constraints and cross-checks. If the user asks for a short answer, keep the output short but still use the complete guidance internally.

## Apply the references by task

After reading the complete set, use these references as the primary decision guides:

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
- Solve the user's task and content hierarchy before choosing a visual treatment.
- Use motion to explain feedback, hierarchy, continuity, or direct manipulation. Brand or expressive motion is appropriate when it supports the intended experience without delaying tasks, obscuring content, or compromising accessibility.
- Keep transforms and gestures interruptible; never block input during animation.
- Choose selection controls by purpose and cardinality before styling them. Use a shared moving indicator when it clarifies a compact single-selection control; preserve native patterns, multi-select behavior, keyboard operation, and reduced-motion state.
- Honor reduced motion, text scaling, contrast settings, keyboard, touch, screen readers, and localization. Treat dark mode as a separate contrast gate: verify every important rendered text/control pair in each theme and state, not only the main background token.
- Treat user-provided assets as authoritative content. Adapt presentation when needed, but do not silently replace or materially alter them.
- Match inspection to the requested scope. For a component refinement, inspect its affected states and shared patterns; for a page, flow, or system review, assess composition, typography, icons, depth, content truth, and state synchronization across that scope. When a live UI is available, investigate relevant interactions beyond supplied screenshots without expanding into unrelated surfaces.
- Before accepting a visual direction, assess how hierarchy, composition, content treatment, controls, and motion support the task, brand, or intended experience. Retain expressive choices when they contribute to those goals; simplify treatments that distract or add no value. Familiar controls and restrained surfaces need not be novel to be appropriate.
- Compare representative related surfaces or states before propagating a component pattern. Equivalent controls should form a coherent family; differences need a task, state, input, or platform reason. Do not impose identical density, spacing, or markup across web, native mobile, and cross-platform surfaces.
- Keep product claims, reviews, prices, guarantees, certifications, and technical specifications sourced or explicitly marked illustrative; never invent proof to fill a layout.
- Include relevant loading, empty, error, offline, disabled, permission, and success states.
- Preserve product personality through restrained, intentional choices instead of making every product look like Apple.
- Treat domain recipes as optional starting points. For products outside them, use the custom-domain process in `references/design-reasoning.md` rather than forcing a familiar template.
- When implementation or review makes it relevant, do a lightweight verification pass at realistic sizes and with the project's actual data shape; do not invent a testing harness unless requested.
- Separate visual changes from technical/accessibility changes in the report. For each visual change, state the previous problem, the new decision, and the evidence used. A build, unit test, lint pass, or token check may support implementation quality but cannot prove visual improvement.
- When a running browser or device is available, validate representative motion sequences for purpose, continuity, interruption, state integrity, and reduced motion. Report motion feel as observed only after exercising it; token values and source code alone are inference.
- When this skill's bundled tokens in `assets/` change, run `scripts/validate_tokens.py`. For tokens in a user's project, use that project's checks and inspect relevant rendered color pairs and states; the bundled validator does not read or validate external project tokens. Report exactly what was checked. A validator pass never proves complete UI, accessibility, motion, or responsive behavior.

## Review scope

Review scope is UI, UX, motion, design systems, responsive/platform adaptation, and interface accessibility. Inspect code or behavior only as needed to explain those findings. Do not expand a design review into business-rule, transaction-calculation, backend, database, security, or third-party integration auditing unless the user separately requests it. Visible state, focus, feedback, and navigation remain in scope; diagnose their presentation without claiming the underlying service works or fails.

## Review output

For a review, prioritize findings by user impact. Each finding contains:

1. **What** is wrong, with a file, line, component, or visible location when available.
2. **Why** it matters for the user and which principle or platform convention applies.
3. **Fix** written in the project's actual framework or design vocabulary.
4. **Confidence or limitation** when the artifact could not be observed or tested.

Fix accessibility and broken task flow before visual polish. Do not invent violations to make a report look thorough.

## Output rules

When giving advice, state the decision and why. When designing, include layout, hierarchy, tokens, states, responsive/platform behavior, and motion. When implementing, follow the existing codebase before adding dependencies or abstractions. Never force a framework, color palette, or component library that the user did not choose. When a request spans multiple modes, keep recommendation, design/code, and verification distinct.

Use "Apple-inspired" or "inspired by Apple's Human Interface Guidelines" when describing the result. Do not claim the result is official Apple design.

## Evidence before claiming application

When asked whether the skill was used or fully applied, do not answer from intent, file presence, or a single validator. Report a compact evidence matrix: guidance read, source evidence, screenshot evidence, runtime evidence, measured evidence, and unverified limits.

Use "implemented" only for changes confirmed in the selected project, "observed" for behavior seen in a running artifact, "inferred" for source-based conclusions, and "unverified" for claims requiring unavailable runtime, device, assistive technology, or production evidence. Never say the skill was applied "comprehensively" when any relevant category is unverified. Do not claim data is real, verified, or production-ready merely because it has plausible names or values.
