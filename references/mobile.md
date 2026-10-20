# Mobile adapter

- Use native platform navigation and back behavior for the target OS.
- Design for touch first with comfortable targets, adequate spacing, safe areas, and system text scaling.
- Use sheets, tab bars, navigation stacks, gestures, haptics, and permission prompts according to the target platform rather than copying web controls.
- Keep common tasks short and preserve context when moving between screens.
- Calibrate reachability to task frequency, hand position, device size, orientation, and interruption level; do not force every primary action to the bottom or copy a fixed iPhone layout.
- Re-evaluate the composition when the keyboard, rotation, split view, fold, or window resize changes available space. Preserve the task, current selection, and return path while controls reflow.
- Support VoiceOver/TalkBack, Reduce Motion, increased contrast, dynamic type or font scaling, keyboard and external input where available.
- For cross-platform frameworks, share content and tokens while allowing platform-specific interaction and motion adapters.

For forms and focused work, account for the on-screen keyboard, safe-area changes, reachable actions, and scroll-to-focused-field behavior. Preserve entered data and relevant context across background/resume and navigation; distinguish pending work from completed work.

Respect system back and edge gestures, and resolve conflicts with nested scrolling or swipe actions. Prefer the platform's existing control and motion behavior where it satisfies the task; Apple inspiration does not require iOS interaction conventions on Android.
