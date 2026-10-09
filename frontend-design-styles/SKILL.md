---
name: frontend-design-styles
description: >
  Design and implement aesthetically distinctive frontend interfaces using ten
  art-directed styles and offline HTML previews. Use when the user asks for a
  beautiful website, a distinctive landing page, a visual UI direction, a style
  comparison, or a new design style, even without naming a design movement.
  Do not use for backend work, behavior-only bug fixes, or palette-only changes
  that leave typography, layout, and components unchanged.
---

# Frontend design styles

Use a coherent visual system, not a generic card grid with a different accent.
The references specify design decisions the previews demonstrate. Their tokens
are starting points, not an instruction to overwrite an existing brand.

## Choose a direction

1. Identify the product, audience, primary task, real content, existing framework,
   and brand constraints from the request and repository. Preserve working flows.
2. If a style is named, use it. Otherwise choose one from the table by content and
   mood; state the choice briefly and proceed. Default to editorial for a
   content-led site and bento for a functional app. Do not blend styles by default.
3. For visual comparison, open `previews/index.html` in a browser. All ten pages
   work directly from disk with no server, installation, or network access.
4. Read only the selected reference below. Open its HTML preview at desktop and
   narrow mobile widths before implementation; inspect the actual visual hierarchy
   and activate its demo control. Do not infer the system from the thumbnail alone.
5. Translate its typography, composition, surfaces, and interaction grammar into
   the project's existing components. Keep the user's actual content and workflows;
   never ship the preview's fictional brand or local demo as production behavior.

| Style | Choose for | Reference to read | HTML preview |
| --- | --- | --- | --- |
| Editorial | Publications, portfolios, narrative products; literary and opinionated | `references/editorial.md` | `previews/editorial.html` |
| Swiss | Exhibitions, cultural events, clear information; rigorous and graphic | `references/swiss.md` | `previews/swiss.html` |
| Brutalist | Independent studios, experimental campaigns; raw and confrontational | `references/brutalist.md` | `previews/brutalist.html` |
| Organic | Wellness, gardens, sustainable goods; warm and tactile | `references/organic.md` | `previews/organic.html` |
| Glass | Audio, focus, ambient digital products; luminous and layered | `references/glass.md` | `previews/glass.html` |
| Retro | Music, food, vintage-inspired commerce; nostalgic and exuberant | `references/retro.md` | `previews/retro.html` |
| Cyber | Technical monitoring and sci-fi experiences; precise and high-contrast | `references/cyber.md` | `previews/cyber.html` |
| Bento | Workspaces and product dashboards; modular and information-led | `references/bento.md` | `previews/bento.html` |
| Art Deco | Cinemas, cultural venues, formal celebrations; geometric and ornamental | `references/art-deco.md` | `previews/art-deco.html` |
| Blueprint | Architecture portfolios, spatial project viewers; measured and technical | `references/blueprint.md` | `previews/blueprint.html` |

## Implement the system

- Establish four signatures before building: type contrast, layout rhythm,
  surface/edge treatment, and a distinctive motif. A palette alone is not a style.
- Map reference roles to project tokens. Retain existing token naming and component
  conventions; do not add a parallel design system or new UI dependency by default.
- Build the primary composition first, then supporting cards, forms, navigation,
  empty/error states, and focus/hover/disabled states. Carry the same grammar through
  these states; do not hide real affordances to make the screenshot cleaner.
- Use real content density to tune the layout. Editorial is not necessarily sparse;
  bento is not permission to tile every sentence; a restrained style must still expose the task.
- Use system font stacks from the references for offline prototypes. If the project
  already ships appropriate licensed fonts, use them; never depend on an unprovided
  font or remote image for the composition to work.
- Express decorative artwork as CSS or local assets, separate from information.
  Give meaningful images alt text; hide decorative SVG from assistive technology.
- Restrict motion to purposeful feedback. Provide reduced-motion behavior. Preserve
  readable contrast, keyboard focus, target size, and natural content order regardless
  of aesthetic. Translucent cards need a legible fallback without blur.

## Verify the actual surface

Open the implemented route, not only the reference. Check desktop and 375px mobile,
long titles and realistic data density, keyboard traversal, and the primary action.
Observe the changed state. Check for horizontal overflow and clipped text; zoom
and stacked layouts must not conceal controls. Keep body text readable (target
WCAG AA: 4.5:1 normal text, 3:1 large text; 3:1 for required UI boundaries).
No fake navigation, dead buttons, decorative-only controls, or invented success states.
The preview interactions are explicitly local demonstrations, not real services.

## Create or extend a style

When none of the catalog styles fits, or the user asks to add a new direction, read
`references/create-style.md` and follow its definition → specimen → verification
workflow. Add a new reference, preview, and catalog row together. Keep new styles
inside this skill; do not create a new skill for every visual direction.

## Gotchas

- Glass is a material treatment, not an excuse for low contrast or slow rendering.
  Limit blur layers and never animate expensive backdrop filters.
- Brutalist and cyber effects must not flicker, break reading order, or force tiny
  type. Heavy borders and mono labels do not replace hierarchy.
- System font metrics vary. Use fluid type and wrapping rather than widths that
  only work on the machine that generated the preview.
- Preview pages are independent specimens. Reuse their design grammar, not their
  monolithic HTML structure in a component-based production application.

## Delivery

Use this concise output structure after implementing and verifying:

```text
Direction: <style> — <why it fits the user's content>
Implemented: <routes/files and distinctive visual decisions>
Verified: <viewports, primary interaction, keyboard/overflow observations>
Constraints: <actual remaining prerequisite, or omit this line>
```
