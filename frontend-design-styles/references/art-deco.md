# Art Deco — Cinema & Cultural Venue

Companion preview: `previews/art-deco.html` (resolved from the skill root).

## Signature

A jewel-navy hall lit by brass linework: concentric fan arches, stepped ziggurat pedestals, and a
strictly bilateral poster that puts one screening at the centre of the page like a marquee. Every
form is *drawn* — rules, arches and sunbursts are vectors, never photographs — and the grid is
symmetric, so the eye always falls down the centre line. Event data is compact and framed: title,
time, certificate and run time stay packed inside a bordered plate instead of floating in space.

Choose for: film programmes, concert and opera seasons, museum evenings, festivals, heritage venues.
Avoid for: fast-scanning feeds, dense data tables, commerce grids, content needing photographic truth.
Nearest styles: **Cyber** is also dark and drawn with 1px hairlines, but it is a near-black technical
console — monospace telemetry, off-centre asymmetric panels, no ornament; Art Deco is jewel-navy,
strictly bilateral, and ornamented with brass keylines, stepped ziggurats and fan arches. **Retro 1970s**
is also posterish and symmetric, but its warmth is chunky and hand-printed — heavy slab serif, 3px rules,
ink-misregistration shadows — where Art Deco is thin, precise and machined: 1px brass rules, stepped
motifs, geometric sans with wide tracking.

## Tokens

| Role | Value | Use |
| --- | --- | --- |
| Canvas | `#0e1a30` | jewel-navy page ground |
| Canvas deep | `#0a1424` | recessed plate, demo field, SVG ground |
| Panel | `#122340` | artwork beds, raised steps |
| Ink | `#f2ecdc` | ivory text on navy (14.7:1) |
| Accent | `#c9a227` | brass: rules, arches, numerals, buttons (7.2:1 on navy) |
| Secondary | `#8c2036` | garnet field for one badge/art layer, always with ivory text (7.5:1) |
| Muted | `#a9b2c4` | secondary copy, captions (8.2:1 on navy) |
| Hairline | `rgba(201,162,39,.45)`; soft `rgba(242,236,220,.14)` | keylines, dividers, arch outlines |

Brass is the only metal and is never used for body copy; the garnet field always carries ivory.

## Typography and rhythm

Display: `"Futura","Century Gothic","Avenir Next","Trebuchet MS",ui-sans-serif,"Segoe UI",sans-serif`,
uppercase, weight 700, `letter-spacing:.14em`, `line-height:1.04`, `clamp(1.9rem,6.4vw,3.4rem)`.
Gilt labels: same stack, weight 600, 11–12px, `letter-spacing:.34em`, uppercase, brass.
Body: `ui-sans-serif,"Segoe UI",Roboto,Helvetica,Arial,sans-serif`, 16px / 1.7, measure ≤62ch.
Pull quotes only: `"Georgia","Palatino Linotype",serif` italic, 18–20px.
Spacing: 8px base; scale 8 / 16 / 24 / 32 / 48 / 64. Section padding 4rem desktop, 2.6rem mobile.

## Composition and materials

- Shell `min(1080px, 100% - 2.6rem)`; the poster plate `min(680px, 100%)`, `padding:2.6rem 1.6rem`.
- Hero = ziggurat: three stacked steps of decreasing width under a keyline plate; the plate centres
  a CSS fan (`repeating-conic-gradient` spokes cut by a radial mask) above the title.
- Keyline recipe: outer 1px brass + 8px inset + inner 1px brass-soft, straight corners with small
  square accents. No radius above 2px anywhere.
- Imagery is inline SVG only: a different geometric motif per screening (fan, chevron, arcade) on a
  fixed 4:3 bed, so the layout never reflows when the artwork changes.
- Long titles: `text-wrap:balance` plus size clamps; the plate grows, nothing clips or ellipsizes.

## Components and states

- Buttons: 1px brass border, 11px / .3em uppercase, `padding:1rem 1.9rem`, transparent fill; hover
  fills brass with navy text over 0.35s `ease`, primary adds an 8% brass wash. Active nudges 1px down.
- Programme rows: `5.4rem / minmax(0,1fr) / auto` — brass time in tabular numerals, title + certificate,
  right-aligned certificate chip. Rows are separated by soft hairlines, no buttons, no hover lift.
- Select: navy fill, 1px brass border, ivory 16px value, custom SVG chevron, `option` forced to
  `--navy-deep` so the native menu never flashes white.
- Demo plate: `--navy-deep` field inside a double keyline, `role="status"` line beneath the button.
- Focus: `:focus-visible{outline:2px solid var(--brass);outline-offset:3px}` on every control.
- Disabled: 42% opacity with the border left solid so the affordance stays legible.

## Motion and accessibility

- One vocabulary only: colour/border-colour and a 1px translate, 0.35s `ease`. The fan never rotates;
  no glow, no parallax, no reveals. Feedback is text plus colour, so it survives reduced motion.
- `@media (prefers-reduced-motion: reduce)` drops every transition; state changes stay instant.
- Decorative arches and fans are `aria-hidden="true"`; artwork beds carry `role="img"` with a live label.
- Contrast pairings: ivory/navy 14.7:1, brass/navy 7.2:1, muted/navy 8.2:1, ivory/garnet 7.5:1.

## Responsive rules

- ≤900px: the feature plate goes single column (artwork above the details), the venue band stacks,
  the programme row drops its chip under the title.
- ≤560px: shell `100% - 1.8rem`, display `clamp(1.7rem,8.4vw,2.4rem)` with tracking at .1em so the
  title clears 375px, buttons go full width, all SVGs `max-width:100%` on their viewBox.
- Ziggurat uses 3 steps on desktop, 2 at ≤560px; artwork beds keep their `aspect-ratio` instead of a
  fixed height so nothing clips.

## Adaptation recipe

1. Choose the navy ground and a single metal accent; verify the metal at ≥4.5:1 on navy before using it.
2. Build the hero pedestal first (steps + keyline plate + fan) — this style is silhouette-driven.
3. Draw the keyline as padding plus two borders; never ship it as a background image.
4. Order bands: poster hero → feature plate → programme rows → venue split → demo plate → specimens.
5. Keep every band bilateral; an off-centre composition is a bug in this style, not a variation.

## Avoid

- Photographs and stock imagery: they break the drawn, machined premise. Use vector motifs.
- Blur, neon glow and gradient bloom; Deco depth is line and step, never light.
- A second metallic accent, or brass used as body text (it is an emphasis and rule colour).
- Rounded corners, rotations and sticker-like chips; symmetry is the brand.
- Heavy drop shadows — repeat a second offset keyline instead of adding blur.

## Specimen

Preview: `previews/art-deco.html`.
Demo: pressing **Next programme** advances through three fictional screenings — the feature SVG
artwork, title, time, certificate and run time all change together, and a live status line names the
newly shown screening; it is a local demo and nothing is booked, held or sent.
