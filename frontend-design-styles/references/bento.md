# Bento grid

Structure is the signature: near-white page, white modular tiles in a deliberately unequal grid, one cobalt accent, hierarchy bought with tile size.

## Signature

- A 12-column tile grid whose panels are deliberately unequal: one 6-column × 2-row hero, one 6-column band tile, three satellites at 3–5 columns. Never a uniform card grid.
- Tile size encodes priority. The headline metric gets the biggest tile; low-detail items get 1×1 space. A tile with no metric, list or status is deleted, not styled.
- Every tile repeats one rhythm: tiny uppercase label, headline value or visual, one line of context. One shared padding token on all four sides of all tiles.
- Surfaces are quiet: near-white page, white tiles, 1px hairline border, 16–20px radius, a single soft shadow. The grid line defines the structure; nothing glows.
- Exactly one accent (cobalt) for the primary action, the highlighted tile and data emphasis. Green/amber/red appear only inside status chips and deltas.
- Functional neutral type: system sans, tabular numerals on every figure, tight negative tracking on large numbers.

## Typography

- Base stack: `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`. No webfonts, no CDN, no icon font.
- Set `font-variant-numeric: tabular-nums;` on every metric, delta, timestamp, fraction and version string so figure columns align when values change.
- Tile label: 11px / 600 / uppercase / `letter-spacing: .08em` / `line-height: 1.2`, colour `#667085`.
- Hero metric: 52px / 700 / `letter-spacing: -.025em` / `line-height: 1.02`. Standard tile metric: 34px / 700 / `letter-spacing: -.02em`.
- Context line and list body: 13px / 400 / `line-height: 1.45`, `#475467`. Captions and footnotes: 12px / 400, `#667085`.
- Page heading: 22px / 650 / `letter-spacing: -.015em`. Controls and buttons: 13.5px / 600. Chips: 11.5px / 600.

## Spacing & layout

- Scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 px. Nothing outside the scale.
- One tile padding token on all four sides: 24px ≥ 1024px, 20px ≤ 1024px, 16px ≤ 460px. Grid gap: 16px desktop, 12px ≤ 1024px — gaps never exceed padding.
- Grid: `grid-template-columns: repeat(12, minmax(0, 1fr))` with spans hero 6 × 2 rows, band tile 6 × 1, satellites 3 / 5 / 4. The lower band stays unequal; never three equal thirds.
- Rows are content-sized (`grid-auto-rows: auto`). Tile height comes from content, so metric text and lists never clip.
- Max width 1200px, centred, page gutter 24px (16px ≤ 460px).
- Give every grid/flex child `min-width: 0` and long strings `overflow-wrap: anywhere`; tile 1×1 is the smallest allowed unit.

## Color tokens

| Token | Value | Role and contrast |
| --- | --- | --- |
| `--page` | `#F6F7F9` | Page background. `#0F1728` on it is 16.6:1, so headings can sit on the page without a tile. |
| `--tile` | `#FFFFFF` | Tile surface. Body `#475467` on white is 7.7:1 — the default body-text pair, AA at 13px. |
| `--line` | `#E4E7EC` | Tile borders and row dividers, decorative only; never the sole boundary of a control. |
| `--field-line` | `#8492A6` | Inputs, selects, secondary buttons and the focus ring fallback; 3.2:1 on white, satisfying the 3:1 UI-boundary rule. |
| `--ink` | `#0F1728` | Headline values and row titles; 17.4:1 on white, 15.3:1 on the accent tint. |
| `--ink-2` | `#475467` | Context lines, metadata, list body; 7.7:1 on white, 7.2:1 on the page. |
| `--ink-3` | `#667085` | Uppercase tile labels and captions; 4.9:1 on white, 4.6:1 on the page — the lightest text allowed anywhere. |
| `--accent` | `#2B59FF` | Primary button fill, peak data bar, focus ring. White on it is 5.3:1; accent text on white is 5.3:1. |
| `--accent-tint` | `#F2F5FF` | The one highlighted tile; `#0F1728` on it is 15.3:1 and `#2B59FF` on it is 4.9:1. |
| `--accent-soft` | `#E3EAFF` | Selected/pressed chips; `#1B3FD8` text on it is 6.4:1. Never `#2B59FF` on this — it drops to 4.4:1. |
| `--good` / `--good-bg` | `#067647` / `#ECFDF3` | Passed chips and positive deltas; 5.4:1. |
| `--warn` / `--warn-bg` | `#B54708` / `#FFFAEB` | Running and degraded chips; 5.2:1. |
| `--bad` / `--bad-bg` | `#B42318` / `#FEF3F2` | Failed chips and negative deltas; 6.1:1. |

## Surfaces & elevation

- Tile: `background: #FFFFFF; border: 1px solid #E4E7EC; border-radius: 18px; box-shadow: 0 1px 2px rgba(16,24,40,.04), 0 1px 3px rgba(16,24,40,.06);`
- Highlighted tile: `background: #F2F5FF; border-color: #C7D2FE;` with the same radius and shadow. Highlight comes from tint, never from elevation.
- Hover/selection lift (tile or button): `box-shadow: 0 2px 4px rgba(16,24,40,.05), 0 8px 20px -8px rgba(16,24,40,.12);` — one step, 160ms.
- Row hover/selection band: `background: #F9FAFB`, or `#E3EAFF` when the row is the pinned/selected one; apply `margin: 0 -8px; padding: 0 8px; border-radius: 10px` so the band bleeds into the tile padding.
- Inner rhythm: label → 12px → metric → 6px → context → 12px → list/visual. The data visual sits at the bottom via `margin-top: auto` so short tiles stay top-aligned.
- No backdrop blur, no gradients, no nested shadows, no glass edges. Depth is exactly one ambient shadow.

## Components & states

- Primary button: `#2B59FF` fill, white 13.5px/600 label, radius 10px, padding 9px 14px. Hover `#1F4AE6`; active `#1B3FD8` + `translateY(1px)`; focus-visible 2px `#2B59FF` outline, 2px offset.
- Secondary button: white fill, `1px solid #8492A6`, ink label. Hover `#F9FAFB` + `#667085` border; active `#F2F4F7`. Disabled: `#F9FAFB` fill, `#667085` label (4.7:1), `cursor: not-allowed`, no hover, no shadow.
- Selected button (`aria-pressed="true"`): `#E3EAFF` fill, `#C7D2FE` border, `#1B3FD8` label.
- Inputs and selects: white fill, `1px solid #8492A6`, radius 10px, padding 9px 12px, 13.5px, `min-height: 38px`. Hover = border `#667085`; focus-visible = accent border plus 2px accent outline at 2px offset. Placeholder `#667085`. Custom select chevron is an inline SVG, `pointer-events: none`.
- Chips: 11.5px/600, radius 999px, padding 3px 9px, soft status background with matching dark text; never a saturated fill with white text.
- Checkbox: 20px, radius 6px, `1.5px solid #8492A6`; checked = accent fill with a white check; disabled = `#F2F4F7` fill and `#CBD2DC` border with no hover.
- Toggle: 38×22px track, 18px thumb, `#CBD2DC` off / accent on, 140ms thumb transform. The label wraps the input so the visible text is the accessible name.
- Rows: 44px minimum height, hairline divider after the first row, hover band on interactive rows only; a right-aligned tabular figure or status chip closes each row.
- Progress: 8px radius-999 track `#EEF2F6` filled by segments; `role="progressbar"` with `aria-valuenow` and an `aria-valuetext` that names each segment share.

## Motion

- Durations 120–320ms only. Easing `cubic-bezier(.2, .7, .3, 1)` for size and position, `ease` for colour.
- Animates: bar `transform: scaleY()` when the headline metric changes (320ms, with `transform-box: fill-box; transform-origin: bottom`), button hover/active 140ms, toggle thumb 140ms, checkbox 120ms, row hover band 120ms, tile hover shadow 160ms.
- Nothing animates on load, nothing loops, no shimmer skeletons, no parallax, no number counters.
- `@media (prefers-reduced-motion: reduce) { *, *::before, *::after { transition-duration: .01ms !important; transition-delay: 0ms !important; animation-duration: .01ms !important; animation-iteration-count: 1 !important; } }` — the metric swap lands instantly while `aria-live` still announces the new state.

## Responsive rules

- ≥ 1024px: 12 columns, spans 6 / 6 / 6 (hero row-span 2) then 3 / 5 / 4.
- ≤ 1024px: 6 columns, padding 20px, gap 12px. Hero and both band tiles span 6 with the hero row-span reset to `auto`; satellites become 3 / 3 / 6.
- ≤ 760px: single column — `grid-template-columns: minmax(0, 1fr)`, every tile `grid-column: 1 / -1`, `grid-row: auto`. Header controls wrap to full-width rows.
- ≤ 460px: tile padding 16px, hero metric 42px, page gutter 16px, gap 12px.
- At exactly 375px: no element is wider than 340px; select, search input and buttons are `width: 100%` inside a wrapping flex column; the bar chart is `width: 100%; height: 72px` with `preserveAspectRatio="none"`; the 30-day availability strip uses `flex: 1 1 0; min-width: 0` so it compresses instead of overflowing; tile text wraps with `overflow-wrap: anywhere`; no fixed tile heights. Check `document.documentElement.scrollWidth === 375`.

## Pitfalls

- Uniform cards. If every tile is one column wide the page reads as a generic dashboard. Keep one 2×2 hero and one band tile with visibly different spans, and let the satellites differ from each other.
- Filler tiles. A tile holding an icon and a label but no metric, list or status is decoration; delete it or fold it into a neighbour.
- Accent creep. Cobalt on icons, borders, headings and links at once destroys the one-accent discipline. Reserve it for the primary action, the selected/pinned state and the peak data mark.
- Hairline-only boundaries. `#E4E7EC` is 1.2:1 and disappears for low-vision users; every control boundary and focus ring must be `#8492A6` or the accent.
- Fixed tile heights. Any `height` on a tile clips long lists and 52px metrics at 375px; size tiles from content and let the grid stretch the hero.
- Missing tabular numerals. Proportional digits make metrics and deltas jitter when the demo cycles periods; set `tabular-nums` on every figure, including chips and fractions.

## Adaptation recipe

1. Inventory the content and label each item's priority: headline metric, working list, status feed, people, progress.
2. Draw the 12-column grid and assign spans by priority — one hero 6 × 2, one 6-wide band, satellites at 3–5. Write the spans as one CSS class per tile.
3. Set the three look-defining tokens (`--page`, `--tile`, `--accent`) and keep the neutral text ramp `#0F1728` / `#475467` / `#667085`.
4. Build the tile shell first — shared padding token, hairline border, 18px radius, one shadow — and reuse the same class for every tile.
5. Apply the recurring tile rhythm (uppercase label, headline value, one context line) in each tile, swapping only the inner visual.
6. Implement the components from `Components & states` before page polish, wiring real hover, active, focus-visible, disabled and selected states.
7. Add the single accent action and confirm it is the only saturated element on the page; verify peak bars and status chips are the only other colour.
8. Add motion last: 120–320ms interaction transitions, `scaleY` on the bars, then the reduced-motion override.
9. Check 1024px, 760px and 375px for span collapse and overflow, long strings, tabular numerals and AA contrast before shipping.

Companion preview: `previews/bento.html` shows the tile shell, the unequal spans, the components and the demo control in place.
