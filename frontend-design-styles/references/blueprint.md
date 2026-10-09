# Blueprint — Drafting Studio & Project Viewer

Companion preview: `previews/blueprint.html` (resolved from the skill root).

## Signature

An analog drafting sheet on screen: pale paper carrying a faint blue rule grid, a measured line drawing at 1:50, dimension strings with 45° ticks and readable numerals, and a ruled title block holding the metadata. Structure comes from drawn geometry — plan, elevation, section hatch, centre lines — plus a side column of facts, dimensions and revisions. Nothing glows and nothing animates: the page is a document, not a console.

Choose for: architecture and survey portfolios, plan/section viewers, engineering archives, specification and drawing-set pages.
Avoid for: real-time monitoring, dashboards, or marketing pages where one giant number or headline must dominate.

Nearest styles: **cyber** — cyber renders live telemetry on a near-black void with monospace readouts, glowing accents and animated traces; blueprint is static, paper-ground, sans-set, and its marks are drawn rules rather than data. **swiss** — swiss is a poster of huge flush-left display type on a grid with an accent numeral doing the shouting; blueprint's largest element is the sheet, its type stays small and subordinate, and hierarchy comes from line weight, poché and dimension strings rather than from scale.

## Tokens

| Role | Value | Use |
| --- | --- | --- |
| Canvas | `#eee9dd` | drafting paper ground |
| Panel | `#f8f6ef` | sheet field, title-block cells, sidebar |
| Ink | `#1d3f6e` | blue drafting ink: text, borders, line work — 8.7:1 on canvas, 9.8:1 on panel |
| Muted | `#4b6588` | secondary copy, notes, captions — 4.9:1 on canvas |
| Markup | `#9b3a22` | revision marks, level symbols, focus ring — 5.7:1 on canvas |
| Grid | `rgba(29,63,110,.09)` | 12px paper grid, decorative only |
| Rule | `rgba(29,63,110,.34)` | cell borders, hairlines |
| Faint | `#7d8ba3` | construction, leader and centre lines, hatch — 2.8:1, never text |
| Poché | `rgba(29,63,110,.34)` | wall hatch in cut sections |

Ink is the ink: `--faint` must never carry a dimension value, or the measurement stops being readable. Paper text on the Ink fill is 9.8:1.

## Typography and rhythm

Display: none in the poster sense. The largest type is the sheet title, sans `ui-sans-serif,"Segoe UI",Roboto,Helvetica,Arial,sans-serif`, `clamp(1.4rem, 3.2vw, 2rem)`, weight 600, tracking `-.01em`.
Body: sans 16px / 1.6, measure `38rem`; notes and captions 0.86rem / 1.55 in Muted. Labels: 0.72rem uppercase, 0.14–0.16em tracking, in a bordered cell above or beside its value.
Dimensions, areas and levels: 0.8rem, `font-variant-numeric: tabular-nums`, tracking `.06em`, so every figure aligns in the sidebar tables and inside the drawing.
Spacing: base 4px; scale `4 / 8 / 12 / 16 / 24 / 32 / 48`; sheet frame padding 8px (6px ≤900px), sidebar padding 16px 18px.
No monospace anywhere — the numerals are drafting figures, not a terminal.

## Composition and materials

- Shell `min(1280px, 100% - 2.4rem)`; twelve columns, `gap: 24px`. Sheet `1 / span 8`, sidebar `9 / span 4`; the title block is a four-cell row whose cells share 1px borders with no gaps and radius 0. Hierarchy: title block → sheet → sidebar, never centred.
- Paper: two `linear-gradient` rules on `background-size: 12px 12px`, alpha ≤10%, over `#eee9dd`; keep the grid under the drawing so line work separates from the ground by weight, not colour.
- Line work: contours 2.4px, secondary 1px, poché hatch at 34% ink, centre lines dash-dot `7 3 1 3`, fittings and hidden edges `6 4`. Dimension strings use 1px extension lines and 45° tick ends, with values drawn `paint-order:stroke` over a 3px paper halo so they stay legible crossing a rule.
- Sheet frame: double rule (2px outer, 1px inner, 8px apart) with corner register marks drawn in the sheet; the north arrow and the segmented scale bar sit in the sheet's foot, not the sidebar. The drawing ships in two authored variants — the full sheet (`viewBox 0 0 660 480`) and a compact general arrangement (`viewBox 0 0 380 320`, fewer annotations, larger relative type on the same 0.72rem-equivalent scale).
- Prose lives in the sidebar as hairline-ruled notes; the sheet is never filled with paragraphs.

## Components and states

- Buttons: 2px Ink outline, uppercase 0.72rem label, radius 0, 40px tall (full width ≤560px). Primary is Ink fill with paper text (hover `#16345c`); secondary fills at 8% ink on hover; ghost is underline-only.
- Title-block cells: Muted caps label above the Ink value, `padding: 8px 12px`, tabular figures.
- Revision table: hairline rows `Rev / Date / Description / By`; the current row gets a 2px Markup left bar with `aria-current="true"`, and markup red is the only warm colour on the page.
- Toggle: a real checkbox (`accent-color` in ink) driving the dimension-line layer (a `dims-off` class on the SVG root), announced through `role="status"`.
- Select: 1:50 / 1:100 / 1:200 sets the level of detail — 1:200 hides the hatch and fitting groups — and re-segments the scale bar. Both drawing variants carry the same `.dims`, `.hatch` and `.furn` hooks, so the toggle and the select act on either one.
- Input: 1px Ink border on Panel; focus adds a 2px Markup ring, invalid adds a Markup border with an explicit written message (never colour alone), reserved message line.
- Disabled specimens stay visibly disabled and say why in the label (“Export DWG — unavailable in this specimen”), so no control is decorative dead weight.
- Focus: `:focus-visible { outline: 2px solid var(--markup); outline-offset: 2px }` — markup red reads on top of blue line work. The scrollable sheet is focusable with the same ring.

## Motion and accessibility

- The drawing view changes with a 180ms opacity crossfade; hover and border changes are 120ms. The width-driven variant repaint is instant — a resize must not animate. No loops, no marching dashes, no counting numbers.
- `prefers-reduced-motion: reduce` removes the animation and transitions; the view swap is instant.
- Each drawing is `role="img"` with a written `aria-label` (“Ground-floor plan, 1:50, three rooms”), and every measured value also appears as text in the sidebar tables — the SVG is never the only source of a number.
- Contrast pairs: Ink 8.7:1, Muted 4.9:1, Markup 5.7:1 on Canvas; paper on Ink fill 9.8:1.

## Responsive rules

- ≤1024px: sheet and sidebar stack (sheet first), title block reflows to a 2×2 cell grid.
- ≤900px: frame padding 6px; the drawing keeps its viewBox proportions so dimension labels scale rather than clip, and the sheet head wraps.
- Below 580px of sheet width (`ResizeObserver` on the sheet box, `getBoundingClientRect().width`, not a viewport breakpoint) the sheet repaints itself as the compact general arrangement: nothing is cropped and the page never scrolls sideways. If the observer is unavailable, fall back to a window `resize` listener.
- ≤560px: revision rows become labelled stacks (`data-label` prefixes), body type falls to 15px, buttons and the scale select go full width, and the scale bar narrows at ≤700px CSS.
- `min-width:0` on grid children and `overflow-wrap:anywhere` on sheet ids; the paper grid is a background, so it can never create overflow.

## Pitfalls

- Do not animate the drawing: marching dashes and pulsing dimensions are the cyber failure mode, not this style.
- Do not set dimensions in `--faint` (2.8:1) or at 0.6rem — the measurement is the content.
- Do not use rounded corners, shadows or blur; every edge in a drawing set is a rule.
- Do not let the paper grid pass ~10% alpha, or the drawing lines stop separating from the ground.
- Do not ship a drawing without its text alternative, and keep the sidebar figures in sync with the SVG values when the view changes.
- Do not introduce monospace or neon “console” accents; that collapses the difference from cyber.
- Do not let the full sheet shrink into a phone column: at 375px its 12-unit dimension figures render near 6px. Author a compact variant with larger relative type instead of clipping, hiding or horizontally scrolling the drawn annotations.

## Adaptation recipe

1. Set Canvas, Ink, Markup and the Ink fill shade; paint the 12px grid at ≤10% alpha.
2. Draw the sheet frame (double rule + register marks) and the title-block cells before any content.
3. Put project facts in the title block, dimensions and revisions in the sidebar, geometry on the sheet.
4. Rebuild the drawing as inline SVG on a fixed viewBox with 1–2.5px strokes and mirror every value into the sidebar tables.
5. Wire the view switch (plan/elevation) and the scale select as local state, announce both in the status line, and crossfade at 180ms.

## Specimen

Preview: `previews/blueprint.html`.
Demo: `Switch to elevation` toggles the sheet between the ground-floor plan and the west elevation — drawing, sheet number, drawing title, scale, dimension table and notes change together; `Dimension lines` and the 1:50 / 1:100 / 1:200 select act on the same local state.
