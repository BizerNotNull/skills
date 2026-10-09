"""Paired light/dark theme catalog, contrast gates, and preview PDF."""

from __future__ import annotations

import json
import re
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
THEMES_PATH = SKILL_ROOT / "themes.json"
PREVIEW_PATH = SKILL_ROOT / "previews" / "color-themes.pdf"

TOKENS = (
    "bg",
    "surface",
    "surface2",
    "text",
    "muted",
    "border",
    "accent",
    "onAccent",
    "success",
    "warning",
    "danger",
)

PAIR_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEX_RE = re.compile(r"^#?[0-9A-Fa-f]{6}$")

PAGE_W = 595
PAGE_H = 842

# (fg, bg, minimum ratio)
GATES = (
    ("text", "bg", 7.0),
    ("text", "surface", 7.0),
    ("muted", "bg", 4.5),
    ("muted", "surface", 4.5),
    ("text", "surface2", 4.5),
    ("onAccent", "accent", 4.5),
    ("accent", "bg", 3.0),
    ("success", "bg", 3.0),
    ("warning", "bg", 3.0),
    ("danger", "bg", 3.0),
    ("border", "bg", 1.4),
)


def normalize_hex(value: str) -> str:
    if not isinstance(value, str) or not HEX_RE.match(value.strip()):
        raise ValueError(f"not a 6-digit hex color: {value!r}")
    raw = value.strip().lstrip("#")
    return f"#{raw.upper()}"


def hex_rgb(value: str) -> tuple[int, int, int]:
    value = normalize_hex(value)
    return tuple(int(value[i : i + 2], 16) for i in (1, 3, 5))


def rel_lum(value: str) -> float:
    def channel(c: int) -> float:
        v = c / 255
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4

    r, g, b = hex_rgb(value)
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast(a: str, b: str) -> float:
    left, right = rel_lum(a), rel_lum(b)
    lighter, darker = max(left, right), min(left, right)
    return (lighter + 0.05) / (darker + 0.05)


def rgb_to_hsl(value: str) -> tuple[float, float, float]:
    r, g, b = [c / 255 for c in hex_rgb(value)]
    mx, mn = max(r, g, b), min(r, g, b)
    light = (mx + mn) / 2
    if mx == mn:
        return 0.0, 0.0, light
    delta = mx - mn
    sat = delta / (2 - mx - mn) if light > 0.5 else delta / (mx + mn)
    if mx == r:
        hue = ((g - b) / delta) % 6
    elif mx == g:
        hue = (b - r) / delta + 2
    else:
        hue = (r - g) / delta + 4
    return hue * 60, sat, light


def hsl_to_hex(hue: float, sat: float, light: float) -> str:
    hue = (hue % 360) / 360
    sat = max(0.0, min(1.0, sat))
    light = max(0.0, min(1.0, light))

    def hue_to_rgb(p: float, q: float, t: float) -> float:
        if t < 0:
            t += 1
        if t > 1:
            t -= 1
        if t < 1 / 6:
            return p + (q - p) * 6 * t
        if t < 1 / 2:
            return q
        if t < 2 / 3:
            return p + (q - p) * (2 / 3 - t) * 6
        return p

    if sat == 0:
        r = g = b = light
    else:
        q = light * (1 + sat) if light < 0.5 else light + sat - light * sat
        p = 2 * light - q
        r = hue_to_rgb(p, q, hue + 1 / 3)
        g = hue_to_rgb(p, q, hue)
        b = hue_to_rgb(p, q, hue - 1 / 3)
    return "#{:02X}{:02X}{:02X}".format(round(r * 255), round(g * 255), round(b * 255))


def ink_for(fill: str) -> str:
    return "#1A1A1A" if rel_lum(fill) > 0.45 else "#F7F7F5"


def load_themes(path: Path | None = None) -> dict:
    path = path or THEMES_PATH
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict) or not isinstance(data.get("pairs"), list):
        raise ValueError(f"{path} must be an object with a pairs array")
    return data


def save_themes(data: dict, path: Path | None = None) -> None:
    path = path or THEMES_PATH
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def failures(pair: dict) -> list[str]:
    found: list[str] = []
    pair_id = pair.get("id", "?")
    for mode in ("light", "dark"):
        tokens = pair.get(mode)
        if not isinstance(tokens, dict):
            found.append(f"{pair_id} {mode} missing token object")
            continue
        missing = [name for name in TOKENS if name not in tokens]
        if missing:
            found.append(f"{pair_id} {mode} missing {', '.join(missing)}")
            continue
        try:
            normalized = {name: normalize_hex(tokens[name]) for name in TOKENS}
        except ValueError as exc:
            found.append(f"{pair_id} {mode} {exc}")
            continue
        for fg, bg, need in GATES:
            ratio = contrast(normalized[fg], normalized[bg])
            if ratio < need:
                found.append(
                    f"{pair_id} {mode} {fg} {normalized[fg]} on {bg} "
                    f"{normalized[bg]} is {ratio:.2f}:1, need {need:.1f}:1"
                )
    return found


def validate_catalog(data: dict) -> list[str]:
    found: list[str] = []
    seen: set[str] = set()
    for pair in data["pairs"]:
        pair_id = pair.get("id", "")
        if not PAIR_RE.match(str(pair_id)):
            found.append(f"bad pair id {pair_id!r}")
        elif pair_id in seen:
            found.append(f"duplicate pair id {pair_id}")
        seen.add(str(pair_id))
        for key in ("lightName", "darkName"):
            if not isinstance(pair.get(key), str) or not pair[key].strip():
                found.append(f"{pair_id} missing {key}")
        found.extend(failures(pair))
    return found


def _semantic(hue: float, light: float) -> dict[str, str]:
    return {
        "success": hsl_to_hex(152, 0.42, light),
        "warning": hsl_to_hex(38, 0.62, light),
        "danger": hsl_to_hex(4, 0.58, light),
    }


def _tune_visible(color: str, bg: str, need: float, prefer_darker: bool) -> str:
    hue, sat, light = rgb_to_hsl(color)
    for _ in range(48):
        if contrast(hsl_to_hex(hue, sat, light), bg) >= need:
            return hsl_to_hex(hue, sat, light)
        light += -0.02 if prefer_darker else 0.02
        light = max(0.08, min(0.92, light))
    return hsl_to_hex(hue, sat, light)


def _accent_pair(seed: str, bg: str, dark_mode: bool) -> tuple[str, str]:
    hue, sat, _ = rgb_to_hsl(seed)
    sat = max(sat, 0.28) if sat > 0.04 else 0.0
    best = None
    for step in range(5, 90):
        light = step / 100
        accent = hsl_to_hex(hue, sat, light)
        if contrast(accent, bg) < 3.0:
            continue
        on_light = "#F7F7F5"
        on_dark = "#161616"
        for on_accent in (on_dark, on_light) if dark_mode else (on_light, on_dark):
            ratio = contrast(on_accent, accent)
            if ratio >= 4.5 and (best is None or ratio > best[0]):
                best = (ratio, accent, on_accent)
    if best:
        return best[1], best[2]
    accent = hsl_to_hex(hue, sat, 0.72 if dark_mode else 0.32)
    return accent, ink_for(accent)


def derive_pair(pair_id: str, seed: str, light_name: str, dark_name: str, overrides: dict[str, str]) -> dict:
    seed = normalize_hex(seed)
    hue, sat, _ = rgb_to_hsl(seed)
    sat = min(sat, 0.55)

    def mode(dark: bool) -> dict[str, str]:
        if dark:
            tokens = {
                "bg": hsl_to_hex(hue, sat * 0.35, 0.09),
                "surface": hsl_to_hex(hue, sat * 0.28, 0.13),
                "surface2": hsl_to_hex(hue, sat * 0.24, 0.18),
                "text": hsl_to_hex(hue, min(sat, 0.12), 0.93),
                "muted": hsl_to_hex(hue, min(sat, 0.10), 0.72),
                "border": hsl_to_hex(hue, sat * 0.2, 0.28),
            }
        else:
            tokens = {
                "bg": hsl_to_hex(hue, sat * 0.28, 0.96),
                "surface": hsl_to_hex(hue, sat * 0.12, 0.99),
                "surface2": hsl_to_hex(hue, sat * 0.22, 0.91),
                "text": hsl_to_hex(hue, min(sat, 0.22), 0.13),
                "muted": hsl_to_hex(hue, min(sat, 0.16), 0.36),
                "border": hsl_to_hex(hue, sat * 0.18, 0.80),
            }
        accent, on_accent = _accent_pair(seed, tokens["bg"], dark)
        tokens["accent"] = accent
        tokens["onAccent"] = on_accent
        semantic_l = 0.68 if dark else 0.32
        tokens.update(_semantic(hue, semantic_l))
        prefix = "dark-" if dark else "light-"
        for name in TOKENS:
            key = prefix + name
            if key in overrides:
                tokens[name] = normalize_hex(overrides[key])
        tokens["text"] = _tune_visible(tokens["text"], tokens["bg"], 7.0, prefer_darker=not dark)
        tokens["text"] = _tune_visible(tokens["text"], tokens["surface"], 7.0, prefer_darker=not dark)
        tokens["muted"] = _tune_visible(tokens["muted"], tokens["bg"], 4.5, prefer_darker=not dark)
        tokens["muted"] = _tune_visible(tokens["muted"], tokens["surface"], 4.5, prefer_darker=not dark)
        tokens["border"] = _tune_visible(tokens["border"], tokens["bg"], 1.4, prefer_darker=not dark)
        for name in ("accent", "success", "warning", "danger"):
            tokens[name] = _tune_visible(tokens[name], tokens["bg"], 3.0, prefer_darker=not dark)
        if contrast(tokens["onAccent"], tokens["accent"]) < 4.5:
            tokens["onAccent"] = ink_for(tokens["accent"])
        return tokens

    pair = {
        "id": pair_id,
        "lightName": light_name,
        "darkName": dark_name,
        "light": mode(False),
        "dark": mode(True),
    }
    return pair


def pdf_escape(text: str) -> str:
    return text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)")


def _rgb(value: str) -> str:
    r, g, b = hex_rgb(value)
    return f"{r / 255:.4f} {g / 255:.4f} {b / 255:.4f}"


def fill_rect(x: float, y: float, w: float, h: float, color: str) -> str:
    return f"{_rgb(color)} rg {x:.2f} {y:.2f} {w:.2f} {h:.2f} re f\n"


def stroke_rect(x: float, y: float, w: float, h: float, color: str, width: float = 1) -> str:
    return f"{width:.2f} w {_rgb(color)} RG {x:.2f} {y:.2f} {w:.2f} {h:.2f} re S\n"


def draw_text(x: float, y: float, text: str, size: float, color: str, bold: bool = False) -> str:
    font = "F2" if bold else "F1"
    return f"BT /{font} {size:.1f} Tf {_rgb(color)} rg {x:.2f} {y:.2f} Td ({pdf_escape(text)}) Tj ET\n"


def _swatch(x: float, y: float, w: float, h: float, name: str, color: str) -> str:
    label = ink_for(color)
    body = fill_rect(x, y, w, h, color)
    body += stroke_rect(x, y, w, h, label, 0.6)
    body += draw_text(x + 8, y + 20, name, 8, label)
    body += draw_text(x + 8, y + 8, color, 8, label)
    return body


def _mock(x: float, y: float, w: float, h: float, tokens: dict[str, str], title: str) -> str:
    body = fill_rect(x, y, w, h, tokens["surface"])
    body += stroke_rect(x, y, w, h, tokens["border"], 1.2)
    body += fill_rect(x, y + h - 28, w, 28, tokens["surface2"])
    body += draw_text(x + 12, y + h - 18, title, 10, tokens["text"], bold=True)
    body += fill_rect(x, y, 108, h - 28, tokens["surface2"])
    for i, label in enumerate(("Overview", "Tokens", "Preview")):
        body += draw_text(x + 12, y + h - 52 - i * 18, label, 9, tokens["text"] if i == 0 else tokens["muted"])
    body += draw_text(x + 124, y + h - 58, "Primary text on surface", 11, tokens["text"])
    body += draw_text(x + 124, y + h - 76, "Muted text stays readable", 9, tokens["muted"])
    body += fill_rect(x + 124, y + 18, 72, 22, tokens["accent"])
    body += draw_text(x + 140, y + 25, "Save", 9, tokens["onAccent"], bold=True)
    for i, name in enumerate(("success", "warning", "danger")):
        cx = x + 208 + i * 78
        body += fill_rect(cx, y + 18, 70, 22, tokens[name])
        body += draw_text(cx + 8, y + 25, name, 8, ink_for(tokens[name]))
    return body


def page_theme(pair: dict, mode: str) -> str:
    tokens = {name: normalize_hex(pair[mode][name]) for name in TOKENS}
    name = pair["lightName"] if mode == "light" else pair["darkName"]
    other = pair["darkName"] if mode == "light" else pair["lightName"]
    body = fill_rect(0, 0, PAGE_W, PAGE_H, tokens["bg"])
    body += fill_rect(0, 0, 8, PAGE_H, tokens["accent"])
    body += draw_text(28, 800, name, 22, tokens["text"], bold=True)
    body += draw_text(28, 778, f"{pair['id']}  ·  {mode}  ·  pair of {other}", 10, tokens["muted"])
    body += _mock(28, 500, 539, 258, tokens, name)
    cols = 4
    sw_w, sw_h, gap_x, gap_y = 128, 42, 10, 22
    origin_y = 430
    for index, token in enumerate(TOKENS):
        col, row = index % cols, index // cols
        x = 28 + col * (sw_w + gap_x)
        y = origin_y - row * (sw_h + gap_y)
        body += _swatch(x, y, sw_w, sw_h, token, tokens[token])
    body += draw_text(28, 24, "color-themes preview", 8, tokens["muted"])
    return body


def _mini(x: float, y: float, w: float, h: float, tokens: dict[str, str], title: str) -> str:
    body = fill_rect(x, y, w, h, tokens["bg"])
    body += stroke_rect(x, y, w, h, tokens["border"])
    body += fill_rect(x, y, 6, h, tokens["accent"])
    body += fill_rect(x + 14, y + 12, w - 78, h - 24, tokens["surface"])
    body += draw_text(x + 22, y + 28, title, 10, tokens["text"], bold=True)
    body += fill_rect(x + w - 54, y + 16, 40, 16, tokens["accent"])
    body += draw_text(x + w - 44, y + 20, "Aa", 8, tokens["onAccent"], bold=True)
    return body


def page_index(pairs: list[dict]) -> list[str]:
    row_h = 68
    top = 748
    per_page = 10
    pages: list[str] = []
    total = max(1, (len(pairs) + per_page - 1) // per_page)
    for page_i in range(total):
        chunk = pairs[page_i * per_page : (page_i + 1) * per_page]
        body = fill_rect(0, 0, PAGE_W, PAGE_H, "#F4F1EA")
        body += draw_text(28, 800, "Color themes", 22, "#1C1915", bold=True)
        subtitle = f"{len(pairs)} light themes, each with a dark counterpart"
        if total > 1:
            subtitle += f"  ·  {page_i + 1}/{total}"
        body += draw_text(28, 778, subtitle, 10, "#5C564C")
        for index, pair in enumerate(chunk):
            number = page_i * per_page + index + 1
            y = top - (index + 1) * row_h
            light = {name: normalize_hex(pair["light"][name]) for name in TOKENS}
            dark = {name: normalize_hex(pair["dark"][name]) for name in TOKENS}
            body += draw_text(28, y + 50, f"{number:02d}  {pair['id']}", 8, "#5C564C")
            body += _mini(28, y, 250, 46, light, pair["lightName"])
            body += _mini(292, y, 250, 46, dark, pair["darkName"])
        footer = "Index, then one page per theme"
        if total > 1:
            footer += f"  ·  index {page_i + 1}/{total}"
        body += draw_text(28, 24, footer, 8, "#5C564C")
        pages.append(body)
    return pages


def build_pdf(streams: list[str]) -> bytes:
    header = b"%PDF-1.4\n%\xe2\xe3\xcf\xd3\n"
    objects: list[bytes] = []

    def add(body: bytes) -> int:
        objects.append(body)
        return len(objects)

    n = len(streams)
    page_ids = [5 + i * 2 for i in range(n)]
    content_ids = [6 + i * 2 for i in range(n)]
    kids = " ".join(f"{i} 0 R" for i in page_ids)
    add(b"<< /Type /Catalog /Pages 2 0 R >>")
    add(f"<< /Type /Pages /Count {n} /Kids [{kids}] >>".encode("ascii"))
    add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>")
    add(b"<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica-Bold >>")
    for pid, cid, stream in zip(page_ids, content_ids, streams):
        raw = stream.encode("latin-1")
        page = (
            f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PAGE_W} {PAGE_H}] "
            f"/Contents {cid} 0 R /Resources << /Font << /F1 3 0 R /F2 4 0 R >> >> >>"
        ).encode("ascii")
        got_page = add(page)
        content = b"<< /Length " + str(len(raw)).encode("ascii") + b" >>\nstream\n" + raw + b"endstream"
        got_content = add(content)
        if got_page != pid or got_content != cid:
            raise RuntimeError("pdf object ids drifted")
    out = bytearray(header)
    offsets = [0]
    for index, obj in enumerate(objects, 1):
        offsets.append(len(out))
        out += f"{index} 0 obj\n".encode("ascii")
        out += obj
        out += b"\nendobj\n"
    xref = len(out)
    out += f"xref\n0 {len(objects) + 1}\n".encode("ascii")
    out += b"0000000000 65535 f \n"
    for offset in offsets[1:]:
        out += f"{offset:010d} 00000 n \n".encode("ascii")
    out += (
        f"trailer << /Size {len(objects) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n"
    ).encode("ascii")
    return bytes(out)


def write_preview(pairs: list[dict], path: Path, index: bool = True) -> None:
    streams: list[str] = []
    if index:
        streams.extend(page_index(pairs))
    for pair in pairs:
        streams.append(page_theme(pair, "light"))
        streams.append(page_theme(pair, "dark"))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(build_pdf(streams))
