#!/usr/bin/env python3
"""Verify that every generated brand artifact matches fl-brand-guide.md."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
GUIDE = ROOT / "fl-brand-guide.md"
REFERENCE = ROOT / "skills" / "fl-brand-guide" / "references" / "fl-brand-guide.md"
SKILL = ROOT / "skills" / "fl-brand-guide" / "SKILL.md"
BUILD = ROOT / "scripts" / "build-site.py"


def generated_files() -> list[Path]:
    return sorted([ROOT / "index.html", *ROOT.glob("logos/**/index.html"), SKILL, REFERENCE])


def snapshot(paths: list[Path]) -> dict[Path, bytes | None]:
    return {path: path.read_bytes() if path.exists() else None for path in paths}


def main() -> None:
    paths = generated_files()
    before = snapshot(paths)
    subprocess.run([sys.executable, str(BUILD)], cwd=ROOT, check=True)
    after = snapshot(generated_files())

    changed = [path.relative_to(ROOT) for path in sorted(set(before) | set(after)) if before.get(path) != after.get(path)]
    if changed:
        formatted = "\n".join(f"  - {path}" for path in changed)
        raise SystemExit(f"Generated brand artifacts were out of sync and have been rebuilt:\n{formatted}")

    if GUIDE.read_bytes() != REFERENCE.read_bytes():
        raise SystemExit("Skill reference does not match fl-brand-guide.md byte-for-byte")

    guide_text = GUIDE.read_text()
    page_text = (ROOT / "index.html").read_text()
    skill_text = SKILL.read_text()
    required = [
        "Default Logo (recommended)",
        "Digital logo menus appear in this order: PNG, WEBP, Compressed, Alternate Logos",
        "H1 line height: `0.9`",
        "Nav font: Work Sans, 500 at `1.1rem`",
        "Header button font: Work Sans, 500 at `1.1rem`",
        "Default item gap: `1.7rem`",
        "Navigation text color: `#414141`",
        "Do not underline links by default",
        "NEVER use Accent Medium or Accent Dark",
        "Official Standards tagline and similar eyebrow labels: Accent Two",
        "Large boxes and images use `border-radius: 1.5rem`",
        "NEVER place rounded boxes inside rounded boxes",
        "Do not place accent-colored borders across the top of boxes by default",
        "Do not use soft or diffuse box shadows",
        "Padding and margins between sections must feel spacious and never crowded",
        "Never place a box over a background when both use the same color",
        "Do not use em dashes unless the user explicitly requests them",
        "Download fl-brand-guide.md",
        "Point `~/.claude/skills` and `~/.codex/skills` to the shared `~/.agents/skills` directory",
        "Generate each report as a completely new document from scratch",
    ]
    for standard in required:
        if standard not in guide_text:
            raise SystemExit(f"Canonical guide is missing required standard: {standard}")

    headings = [line[3:] for line in guide_text.splitlines() if line.startswith("## ")]
    for heading in headings:
        if f"<h2>{heading}</h2>" not in page_text:
            raise SystemExit(f"Public page is missing canonical section: {heading}")
    if page_text.count('<hr aria-hidden="true">') != len(headings):
        raise SystemExit("Public page does not have exactly one horizontal rule per H2")
    if "download=\"fl-brand-guide.md\"" not in page_text:
        raise SystemExit("Public page is missing the Markdown download action")
    palette = page_text[page_text.index("<h2>Color Palette</h2>") : page_text.index("<h2>Element Colors</h2>")]
    if palette.index("Accent Two Dark:") > palette.index("Accent color note:"):
        raise SystemExit("Accent color note must follow the complete palette list")
    if "The canonical Markdown is the sole standards source" not in skill_text:
        raise SystemExit("Skill sync contract is missing")

    print("Brand guide page, Markdown, and skill are synchronized.")


if __name__ == "__main__":
    main()
