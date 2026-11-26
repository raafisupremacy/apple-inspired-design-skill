# Desktop, iPad, watch, TV, spatial, and widgets

## macOS (and desktop web or Electron apps that target Mac users)

- Window structure: sidebar (source list) → content → optional inspector; unified toolbar on Liquid Glass with title, navigation, and actions.
- Every command lives in the menu bar with a keyboard shortcut; toolbars show the frequent ones. Support right-click context menus, drag and drop, multiple windows, and resizing to small sizes.
- Density: 13pt body, small/regular control sizes, rows ~24–32pt. Pointer hover states on interactive elements.
- Settings in a dedicated Settings window organized by category.
- Use the generated accent as the app tint; respect the user's system accent where the platform applies it.

## iPadOS

- Sidebar that can collapse into a tab bar; split views for list → detail; windows that resize freely — layouts must adapt continuously, not just at two sizes.
- Pointer and keyboard: hover effects, shortcuts (show the shortcut list), drag and drop between apps.
- Larger canvases deserve bigger media and multi-column compositions, not stretched phone layouts.

## watchOS

- Glanceable: one key piece of information per screen, readable in a second. Big type, bold numbers, short labels.
- Full-color backgrounds or black depending on content; category and brand colors carry meaning. Digital Crown for scrolling and value changes.
- Vertical tab-style pages, toolbar buttons in corners, Smart Stack widgets and complications for the most important info.

## tvOS

- Focus-driven: every interactive element has a clear focused state (scale, lift, highlight); parallax on focused artwork.
- 10-foot typography and generous spacing; avoid dense text. Large artwork shelves.

## visionOS (spatial)

- Windows on glass material, ornaments for toolbars, tab bars as vertical ornaments, volumes for 3D content.
- Interactive elements need ~60pt of space; hover effects show what eyes are targeting. Keep important content in the field of view, comfortable distance, and avoid large bright white areas.
- Depth and motion should be subtle and comfortable; never move the user's world without intent.

## Widgets and Live Activities

- One glanceable job per widget family size; real data, no app-like controls beyond simple interactive buttons/toggles.
- Support the system rendering modes (full color, accented/tinted, and clear appearances on current OS versions): design the layout so it still reads when colors are removed or tinted.
- Live Activities show the one changing value (time, score, progress) with the brand color as an accent.

## Sources

Checked 2026-11-26: [HIG: Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [iPadOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ipados), [watchOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-watchos), [tvOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-tvos), [visionOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-visionos), [Widgets](https://developer.apple.com/design/human-interface-guidelines/widgets).
