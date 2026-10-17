# Compatibility and testing

## Capability first

Choose behavior from the user task and available capability, not from a favorite API. Detect or feature-test support for View Transitions, container queries, scroll-driven animation, service workers, and other optional browser features. Keep the core content and interaction usable when a feature is unavailable.

Do not use user-agent strings as the primary responsive strategy. Prefer viewport, container, input, preference, and capability signals. A phone-sized viewport may have a keyboard or pointer; a wide viewport may still be touch-first.

## Evidence levels

When reporting quality, label the evidence:

- **Observed**: seen in the running artifact, source, or a supplied screenshot.
- **Measured**: supported by a contrast calculation, performance trace, automated test, or viewport check.
- **Inferred**: likely from the implementation but not executed.
- **Unverified**: requires a device, browser, assistive technology, or production data that was unavailable.

Never turn an inference into a pass claim.

## Minimum verification

- Responsive: narrow mobile, large mobile, tablet or intermediate container, desktop, zoom/text scaling, and long content.
- Input: keyboard and focus, touch, coarse pointer, fine pointer, and platform back behavior where relevant.
- Preferences: light/dark, increased contrast, reduced motion, reduced transparency, and locale/RTL where supported.
- States: loading, empty, error, offline, retry, disabled, permission, validation, success, and destructive recovery.
- Media: slow image loading, failed image loading, user-provided asset dimensions, and layout-shift prevention.
- Motion: interrupt a transition, reverse it, navigate during it, and verify reduced motion.
- Performance: inspect long lists, image-heavy screens, low-power conditions, and Web Vitals or the platform equivalent when the task requires it.

## What a score means

Lighthouse, automated accessibility checks, a design-token validator, or a successful build are useful evidence for their own scope. None of them proves that hierarchy, platform fit, copy, motion feel, or the complete user task are good. Combine automated checks with artifact inspection and a small manual task walkthrough.
