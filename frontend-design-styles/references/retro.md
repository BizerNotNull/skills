# Retro 1970s

A flat screen-printed system: ochre bands, chunky slab-serif display type, hard offset edges and one concentric record motif, as if a record-shop poster were pulled in three inks.

## Signature

- Horizontal bands: 12–16px stripe strips in ochre/rust/avocado split the page into zones; nothing floats free, every section sits on a band.
- Chunky heavy serif display type at 28–56px carrying a static 2-layer offset shadow that fakes cheap ink misregistration.
- One concentric-circle record motif (grooves + centre label) drawn as inline SVG, repeated small as a marker on cards and rows.
- Hard-edged surfaces only: 3px solid rules, hard offset shadows, no blur, no gloss, corner radius 2px on panels.
- Rounded oval price tags and pill labels (genre, condition, shelf) as the only curved shapes on the page.
- Generous whitespace between bands (48–64px); density lives inside a band, never between bands.

## Typography

- Display stack: `"Rockwell", "Bookman Old Style", Georgia, "Times New Roman", serif`.
- Body stack: `"Bookman Old Style", Georgia, "Palatino Linotype", "Times New Roman", serif`.
- Numeric stack for prices, catalog numbers, years: `"Courier New", "Lucida Console", monospace`.
- Display scale: 56 / 40 / 28 / 21px, weight 700, `letter-spacing: -0.01em`, `line-height: 0.98`.
- Body 17px / 1.6 weight 400; secondary copy 15px / 1.55; captions and labels 12px uppercase, weight 700, `letter-spacing: 0.14em`.
- Misregistration: `text-shadow: 2px 2px 0 var(--ochre), 4px 4px 0 var(--rust)` on display headings only, never on body copy.
- Never below 12px, never letterspaced body copy, never italic for emphasis — use weight and the rust accent instead.

## Spacing & layout

- Scale: 4 / 8 / 12 / 16 / 24 / 32 / 48 / 64 (px). Every gap is a member; no 18px or 30px inventions.
- Container: `max-width: 1120px`, `padding-inline: clamp(16px, 4vw, 32px)`, centred; band fills stay full-bleed behind it.
- 12-column grid, `gap: 24px`; record card grids use `repeat(auto-fill, minmax(230px, 1fr))`.
- Band anatomy: 3px top rule, a small uppercase tag at the left, then content 24px below; 64px between bands on desktop, 40px on mobile.
- Text measure capped at `68ch`; hero split is `minmax(0, 1.05fr) minmax(0, 1fr)` so neither column can be pushed wider by its content.
- `min-width: 0` on every flex/grid child; long titles wrap, they never widen the track.

## Color tokens

| Token | Value | Role and contrast |
| --- | --- | --- |
| `--paper` | `#F7EBD3` | Primary surface, all body text. Ink on paper is 11.6:1 — passes AA at every size. |
| `--paper-deep` | `#EFDFC0` | Recessed bands, price tags, chip rests. Ink on it is 10.4:1, AA. |
| `--ink` | `#3B2A1E` | Body and display text, borders, offset shadows. 11.6:1 on paper, far above the 3:1 UI-boundary floor. |
| `--ink-muted` | `#6B5340` | Secondary copy, meta lines, artist names. 6.1:1 on paper — AA body text. |
| `--ochre` | `#D9971F` | Primary band fill, chip selected state. Always carries `--ink` text (5.5:1); cream on ochre is 2.1:1 and is forbidden. |
| `--rust` | `#B4461F` | Primary buttons, rules, first misregistration layer. Cream text on it is 4.6:1 — AA body text, and it never sits under muted copy. |
| `--avocado` | `#55622C` | Genre pills, stock tags. Cream text on it is 5.6:1 — AA body text. |
| `--line` | `#3B2A1E` | Border and shadow colour; identical to ink so edges and type read as one printed layer. |

Baseline pair: `--ink` on `--paper` at 11.6:1 for all reading text. On ochre bands switch the text to `--ink` (5.5:1) and never cream. Cream is reserved for rust and avocado fills, where it measures 4.6:1 and 5.6:1.

## Surfaces & elevation

- Zero blur anywhere. Depth is a hard offset: `box-shadow: 6px 6px 0 var(--rust)` on panels, `5px 5px 0 var(--ink)` on buttons.
- Stripe strips: `repeating-linear-gradient(90deg, var(--ochre) 0 14px, var(--rust) 14px 28px, var(--paper-deep) 28px 42px, var(--avocado) 42px 56px)` at 14px tall with 3px ink rules top and bottom — separators, never fills behind text.
- Card interiors: `--paper` fill, `border: 3px solid var(--ink)`, `border-radius: 2px`, `padding: 20px`, sleeve art as stacked hard-stop `linear-gradient`/`radial-gradient` planes in ochre, rust and avocado.
- Hover lifts the shadow, never blurs it: `translate(-2px, -2px)` with `8px 8px 0 var(--ochre)`.
- No translucency, no backdrop-filter, no soft gradient stops, no glossy radial highlights, no drop shadows with blur radii.

## Components & states

- Primary button: rust fill, cream 14px/700 uppercase, `padding: 13px 22px`, `border: 3px solid var(--ink)`, `border-radius: 999px`, `box-shadow: 5px 5px 0 var(--ink)`; hover darkens to `#9E3B18` and lifts 2px; active presses to `translate(3px, 3px)` with `2px 2px 0`.
- Secondary button: paper fill, ink text, same border and pill radius; hover fills ochre keeping ink text.
- Input and select: paper fill, `border: 3px solid var(--ink)`, `border-radius: 2px`, 12px/14px padding, 16px value type to stop mobile zoom; placeholder uses `--ink-muted`.
- Checkbox chips: pill of `--paper-deep` with ink text and a 20px square checkbox; checked = rust box with a paper inner ring plus an ochre pill fill; unchecked → checked is the only state change animated.
- Toggle: pill track filled `--paper-deep`, 24px knob in ink; on = track rust, knob translated 20px.
- Focus-visible everywhere: `outline: 3px solid var(--ink); outline-offset: 3px`, with `border-radius: 2px` so the ring hugs pills and squares alike — never `outline: none` without a replacement.
- Disabled: 45% opacity, no offset shadow, `cursor: not-allowed`; the 3px border stays solid so the control is still legible.

## Motion

- Two moves only: 120ms `ease-out` for colour/background swaps, 160ms `cubic-bezier(.2, .8, .3, 1)` for press/lift translations.
- Nothing rotates, pulses, marquees, or jitters; the misregistration shadow is static so type never flickers.
- No entrance choreography beyond one 180ms fade on first paint; demo state changes swap text without motion.
- `@media (prefers-reduced-motion: reduce)`: set all transition and animation durations to `0.01ms`, cancel hover/active translate and shadow shifts, and let filters and demo cycles switch state instantly.

## Responsive rules

- Breakpoints: 1024px (grid drops to 3 across), 860px (hero and band splits go single column), 620px (cards to one column, buttons full-width, band padding 16px), floor at 375px.
- At 375px nothing exceeds 340px: the hero record is `width: 100%; max-width: 300px; height: auto` on a `viewBox`, never a fixed pixel width.
- Grids collapse to a single column; tag and chip rows `flex-wrap: wrap`; every flex/grid child keeps `min-width: 0` so long record titles wrap instead of pushing the layout.
- `overflow-wrap: anywhere` on titles, prices and address lines; body copy is never truncated with an ellipsis.
- Stripe strips stay full-bleed, horizon-independent of the container so they cannot create a horizontal scrollbar.
- Verified at 375px: no horizontal overflow, no `100vw` units, no negative margins wider than the 16px inline padding, no fixed heights.

## Pitfalls

- Glossy retro: bevels, specular highlights and blurred drop shadows destroy the screen-printed flatness. Flat fills plus hard offset shadows only.
- Animating the misregistration: a jittering offset shadow reads as a rendering bug and is a vestibular hazard. Keep it static and 2–4px at most.
- Cream text on ochre: ochre is mid-lightness, so cream lands at 2.1:1. Ochre surfaces always take ink text.
- Stripe flooding: using the stripe gradient as a large background behind copy makes bands unreadable. Stripes are 14px separators and small accents.
- Uppercase micro-type: letterspaced uppercase below 12px collapses on system fonts; restrict it to tags, prices and button labels.
- Pill overuse: when every label, heading and price is an oval, hierarchy disappears. Reserve pills for tags, prices and buttons.

## Adaptation recipe

1. Set `--paper` and `--paper-deep` first; every other token is chosen and contrast-checked against them.
2. Pick one warm primary and one support accent plus a dark neutral; verify each text/fill pair at 4.5:1 before styling anything.
3. Load the display and body stacks, set the 56/40/28/21 scale, and add the 2-layer offset shadow only to the leading heading of each band.
4. Cut the page into bands: one band per job (hero, feature, filters, grid, footer), each opened by a stripe strip and a 3px rule.
5. Draw one inline SVG record with real geometry (outer disc, 8–12 groove rings, accent rings, ochre label, centre hole) and reuse a small CSS variant as a card marker.
6. Build components in order — primary button, secondary button, input, select, chip, toggle, card, list row — checking hover, active, focus-visible and disabled for each before moving on.
7. Add the two transition timings and the reduced-motion override before any other motion exists.
8. Collapse to one column at 860px, then test at 375px for overflow, wrapping and the 12px type floor with real long titles.

Companion preview: `previews/retro.html`
