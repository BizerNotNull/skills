"""Write the theme preview PDF. No prompts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from theme_lib import PREVIEW_PATH, SKILL_ROOT, THEMES_PATH, load_themes, validate_catalog, write_preview


def main() -> int:
    parser = argparse.ArgumentParser(description="Write a PDF preview of color themes.")
    parser.add_argument("--pair", help="Preview one pair instead of the full catalog.")
    parser.add_argument("--themes", type=Path, default=THEMES_PATH)
    parser.add_argument("--pdf", type=Path)
    args = parser.parse_args()

    data = load_themes(args.themes)
    problems = validate_catalog(data)
    if problems:
        print("catalog failed contrast checks:", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        print("next: fix themes.json or recreate the pair with scripts/create_theme.py", file=sys.stderr)
        return 1

    pairs = data["pairs"]
    if args.pair:
        pairs = [pair for pair in pairs if pair["id"] == args.pair]
        if not pairs:
            known = ", ".join(pair["id"] for pair in data["pairs"])
            print(f"unknown pair {args.pair}. known: {known}", file=sys.stderr)
            print("next: python scripts/preview_pdf.py --pair dune", file=sys.stderr)
            return 1
        out = args.pdf or (SKILL_ROOT / "previews" / f"{args.pair}.pdf")
        write_preview(pairs, out, index=False)
    else:
        out = args.pdf or PREVIEW_PATH
        write_preview(pairs, out, index=True)
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
