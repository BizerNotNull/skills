# Aurora Glass

Deep violet→indigo→teal aurora light diffuses behind stacked translucent glass panels, while every readable word sits on one near-opaque foreground sheet so contrast never depends on `backdrop-filter`.

Companion preview: `previews/glass.html`

## Signature

- **Aurora field, not shapes.** Three oversized soft-edged radial gradients (violet `#7C5CFF`, indigo `#3B2E8F`, teal `#3FD8C8`) drift over a `#0B0920` base on 22–30s loops; nothing else on the page is that soft or that large.
- **Exactly three glass depths.** Page chrome (`--glass-1`) contains cards (`--glass-2`) which contain the floating player (`--glass-3`). Each pane = translucent white fill + 1px hairline + inset white top-edge highlight + wide violet shadow.
- **One opaque text sheet per region.** All copy, labels and controls live on `rgba(18,16,42,0.96)` stacked above the glass, so AA contrast survives a missing or blocked `backdrop-filter`.
- **Low-mass luminous type.** 300-weight display sizes, teal for live state and numerals, muted lavender for secondary copy.
- **Slow sky, fast controls.** Atmosphere breathes over tens of seconds; buttons, toggles and rows answer in 120–200ms.

## Typography

System stacks only — no webfonts, no CDN, no `@import`.

- UI / display: `"Segoe UI Variable Display", "Segoe UI", -apple-system, BlinkMacSystemFont, "SF Pro Display", Roboto, "Helvetica Neue", Arial, sans-serif`
- Numerals / time: `ui-monospace, "SF Mono", "Cascadia Mono", "Segoe UI Mono", Consolas, Menlo, monospace` with `font-variant-numeric: tabular-nums`.

| Role | Size | Weight | Tracking | Line-height |
|---|---|---|---|---|
| Display (h1) | `clamp(30px, 6vw, 46px)` | 300 | `-0.02em` | 1.08 |
| Section (h2) | `clamp(18px, 3vw, 23px)` | 450 | `-0.01em` | 1.2 |
| Card title (h3) | `15px` | 600 | `0.005em` | 1.3 |
| Body | `15px` | 400 | `0.005em` | 1.6 |
| Timer readout | `clamp(38px, 10vw, 64px)` | 300 | `-0.03em` | 1 |
| Label / eyebrow | `12.5px` (uppercase variant `11px`/600/`0.16em`) | 500 | `0.02em` | 1.4 |

Body copy is capped at `max-width: 62ch`, never rendered below 13px, and never placed on a glass-only surface.

## Spacing & layout

- Scale: `4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 / 96` px. Every margin, padding and gap draws from it; no arbitrary values.
- Container: `max-width: 1120px; margin-inline: auto; padding-inline: clamp(16px, 4vw, 32px)`.
- App shell: 12-column grid, `gap: 24px`; above 900px the split is `minmax(0, 1.5fr) minmax(0, 1fr)` (player + sidebar), collapsing to one column below. Panels sit in a 24–32px gutter with 24px sheet padding; card stacks use 12px gaps; sections are 48px apart desktop / 32px mobile.
- Depth budget: three glass layers maximum — a fourth stacking level reads as mush. Every grid/flex child gets `min-width: 0`; long track names use `overflow-wrap: anywhere`.

## Color tokens

| Token | Value | Role | Contrast |
|---|---|---|---|
| `--aurora-violet` | `#7C5CFF` | Aurora light, focus-ring base, icon accents | `#FFFFFF` on it = 4.35:1 → large text/icons only |
| `--aurora-violet-deep` | `#5B3FE0` | Primary button fill | `#FFFFFF` on it = 6.5:1 → passes AA for body text |
| `--aurora-indigo` | `#3B2E8F` | Aurora mid-light, primary pressed | Decorative only |
| `--aurora-teal` | `#3FD8C8` | Accent, active waveform, links, switch-on | `#3FD8C8` on `#12102A` = 10.5:1 → AAA |
| `--fg` | `#F4F3FF` | All body/heading text on opaque sheets | `#F4F3FF` on `#12102A` = 17:1 → AAA |
| `--fg-muted` | `#B9B4E6` | Secondary text, metadata, helper copy | `#B9B4E6` on `#12102A` = 9.5:1 → AAA |
| `--panel-a` / `--panel-b` | `#181536` / `#12102A` | Opaque text-sheet gradient (0.97→0.96 alpha) | +4% aurora bleed still ≈16:1 |
| `--surface-glass` / `--hairline` | `rgba(255,255,255,0.07)` / `rgba(255,255,255,0.16)` | Glass pane fill, 1px glass border and dividers | Decorative — never carries text |
| `--page` | `#0B0920` | Base canvas under the aurora | `#F4F3FF` on it = 17.8:1 |
| `--danger` | `#FF9B9B` | Stop / destructive labels on opaque sheets | `#FF9B9B` on `#12102A` = 9.2:1 → AA+ |

Body copy pair is always `--fg` on `--panel-b`; the only exception is the primary button (`#FFFFFF` on `--aurora-violet-deep`), which still passes AA. Teal is never used for body copy on glass, only on the opaque sheet.

## Surfaces & elevation

Tokens: `--glass-1: rgba(255,255,255,0.045)` (chrome), `--glass-2: rgba(255,255,255,0.070)` (cards), `--glass-3: rgba(255,255,255,0.095)` (floating player), `--blur: blur(22px) saturate(140%)`, `--shadow-3: 0 24px 60px -22px rgba(8,4,36,0.8)`.

Glass pane: translucent fill + `backdrop-filter`/`-webkit-backdrop-filter: var(--blur)` + `border: 1px solid var(--hairline)` + `box-shadow: inset 0 1px 0 rgba(255,255,255,0.22), var(--shadow-3)` + `border-radius: 24px`.
Opaque sheet: `linear-gradient(180deg, rgba(24,21,54,0.97), rgba(18,16,42,0.96))`, `border: 1px solid rgba(255,255,255,0.10)`, `border-radius: 20px`.
Aurora field: `position: fixed; inset: 0; overflow: hidden`, base `#0B0920` plus three blob layers (`filter: blur(70px)`, 22–30s `ease-in-out alternate` drift).

**Required blur fallback** — glass degrades to a solid gradient, never to transparent:

```css
@supports not ((backdrop-filter: blur(1px)) or (-webkit-backdrop-filter: blur(1px))) { .glass { background: linear-gradient(160deg, #241C56, #16113A); backdrop-filter: none; -webkit-backdrop-filter: none; } }
```

## Components & states

- **Primary button:** `#5B3FE0` fill, `#FFFFFF` 15px/600 text, 999px radius, 12/22px padding. Hover `#6B50EE`; active `#4B31C4` + `translateY(1px)`; disabled `rgba(255,255,255,0.10)` fill with `--fg-muted` text and `cursor: not-allowed`.
- **Secondary + ghost / row button:** secondary = transparent fill + `1px solid rgba(255,255,255,0.28)`; hover `rgba(255,255,255,0.10)`, active `rgba(255,255,255,0.16)`. Picker rows are full-width, left-aligned, 14px radius: hover adds `rgba(255,255,255,0.06)` + hairline; selected (`aria-pressed="true"`) gets `rgba(63,216,200,0.12)` fill, `rgba(63,216,200,0.5)` border and a teal "Playing" pill.
- **Inputs / select:** `rgba(255,255,255,0.05)` fill on the opaque sheet, `1px solid rgba(255,255,255,0.18)`, `--fg` text, 12px radius, 12/14px padding. Hover border `rgba(255,255,255,0.30)`; focus adds a `rgba(63,216,200,0.25)` glow; disabled drops to 55% opacity.
- **Range slider + switch:** 6px track, filled portion teal `#3FD8C8`, remainder `rgba(255,255,255,0.16)`, 18px `#F4F3FF` thumb with a 2px teal ring. Switch is a 46×26px pill, off `rgba(255,255,255,0.18)`, on `#3FD8C8` with a `#0B0920` knob translated 20px over 180ms.
- **Focus-visible (every interactive element):** `outline: 2px solid #9FE9DF; outline-offset: 2px;` — never `outline: none` without an equivalent replacement.
- **Cards:** glass pane wrapping an opaque sheet; hover lifts the border to `rgba(255,255,255,0.22)` and deepens the shadow to `0 30px 70px -24px rgba(8,4,36,0.9)` over 240ms.

## Motion

- Aurora drift: 22s / 26s / 30s, `ease-in-out`, `alternate`, opacity 0.45–0.75.
- Waveform bars: `scaleY(0.35 → 1.15)` over `1.6s ease-in-out infinite alternate`, staggered by `--i * 90ms`; idle state uses `animation-play-state: paused`.
- UI feedback: 120ms color/background, 180ms transform (switch knob), 240ms card shadow, all on `cubic-bezier(0.2, 0.8, 0.25, 1)`; nothing larger and nothing animated on scroll.
- `@media (prefers-reduced-motion: reduce)`: `animation: none` on the aurora and the bars (bars pinned to static heights), and transitions collapsed to `0.001ms` so hover/active states still apply instantly.

## Responsive rules

- ≥1200px: full 1.5fr/1fr shell, 96px section rhythm, sticky sidebar; 900–1199px keeps the split with a 32px gutter.
- ≤900px: single column — player, then soundscape picker, then stats; section rhythm 32px.
- ≤560px: button rows wrap to full-width blocks, the stats grid goes 2-up, and the timer readout clamps toward 38px; ≤420px sheet padding drops to 16px and picker rows stack name above metadata.
- **375px:** `padding-inline: 16px`, no fixed width above ~340px, the waveform SVG uses `preserveAspectRatio="none"` at `width: 100%`, `overflow-wrap: anywhere` guards long track names — the page scrolls vertically only, with zero horizontal overflow.

## Pitfalls

1. **Text on glass.** The most common failure: pretty translucent cards make 4.5:1 impossible over a bright aurora. Fix: glass is chrome only, every string goes on a 0.96-alpha sheet, and you verify the worst-case composite rather than the average one.
2. **Blur as a load-bearing effect.** Without `backdrop-filter` (flags, forced-colors, older Safari) translucent panes turn into washed-out noise. Fix: ship the `@supports not (...)` solid-gradient swap in the same stylesheet as the glass rules.
3. **Depth inflation.** Every new panel gets its own blur stack until the page is grey soup and scrolling stutters. Fix: exactly three glass tokens and nest sheets instead of adding layers.
4. **Blurring large areas.** Full-viewport blur and 70px blurs over scrolling content drop frames on mid-range hardware. Fix: keep pane blur ≤24px, keep the huge blurs on a `position: fixed` aurora that never repaints with scroll, and never animate `backdrop-filter`.
5. **Aurora swallowing the foreground.** Saturated violet gradients steal attention from the product. Fix: cap aurora opacity and let the deepest element on screen be the opaque sheet holding the primary action.

## Adaptation recipe

1. Set the canvas: `--page: #0B0920` on `body`, then add a fixed, `overflow: hidden` aurora layer with three blurred radial-gradient blobs in violet, teal and indigo.
2. Define the three glass tokens, the blur value, the hairline and the violet shadow; write the `@supports not (backdrop-filter)` fallback immediately after them.
3. Define `--panel-a`/`--panel-b` and build a `.sheet` primitive; route every piece of copy and every control through one.
4. Apply typography: 300-weight clamped display, 15px/1.6 body, monospace tabular numerals for any number that changes.
5. Build the shell (`max-width: 1120px`, 24px gutter, 1.5fr/1fr grid, `min-width: 0` everywhere) and place one `--glass-2` card with a `--glass-3` floating element to establish the depth story.
6. Implement components — primary, secondary and ghost/row buttons, labeled input/select, teal switch, selectable rows with a selected state — then add the motion layer and the full `prefers-reduced-motion: reduce` override in the same edit.
7. Test at 1200 / 900 / 560 / 375px, then re-test with blur disabled to confirm the opaque-sheet contrast holds.
