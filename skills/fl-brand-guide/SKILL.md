---
name: fl-brand-guide
description: "Official Fuel Logic visual brand standards. MUST use for any Fuel Logic design, visual explanation, HTML report, document, presentation, webpage, email design, social graphic, video graphic, PDF, or other branded artifact. Applies across Pi, Codex, Claude Code, and other Agent Skills-compatible harnesses."
license: Proprietary Fuel Logic brand standards and assets
compatibility: Works in any harness that supports the Agent Skills standard; browser access is useful for public logo assets and the live guide.
metadata:
  brand: Fuel Logic
  version: "1.1"
  guide: https://xammis.github.io/fl-brand-guide/
---

# Fuel Logic Brand Guide

Use the official Fuel Logic standards for every Fuel Logic visual or designed artifact.

## Required first step

Before designing, read the canonical standards in:

```text
references/fl-brand-guide.md
```

That reference is the initial Fuel Logic-provided Markdown preserved unchanged. The public human- and agent-readable version is:

```text
https://xammis.github.io/fl-brand-guide/
```

Treat the guide as a hard brand constraint, not inspiration. Do not substitute a template's default fonts, colors, logo, or typography.

## Asset resolution

Paths beginning with `/logos/` in the canonical Markdown are relative to the brand-guide site. Resolve them against:

```text
https://xammis.github.io/fl-brand-guide
```

For portable HTML, use absolute public URLs. The default logo is therefore:

```text
https://xammis.github.io/fl-brand-guide/logos/digital/png/primary-logos/fl-logo-horizontal.png
```

Use only assets beneath the public logo library. Do not redraw, recolor, distort, crop, rotate, add effects to, or typeset a replacement for an official logo. Preserve its aspect ratio and transparent background.

## Core implementation tokens

Use these names when a format supports design tokens or CSS custom properties:

```css
:root {
  --fl-brand-primary: #A2CD3A;
  --fl-base: #FFFFFF;
  --fl-base-two: #F4F4F4;
  --fl-base-three: #E9E9E9;
  --fl-base-four: #EFF6DE;
  --fl-base-five: #ECF8FD;
  --fl-contrast: #414141;
  --fl-contrast-two: #7D7E7F;
  --fl-contrast-three: #A2A3A6;
  --fl-accent: #A2CD3A;
  --fl-accent-medium: #85B33A;
  --fl-accent-dark: #678C2B;
  --fl-accent-two: #ff8c57;
  --fl-accent-two-light: #FFA67D;
  --fl-accent-two-dark: #AC603C;
}
```

Use Work Sans from Google Fonts with the weights defined in the canonical guide. Default paragraph text is `1.3rem`. Use the guide's element-color assignments exactly.

## Global typography and layout rules

Apply these standards unless the user explicitly requests an exception:

- H1 line height: `0.9`.
- Nav Font: Work Sans 500, `font-size: 1.3rem`, `color: #414141`, with no underlining.
- Global links: do not underline links by default. Use another clear interaction cue, such as the approved link color and a distinct hover or focus state.
- Large boxes and images: use `border-radius: 1.5rem` by default.
- Box accents: do not place accent-colored borders across the top of boxes by default.
- Shadows: do not use soft or diffuse box shadows. Prefer spacing, borders, or contrasting approved surface colors to establish hierarchy.
- Punctuation: do not use em dashes. This means Unicode U+2014. Use commas, periods, colons, parentheses, or separate sentences instead. Use an em dash only when the user explicitly requests it.
- Section spacing: padding and margins between sections must feel spacious and never crowded. Use a consistent responsive spacing rhythm with clear separation between content groups.
- Surface contrast: never place a box over a background when both use the same color. For example, do not place a white box on a white background or a black box on a black background. Choose a different approved surface color, border treatment, or surrounding background so the box remains visually distinct.

Use this baseline when authoring CSS:

```css
h1 {
  line-height: 0.9;
}

a {
  text-decoration: none;
}

nav,
nav a {
  color: #414141;
  font-family: "Work Sans", sans-serif;
  font-size: 1.3rem;
  font-weight: 500;
  text-decoration: none;
}

.large-box,
.content-image {
  border-radius: 1.5rem;
}
```

Do not add `box-shadow` or a top accent border to the default box treatment.

## Visual Explainer integration

When creating a Fuel Logic report with `visual-explainer` or another HTML generator:

1. Read `references/fl-brand-guide.md` fresh before each pass.
2. Read the source content separately from the previous rendered report.
3. Generate a completely new HTML document from scratch. Never edit, restyle, or copy CSS/layout from the previous pass.
4. Preserve the source report's facts, sections, caveats, and meaning, but derive every visual decision only from the current brand guide and the content's information architecture.
5. Load Work Sans weights 400, 500, and 700 from Google Fonts.
6. Use the official logo, font sizes, palette, element colors, button typography, navigation treatment, H1 line height, radius, and spacing rules.
7. Override visual-explainer template fonts and palettes. Do not retain template-specific serif, teal, violet, neon, or unrelated brand treatments.
8. Remove default soft shadows, top accent borders on boxes, underlined links, and em dashes unless the user explicitly requested them.
9. Keep the page responsive, semantic, readable, spacious, and free of horizontal overflow.
10. Ensure every box contrasts with the background beneath it.
11. Publish through the required live-report workflow and return the verified public HTML link.

This fresh-pass rule makes brand-guide testing trustworthy: every edition reflects only the standards available for that pass, not accumulated manual tweaks.

## Design checklist

Before delivery, confirm:

- the artifact is recognizably Fuel Logic before reading the copy;
- Work Sans is the only primary type family;
- paragraph text defaults to `1.3rem` where the medium permits;
- H1 line height is `0.9`;
- navigation uses Work Sans 500 at `1.3rem`, `#414141`, with no underlining;
- headline and body colors use `Contrast`;
- emphasized headline words use `Accent` only;
- links use `Accent Two` without underlining by default;
- captions use `Contrast Three`;
- buttons use `Accent` backgrounds, `Base` text, Work Sans 500, and `1.3rem` text;
- large boxes and images default to a `1.5rem` radius;
- boxes do not use top accent borders or soft shadows by default;
- sections have spacious, uncrowded padding and margins;
- every box contrasts with the background beneath it;
- no em dashes appear unless the user explicitly requested them;
- an official logo is used at its correct aspect ratio;
- no unapproved colors or substitute logos were introduced;
- the canonical brand Markdown itself was not silently corrected or rewritten.
