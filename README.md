# Apple-inspired design

An agent skill for designing, reviewing, advising on, and implementing calm, precise web and mobile interfaces with Apple-inspired clarity and motion.

It works across web, iOS, Android, React Native, Flutter, and similar stacks. The skill adapts to the product's brand, content, platform conventions, and user-provided assets; it does not require Apple branding.

## What it covers

The skill helps an agent make decisions about:

- UI hierarchy, composition, typography, color, spacing, surfaces, depth, and design tokens
- UX flows, navigation, forms, feedback, loading, empty, error, offline, disabled, permission, and success states
- Purposeful motion, shared transitions, selection continuity, gestures, interruption, and reduced motion
- Responsive web layouts, mobile adaptation, safe areas, touch, keyboard, text scaling, and platform conventions
- Accessibility, localization, content truth, icon consistency, and user-provided images or other media
- Brand adaptation without forcing every product into the same Apple-like visual template

It can advise, produce a design specification, review an existing artifact, or implement UI changes in the project's existing stack.

## Install

```bash
npx skills add raafisupremacy/apple-inspired-design-skill
```

After installation, ask your coding agent to use `apple-inspired-design` for UI advice, design specifications, visual reviews, or implementation work.

Restart or refresh the agent after installation if it does not discover the skill immediately. To update it, run the same install command again and follow the installer’s prompts to replace the existing installation. To remove it, use the agent’s skill manager or delete this skill’s installed folder from that manager’s skills directory; do not delete the project being designed.

## Use it

After installation, use the skill by asking your coding agent in normal language. The prompt below is an example of a **Review** request: it tells the agent to inspect an existing mobile checkout screen, keep the current brand, and organize the findings as What, Why, Fix, and Evidence.

```text
Use apple-inspired-design in Review mode. Audit this mobile checkout screen for hierarchy,
accessibility, states, and motion. Keep the existing brand and report What / Why / Fix / Evidence.
```

You can attach a screenshot, provide a project path, or point the agent at the existing UI code. Include the product task, target platform, real content, brand constraints, and requested outcome when those details matter. The mode is optional; the agent can infer it from your request.

Examples:

```text
Advise me on whether this web dashboard should use a table or grouped list for reviewing invoices.
Keep the existing blue brand and explain the trade-off.
```

```text
Design an iOS and Android onboarding flow for a budgeting app. Define the hierarchy, states,
tokens, responsive/platform differences, accessibility, and purposeful motion.
```

```text
Implement this responsive product page in the project’s existing React stack. Use the supplied
images as-is, preserve the current data flow, include loading and error states, and report the
files changed and checks performed.
```

The available modes are:

- **Advise** returns a recommended design decision, the reason, and relevant trade-offs.
- **Review** returns prioritized What / Why / Fix / Evidence findings for an existing screen, flow, screenshot, running UI, or codebase.
- **Design** returns a screen or flow specification covering hierarchy, layout, tokens, states, responsive or platform adaptation, accessibility, and motion.
- **Implement** edits the selected project's UI using its existing stack, preserves data and error handling, and reports files changed and checks performed.
- **Enforce** applies only explicitly requested, bounded fixes and then re-reviews the result.

For the best result, provide real content and user-provided images when available. The agent should preserve those assets, ask only for missing constraints that affect the decision, and state what it could not observe or verify.

Use the request type that matches your goal:

- **Advice only:** name the task, platform, current brand, and decision you need to make.
- **Design/specification:** name the task, users, content shape, target sizes, states, and desired deliverable.
- **Review/audit:** provide the project path, screen or URL, representative content, target viewports, and interactions to inspect.
- **Implementation:** explicitly authorize edits in the selected project and provide the existing stack, assets, and acceptance criteria.

When you provide images, logos, screenshots, or video, the agent treats them as authoritative project content. It may recommend a different crop, scale, placement, or responsive treatment, but it should not silently replace or materially alter the supplied asset.

For a visual redesign, ask the agent to connect observed visual problems to composition changes and compare the result with the baseline. Keep technical repairs and visual results separate. Existing brand and behavior can be preserved while hierarchy, grouping, and layout change. If context is missing, supply the task, platform, real content, and intended outcome; a generic result is not automatically caused by an inadequate user prompt.

```text
Use apple-inspired-design to redesign the selected interface. Inspect the current artifact,
identify the highest-impact visual problems, and implement concrete composition and hierarchy
improvements while preserving brand, platform conventions, and business behavior. Compare before
and after where rendering is available. Cover the requested screens; use one representative
surface to calibrate, not to silently reduce scope. Report visual results separately from
build/test/accessibility checks, and label unverified rendering or interaction explicitly.
```

## What the package contains

- `SKILL.md`: entry point, safety boundaries, modes, and routing
- `AGENTS.md`: integration workflow for agent runtimes
- `references/`: focused web, mobile, motion, accessibility, content, brand, and reasoning guidance
- `assets/`: framework-neutral starter tokens in CSS and JSON
- `scripts/`: local validators with no third-party dependencies. `check_references.py` checks all Markdown links; `validate_tokens.py` checks starter color, motion, and directly mapped CSS/JSON token parity.

## Scope

- Web apps, websites, PWAs, and responsive browser interfaces
- Native and cross-platform mobile interfaces
- Interaction design with deliberate, smooth motion
- Design advice, reviews, specifications, and implementation guidance

The skill supports products beyond the included recipes: CRM, commerce, advertising, company profiles, and other web or mobile tasks use the same context-driven decision process. Recipes are optional starting points, not a catalog of the only supported products. Real-project audits improve general decision criteria rather than making the audited website a mandatory template.

Updating the installed skill updates the agent's guidance; it does not automatically rewrite existing project code. Ask the agent to apply the updated skill to the intended design or implementation task.

Reviews focus on UI, UX, motion, design systems, responsive/platform adaptation, and interface accessibility. Business logic, backend, database, and payment/shipping integration audits are separate tasks. Real-project reviews used to improve the skill extract reusable design criteria rather than product-specific requirements.

For a UI audit, expect checks of hierarchy, typography, spacing, color and theme states, icon language, imagery, responsive composition, navigation, interaction states, accessibility behavior, and motion. It does not verify transaction calculations, API correctness, database behavior, authentication, payment processing, shipping, or other application logic unless those are separately requested.

The skill is a design system and agent workflow, not a bundled device lab or automated visual-testing framework. When a browser or device is available, the agent can perform a scoped runtime review and report observed motion feel, responsive behavior, focus, and state transitions. Without a running artifact, those results remain unverified.

Evidence has separate levels:

- **Static/source:** files, tokens, component structure, and declared states inspected in code.
- **Measured:** calculations such as token contrast or layout dimensions produced by a script or inspection.
- **Runtime observed:** behavior exercised in a running browser or device, including motion feel and interruption.
- **Unverified:** behavior requiring a runtime, device, assistive technology, production data, or other evidence that was unavailable.

A passing validator or successful build does not prove that the complete design guidance was applied.

The bundled token files are starter values, not a complete project theme. Keep `tokens.json` and `tokens.css` synchronized for directly mapped values, then run the validators. A passing validator covers file links and token structure/parity only; it does not prove contrast for every rendered state, responsive behavior, accessibility, or motion feel. For motion validation, provide a running browser or device and ask the agent to inspect representative interactions using the evidence labels in `references/compatibility-testing.md`.

## Security

The repository contains guidance, static tokens, and local standard-library validators only. It has no install hooks, runtime services, telemetry, network client, credential handling, or bundled executable. See [SECURITY.md](SECURITY.md) for the trust boundaries and audit notes.

The skill is Apple-inspired guidance, not Apple’s official design system and not a guarantee of WCAG conformance, device behavior, performance, or visual similarity.

## Not for

Do not use this skill as a backend, database, API, payment, shipping, security, load-testing, device-farm, or automated visual-regression system. It can inspect implementation code when needed to explain a UI finding, but its design review scope remains the interface and user experience.

## Troubleshooting

- **The skill is not detected:** restart or refresh the agent, then confirm the installer placed a folder named `apple-inspired-design` containing `SKILL.md` at its root.
- **The agent gives only generic advice:** provide the actual screen, code, screenshot, or project path and name the user task; ask for Review or Implement mode explicitly.
- **The output ignores the brand:** provide the existing logo, colors, type, copy tone, and user-supplied media, then ask the agent to preserve them.
- **Motion feels wrong:** specify the interaction, interruption behavior, target platform, and reduced-motion requirement; the skill does not claim Apple’s private timing values.
- **A project needs runtime proof:** ask for proportionate browser/device/accessibility/performance verification separately; this package is a design and agent-guidance skill, not an automated test lab.
