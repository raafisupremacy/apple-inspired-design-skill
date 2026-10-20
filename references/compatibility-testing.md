# Compatibility and testing

## Capability first

Choose behavior from the user task and available capability, not from a favorite API. Detect or feature-test support for View Transitions, container queries, scroll-driven animation, service workers, and other optional browser features. Keep the core content and interaction usable when a feature is unavailable.

Do not use user-agent strings as the primary responsive strategy. Prefer viewport, container, input, preference, and capability signals. A phone-sized viewport may have a keyboard or pointer; a wide viewport may still be touch-first.

## Evidence levels

When reporting quality, label the evidence:

- **Source evidence**: declarations and structure inspected in files; this does not establish runtime behavior.
- **Screenshot evidence**: appearance visible in a supplied or captured still image; this does not establish transitions, interaction, or unshown states.
- **Observed**: behavior exercised in a running artifact, with the input, state, and viewport identified.
- **Measured**: supported by a contrast calculation, performance trace, automated test, or viewport check.
- **Inferred**: likely from the implementation but not executed.
- **Unverified**: requires a device, browser, assistive technology, or production data that was unavailable.

Never turn an inference into a pass claim.

## Minimum verification

Select checks affected by the requested change and supported platforms. This is a relevance matrix, not a requirement to test every category for a label or component fix. For appearance work, use the before/after comparison in `design-reasoning.md`; report visual acceptance separately from technical checks.

- Responsive: narrow mobile, large mobile, tablet or intermediate container, desktop, zoom/text scaling, and long content.
- Input: keyboard and focus, touch, coarse pointer, fine pointer, and platform back behavior where relevant.
- Preferences: light/dark, increased contrast, reduced motion, reduced transparency, and locale/RTL where supported.
- States: loading, empty, error, offline, retry, disabled, permission, validation, success, and destructive recovery.
- Media: slow image loading, failed image loading, user-provided asset dimensions, and layout-shift prevention.
- Motion: interrupt a transition, reverse it, navigate during it, and verify reduced motion.
- Performance: inspect long lists, image-heavy screens, low-power conditions, and Web Vitals or the platform equivalent when the task requires it.

## What a score means

Lighthouse, automated accessibility checks, a design-token validator, or a successful build are useful evidence for their own scope. None of them proves that hierarchy, platform fit, copy, motion feel, or the complete user task are good. Combine automated checks with artifact inspection and a small manual task walkthrough.

## Scope of verification claims

Verification is scoped evidence, not a certificate. A successful build or token check cannot establish that the full design guidance was applied. Do not infer runtime behavior from a CSS declaration, ARIA attribute, transition duration, or code path alone. Confirm interaction by exercising it; confirm responsive behavior at the relevant viewport; confirm reduced motion with the preference active; and report the exact scope of each check.

## Runtime motion and feel

When a running browser or device is available, validate motion as an interaction sequence rather than from timing values alone. For each representative transition or gesture, record:

- **Purpose:** what state, relationship, hierarchy, or direct manipulation the movement explains.
- **Continuity:** whether the moving content, selection surface, or shared element follows the user’s action without a jump, flash, or unexplained change of identity.
- **Physical response:** whether acceleration, deceleration, overshoot, and settling feel proportionate to the distance, surface, and input; do not claim Apple’s private curve or spring values.
- **Interruption:** whether a second tap, reverse drag, back action, dismissal, or navigation change cancels or redirects the current motion cleanly.
- **State integrity:** whether focus, selected state, open/closed visibility, scroll position, and content remain correct when the motion is interrupted or completed.
- **Reduced motion:** whether travel, bounce, shimmer, parallax, and count-up effects become an immediate or short opacity/state change while preserving visibility and operability.

Exercise the interaction at its intended viewport and input method, then repeat with slow and rapid input where interruption matters. Label the result **Observed** only after running it; label timing or source inspection **Inferred**; label unavailable browser/device interaction **Unverified**. A static duration, easing token, screenshot, or successful build is not evidence of motion feel.

Use the narrowest accurate verb: “declared” for source, “measured” for a calculation, “observed” for runtime, and “verified” only when the stated acceptance condition was actually checked.
