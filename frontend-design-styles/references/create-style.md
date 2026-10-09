# Create a new design style

Read this when adding a visual direction or when no catalog style fits the brief.
Paths below resolve from the skill root. Keep one workflow with multiple styles,
not separate skills that compete for the same frontend request.

## 1. Define a distinct premise

Write a one-sentence aesthetic thesis tied to a product and audience. Compare it
with the nearest two catalog styles. Require at least three structural differences
across typography, composition, surface/edge treatment, imagery/motif, and component
behavior. If only colors differ, adapt an existing style instead of adding a row.

Choose a short lowercase hyphenated slug. Confirm it is not already in the catalog.
Use the same slug for the reference and preview filenames.

## 2. Specify before styling

Create `references/<slug>.md` using the template below. Concrete values make the
recipe reproducible; reasons and constraints make it adaptable. Do not prescribe
new production dependencies. Prefer system fonts and locally available assets.

```markdown
# <Style name>

## Signature
<One sentence about aesthetic, intended audience, and primary visual tension.>
Choose for: <products/content it serves>.
Avoid for: <content or constraints it undermines>.
Nearest styles: <two names and the structural differences>.

## Tokens
| Role | Value | Use |
| --- | --- | --- |
| Canvas | <CSS color> | <surface role> |
| Ink | <CSS color> | <text on named surface> |
| Accent | <CSS color> | <action emphasis; foreground pair> |
| Muted | <CSS color> | <readable secondary copy> |
| Border | <CSS color> | <decorative or required boundary> |

## Typography and rhythm
Display: <system stack, size/clamp, weight, line height, tracking>.
Body: <system stack, size, line height, measure>.
Labels: <case, weight, size; don't use tiny metadata>.
Spacing: <base unit and a small explicit scale>.

## Composition and materials
<Container, grid, hierarchy, whitespace, edge treatment, shadows, motif.>
<What happens with long headings or dense content.>

## Components and states
<Button hierarchy, navigation, input/validation, cards, empty/error states.>
<Hover, keyboard focus, active, disabled; semantic affordances remain visible.>

## Motion and accessibility
<Feedback timing, reduced-motion behavior, contrast pairs, decorative semantics.>
<Material fallback and asset/font fallback where applicable.>

## Responsive rules
<Desktop columns, mobile stacking order, fluid type, control size, overflow rules.>

## Adaptation recipe
<Ordered primary composition → tokens → components → realistic content steps.>

## Avoid
<Specific choices that destroy this style or readability.>

## Specimen
Preview: `previews/<slug>.html`.
Demo: <one observable, explicitly local state transition>.
```

## 3. Build an offline specimen

Create `previews/<slug>.html` as a complete UTF-8 HTML document with a viewport
meta tag, inline CSS, and optional inline JavaScript/SVG. No build tool, CDN,
external font, analytics, network request, or image download. Local artwork
must be integral to the specimen, not a broken placeholder.

Give it a fictional product matching the direction. Include a primary composition,
secondary content, and representative components. Do not copy another style's
layout and recolor it. Design the mobile composition deliberately.

Include a visible `All styles` link to `index.html`. Include a meaningful button
with `id="demo-action"` whose activation changes visible local state. Label the
interaction as a demo; do not imply it sent data, bought something, or booked a
real service. Use native controls, visible focus, and a live status region when
feedback would otherwise be silent. Avoid useless controls and `href="#"`.

## 4. Inspect and revise

Open the page in a real browser from disk. Inspect at 1440px and 375px widths.
Activate the demo and observe the result; use keyboard traversal. Check:

- Heading, primary action, and supporting information remain visually distinct.
- Text wraps without overlap, clipping, or document-level horizontal scrolling.
- Actual foreground/background pairs meet AA contrast; gradients/translucency
  require checking the least favorable region, not only the token color.
- Essential controls remain legible without hover; focus is visible.
- No network dependencies, script errors, or broken navigation.
- Motion is nonessential and obeys reduced-motion when animation exists.
- Font fallback and loss of material effects preserve information hierarchy.
- The new style differs structurally from its nearest two neighbors.

Revise the reference when visual tuning changes its values. The reference and
specimen should agree; neither is a changelog of abandoned experiments.

## 5. Register and deliver

Add a row to the catalog in `SKILL.md` with selection guidance, reference path,
and preview path. Add a gallery entry in `previews/index.html`, matching its
existing entry structure and visual cue conventions. Preserve existing links.
Update any collection totals in the skill description, gallery title, heading,
range label, and initial count. Verify intent filters count the expanded catalog;
do not leave an old total while the new entries are present.
Check all skill-root paths exist and all gallery links resolve. Keep SKILL.md
under 500 lines and keep reference loading conditional on style selection.

Deliver the new style name, both file paths, the three distinguishing decisions,
and the observed browser verification. Remove throwaway tooling or screenshots
unless explicitly requested as deliverables.
