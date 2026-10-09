# Swiss — International Typographic Poster

Companion preview: `previews/swiss.html` (resolved from the skill root).

## Signature

Mid-century Swiss exhibition poster, translated to screen: one grotesk face, three colours,
and a twelve-column grid held with near-religious discipline. Display type is flush left, set
tight and uppercase, and the huge numeral is a compositional element rather than a label.
Everything is aligned to the grid; borders are hairlines, and the only filled band is the
red one. Negative space is the main material — resist the urge to fill it.

## Typography

```css
--grotesk:"Helvetica Neue",Helvetica,Inter,Arial,"Segoe UI",Roboto,sans-serif;
```

- Display: `clamp(3.2rem, 13vw, 10.5rem)`, weight 700, `line-height:.82`,
  `letter-spacing:-.045em`, uppercase. Mixed weights inside one word (`Kon**strukt**`) are the
  one permitted flourish.
- Numeral: `clamp(3.6rem, 11vw, 9rem)`, `letter-spacing:-.05em`, red, right-aligned in
  columns 10–12.
- Section head: `clamp(1.6rem, 4vw, 2.6rem)`, uppercase, `letter-spacing:-.03em`.
- Body/labels: 16px base; metadata 0.72–0.86rem with 0.14–0.22em tracking, uppercase.
- No italic, no serif, no third weight. Weight 400 and 700 only.

## Spacing & layout

- Shell `min(1240px, 100% - 2.4rem)`; gutter token `--col-gap:1.25rem`.
- Every block is `grid-template-columns: repeat(12, minmax(0,1fr))` with `gap: 0 var(--col-gap)`.
  Rows are separated by hairlines, never by margin alone.
- Programme rows: `7rem / 1fr / 9rem / 5rem` — time column fixed, description fluid, tag pushed
  to the far right so all four rows share one visual edge.
- Baseline is 22px; the demo grid overlay draws the columns and that baseline literally.

## Color tokens (roles)

| Token | Value | Role | Measured |
|---|---|---|---|
| `--white` | `#ffffff` | page ground | — |
| `--paper` | `#f2f2f2` | demo strip | — |
| `--black` | `#111111` | text, borders, filled buttons | 19:1 on white |
| `--grey` | `#6b6b6b` | secondary metadata only | 5.3:1 on white |
| `--rule` | `#d4d4d4` | row separators | decorative |
| `--red` | `#e30613` | accents, numerals, red band | 4.9:1 on white, 3.9:1 on black (large/decor only) |

Rules: red is never the ground for small text on black; use white text on the red band
(4.9:1). Grey is never used for headings.

## Surfaces

Flat, unshadowed, radius 0. White fills or 2px black outlines. The red band is the single
large colour field on the page; add a second and the poster stops being Swiss.

## Components & states

- Top bar: hairline under a 0.72rem uppercase row; `All styles` is a 2px outlined block that
  fills red on hover.
- Fact list: 2px black rule on top, hairline between rows, `b` in caps flush left and the value
  grey on the right.
- Rows: `<span>` grid children only — no wrappers, so mobile reflow is a pure template change.
- Tags: 1px outline chips; `.tag.full` is inverted (black fill, white text) for the one “live
  today” item. `Ausgebucht` stays outlined and grey-adjacent — full is not a status colour.
- Buttons: 2px outline, uppercase, 0.14em tracking. Primary is black fill → red on hover.
- Specimen controls: ticket/tour/catalogue buttons carry `data-demo="…"` and write an explicit
  “Demo only — no ticket is issued, no tour is booked” line into their group's `role="status"`
  slot. No control is left dead.
- Cards: 1px border, giant red-orange numeral, colourway swatches with `role="img"` labels.
- Focus: `:focus-visible { outline:3px solid var(--red); outline-offset:2px }`.

## Motion

None, by design. State changes are instant swaps — a Swiss poster does not ease. The
`prefers-reduced-motion` block exists only to neutralise inherited transitions.

## Responsive

- ≤900px: all hero/head blocks collapse to `1 / -1`; numerals left-align; programme rows become
  a two-column title/tag template with description and speaker on their own lines; poster cards
  stack; component columns go full width.
- ≤560px: demo strip stacks (full-width toggle button), display clamps hard to
  `clamp(1.9rem, 12.5vw, 3rem)` so the nine-character title still clears 375px, and the row
  template collapses to one column.
- `min-width:0` on all grid children plus `100% - 2.4rem` shell: 375px shows no horizontal scroll.

## Pitfalls

- Do not centre anything. Centre alignment is the fastest way to lose the style.
- Do not use rounded corners, shadows, or gradients — silhouette is drawn with 1–3px rules.
- Tracking on display type must stay **negative**; positive tracking turns the poster into
  a newsletter.
- Uppercase everywhere except prose: apply `text-transform` per component, never to `body`, or
  screen readers get shouted too (transform is visual only, but review prose separately).
- The grid overlay uses `position:fixed` with `pointer-events:none`; leave both, or the toggle
  breaks scrolling.
- Keep the numeral `aria-hidden` — it is decoration, not content.

## Adaptation recipe

1. Set the 12-column shell and gutter first, then place content; never the reverse.
2. Choose the single accent and verify 4.5:1 against white before using it for any text.
3. Keep exactly one filled colour band per page.
4. Rebuild the programme row template to the client's real columns, keeping the far-right tag edge.
5. If motion is demanded, animate only opacity and let the grid stay still.
