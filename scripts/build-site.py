#!/usr/bin/env python3
"""Build the static Fuel Logic brand guide and logo gallery pages."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "fl-brand-guide.md"
LOGOS = ROOT / "logos"

STYLE = """
:root {
  --brand-primary: #A2CD3A;
  --base: #FFFFFF;
  --base-two: #F4F4F4;
  --base-three: #E9E9E9;
  --base-four: #EFF6DE;
  --base-five: #ECF8FD;
  --contrast: #414141;
  --contrast-two: #7D7E7F;
  --contrast-three: #A2A3A6;
  --accent: #A2CD3A;
  --accent-medium: #85B33A;
  --accent-dark: #678C2B;
  --accent-two: #ff8c57;
  --accent-two-light: #FFA67D;
  --accent-two-dark: #AC603C;
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--base); color: var(--contrast); font: 400 1.3rem/1.62 "Work Sans", sans-serif; }
a { color: var(--accent-two); text-decoration: none; }
a:hover { color: var(--accent-two-dark); }
h1,h2,h3,h4,h5,h6 { color: var(--contrast); font-family: "Work Sans", sans-serif; font-weight: 700; line-height: 1.08; letter-spacing: -.035em; text-wrap: balance; }
h1 { font-size: clamp(3.1rem, calc(3.1rem + ((1vw - .2rem) * 1.5)), 4rem); line-height: .9; margin: 0 0 1rem; }
h2 { font-size: clamp(1.85rem, calc(1.85rem + ((1vw - .2rem) * 1.583)), 2.8rem); margin: 3rem 0 1rem; }
h3 { font-size: 1.5rem; } h4,h5,h6 { font-size: 1.3rem; }
small,.small { color: var(--contrast-three); font-size: .9rem; }
.topline { height: 8px; background: var(--accent); }
.shell { width: min(1140px, calc(100% - 32px)); margin: auto; padding: 42px 0 72px; }
.header { display: flex; align-items: center; justify-content: space-between; gap: 28px; padding-bottom: 34px; border-bottom: 1px solid var(--base-three); }
.header img { width: min(390px, 52vw); height: auto; display: block; }
.nav { display: flex; align-items: center; gap: 27px; flex-wrap: wrap; margin-left: auto; font-size: 1.3rem; font-weight: 500; }
.nav a:not(.button) { color: var(--contrast); text-decoration: none; }
.nav a:not(.button):hover { color: var(--accent-two); }
.hero { padding: clamp(42px, 8vw, 92px) 0 24px; max-width: 900px; }
.eyebrow { color: var(--accent-dark); font-size: .9rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; }
.accent { color: var(--accent); }
.lead { color: var(--contrast-two); max-width: 760px; }
.guide { max-width: 920px; }
.guide hr { margin: 3rem 0 0; border: 0; border-top: 1px solid var(--base-three); }
.guide hr + h2 { margin-top: 1.4rem; }
.guide ul { padding-left: 1.3em; }
.guide li { margin: .45rem 0; overflow-wrap: anywhere; }
.guide code { background: var(--base-two); border: 1px solid var(--base-three); border-radius: 5px; padding: .08em .35em; }
.actions { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 28px; }
.button { display: inline-flex; align-items: center; justify-content: center; border: 0; border-radius: 8px; background: var(--accent); color: var(--base); font: 500 1.3rem "Work Sans", sans-serif; padding: .72em 1.1em; text-decoration: none; }
.button:hover { background: var(--accent-medium); color: var(--base); }
.button.secondary { background: var(--contrast); }
.logo-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(230px, 1fr)); gap: 18px; margin-top: 30px; }
.logo-card { min-width: 0; border: 1px solid var(--base-three); border-radius: 1.5rem; overflow: hidden; background: var(--base); }
.logo-preview { height: 210px; display: grid; place-items: center; padding: 22px; background-image: linear-gradient(45deg,var(--base-two) 25%,transparent 25%),linear-gradient(-45deg,var(--base-two) 25%,transparent 25%),linear-gradient(45deg,transparent 75%,var(--base-two) 75%),linear-gradient(-45deg,transparent 75%,var(--base-two) 75%); background-size: 24px 24px; background-position: 0 0,0 12px,12px -12px,-12px 0; }
.logo-preview.dark { background: var(--contrast); }
.logo-preview img { max-width: 100%; max-height: 164px; border-radius: 1.5rem; object-fit: contain; }
.logo-meta { padding: 15px; border-top: 1px solid var(--base-three); }
.logo-meta b { display: block; font-size: .9rem; overflow-wrap: anywhere; }
.logo-meta span { display: block; color: var(--contrast-three); font-size: .9rem; margin-top: 4px; }
.folder-grid { display: grid; grid-template-columns: repeat(auto-fit,minmax(230px,1fr)); gap: 14px; margin: 28px 0; }
.folder { display: block; padding: 20px; border-radius: 1.5rem; background: var(--base-four); border: 1px solid color-mix(in srgb,var(--accent) 35%,var(--base-three)); color: var(--contrast); text-decoration: none; font-weight: 700; }
.folder:hover { background: var(--accent); color: var(--base); }
.folder.recommended { background: var(--accent-two); border-color: var(--accent-two); color: var(--base); }
.folder.recommended:hover { background: var(--accent-two-dark); }
.folder-kicker { display: block; margin-bottom: 4px; color: var(--base); font-size: .9rem; font-weight: 500; letter-spacing: .08em; text-transform: uppercase; }
.notice { margin: 28px 0; padding: 18px 20px; border-radius: 1.5rem; background: var(--base-five); border-left: 5px solid var(--accent-two); }
.footer { margin-top: 60px; padding-top: 20px; border-top: 1px solid var(--base-three); color: var(--contrast-three); font-size: .9rem; }
@media(max-width:1050px){
  .header { align-items: flex-start; flex-direction: column; }
  .header img { width: min(330px, 65vw); }
  .nav { display: grid; grid-template-columns: repeat(5, max-content); justify-content: space-between; width: 100%; margin-left: 0; gap: 18px; }
}
@media(max-width:700px){
  .shell { width: min(100% - 24px, 1140px); padding-top: 28px; }
  .header { gap: 22px; padding-bottom: 26px; }
  .header img { width: min(300px, 76vw); }
  .nav { grid-template-columns: 1fr 1fr; gap: 6px 18px; }
  .nav a { display: flex; align-items: center; min-height: 48px; }
  .nav .button { grid-column: 1 / -1; width: 100%; margin-top: 6px; }
  .logo-grid { grid-template-columns: 1fr; }
  .logo-preview { height: 180px; }
}
"""


def linkify(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"(https?://[^\s<]+)", lambda m: f'<a href="{m.group(1)}">{m.group(1)}</a>', escaped)
    return re.sub(
        r"&quot;(/logos/[^<]*?)&quot;",
        lambda m: f'<a href="{html.escape(m.group(1).lstrip("/"))}">{m.group(1)}</a>',
        escaped,
    )


def promote_default_logo(lines: list[str]) -> list[str]:
    default_index = next((i for i, line in enumerate(lines) if line.startswith("- Default Logo:")), None)
    logos_index = next((i for i, line in enumerate(lines) if line.startswith("## Logos")), None)
    if default_index is None or logos_index is None:
        return lines
    first_bullet = next((i for i in range(logos_index + 1, len(lines)) if lines[i].startswith("- ")), None)
    if first_bullet is None or default_index == first_bullet:
        return lines
    default_line = lines.pop(default_index)
    lines.insert(first_bullet, default_line)
    return lines


def list_item(text: str) -> str:
    if text.startswith("Default Logo:"):
        path = text.partition(":")[2].strip()
        return f'<strong>Default Logo (recommended):</strong> {linkify(path)}'
    return linkify(text)


def markdown_body(source: str, *, omit_intro: bool = False) -> str:
    lines = source.splitlines()
    if omit_intro:
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and lines[0].startswith("# "):
            lines.pop(0)
        while lines and not lines[0].strip():
            lines.pop(0)
        if lines and not lines[0].startswith(("#", "- ")):
            lines.pop(0)

    lines = promote_default_logo(lines)
    out: list[str] = []
    in_list = False
    for raw in lines:
        line = raw.rstrip()
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append(f"<li>{list_item(line[2:])}</li>")
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if not line:
            continue
        if line.startswith("## "):
            out.append('<hr aria-hidden="true">')
            out.append(f"<h2>{html.escape(line[3:])}</h2>")
        elif line.startswith("# "):
            out.append(f"<h1>{html.escape(line[2:])}</h1>")
        else:
            out.append(f"<p>{linkify(line)}</p>")
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


def page(title: str, body: str, depth: int = 0) -> str:
    prefix = "../" * depth
    logo = f"{prefix}logos/digital/png/primary-logos/fl-logo-horizontal.png"
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)} · Fuel Logic</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Work+Sans:wght@400;500;700&display=swap" rel="stylesheet">
<style>{STYLE}</style></head><body><div class="topline"></div><div class="shell">
<header class="header"><a href="{prefix}"><img src="{logo}" alt="Fuel Logic"></a><nav class="nav"><a href="{prefix}">Brand guide</a><a href="{prefix}logos/">All logos</a><a href="{prefix}fl-brand-guide.md">Markdown</a><a href="https://github.com/Xammis/fl-brand-guide">GitHub</a><a class="button" href="https://github.com/Xammis/fl-brand-guide/tree/main/skills/fl-brand-guide">Install Skill</a></nav></header>
{body}<footer class="footer">Fuel Logic Brand Guide v1.0 · Public standards for people and AI agents</footer></div></body></html>'''


def build_home() -> None:
    body = f'''<section class="hero"><div class="eyebrow">Official standards · v1.0</div><h1>Fuel Logic <span class="accent">Brand Guide</span></h1><p class="lead">One public source for the people and AI agents creating Fuel Logic designs, documents, reports, and digital experiences.</p><div class="actions"><a class="button" href="logos/">Browse logos</a><a class="button secondary" href="fl-brand-guide.md">Open raw Markdown</a><a class="button secondary" href="https://github.com/Xammis/fl-brand-guide/tree/main/skills/fl-brand-guide">Install AI skill</a></div></section><article class="guide">{markdown_body(GUIDE.read_text(), omit_intro=True)}</article>'''
    (ROOT / "index.html").write_text(page("Brand Guide", body))


def file_card(path: Path, current: Path) -> str:
    rel = path.relative_to(current).as_posix()
    name = path.name
    suffix = path.suffix.lower()
    if suffix in {".png", ".webp"}:
        dark = " dark" if "white" in name or "dark-bg" in name else ""
        preview = f'<a class="logo-preview{dark}" href="{html.escape(rel)}"><img loading="lazy" src="{html.escape(rel)}" alt="{html.escape(path.stem)}"></a>'
        kind = suffix[1:].upper() + " digital logo"
    else:
        preview = f'<a class="logo-preview" href="{html.escape(rel)}"><span class="button">Open PDF</span></a>'
        kind = "PDF print logo"
    return f'<article class="logo-card">{preview}<div class="logo-meta"><b>{html.escape(name)}</b><span>{kind}</span></div></article>'


def folder_sort_key(directory: Path, child: Path) -> tuple[int, str]:
    if directory == LOGOS / "digital":
        digital_order = {"png": 0, "webp": 1, "compressed-for-web": 2, "alternate-logos": 3}
        return digital_order.get(child.name, 99), child.name
    return (1 if child.name == "alternate-logos" else 0), child.name


def folder_label(directory: Path, child: Path) -> str:
    if directory == LOGOS / "digital":
        return {
            "png": "PNG",
            "webp": "WEBP",
            "compressed-for-web": "Compressed",
            "alternate-logos": "Alternate Logos",
        }.get(child.name, child.name.replace("-", " ").title())
    if child.name in {"png", "webp", "pdf"}:
        return child.name.upper()
    return child.name.replace("-", " ").title()


def folder_link(directory: Path, child: Path) -> str:
    recommended = directory == LOGOS / "digital" and child.name == "png"
    class_name = "folder recommended" if recommended else "folder"
    kicker = '<span class="folder-kicker">Recommended</span>' if recommended else ""
    label = html.escape(folder_label(directory, child))
    return f'<a class="{class_name}" href="{html.escape(child.name)}/">{kicker}{label}</a>'


def build_directory(directory: Path) -> None:
    depth = len(directory.relative_to(ROOT).parts)
    dirs = sorted([p for p in directory.iterdir() if p.is_dir()], key=lambda p: folder_sort_key(directory, p))
    files = sorted([p for p in directory.iterdir() if p.is_file() and p.name not in {"index.html", "manifest.json"}], key=lambda p: p.name)
    crumbs = " / ".join(part.replace("-", " ").title() for part in directory.relative_to(ROOT).parts)
    folder_links = "".join(folder_link(directory, d) for d in dirs)
    cards = "".join(file_card(f, directory) for f in files)
    body = f'<section class="hero"><div class="eyebrow">Official assets</div><h1>{html.escape(crumbs)}</h1><p class="lead">Download approved Fuel Logic logo files. Filenames are lowercase and dash-separated for predictable use across teams and tools.</p></section>'
    if folder_links:
        body += f'<div class="folder-grid">{folder_links}</div>'
    if cards:
        body += f'<div class="logo-grid">{cards}</div>'
    if not folder_links and not cards:
        body += '<div class="notice">No files in this folder.</div>'
    (directory / "index.html").write_text(page(crumbs, body, depth))


def build_virtual_fallback() -> None:
    directory = LOGOS / "digital" / "alternate-logos"
    directory.mkdir(exist_ok=True)
    depth = len(directory.relative_to(ROOT).parts)
    body = '''<section class="hero"><div class="eyebrow">Fallback logos</div><h1>Digital Alternate Logos</h1><p class="lead">Choose the file format needed for dark backgrounds and unique placements.</p></section><div class="folder-grid"><a class="folder" href="../png/alternate-logos/">PNG alternate logos</a><a class="folder" href="../webp/alternate-logos/">WebP alternate logos</a></div>'''
    (directory / "index.html").write_text(page("Digital Alternate Logos", body, depth))


def main() -> None:
    build_home()
    for directory in sorted([LOGOS, *[p for p in LOGOS.rglob("*") if p.is_dir()]], key=lambda p: len(p.parts), reverse=True):
        build_directory(directory)
    build_virtual_fallback()


if __name__ == "__main__":
    main()
