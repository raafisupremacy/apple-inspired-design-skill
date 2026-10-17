# Anti-patterns

Use this as a diagnostic list, not a rigid ban on every visual technique.

- **Card soup**: many sibling cards with separate borders, fills, and shadows where one grouped surface would scan better.
- **Decoration-first hierarchy**: gradients, glass, glow, icons, or illustrations added before the task and content are clear.
- **Token theater**: many named tokens that do not map to semantic roles or are not used consistently.
- **Platform cosplay**: web controls dressed as native UI, or native apps forced into web dashboard patterns.
- **Animation wallpaper**: motion that repeats, delays work, distracts, or has no explanatory purpose.
- **Static selection swap**: a segmented control or variant picker changes fill or text color independently on each button instead of moving one shared selection surface, losing continuity between states.
- **Screenshot success**: a layout that looks polished in one static viewport but fails with real content, keyboard, text scaling, or interaction.
- **Color semantics drift**: the same color means different states, or status is communicated only by color.
- **Placeholder blindness**: lorem ipsum, perfect round numbers, generic names, or empty states that hide the real content shape.
- **Asset disrespect**: silently replacing, cropping away important content, filtering, or fabricating user-provided media.
- **Accessibility afterthought**: tiny text, missing focus, inaccessible gestures, auto-dismissed critical messages, or contrast fixes that destroy hierarchy.
- **API fog**: component and prop names that conceal intent, duplicate the design decision, or make the usage harder to understand.

When finding an anti-pattern, name the underlying problem and propose the smallest change that repairs it.
