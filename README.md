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
mkdir -p ~/.agents/skills ~/.claude/skills ~/.codex/skills
ln -sfn ~/fl-brand-guide/skills/fl-brand-guide ~/.agents/skills/fl-brand-guide
ln -sfn ~/.agents/skills/fl-brand-guide ~/.claude/skills/fl-brand-guide
ln -sfn ~/.agents/skills/fl-brand-guide ~/.codex/skills/fl-brand-guide
```

- Pi discovers `~/.agents/skills/` globally.
- Codex uses the shared Agent Skills location; the explicit symlink also supports installations expecting `~/.codex/skills/`.
- Claude Code receives the same canonical skill through `~/.claude/skills/`.
- Every harness resolves to one version-controlled skill and one unchanged standards reference.

Reload or restart an already-running harness after installation.

## Build

```bash
python3 scripts/build-site.py
```

GitHub Pages serves the repository root from `main`.

## Asset rights

Fuel Logic logo files are official proprietary brand assets. Public availability does not transfer ownership or grant permission for unrelated use.
