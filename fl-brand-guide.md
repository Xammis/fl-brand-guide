# Fuel Logic Brand Guide v1.3

Official Fuel Logic standards for people and AI agents creating designs, documents, reports, websites, presentations, email designs, social graphics, video graphics, PDFs, and other branded artifacts.

## Canonical Guide and Skill

- [Fuel Logic Brand Guide](https://xammis.github.io/fl-brand-guide/)
- [Download fl-brand-guide.md](https://xammis.github.io/fl-brand-guide/fl-brand-guide.md)
- [Install the Fuel Logic Agent Skill](https://github.com/Xammis/fl-brand-guide/tree/main/skills/fl-brand-guide)

## Logos

Use only official Fuel Logic logo assets. Preserve the original aspect ratio and transparent background. Never redraw, recolor, distort, crop, rotate, add effects to, or typeset a replacement for an official logo.

- [**Default Logo (recommended)**](https://xammis.github.io/fl-brand-guide/logos/digital/png/primary-logos/fl-logo-horizontal.png)
- [All Logos](https://xammis.github.io/fl-brand-guide/logos/)
- [Digital Logos](https://xammis.github.io/fl-brand-guide/logos/digital/)
- [Print Logos](https://xammis.github.io/fl-brand-guide/logos/print/)
- [Primary Logo Set](https://xammis.github.io/fl-brand-guide/logos/digital/png/primary-logos/)
- [Secondary Logo Fallbacks](https://xammis.github.io/fl-brand-guide/logos/digital/png/alternate-logos/)
- [Badge](https://xammis.github.io/fl-brand-guide/logos/digital/png/primary-logos/fl-logo-badge.png)
- [Fallback Logos](https://xammis.github.io/fl-brand-guide/logos/digital/alternate-logos/)

## Logo Library Presentation

- PNG is the recommended digital format
- Highlight the PNG menu item with Accent Two and place a small `Recommended` label above its title

## Fonts

- Paragraph and text font: Work Sans, 400
- Headline font: Work Sans, 700
- Button font: Work Sans, 500
- Header button font: Work Sans, 500 at `1.1rem`
- Nav font: Work Sans, 500 at `1.1rem`, color `#414141`, with no underlining
- Icons: [Font Awesome Icons Free](https://fontawesome.com/)

## Font Sizes and Line Height

- H1: `clamp(3.1rem, calc(3.1rem + ((1vw - .2rem) * 1.5)), 4rem)`
- H1 line height: `0.9`
- H2: `clamp(1.85rem, calc(1.85rem + ((1vw - .2rem) * 1.583)), 2.8rem)`
- H3: `1.5rem`
- H4: `1.3rem`
- H5: `1.3rem`
- H6: `1.3rem`
- Paragraph and text size: `1.3rem`
- Small text size: `0.9rem`
- Button text size: `1.3rem`
- Header button text size: `1.1rem`
- Nav text size: `1.1rem`

## Navigation

- Default item gap: `1.7rem`, approximately 50 percent more space than an 18px baseline
- Navigation text color: `#414141`
- Navigation links have no underlining

## Color Palette

- Brand Primary: `#A2CD3A` (Official Green, also Accent)
- Base: `#FFFFFF` (White)
- Base Two: `#F4F4F4` (Lighter Grey)
- Base Three: `#E9E9E9` (Light Grey)
- Base Four: `#EFF6DE` (Light Green)
- Base Five: `#ECF8FD` (Light Blue)
- Contrast: `#414141` (Matte Black)
- Contrast Two: `#7D7E7F` (Dark Grey)
- Contrast Three: `#A2A3A6` (Grey)
- Accent: `#A2CD3A` (Official Green, Brand Primary)
- Accent Medium: `#85B33A` (Medium Green)
- Accent Dark: `#678C2B` (Dark Green)
- Accent Two: `#ff8c57` (Orange)
- Accent Two Light: `#FFA67D` (Light Orange)
- Accent Two Dark: `#AC603C` (Dark Orange)

> **Accent color note:** NEVER use Accent Medium or Accent Dark unless absolutely necessary. Use either shade only as a fallback when Brand Primary or Accent creates a contrast issue. Do not use these darker greens for decoration, variety, labels, or routine hover states.

## Element Colors

- Text: Contrast
- Heading: Contrast
- Heading alternate color: Accent, only to highlight words or phrases for emphasis
- Background: Base
- Link: Accent Two
- Captions: Contrast Three
- Official Standards tagline and similar eyebrow labels: Accent Two
- Button background: Accent
- Button text: Base

## Links

- Do not underline links by default
- Use Accent Two for links
- Provide a clear hover or focus state without depending on an underline

## Buttons

- Default button font: Work Sans, 500 at `1.3rem`
- Header button font: Work Sans, 500 at `1.1rem`
- Default button background: Accent
- Default button text: Base

## Layout, Surfaces, and Spacing

- Large boxes and images use `border-radius: 1.5rem` by default
- Do not create an unnecessary amount of boxes nested inside other boxes
- NEVER place rounded boxes inside rounded boxes
- Do not place accent-colored borders across the top of boxes by default
- Do not use soft or diffuse box shadows
- Use spacing, approved borders, and contrasting approved surface colors to establish hierarchy
- Padding and margins between sections must feel spacious and never crowded
- Use a consistent responsive spacing rhythm with clear separation between content groups
- Never place a box over a background when both use the same color
- Do not place white boxes on white backgrounds or black boxes on black backgrounds
- Choose a different approved surface color, border treatment, or surrounding background so every box remains visually distinct

## Writing and Punctuation

- Do not use em dashes unless the user explicitly requests them
- Use commas, periods, colons, parentheses, or separate sentences instead

## Public Guide Presentation

- Generate the public guide directly from this Markdown
- Display the guide title and introductory paragraph once in the hero, without duplicating them in the standards body
- Keep the guide navigation usable on desktop, tablet, large phone, and small phone layouts

## Agent Skill Distribution and Synchronization

- `fl-brand-guide.md` is the sole standards source of truth
- Generate the public page from this Markdown
- Synchronize this Markdown byte-for-byte into `skills/fl-brand-guide/references/fl-brand-guide.md`

## Visual Explainer and Generated Reports

- Read this guide fresh before every Fuel Logic visual pass
- Read source content separately from any previous rendered report
- Generate each report as a completely new document from scratch
- Never edit, restyle, or copy CSS or layout from a previous pass
- Preserve source facts, sections, caveats, and meaning
- Derive every visual decision from this guide and the content's information architecture
- Override template fonts, palettes, shadows, accent borders, link treatments, radii, and spacing when they conflict with this guide
- Keep pages responsive, semantic, readable, spacious, and free of horizontal overflow
- Ensure every box contrasts with the background beneath it
- Publish reports through the required verified public Live Reports workflow
