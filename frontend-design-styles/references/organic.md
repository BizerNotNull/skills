# Organic — Botanical Wellness & Garden

Companion preview: `previews/organic.html` (resolved from the skill root).

## Signature

Cream ground, moss and clay, and shapes that were never quite circles. Every container is an
irregular rounded form (asymmetric `border-radius` per corner, blob radius for illustration
fields), every shadow is soft and low-contrast, and illustration is drawn, not photographed:
inline SVG line-and-fill leaves in the accent colours. Warm serif copy at 1.7 leading reads like
a well-printed label. Handmade but tidy — nothing sharp, nothing grey.

## Typography

```css
--serif:"Iowan Old Style","Palatino Linotype",Georgia,"Book Antiqua","Times New Roman",serif;
--sans: ui-sans-serif,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
```

- Display: `clamp(2.2rem, 6.4vw, 4.2rem)`, weight 400, `line-height:1.04`,
  `letter-spacing:-.02em`, with the key phrase set italic in moss.
- Section head: `clamp(1.6rem, 4vw, 2.5rem)`, `max-width:34ch`.
- Body: 17px / 1.7 in the serif stack; secondary copy `--ink-soft`.
- Sans (uppercase, tracked) is the label voice: kickers 0.72rem/0.26em, buttons 0.8rem/0.12em,
  product meta 0.72rem/0.14em.
- Weights never exceed 700, and only on sans labels. Serif stays at 400.

## Spacing & layout

- Shell `min(1140px, 100% - 2.6rem)`; section padding 3.2rem (2.4rem ≤900px).
- Every band has a different skeleton — hero split `1.05fr .95fr`, ritual split `.9fr 1.1fr`,
  product shelf `repeat(3,1fr)`, garden notes `.85fr 1.15fr`, components `span 4` of 12.
- The shelf's middle card is nudged `translateY(1.6rem)` for a hand-placed feel; that offset is
  dropped at ≤900px, or one card visibly floats once the shelf stacks.
- Card padding 1.7rem; grid gaps 1.8–2.6rem. Blobs and shadows keep generous space from reading
  as emptiness by giving the ground texture.

## Color tokens (roles)

| Token | Value | Role | Measured |
|---|---|---|---|
| `--cream` | `#f4efe3` | page ground | — |
| `--cream-deep` | `#e8e0cf` | ritual panel | — |
| `--card` | `#fbf8f0` | card fill (one step up from ground) | — |
| `--ink` | `#33322a` | body text (warm near-black, never `#000`) | 11.2:1 |
| `--ink-soft` | `#6a6553` | secondary copy | ~5.2:1 |
| `--moss` | `#4a6136` | primary accent, buttons | 6.0:1 |
| `--moss-light` | `#7d9159` | illustration fills, gradients | decorative |
| `--clay` | `#b4674a` | illustration, dots, gradients | decorative only |
| `--clay-ink` | `#8f4f36` | clay **as text** (links, kickers, prices) | 5.5:1 |

The clay/moss pairing must be split into field and text shades. Raw `--clay` fails AA for small
text (3.7:1); `--clay-ink` is the text variant.

## Surfaces

Three stacked warm neutrals: ground `#f4efe3`, panel `#e8e0cf`, card `#fbf8f0`. Cards carry
`--lift: 0 12px 28px rgba(58,52,38,.12)` — soft, warm, low alpha. Radii are the signature: cards
`2.4rem 1.5rem 2.8rem 1.7rem`, buttons are pills, illustration fields use
`--blob-radius: 42% 58% 62% 38% / 48% 42% 58% 52%`. Inputs add a soft inset top highlight.

## Components & states

- Buttons: moss pill, cream label, `--lift`; hover shifts to `--clay-ink` and lifts `-2px` over
  0.25s. `.ghost` is a 2px moss outline that fills on hover.
- Numbered steps: blob-radius numeral disc in moss plus a card row (`<b>` title + soft-coloured
  description). Product cards: blob-gradient pot, meta line, price pinned via `margin-top:auto`.
- Quotes: italic serif in a rounded card with sans-caps attribution.
- Inputs: rounded asymmetric field on card fill, 1px at 20% ink, placeholder `#9a9384`.
- Focus: `:focus-visible { outline:3px solid var(--clay-ink); outline-offset:3px }`.
- Communicate states with colour and position; never flatten the whole card's shadow.
- Specimen controls: hero and shelf buttons carry `data-demo="…"` and report “Demo only — no item
  is added, no basket is created” into their group's `role="status"` slot.

## Motion

- Leaf illustration sways: `@keyframes sway` rotating ±1.6° with an 8px rise over 9s,
  `ease-in-out`, infinite — slow enough to read as a draught. Hover transitions: `transform` and
  `background-color`, 0.25s ease. `prefers-reduced-motion` removes both; nothing depends on motion.

## Responsive

- ≤900px: hero, ritual and notes splits collapse to one column (`gap:2rem`), the illustration is
  capped at 26rem so it does not dominate, the shelf stacks and the middle-card offset is
  removed, components go full width.
- ≤520px: body 16px, ritual panel padding 1.5rem with a smaller radius, the corner dot shrinks
  to 3.6rem, buttons become full width with centred labels. Blob radii and aspect-ratio squares
  scale automatically, so 375px needs no fixed pixel width and cannot overflow.

## Pitfalls

- Do not use `#000`, pure grey, or blue-tinted neutrals — every neutral is warm here.
- Never combine a sharp radius with a soft shadow: pick organic radius + soft shadow, or the page
  reads as two styles fighting.
- `border-radius` percentage blobs distort on non-square elements; keep blob fields at
  `aspect-ratio:1/1` or use the corner-list form for rectangles.
- Raw clay is not a text colour (3.7:1) — use `--clay-ink`.
- Shadows stay warm (`rgba(58,52,38,…)`) with alpha under ~0.14; darker reads as darkness.
- Equal radii everywhere loses the hand-drawn feel; the asymmetry between corners sells it.

## Adaptation recipe

1. Choose one warm ground and one accent plant colour; derive a darker text shade for links,
   kickers and prices before using the accent anywhere small.
2. Set radii first (`--blob-radius` plus per-card corner lists), then spacing — the radius is the
   identity mark.
3. Draw illustrations as inline SVG with two fills (accent + light accent) over cream strokes;
   never fetch icons.
4. Keep one micro-animation maximum, at 8–10s and low amplitude, then re-check every card's
   contrast against the card fill (which is lighter than the page ground), not the ground.
