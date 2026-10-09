# Brutalist — Raw Creative Studio

Companion preview: `previews/brutalist.html` (resolved from the skill root).

## Signature

Studio site as a stack of heavy slabs. Acid yellow or purple on bone, 3px black outlines,
unblurred offset shadows, zero corner radius, and type set far too large on purpose. Layout is
deliberately un-gridlike: full-bleed slabs, rotated stickers, a running ticker, and rows that
snap rather than align. The tone is loud and plainspoken — copy says “no beige” and the CSS
agrees. Every interaction is a physical press: translate plus shadow, no easing curve.

## Typography

```css
--heavy:"Arial Black","Helvetica Neue",Impact,system-ui,"Segoe UI",sans-serif;
--mono: ui-monospace,"Cascadia Mono",Consolas,"Courier New",monospace;
```

- Display `h1`: `clamp(2.9rem, 11.5vw, 8.6rem)`, `line-height:.85`, `letter-spacing:-.045em`,
  uppercase. Weight comes from the Arial Black/Impact face, not `font-weight:900` (which
  syntheses badly in that family).
- Stats: `clamp(2.6rem, 8vw, 5.4rem)`, `letter-spacing:-.05em`.
- Quote: `clamp(1.4rem, 4.6vw, 2.8rem)`, tight leading, with one phrase coloured.
- Body, buttons, labels: the mono stack, uppercase for controls and metadata, sentence case for
  paragraphs. Mono is the shock absorber — it keeps the shouting legible.
- Letter-spacing only goes negative on display type; controls use +.02–.14em.

## Spacing & layout

- Shell `min(1180px, 100% - 2rem)`; block padding 1.6rem; stack gaps 1.2–1.6rem.
- No 12-column grid for content. Sections are flex/grid of unequal slabs: hero (full width),
  ticker (full bleed), stats (`repeat(3,1fr)`), service rows (`5rem / 1fr / auto`), work
  (`repeat(3,1fr)`), quote slab, demo band, components (`span 4` of 12).
- Rotation is a layout tool: stickers alternate −2.4° / +1.8°, card headers −1°, the struck word
  −1.2°. Never rotate body text.
- Shadow tokens: `--shadow:10px 10px 0` for slabs, 4–8px for small controls. Shadows are solid
  black, never blurred.

## Color tokens (roles)

| Token | Value | Role | Measured |
|---|---|---|---|
| `--bone` | `#f3f1e4` | page ground, card fills | — |
| `--black` | `#0b0b0b` | outlines, shadows, text, ticker band | 18.6:1 on bone |
| `--acid` | `#e8ff00` | default accent field | 18.3:1 with black text |
| `--purple` | `#7b2ff7` | alternate accent field | 5.9:1 with white text; **3.2:1 with black — never pair** |
| `--accent` / `--accent-ink` | swapped pair | accent field + its text colour | always ship as a pair |

The demo switch flips `html[data-accent="purple"]`, which redefines `--accent` **and**
`--accent-ink` together. Never set one without the other; that is how acid-yellow black text
ends up on purple.

## Surfaces

Bone panels with 3px black borders and hard offset shadows. Filled fields are either the accent
or pure black. Patterned thumbs (`repeating-linear-gradient` stripes) stand in for imagery —
45° purple/black, 0° black/acid — plus one inline SVG zigzag. No photography, no blur, no radius.

## Components & states

- Buttons: `.btn` bone → `.accent` accent fill → `.fill` black. Hover `translate(-3px,-3px)`
  with a bigger shadow; active `translate(7px,7px)` and no shadow. Transitions use
  `steps(2, end)` so the motion snaps instead of gliding.
- Ticker: black band, duplicated track, `@keyframes slide` translating −50% over 22s,
  `aria-hidden="true"` because it is decoration.
- Service row: accent numeral tile, uppercase headline, mono description, right-aligned price;
  price drops under the text at ≤900px.
- Cards: patterned thumb, body, dashed-divider facts; tags are 2px outline chips.
- Demo band: background is `--accent` with `--accent-ink` text; the toggle is a bone button with
  an 8px shadow, so it stays readable in both accents.
- Focus: `:focus-visible { outline:4px dashed var(--purple); outline-offset:3px }`, switching to
  black when the page is already purple.

## Motion

Snappy and minimal: transform/shadow steps plus the ticker. The ticker is the only continuous
animation. `prefers-reduced-motion` disables both the ticker and the press transitions, leaving
instant state swaps (`aria-pressed`-style text and colour changes still work).

## Responsive

- ≤900px: stats and work grids go single column; service rows become numeral + content with the
  price on its own line; component columns full width.
- ≤560px: display clamps to `clamp(2.4rem,14vw,4.2rem)`, demo band stacks, the toggle becomes
  full width, slab padding drops to 1.1rem, stickers shrink to 0.75rem.
- Offsets are kept small (±3px hover, 10px shadow) so nothing pushes past the viewport; body has
  `overflow-x:hidden` as a belt-and-braces guard against rotated elements.

## Pitfalls

- Do not add easing (`ease`, `cubic-bezier`) to the press — the snap is the style.
- Never blur a shadow, and never use a grey shadow. Hard black or nothing.
- Purple with black text fails AA (3.2:1); always pair purple with white.
- Keep rotations under ~3°; more turns the page into a ransom note and clips at the viewport.
- Impact/Arial Black are absent on some Linux and Android builds — the stack must end in a
  usable sans, and display sizes must survive the fallback.
- The ticker needs `width:max-content` and a duplicated track, or the loop visibly jumps.

## Adaptation recipe

1. Pick the boldest available display sans and re-tune the clamp to that face's width.
2. Keep two accents that are already contrast-safe with their own text colours; expose them as
   `--accent` + `--accent-ink` and switch with one attribute.
3. Rebuild the section order as slabs — never convert this into cards on a grid.
4. Replace the patterned thumbs with the client's own strong imagery if it exists; keep the
   outlined frame and hard shadow.

Every auxiliary button (`Start a project`, `Book a call`, …) carries `data-demo="…"` and writes an
explicit “Demo only — nothing is scheduled, sent or downloaded” line into its group's live region.
