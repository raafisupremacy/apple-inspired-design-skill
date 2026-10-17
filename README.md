# Apple-inspired design

An agent skill for designing, reviewing, advising on, and implementing calm, precise web and mobile interfaces with Apple-inspired clarity and motion.

It works across web, iOS, Android, React Native, Flutter, and similar stacks. The skill adapts to the product's brand, content, platform conventions, and user-provided assets; it does not require Apple branding.

## Install

```bash
npx skills add raafisupremacy/apple-inspired-design-skill
```

After installation, ask your coding agent to use `apple-inspired-design` for UI advice, design specifications, visual reviews, or implementation work.

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
