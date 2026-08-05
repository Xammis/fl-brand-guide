# Fuel Logic Brand Guide

Public Fuel Logic brand standards, official logo assets, and a harness-agnostic Agent Skill for people and AI systems.

## Public guide

https://xammis.github.io/fl-brand-guide/

## Source of truth

- `fl-brand-guide.md` — the initial v1.0 standards supplied by Fuel Logic, preserved unchanged.
- `logos/` — official digital and print logo assets downloaded from the approved Dropbox collection.
- `logos/manifest.json` — original Dropbox paths, normalized public paths, file sizes, and SHA-256 hashes.
- `skills/fl-brand-guide/` — Agent Skills-compatible instructions for Pi, Codex, and Claude Code.
- `scripts/build-site.py` — deterministic static-site and logo-gallery builder.

## Asset naming

All published asset paths use lowercase filenames with dashes instead of spaces. The original Dropbox filename remains recorded in `logos/manifest.json` for traceability.

## Build

```bash
python3 scripts/build-site.py
```

GitHub Pages serves the repository root from `main`.

## Asset rights

Fuel Logic logo files are official proprietary brand assets. Public availability does not transfer ownership or grant permission for unrelated use.
