# Editorial — Literary Magazine

Companion preview: `previews/editorial.html` (resolved from the skill root).

## Signature

Print-first literary quarterly. Ivory stock, near-black ink, a single vermillion accent used
like a second ink pass. Oversize serif display, tight column rules, and an asymmetric feature
composition: an 8-column headline block, a 4-column plate, then a 7-column two-column body with
the pull quote and issue index pushed into the right margin. The page should read as set type,
not as an app: rules do the work that borders and cards do elsewhere.

## Typography

```css
--serif: "Iowan Old Style","Palatino Linotype",Palatino,"Book Antiqua",Georgia,"Times New Roman",serif;
--sans:  ui-sans-serif,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
```

- Display / masthead: `clamp(2.5rem, 8.4vw, 5.6rem)`, weight 600, `line-height:.92`,
  `letter-spacing:-.015em`, centred, `text-wrap:balance` on article headlines.
- Deck: 1.22rem italic, 1.4 line-height, `max-width:34rem` measure.
- Body: 17px / 1.55, measure 34rem, `break-inside:avoid-column` per paragraph.
- Drop cap: `::first-letter`, `float:left`, `3.9em`, `line-height:.78`, vermillion.
- Sans is reserved for furniture only: kickers, folio lines, labels, buttons, captions.
  Never set running text in the sans stack.

## Spacing & layout

- Shell: `width:min(1180px, 100% - 2.5rem)`; vertical rhythm in 0.4rem steps.
- Feature grid: `repeat(12, minmax(0,1fr))`, `gap: 0 2rem` (gutter only, rules carry separation).
- Column rules: body text uses `columns:2; column-gap:2.1rem; column-rule:1px solid var(--rule)`.
- Hairlines: 1px at `rgba(22,19,15,.22)`; double rules (3px `double`) close the masthead and footer.

## Color tokens (roles)

| Token | Value | Role | Measured on `--ivory` |
|---|---|---|---|
| `--ivory` | `#f6f1e4` | page ground | — |
| `--paper` | `#fbf8f1` | plates, cards, demo strip | — |
| `--ink` | `#16130f` | body, rules, button fill | 15.9:1 |
| `--ink-soft` | `#4a443b` | deks, secondary copy | ~8.2:1 |
| `--ink-faint` | `#8b8375` | labels ≥0.7rem uppercase only | ~3.1:1 (non-text use) |
| `--vermillion-ink` | `#a3361f` | small text, links, kickers | 6.0:1 |
| `--vermillion` | `#c2442c` | display marks, drop cap, rules | 4.4:1 (large/decorative only) |

Rule: `#c2442c` never carries small text; use `#a3361f` whenever the mark is under 1.5em.

## Surfaces

Flat stock only. `--paper` for plates and cards, `--ivory` for the page, a 1px hairline or a
2–3px rule instead of shadow. Corner radius 2px max — anything rounder reads as software.

## Components & states

- Kicker: sans 0.7rem/0.3em uppercase, vermillion, with a trailing 2px vermillion rule
  (`::after { flex:1 }`) that binds it to the headline.
- Plate: 1px ink border, 0.5rem padding, inline SVG engraving, caption over a hairline.
- Pull quote: 2px ink rules top and bottom, no side borders, italic, attributed in sans caps.
- Issue index: `counter(also, decimal-leading-zero)` in vermillion, hairline between items.
- Buttons: ink fill / ivory text; hover swaps to vermillion fill. `.ghost` is ink-outlined and
  inverts on hover. No radius above 2px, no shadow.
- Specimen controls: auxiliary buttons carry `data-demo="…"` and write an explicit “Demo only —
  nothing is ordered or sent” line into their group's `role="status"` slot. No dead controls.
- Form: 1px ink input on `--paper`, placeholder `--ink-faint`, message line reserved
  (`min-height:1.2em`) so submitting never shifts layout.
- Focus: `:focus-visible { outline:2px solid var(--vermillion); outline-offset:3px }` — 2px
  outline everywhere, never removed.

## Motion

None. Hover color swaps only (instant, no transition). `prefers-reduced-motion` block still
neutralises transitions and smooth scrolling for anything a host page may add.

## Responsive

- ≤900px: feature collapses to one column, body `columns:1`, plate moves below the deck,
  component columns stack. Masthead kicker and folio stay centred/left as set.
- Collapse the templates themselves (`.feature`, `.components` → `minmax(0,1fr)`), not just the
  children's spans: eleven fixed gutters (2rem/2.2rem) set a 352–387px intrinsic minimum that
  overflows a 375px shell, and `grid-column:1/-1` keeps every one of those gaps. `min-width:0` on
  the inputs plus `minmax(0,1fr)` on the subscribe form keeps the field freely shrinkable.
- ≤520px: body 16px, util bar drops to a 0.6rem padded row, pull quote drops to 1.15rem.
- Long headlines use `text-wrap:balance` plus `min-width:0` on grid children; no element is
  allowed a fixed width, so 375px never produces horizontal overflow.

## Pitfalls

- Do not add card shadows or gradients — the aesthetic is ink on stock.
- Do not set running text in the sans stack or the page becomes a blog.
- Do not let the vermillion past `#c2442c` for text; it fails AA at small sizes.
- Column rules on multi-paragraph blocks need `break-inside:avoid-column`, or a paragraph
  splits across the rule and the seam becomes visible.
- Drop caps fail on multi-word openers' punctuation; keep the opener's first sentence short.
- Keep the drop cap off the first paragraph when that paragraph is swapped dynamically — reapply
  `::first-letter` via CSS on the container, never by injecting markup.

## Adaptation recipe

1. Replace the display serif with the brand's text face, keeping the size/leading ratios above.
2. Re-pick one accent from three candidates and verify ≥4.5:1 on the ivory ground; derive the
   small-text variant by darkening ~12%.
3. Set the feature grid spans (headline/plate/body/aside) to the client's real content volume;
   keep the asymmetry, never centre-stack the three blocks.
4. Swap the plate SVG for editorial art at the same 4:5 ratio so the cap heights stay aligned.
5. Keep the demo strip labelled as a demo if the specimen ships to stakeholders.
