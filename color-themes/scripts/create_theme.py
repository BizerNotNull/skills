"""Add one light/dark pair and regenerate the preview PDF. No prompts."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from theme_lib import (
    PAIR_RE,
    PREVIEW_PATH,
    THEMES_PATH,
    TOKENS,
    derive_pair,
    failures,
    load_themes,
    normalize_hex,
    save_themes,
    write_preview,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Create a paired light and dark color theme.")
    parser.add_argument("--pair", required=True, help="Kebab-case pair id, e.g. dune.")
    parser.add_argument("--seed", required=True, help="Shared accent hex, e.g. C4A46A.")
    parser.add_argument("--light-name", required=True)
    parser.add_argument("--dark-name", required=True)
    parser.add_argument("--themes", type=Path, default=THEMES_PATH)
    parser.add_argument("--pdf", type=Path, default=PREVIEW_PATH)
    for mode in ("light", "dark"):
        for token in TOKENS:
            parser.add_argument(f"--{mode}-{token}", dest=f"{mode}_{token}")
    args = parser.parse_args()

    if not PAIR_RE.match(args.pair):
        print(f"bad pair id {args.pair!r}; use lowercase kebab-case", file=sys.stderr)
        print(
            "next: python scripts/create_theme.py --pair dune --seed C4A46A "
            "--light-name Dune --dark-name Dusk",
            file=sys.stderr,
        )
        return 1
    try:
        seed = normalize_hex(args.seed)
    except ValueError as exc:
        print(str(exc), file=sys.stderr)
        print("next: pass --seed as 6 hex digits, e.g. C4A46A", file=sys.stderr)
        return 1

    overrides = {}
    for mode in ("light", "dark"):
        for token in TOKENS:
            value = getattr(args, f"{mode}_{token}")
            if value:
                try:
                    overrides[f"{mode}-{token}"] = normalize_hex(value)
                except ValueError as exc:
                    print(f"--{mode}-{token}: {exc}", file=sys.stderr)
                    print(f"next: pass --{mode}-{token} as 6 hex digits", file=sys.stderr)
                    return 1

    data = load_themes(args.themes)
    if any(pair["id"] == args.pair for pair in data["pairs"]):
        print(f"pair {args.pair} already exists", file=sys.stderr)
        print("next: pick a new --pair id", file=sys.stderr)
        return 1

    pair = derive_pair(args.pair, seed, args.light_name.strip(), args.dark_name.strip(), overrides)
    problems = failures(pair)
    if problems:
        print("new pair failed contrast checks:", file=sys.stderr)
        print("\n".join(problems), file=sys.stderr)
        print(
            "next: rerun with token overrides, e.g. --light-text 1A140C --dark-muted C8BEB0",
            file=sys.stderr,
        )
        return 1

    data["pairs"].append(pair)
    save_themes(data, args.themes)
    write_preview(data["pairs"], args.pdf, index=True)
    print(f"added {args.pair}")
    print(args.pdf)
    return 0


if __name__ == "__main__":
    sys.exit(main())
