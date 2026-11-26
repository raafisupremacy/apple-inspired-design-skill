# SwiftUI and UIKit

Native Apple platforms get the most from system components: they bring Liquid Glass, Dynamic Type, accessibility, and platform motion for free. Customize content and color; keep the structure native.

## Tokens

- `python scripts/palette.py "<seed>" --format swiftui` produces an `AppColor` enum with light/dark dynamic colors. For production, the same values can move into an asset catalog (Any / Dark appearances); keep one source.
- Set the accent: an `AccentColor` asset and/or `.tint(AppColor.accent)` at the root.
- Use system semantic colors (`.primary`, `.secondary`, `Color(.systemGroupedBackground)`) for chrome when the brand calls for neutral; use `AppColor` roles for tinted grounds, brand moments, and content.

## Structure

```swift
TabView {
    Tab("Today", systemImage: "sun.max") { NavigationStack { TodayView() } }
    Tab("Browse", systemImage: "square.grid.2x2") { NavigationStack { BrowseView() } }
    Tab(role: .search) { NavigationStack { SearchView() } }
}
.tint(AppColor.accent)
.tabBarMinimizeBehavior(.onScrollDown)        // iOS 26+
```

```swift
struct TodayView: View {
    var body: some View {
        ScrollView {
            LazyVStack(alignment: .leading, spacing: 28) {
                HeroCard(item: featured)
                ShelfSection(title: "Continue", items: recent)
            }
            .padding(.horizontal, 20)
        }
        .background(AppColor.bg)
        .navigationTitle("Today")              // large title by default at top level
        .toolbar { ToolbarItem { Button("Add", systemImage: "plus") { add() } } }
    }
}
```

## Craft details

- **Type:** `.font(.largeTitle.bold())`, `.title2.weight(.semibold)`, `.body`, `.subheadline`, `.footnote`; `.monospacedDigit()` for changing numbers; `.fontDesign(.rounded)` for friendly products. Never fixed point sizes for reading text; use `@ScaledMetric` for custom spacing that should scale.
- **Shapes:** `RoundedRectangle(cornerRadius: 22, style: .continuous)`, `.containerShape` / `ConcentricRectangle` (iOS 26) for concentric corners, `Capsule()` for buttons.
- **Buttons:** `.buttonStyle(.borderedProminent)` or `.glassProminent` for the primary action, `.bordered` / `.glass` for secondary, `.controlSize(.large)` for full-width primary.
- **Press feedback:** a custom `ButtonStyle` that scales to 0.97 with `.animation(.snappy, value: configuration.isPressed)`.
- **Lists:** `List { Section { … } header: { … } footer: { … } }.listStyle(.insetGrouped)`; colored icon tiles via `Label` with a rounded rectangle background.
- **Sheets:** `.sheet(isPresented:) { … .presentationDetents([.medium, .large]) .presentationDragIndicator(.visible) }`.
- **Transitions:** `.navigationTransition(.zoom(sourceID: id, in: namespace))` with `.matchedTransitionSource(id:in:)` for card → detail; `matchedGeometryEffect` for in-place changes; `.contentTransition(.numericText())` for changing numbers; `.symbolEffect(.bounce, value:)`.
- **Scroll:** `.scrollTransition { content, phase in content.scaleEffect(phase.isIdentity ? 1 : 0.94).opacity(phase.isIdentity ? 1 : 0.8) }` for shelves; `.scrollTargetBehavior(.viewAligned)` for snapping.
- **Haptics:** `.sensoryFeedback(.selection, trigger: selection)`, `.success`, `.impact(weight: .light)`.
- **Glass:** `.glassEffect()`, `GlassEffectContainer`, `.glassEffectID` — functional layer only (`../foundations/depth-materials.md`). Gate with `if #available(iOS 26, *)` and fall back to materials.
- **Empty states:** `ContentUnavailableView("No Trips", systemImage: "airplane", description: Text("Trips you plan appear here."))`.

## Accessibility

Test the largest accessibility text sizes (switch to vertical stacks with `ViewThatFits` or `dynamicTypeSize` checks), VoiceOver labels (`.accessibilityLabel`, `.accessibilityValue`, combine children), `@Environment(\.accessibilityReduceMotion)` and `\.accessibilityReduceTransparency`, Increase Contrast, and Smart Invert. Use Xcode Previews with multiple traits (dark, large text, landscape) as quick evidence.

## UIKit

`UINavigationBar.prefersLargeTitles = true`, `UISheetPresentationController` detents, `UIGlassEffect` (iOS 26), `UIFont.preferredFont(forTextStyle:)` with `adjustsFontForContentSizeCategory`, `UIViewPropertyAnimator` / `UIView.animate(springDuration:bounce:)` for springs, `UIImpactFeedbackGenerator` for haptics.
