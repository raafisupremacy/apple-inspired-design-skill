# Web apps, SaaS, PaaS, dashboards, and developer tools

For working software, Apple's best reference is the Mac: a calm sidebar, a clear toolbar, focused content, an optional inspector, keyboard-first operation, and density that respects repeated work.

## App shell

```text
┌────────────┬──────────────────────────────────────┬─────────────┐
│ ● Acme     │ Title                 [Filter] [+ New]│ Inspector   │
│            ├──────────────────────────────────────┤ (optional)  │
│ ⌂ Home     │                                      │ selected    │
│ ▤ Projects │  primary content: table, board,      │ item detail │
│ ◷ Activity │  editor, canvas, dashboard           │             │
│            │                                      │             │
│ TEAMS      │                                      │             │
│ ● Design   │                                      │             │
│ ⚙ Settings │                                      │             │
└────────────┴──────────────────────────────────────┴─────────────┘
```

- **Sidebar:** grouped destinations with small headers, icon + label, current item on an `accentSoft` or neutral selected fill, collapsible; a subtle tinted or translucent background distinguishes it from content.
- **Toolbar:** page title, view switcher (segmented control), search, and one primary action. Secondary actions in a menu.
- **Inspector:** properties of the selected object; hide it on narrow widths.
- **Command palette (⌘K / Ctrl K)** for navigation and actions; show shortcuts in menus and tooltips.
- Preserve context: filters, selection, scroll position, and deep links survive navigation.

## Density and type

- Dense desktop apps work at 13–15px body (macOS uses 13pt) with 28–36px rows; touch layouts need 44px targets. Pick per surface, not globally.
- Titles still get contrast: a 22–28px bold page title over 13–15px content. Numbers are tabular.
- Group with spacing and alignment before borders. One unified panel with separators beats a wall of cards.

## Tables and lists

Sticky header, left-aligned text, right-aligned numbers, no heavy zebra or grid lines, hover and selected states, inline row actions on hover plus a visible overflow menu for touch/keyboard, bulk actions bar on selection, empty/loading/error rows. On compact widths turn rows into prioritized stacked items or a list → detail flow.

## Dashboards

- Answer one primary question first: the current state, the exception that needs attention, and the next action.
- Then a small group of related metrics: label (13 semibold secondary), value (28–40 bold tabular) with unit, trend with semantic color + arrow + text.
- Avoid a wall of equal stat cards; give one region dominance.
- Include stale data, partial failure, no data, permissions, and export states. Move from summary to source records without losing filters.

### Charts (Swift Charts-like character)

Few or no gridlines, rounded bar ends, direct labels instead of legends where possible, category colors from the palette (5–8 hues of similar lightness), a big summary number above the chart ("Average 7h 12m"), and an interactive scrubber with a vertical rule and a value callout. Pair color with labels; provide a data table alternative.

## Settings, account, billing

macOS System Settings style: sidebar of categories, grouped form rows with labels left and controls right, explanatory footers, clear current values, explicit destructive zones with confirmation and recovery. Separate local preferences, account, privacy, security, billing, and help.

## Developer tools and PaaS

- **Docs:** three columns — navigation tree, content (max ~720px), on-this-page outline. Declarations and code blocks in a mono font with copy buttons and language tabs; callouts for notes/warnings; versioned and searchable. Apple's developer documentation is a good reference for calm hierarchy.
- **Console and resources:** resource lists with status (text + icon + color), environment badges (Production stands out), primary action per resource, activity timeline.
- **Logs and terminals:** mono, tabular timestamps, level colors that pass contrast in dark themes, filters, follow-tail toggle, copy/share.
- **Deploys:** step timeline with live progress, durations, failure with the failing step expanded and a next action.
- **CLI snippets:** one-line install with copy, OS tabs.
- Developers often prefer dark: offer both themes; the `neutral` or `immersive` strategy with the brand accent works well.

## Onboarding and empty states

First-run should reach a useful result fast: a short checklist, sample data clearly labeled as sample, empty states with one clear action and a link to docs.

## Pricing pages

3–4 plans maximum in aligned columns with identical row order, one recommended plan highlighted with the accent, annual/monthly toggle that updates every price, footnotes for limits, and a comparison table below.

## Sources

Checked 2026-11-26: [HIG: Designing for macOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-macos), [HIG: Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars), [HIG: Charts](https://developer.apple.com/design/human-interface-guidelines/charts), [Apple Developer Documentation](https://developer.apple.com/documentation/). Web recipes are this skill's adaptation.
