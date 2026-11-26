# Flutter and React Native

Share tokens, content, and composition across platforms; adapt navigation, controls, and motion per platform (`../surfaces/mobile-android-crossplatform.md`).

## Flutter

- **Tokens:** `python scripts/palette.py "<seed>" --format flutter` → `AppColorsLight/Dark` and `lightColorScheme`/`darkColorScheme`. Use `ThemeData(useMaterial3: true, colorScheme: lightColorScheme)` and `darkTheme`; add a `ThemeExtension` if you need the extra roles (`brand`, `textTertiary`, `link`) inside widgets.
- **Structure:** `CustomScrollView` + `CupertinoSliverNavigationBar` on iOS / `SliverAppBar.large` on Android for the large-title effect; `CupertinoTabScaffold` or `NavigationBar` per platform; `showModalBottomSheet` / `showCupertinoSheet` with drag handles.
- **Adaptive widgets:** `Switch.adaptive`, `Slider.adaptive`, `CircularProgressIndicator.adaptive`, `showAdaptiveDialog`, `Theme.of(context).platform` for branching.
- **Craft:** `BorderRadius.circular(22)` cards with `clipBehavior: Clip.antiAlias`; `AnimatedScale(scale: pressed ? .97 : 1, duration: 120ms)` on press; `Hero` for card → detail; `PageView`/`ListView` with `PageScrollPhysics` or snapping for shelves; `BackdropFilter` for translucent bars only; `HapticFeedback.selectionClick()`.
- **Springs:** `SpringSimulation(SpringDescription(mass: 1, stiffness: 273, damping: 28.4), from, to, velocity)` driven by an `AnimationController`, or `Curves.easeOutCubic` for short fades.
- **Type:** system fonts per platform by default; `TextTheme` with bold display/headline roles and `FontFeature.tabularFigures()` for numbers. Respect `MediaQuery.textScalerOf(context)`.
- **Accessibility:** `Semantics` labels, `MediaQuery.disableAnimationsOf(context)` for reduced motion, text scaling up to 200%, 44–48 targets.

## React Native / Expo

- **Tokens:** generate `--format json` and expose a typed theme object (light/dark) through the project's theming approach; switch with `useColorScheme()` plus a user override if the app has one.
- **Navigation:** React Navigation / Expo Router native stack with `headerLargeTitleEnabled: true` (React Navigation 7; `headerLargeTitle` in v6 — check the installed version), `headerLargeTitleShadowVisible: false`, `headerTransparent` + `headerBlurEffect` on iOS; native bottom tabs where available; Android gets Material-style headers and system back.
- **Craft:** `Pressable` with a Reanimated scale to 0.97 using `withSpring(…, { mass: 1, stiffness: 273, damping: 28.4 })`; `FlatList` horizontal with `snapToInterval` and `decelerationRate="fast"` for shelves; `borderRadius: 22` with `borderCurve: 'continuous'` on iOS; shared element transitions where the navigation library supports them; `expo-haptics` if present; a blur view only if a blur library is already installed.
- **Type:** system font by default; `fontVariant: ['tabular-nums']`; allow font scaling (`allowFontScaling` stays true; cap with `maxFontSizeMultiplier` only for chrome, never for reading text).
- **Accessibility:** `accessibilityRole`, `accessibilityLabel`, `accessibilityState`; `AccessibilityInfo.isReduceMotionEnabled()` / Reanimated's `useReducedMotion()`; 44–48 targets; both themes.

## Checks

Run on an iOS simulator and an Android emulator (or devices) at small and large phone sizes, largest text, both themes, and reduced motion. Compare the same screen on both platforms: composition and color should match; chrome and controls should feel native to each.
