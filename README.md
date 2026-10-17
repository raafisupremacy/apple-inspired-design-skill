# Apple-inspired design

An agent skill for designing, reviewing, advising on, and implementing calm, precise web and mobile interfaces with Apple-inspired clarity and motion.

It works across web, iOS, Android, React Native, Flutter, and similar stacks. The skill adapts to the product's brand, content, platform conventions, and user-provided assets; it does not require Apple branding.

## Install

```bash
npx skills add raafisupremacy/apple-inspired-design-skill
```

After installation, ask your coding agent to use `apple-inspired-design` for UI advice, design specifications, visual reviews, or implementation work.

Restart or refresh the agent after installation if it does not discover the skill immediately. To update it, run the same install command again and accept the installer’s update prompt. To remove it, use the agent’s skill manager or delete this skill’s installed folder from that manager’s skills directory; do not delete the project being designed.

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

- **Advise** for a design decision or trade-off
- **Review** for an existing screen, flow, screenshot, or codebase
- **Design** for a screen or flow specification
- **Implement** for writing or editing UI code
- **Enforce** only when you explicitly request bounded fixes and re-review

For the best result, provide real content and user-provided images when available. The agent should preserve those assets, ask only for missing constraints that affect the decision, and state what it could not observe or verify.

If the agent produces a generic result, add the missing context rather than repeating “make it more Apple”: name the primary user task, platform and input method, current project path, real content shape, brand constraints, and the outcome you want. For an implementation request, explicitly authorize code changes in the selected project.

## What the package contains

- `SKILL.md`: entry point, safety boundaries, modes, and routing
- `AGENTS.md`: integration workflow for agent runtimes
- `references/`: focused web, mobile, motion, accessibility, content, brand, and reasoning guidance
- `assets/`: framework-neutral starter tokens in CSS and JSON
- `scripts/`: local validators with no third-party dependencies

## Scope

- Web apps, websites, PWAs, and responsive browser interfaces
- Native and cross-platform mobile interfaces
- Interaction design with deliberate, smooth motion
- Design advice, reviews, specifications, and implementation guidance

The skill is a design system and agent workflow, not a device lab or automated visual-testing framework.

## Security

The repository contains guidance, static tokens, and local standard-library validators only. It has no install hooks, runtime services, telemetry, network client, credential handling, or bundled executable. See [SECURITY.md](SECURITY.md) for the trust boundaries and audit notes.

The skill is Apple-inspired guidance, not Apple’s official design system and not a guarantee of WCAG conformance, device behavior, performance, or visual similarity.

## Troubleshooting

- **The skill is not detected:** restart or refresh the agent, then confirm the installer placed a folder named `apple-inspired-design` containing `SKILL.md` at its root.
- **The agent gives only generic advice:** provide the actual screen, code, screenshot, or project path and name the user task; ask for Review or Implement mode explicitly.
- **The output ignores the brand:** provide the existing logo, colors, type, copy tone, and user-supplied media, then ask the agent to preserve them.
- **Motion feels wrong:** specify the interaction, interruption behavior, target platform, and reduced-motion requirement; the skill does not claim Apple’s private timing values.
- **A project needs runtime proof:** ask for proportionate browser/device/accessibility/performance verification separately; this package is a design and agent-guidance skill, not an automated test lab.
