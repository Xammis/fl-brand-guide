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

## Install the Agent Skill

The canonical skill lives at `skills/fl-brand-guide/` and follows the Agent Skills standard.

### Shared cross-harness installation

```bash
git clone https://github.com/Xammis/fl-brand-guide.git ~/fl-brand-guide
mkdir -p ~/.agents/skills ~/.claude ~/.codex
ln -sfn ~/fl-brand-guide/skills/fl-brand-guide ~/.agents/skills/fl-brand-guide
ln -sfn ../.agents/skills ~/.claude/skills
ln -sfn ../.agents/skills ~/.codex/skills
```

- Pi discovers `~/.agents/skills/` globally.
- `~/.claude/skills` and `~/.codex/skills` both resolve to the complete shared `~/.agents/skills/` directory.
- Every harness sees one global skill collection, one version-controlled Fuel Logic skill, and one unchanged standards reference.

If either harness-specific path already exists as a real directory, migrate any unique skills into `~/.agents/skills/` before replacing it with the symlink. Reload or restart an already-running harness after installation.

## Build

```bash
python3 scripts/build-site.py
```

GitHub Pages serves the repository root from `main`.

## Asset rights

Fuel Logic logo files are official proprietary brand assets. Public availability does not transfer ownership or grant permission for unrelated use.
