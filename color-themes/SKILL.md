---
name: color-themes
description: >
  Preview and create paired light and dark color themes from the catalog
  in themes.json. Use when the
  user asks for a color theme, palette, light and dark variants, a theme
  preview PDF, or a new theme, even if they only say "preview the colors"
  or "make a darker version". Do not use for image recoloring, logo
  design, or CSS that does not use these theme tokens.
---

# Color themes

Catalog: `themes.json`. Currently empty. Each pair has `light` and `dark` and the same tokens: `bg`, `surface`, `surface2`, `text`, `muted`, `border`, `accent`, `onAccent`, `success`, `warning`, `danger`. Do not invent a second format.

Preview: `previews/color-themes.pdf`. Index, then one page per theme. The index continues on another page when the catalog does not fit. Regenerate it. Do not hand-edit the PDF.

## Preview

```
python scripts/preview_pdf.py
```

One pair, written to `previews/<pair>.pdf` without replacing the catalog PDF:

```
python scripts/preview_pdf.py --pair dune
```

Give the user the PDF path. Do not paste hex tables unless they ask for tokens.

## Create

Add the light theme and its dark counterpart together. `--seed` is the shared accent hue. The script derives both modes, checks contrast, appends the pair, and regenerates `previews/color-themes.pdf`.

```
python scripts/create_theme.py --pair dune --seed C4A46A --light-name Dune --dark-name Dusk
```

Override any token with `--light-<token>` or `--dark-<token>`:

```
python scripts/create_theme.py --pair dune --seed C4A46A --light-name Dune --dark-name Dusk --light-bg FBF6EE --dark-accent E6C07B
```

## Contrast

- `text` on `bg` and on `surface`: at least 7:1
- `muted` on `bg` and on `surface`: at least 4.5:1
- `text` on `surface2`: at least 4.5:1
- `onAccent` on `accent`: at least 4.5:1
- `accent`, `success`, `warning`, `danger` on `bg`: at least 3:1
- `border` on `bg`: at least 1.4:1

A failure prints the ratio and the next command. Fix with an override flag. Do not lower the gates.

## Gotchas

- Pair id is unique lowercase kebab-case.
- Dark is not an inversion. Its accent is lighter so `onAccent` can stay dark.
- Scripts resolve the skill root from their own path. Run them as `python scripts/<name>.py` from the skill root, or pass that path.
- After create, report the new pair id and `previews/color-themes.pdf`. Do not dump the catalog.
