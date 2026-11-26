# Jetpack Compose (Android)

Express Apple-inspired qualities through Material 3, not by imitating iOS.

## Tokens

- `python scripts/palette.py "<seed>" --format compose` produces `AppColorsLight/Dark` objects and `AppLightColorScheme` / `AppDarkColorScheme`.
- In the app theme: `MaterialTheme(colorScheme = if (dark) AppDarkColorScheme else AppLightColorScheme, typography = AppTypography, shapes = AppShapes)`.
- Dynamic color: decide explicitly. For a strong brand keep the generated scheme; if you support dynamic color, keep brand moments (hero, primary action) on the brand roles.

## Structure

`Scaffold` with `LargeTopAppBar` / `MediumTopAppBar` and `TopAppBarDefaults.exitUntilCollapsedScrollBehavior()`; `NavigationBar` (or `NavigationSuiteScaffold` for adaptive rail/drawer); `ModalBottomSheet`; edge-to-edge with `enableEdgeToEdge()`; predictive back via the navigation library.

## Craft details

- **Type:** a `Typography` with bold `headlineLarge`/`displaySmall` for top titles and metrics, `bodyLarge` for reading, `labelMedium` for captions; `fontFeatureSettings = "tnum"` for numbers.
- **Shapes:** `Shapes(small = RoundedCornerShape(10.dp), medium = RoundedCornerShape(18.dp), large = RoundedCornerShape(28.dp))`; `CircleShape`/full rounding for primary buttons.
- **Press feedback:** combine ripple with a scale: collect `interactionSource.collectIsPressedAsState()` and animate `graphicsLayer { scaleX = s; scaleY = s }` with `spring(dampingRatio = 0.86f, stiffness = 273f)`.
- **Motion:** `animateContentSize()`, `AnimatedContent`, `SharedTransitionLayout` + `Modifier.sharedElement()` for card → detail, `LazyRow` with `rememberSnapFlingBehavior` for shelves.
- **Haptics:** `LocalHapticFeedback.current.performHapticFeedback(HapticFeedbackType.TextHandleMove)` or `View.performHapticFeedback(HapticFeedbackConstants.CONFIRM)`.
- **Surfaces:** tonal elevation via `surfaceContainer*` roles rather than heavy shadows; `Card` with generous radius and padding.

## Accessibility

Font scale up to 200%, TalkBack labels (`Modifier.semantics`), `contentDescription` for icons, 48dp touch targets, reduced motion via `Settings.Global.ANIMATOR_DURATION_SCALE` / `LocalAccessibilityManager`, both themes. Use `@PreviewFontScale`, `@PreviewLightDark`, and `@PreviewScreenSizes` as quick evidence.
