# Cyber Mission Control

A near-black orbital operations console: hairline grids, monospace telemetry, cyan and lime readouts, and slow non-flickering scan accents.

Companion preview: `previews/cyber.html`

## Signature

- Near-black void base (`#04070C`) with lifted panels (`#0B1220`) separated by 1px hairlines (`#16283A`) — structure comes from rules, not shadows.
- Every number, id, timestamp, and unit is monospace at small size with wide tracking; prose is rare and set in a plain sans.
- Uppercase metadata labels (`11px`, `0.14em` tracking) sit above their values, forming a label/value pair everywhere.
- One cyan accent (`#39E1FF`) drives focus, primary actions, and the live trace; lime (`#B6F36B`) means nominal, amber (`#FFB86B`) is rationed to a single warning.
- Accents are static or slow: a fixed low-opacity scanline overlay, corner brackets, and one 18s sweep — never blinking, never strobing.
- Visualizations are dual-encoded: an SVG trace plus the same numbers as text or a table.

## Typography

Metadata/UI stack: `ui-monospace, "SF Mono", "Cascadia Mono", "Cascadia Code", Consolas, "Liberation Mono", Menlo, monospace`. Prose stack: `system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif`.

| Role | Size | Weight | Tracking | Line-height |
|---|---|---|---|---|
| Console title (h1) | 24px (clamp 20–28px) | 600 | 0.06em | 1.2 |
| Panel heading (h2) | 13px uppercase | 600 | 0.16em | 1.3 |
| Section heading (h3) | 12px uppercase | 600 | 0.14em | 1.3 |
| Metadata label | 11px uppercase | 500 | 0.14em | 1.4 |
| Body / log entry | 13px | 400 | 0.01em | 1.55 |
| Readout value (large) | 30px | 600 | 0.02em | 1.0 |
| Readout value (inline) | 16px | 600 | 0.02em | 1.2 |
| Table cell | 12.5px | 400 | 0.02em | 1.5 |
| Unit suffix | 11px | 400 | 0.08em | 1.0 |

Prose runs at 13.5px/1.6, capped at 68ch; all values use `font-variant-numeric: tabular-nums`.

## Spacing & layout

- Scale `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64`; panel padding 16px, grid gutter 12px, section gap 24px, page block gap 32px.
- Page shell: `max-width: 1240px`, `margin-inline: auto`, padding 16px (24px at ≥768px).
- Desktop grid: `repeat(12, minmax(0, 1fr))` with 12px gutters; chart spans 8 columns, power meter 4; subsystem table 7, event log 5.
- Collapse 12 → 6 columns at 900px → single column at 640px; every grid/flex child gets `min-width: 0`.
- Panels are flush-edged rectangles with 2px radius and gaps no larger than 12px, each with a 40px header bar (label left, mono meta right) and a 1px bottom rule.

## Color tokens

| Token | Value | Role | Contrast |
|---|---|---|---|
| `--void` | `#04070C` | Page base behind everything | Background for all pairs below |
| `--void-2` | `#080D14` | Alternating rows, inset wells | `#D7ECF7` on it = 16.3:1 |
| `--panel` | `#0B1220` | Panel and surface fill | `#D7ECF7` on it = 15.5:1 |
| `--hairline` | `#16283A` | 1px borders, grid rules, dividers | 1.4:1 vs `--void` — decorative only, never an information cue |
| `--cyan` | `#39E1FF` | Focus ring, primary button, live trace | 12.9:1 vs `--void` |
| `--lime` | `#B6F36B` | Nominal/positive status, secondary trace | 15.4:1 vs `--void` |
| `--amber` | `#FFB86B` | Warning only, one at a time | 11.8:1 vs `--void` |
| `--dim` | `#6E8AA6` | Labels, units, secondary metadata | 5.1:1 on `--panel` (AA body) |
| `--text` | `#D7ECF7` | Primary body and readout text | 15.5:1 on `--panel` |
| `--ink` | `#04070C` | Text on cyan/lime fills | 12.9:1 on `--cyan` |

Body text is `--text` on `--panel` (15.5:1, AAA). Metadata is `--dim` on `--panel` (5.1:1, clears AA at 11px). Text on accented fills is always `--ink`. Amber is never body copy — only an 11px bold pill label, where it reaches 11.8:1.

## Surfaces & elevation

- Elevation by border, not blur: every panel gets `border: 1px solid var(--hairline)` over `background: var(--panel)`; raised surfaces add `box-shadow: 0 0 0 1px #16283A, 0 18px 40px -20px #000, inset 0 1px 0 #1E3A54`.
- Inset wells (plot area, log viewport): `background:#080D14; border:1px solid #16283A; box-shadow: inset 0 0 40px -24px #39E1FF`.
- Scanlines (static, `aria-hidden`): `repeating-linear-gradient(180deg, rgba(57,225,255,.05) 0 1px, transparent 1px 4px)` at `opacity:.35`, `pointer-events:none`.
- Sweep: `linear-gradient(90deg, transparent, rgba(57,225,255,.10), transparent)` translating -30% → 130% over 18s linear.
- Corner brackets: 14×14px `::before/::after` showing two borders at `#39E1FF`, `opacity:.5`. No backdrop blur anywhere.

## Components & states

- **Buttons** (32px tall, 2px radius, 11.5px uppercase 0.12em label): primary `background:#39E1FF; color:#04070C`, hover `#63E9FF`, active `translateY(1px)` + `#25CCE8`, disabled `#16283A` fill with `#8AA6C0` text.
- Secondary: transparent fill, `1px solid #16283A`, `color:#D7ECF7`; hover `border-color:#39E1FF; color:#39E1FF; background:rgba(57,225,255,.06)`; active `background:rgba(57,225,255,.12)`. Ghost: no border, `#6E8AA6` → hover `#D7ECF7` on `#0F1A2A`.
- Focus-visible on every control: `outline: 2px solid #39E1FF; outline-offset: 2px` — never `outline: none`.
- Inputs/selects: 32px tall, `background:#080D14`, `border:1px solid #16283A`, `color:#D7ECF7`, 12.5px mono, placeholder `#6E8AA6`; hover `#1E3A54`; focus adds `border-color:#39E1FF`; invalid `#FFB86B` border with an amber 11px helper line.
- Toggle: 34×18px track with a 12px knob; checked track `rgba(57,225,255,.18)`, `border-color:#39E1FF`, knob `#39E1FF` — a real checkbox styled through `:checked + span`.
- Pills: 22px tall, 10.5px uppercase 0.12em label plus a 6px square glyph (never a pulsing dot). Nominal `#B6F36B` on `rgba(182,243,107,.08)` with a `.35` border; warning uses the amber equivalents; selected adds `inset 0 -2px 0 currentColor`.
- Table rows: hairline bottom rule, 8px/12px padding, hover `#0F1A2A`, `[aria-current="true"]` gets a 2px left cyan bar.

## Motion

- Durations 120ms (state changes), 200ms (plot fade when a snapshot loads), 400ms (meter fill width); UI easing `cubic-bezier(.2,.7,.3,1)`, ambient sweeps `linear`.
- Animates: color, border-color, background-color, opacity, `transform: translateY(1px)` on press, meter width; ambient motion is one 18s linear sweep with static status glyphs (no pulsing).
- `prefers-reduced-motion: reduce`: `animation: none !important; transition: none !important`, the sweep is hidden, and values snap instantly.

## Responsive rules

- ≥1100px: full 12-column grid as specified. 900–1099px: chart and meter span 6 columns each, table and log stack full width.
- 640–899px: every panel takes `grid-column: 1 / -1`; header metadata wraps onto a second line.
- ≤639px: single column, 12px panel padding, 22px readouts; the table scrolls inside its panel (`overflow-x:auto` wrapper, 480px min-width table) so the page itself never scrolls sideways.
- At 375px: never rely on `overflow-x:hidden` — keep `min-width:0` on flex/grid children, `overflow-wrap:anywhere` on long ids and log lines, `flex-wrap:wrap` on the filter row, and no fixed width above 340px.

## Pitfalls

- **Neon soup.** Cyan on borders, text, and fills at once destroys hierarchy — keep it for focus, one primary action, and one live trace.
- **Dim text pushed too dark.** Dropping `--dim` to something like `#4E6A86` collapses metadata to 3.5:1 on the `#080D14` wells and fails AA; keep `--dim` at `#6E8AA6` (5.1:1 on `--panel`) or lighter.
- **Blinking everything.** Pulsing dots and blinking cursors read as a toy and cause discomfort — use static glyphs and one slow sweep.
- **Charts with no text alternative.** A bare SVG trace is invisible to screen readers; always pair it with `role="img"` + `aria-label` and a table of the same values.
- **Shadow-based depth.** Drop shadows fight the flat instrument face and go muddy over near-black; express depth with 1px borders and inset glows.

## Adaptation recipe

1. Set `--void:#04070C`, `--panel:#0B1220`, `--hairline:#16283A` as the new product's page background, surface, and border.
2. Apply the mono stack to numeric and identifier UI and the sans stack to prose; establish the 11px uppercase label above a tabular-nums value.
3. Give every container a 1px hairline and remove all drop shadows; use the inset glow only where a well is needed.
4. Pick exactly two accents (cyan + lime, or cyan + amber) and give each one job: focus/primary action, and status.
5. Lay out a 12-column grid with 12px gutters, assign spans, and add `min-width: 0` to every grid/flex child.
6. Add the decorative fixed scanline overlay and corner brackets as `aria-hidden` pseudo-elements or spans.
7. Build the component set — primary/secondary/ghost buttons, hairline inputs, real-checkbox toggle, pills, table rows — each with hover/active/focus-visible/disabled/selected states.
8. Wire motion at 120/200/400ms with linear ambient sweeps only, plus the `prefers-reduced-motion: reduce` kill switch.
9. Give every visualization a text alternative and the same values as a table or readout row.
10. Check 375px: no horizontal scroll, wrapped filter row, readable chart and table.
