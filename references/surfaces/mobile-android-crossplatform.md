# Android and cross-platform mobile

Apple-inspired on Android means Apple's qualities — content first, confident type, one color story, generous grouping, physical motion — expressed through Android's own conventions. Do not ship iOS chevrons, an iOS tab bar look, or swipe-back-only navigation to Android users.

## Android (Material 3)

- **Structure:** edge-to-edge layout; top app bar (large or medium collapsing bar is the counterpart of the iOS large title); navigation bar for 3–5 destinations, navigation rail on tablets and foldables; bottom sheets and dialogs from Material.
- **Back:** system back and predictive back animations must work everywhere.
- **Color:** when the user chose a brand color, map `palette.py --format compose` into `lightColorScheme`/`darkColorScheme` and decide deliberately about dynamic color (wallpaper-based): either off for a strong brand, or on with the brand kept for key moments. Do not let dynamic color erase the brand by accident.
- **Type:** Material roles with Roboto Flex or the brand font; make the top-level title large and bold, metrics bold and tabular.
- **Shape:** Material's shape scale with generous corners on cards and sheets; capsule buttons are native here too.
- **Motion:** Material's spring-based motion; shared element transitions; press states via ripple or scale. Use `HapticFeedbackConstants` for meaningful moments.
- **Components:** use Material components (cards, lists, chips, segmented buttons, switches) and restyle through the theme rather than rebuilding them.

## Cross-platform (Flutter, React Native, Expo, Kotlin Multiplatform)

Share tokens, content, information architecture, and composition. Adapt navigation, controls, and motion per platform.

| Concern | iOS | Android |
| --- | --- | --- |
| Top-level title | large title that collapses | large/medium top app bar |
| Destinations | tab bar | navigation bar |
| Back | edge swipe + back button | system back, predictive back |
| Toggles, pickers, alerts | Cupertino-style | Material |
| Sheets | detents, grabber | Material bottom sheet |
| Haptics | light impacts, selection | `HapticFeedbackConstants` |

Practical mappings:

- **Flutter:** `CupertinoSliverNavigationBar` (large title) on iOS and `SliverAppBar.large` on Android; `.adaptive` constructors (`Switch.adaptive`, `Slider.adaptive`, `showAdaptiveDialog`); `ColorScheme` from `palette.py --format flutter`; `Hero` for card-to-detail; `HapticFeedback.selectionClick()`.
- **React Native / Expo:** native-stack headers with `headerLargeTitleEnabled: true` (`headerLargeTitle` in React Navigation 6) and `headerTransparent`/blur on iOS; platform tabs; a bottom-sheet library only if already in the project; `Platform.select` for control styling; Reanimated + Gesture Handler for springs and gestures (`../foundations/motion.md`); `expo-haptics` when present.
- **Compose Multiplatform / KMP:** keep Material on Android; on iOS prefer native SwiftUI screens or careful adaptive components.

Use the system font on each platform unless the brand supplies a licensed font for both.

## Recipes

The iOS screen recipes in `mobile-ios.md` (Today, summary dashboard, list → detail, settings, onboarding, media, forms, empty states) translate directly: keep the composition and color story, swap the navigation chrome and controls for the platform's.

## Checks

Test on a small and a large phone, a tablet/foldable width, with the keyboard open, at the largest font scale, with TalkBack/VoiceOver, with reduced motion, and in both themes. Make sure the brand color survives dark mode and dynamic color decisions.

## Sources

Checked 2026-11-26: [Material 3](https://m3.material.io/), [Android: Edge-to-edge](https://developer.android.com/develop/ui/views/layout/edge-to-edge), [Android: Predictive back](https://developer.android.com/guide/navigation/custom-back/predictive-back-gesture), [Flutter adaptive design](https://docs.flutter.dev/ui/adaptive-responsive), [React Navigation native stack](https://reactnavigation.org/docs/native-stack-navigator/).
