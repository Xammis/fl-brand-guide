# Fuel Logic Brand Guide

Public Fuel Logic brand standards, official logo assets, and a harness-agnostic Agent Skill for people and AI systems.

## Public guide

https://xammis.github.io/fl-brand-guide/

## Single source of truth

`fl-brand-guide.md` is the only authored standards document. Every current Fuel Logic rule belongs there.

The deterministic build produces all other representations:

- `index.html` and logo-gallery pages from the canonical Markdown and logo manifest.
- `skills/fl-brand-guide/references/fl-brand-guide.md` as a byte-for-byte synchronized skill reference.
- `skills/fl-brand-guide/SKILL.md` as a procedural Agent Skills wrapper that points to the synchronized reference.

Supporting files:

- `logos/` contains the approved digital and print assets.
- `logos/manifest.json` preserves original Dropbox paths, normalized public paths, sizes, and SHA-256 hashes.
- `scripts/build-site.py` synchronizes the skill and generates the public site.
- `scripts/verify-sync.py` fails if any generated representation drifts.

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

## Edit, build, and verify

1. Edit only `fl-brand-guide.md` when changing standards.
2. Rebuild every generated representation.
3. Verify synchronization before committing.

```bash
python3 scripts/build-site.py
python3 scripts/verify-sync.py
```

Do not hand-edit `index.html`, `skills/fl-brand-guide/SKILL.md`, or the synchronized skill reference. GitHub Actions runs the same verification on every push and pull request. GitHub Pages serves the repository root from `main`.

## Asset rights

Fuel Logic logo files are official proprietary brand assets. Public availability does not transfer ownership or grant permission for unrelated use.
