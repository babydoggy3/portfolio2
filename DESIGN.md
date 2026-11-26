---
name: Claude Daigan · Projects (portfolio2)
description: A signal-box mimic panel in which every project is a numbered route from input to output.
colors:
  enamel: "#cdd5c7"
  enamel-hi: "#d8dfd2"
  gridline: "rgb(30 44 28 / 0.075)"
  ink: "#121512"
  ink-2: "#384236"
  plate: "#161916"
  plate-2: "#232823"
  plate-text: "#eef1e8"
  plate-dim: "#b9c1b4"
  lamp: "#fbfbf2"
  occupied: "#e2392f"
  available: "#49c968"
  push: "#f4c62f"
  push-rim: "#9a7608"
  sheet-paper: "#f4f6f1"
typography:
  display:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(2.35rem, 7.4vw, 6rem)"
    fontWeight: 800
    lineHeight: 0.92
    letterSpacing: "-0.02em"
    fontVariation: "'wdth' 125"
  headline:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.05rem, 2vw, 1.35rem)"
    fontWeight: 800
    lineHeight: 1.1
    letterSpacing: "0.05em"
    fontVariation: "'wdth' 125"
  title:
    fontFamily: "Archivo, sans-serif"
    fontSize: "clamp(1.45rem, 2.6vw, 2.1rem)"
    fontWeight: 800
    lineHeight: 1.08
    letterSpacing: "-0.01em"
    fontVariation: "'wdth' 118"
  body:
    fontFamily: "Archivo, sans-serif"
    fontSize: "1.0625rem"
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: "B612 Mono, monospace"
    fontSize: "0.75rem"
    fontWeight: 400
    lineHeight: 1.3
    letterSpacing: "0.06em"
rounded:
  chip: "3px"
  panel: "6px"
  bezel: "10px"
  pill: "999px"
spacing:
  tile: "24px"
  sm: "0.75rem"
  md: "1.25rem"
  pad: "clamp(1rem, 4vw, 3rem)"
  section: "clamp(3.5rem, 8vw, 6.5rem)"
components:
  push-button:
    backgroundColor: "{colors.push}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: "0.8rem 1.4rem"
    height: "3.25rem"
  plate-button:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.plate-text}"
    rounded: "{rounded.chip}"
    padding: "0.6rem 1rem"
    height: "2.75rem"
  ghost-button:
    textColor: "{colors.ink}"
    rounded: "{rounded.chip}"
    padding: "0.6rem 1rem"
    height: "2.75rem"
  plate-label:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.plate-text}"
    rounded: "{rounded.chip}"
    padding: "0.5rem 0.85rem"
  station-chip:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.plate-text}"
    rounded: "{rounded.chip}"
    padding: "0.45rem 0.55rem"
  vdu-bezel:
    backgroundColor: "{colors.plate}"
    rounded: "{rounded.bezel}"
    padding: "0.9rem 0.9rem 0"
---

# Design System: Claude Daigan · Projects

## Overview

**Design North Star: "The Signal Box"**

The page is a railway signal-box mimic panel, not a website wearing a theme. A pale enamel board with a printed 24px mosaic grid carries black track strips; each of the eleven projects is a numbered route drawn left to right from what goes in to what comes out, with station plates along the track. Setting a route lights it: a white centre line appears in steps, the station borders light one after another, and a red occupancy block runs the length of the track. The panel is the argument — the whole network is visible at once, so a recruiter can read eleven projects in one glance instead of scrolling a stack of cards.

Everything is either printed on enamel or mounted on it. Printed things are Archivo, black on green-grey, with no container except the page itself. Mounted things are black traffolyte plates with engraved ivory caps in B612 Mono: the name bar, section headings, station labels, buttons, the route numbers, the legend. One control is illuminated — the yellow Email push button — and it is the only warm colour on the board. The result is calm, instrument-like and slightly industrial: dense with information, quiet in colour, and legible at a glance because the structure (IN → stations → OUT) repeats eleven times. Motion is the panel doing its job, not decoration: light arrives in discrete steps, because a lamp is either lit or not, and the one sustained movement — the auto-route cycle — can be stopped.

**Key Characteristics:**
- Enamel board + 24px printed tile grid as the page, never a dark background.
- Black track strips, white route lamps, one red occupancy block: the schematic is the layout.
- Two typefaces only: Archivo (voice) and B612 Mono (labels, numbers, plates).
- Round route-number badges as the only repeated circle besides lamps.
- One yellow push button per viewport, for Email.
- Stepped, relay-like motion; a complete still panel under reduced motion.

## Colors

A pale grey-green enamel field, near-black equipment, and three signal colours that each mean exactly one thing.

### Primary
- **Panel Black** (#121512): all text printed on enamel, every keyline, every track strip, and the fill of mounted plates. Green-tinted near-black, never pure #000.
- **Illuminated Yellow** (#f4c62f): the Email push button only — hero and contact. Its rim (#9a7608) is the button's thickness, not a shadow colour.

### Secondary
- **Route Lamp White** (#fbfbf2): the lit centre line inside a track, the lit ring around a route number, lamp dots in captions. Warm off-white, never #fff.
- **Occupied Red** (#e2392f): the occupancy block that runs a set route, and the "Running" legend swatch. Never used for emphasis, errors or badges.
- **Available Green** (#49c968): the single availability lamp in the status plate. Never decorative.

### Neutral
- **Pale Enamel** (#cdd5c7) and **Rack Enamel** (#d8dfd2): page board, and every raised enamel surface (panel, junction diagram, toggle knob).
- **Mosaic Gridline** (rgb(30 44 28 / 0.075)): the 24px printed grid, two 1px linear-gradients on the body.
- **Traffolyte Black** (#161916, hover lift #232823): every mounted plate, chip and button.
- **Engraved Ivory** (#eef1e8): text on plates.
- **Dim Silkscreen** (#b9c1b4): secondary text on plates — captions, timestamps, the email line.
- **Engraved Grey-Green** (#384236): secondary text on enamel — notes, IN/OUT values, dates.
- **Sheet Paper** (#f4f6f1): certificate wells and the SVG spreadsheet symbol.

### Named Rules
**The Two Lamps Rule.** Green means available, red means occupied/running. No third status colour, no colour-coded technology logos, no red for emphasis.

**The Yellow Belongs to Email Rule.** The yellow appears on the primary action and nowhere else; one yellow element per viewport, and it always says Email.

**The Enamel Is the Page Rule.** Black is equipment mounted on enamel, never the page behind it. A full-bleed dark section breaks the world.

## Typography

**Display Font:** Archivo (variable, 400–800 weight, 100–125% width; `assets/fonts/archivo-var.woff2`)
**Body Font:** Archivo (same file)
**Label/Mono Font:** B612 Mono 400/700 (`b612-mono-400.woff2`, `b612-mono-700.woff2`)

**Character:** One grotesque carries every sentence; one technical mono carries every label, number, date and plate. Both are self-hosted and preloaded with `font-display: block`, so the panel never reflows into a fallback mid-read. The mono is slightly narrow and mechanical — it reads as engraving, not as code.

### Hierarchy
- **Display** (800, clamp 2.35–6rem, 0.92): the name only, uppercase, width axis 125%, `width: min-content` so it breaks into two stacked lines.
- **Headline** (800, clamp 1.05–1.35rem, 1.1): section plates ("Projects", "About me", "Work experience") in mono-adjacent caps on black, letter-spaced 0.05em. The contact headline is the exception at clamp 1.8–3.6rem.
- **Title** (800, clamp 1.45–2.1rem, 1.08): project names in case sheets; sheet cards step down to clamp 1.15–1.4rem at 112% width.
- **Body** (400, 17px / 1.55, 16px at ≤30rem): paragraphs capped at 62ch in case sheets, 60ch in About, 52ch for section notes.
- **Lede** (400, clamp 1.1–1.375rem, 1.4, 36ch): the one-sentence thesis under the name.
- **Label** (B612 Mono 400/700, 11–13px, 0.02–0.12em, uppercase): status bar, nav, IN/OUT terminals, station chips, tags, captions, dates, footer.

### Named Rules
**The Plate Speaks Mono Rule.** Anything mounted on black is B612 Mono in caps. Anything printed on enamel is Archivo. A sentence in mono on enamel or a sans-serif label on a plate is the tell that the world has slipped.

**The Expanded Name Rule.** The width axis is used for hierarchy, not decoration: 125% on the name and section plates, 118% on case titles, 112% on card titles and the push button, 100% for all body text.

## Layout

A single centred column, `min(100% - 2 × pad, 86rem)` with `pad: clamp(1rem, 4vw, 3rem)`. The hero is a top strip (status plate left, section nav right) over a two-column block: the name at `min-content` width, and a side stack (role, lede, actions) aligned to its baseline. Everything below is a section with `padding-block: clamp(3.5rem, 8vw, 6.5rem) 0` and a plate heading in a flex head row.

The mimic panel is one instrument, not eleven cards: a 2px keyline box at 6px radius whose list rows are a five-column schematic grid — `2.5rem` number / `15rem` name / `10.5rem` IN / `1fr` track / `11.5rem` OUT — with 0.9rem gaps and every other row tinted 22% white. Case sheets below repeat the same reading order in two columns (`5fr / 7fr`), text left, screenshot right, stacked with `clamp(3.5rem, 8vw, 6rem)` between them. The Sheets systems sit under a full-width junction diagram and a two-column card grid (wide card spans both). About is `7fr / 5fr`; the service record is `12rem / 18rem / 1fr` with hairline rules; certificates are `auto-fill minmax(15.5rem, 1fr)`; contact is a black plate at `1fr auto`.

Breakpoints: **68rem** — routes reflow to two columns (number, then name/track/terminals), hero, case and about go single-column; **47rem** — the horizontal junction SVG is swapped for a vertical one, sheets and contact stack, the four-node chain turns vertical; **30rem** — body drops to 16px, the nav and legend hide, station chips tighten, buttons stretch to fill.

### Named Rules
**The Left-to-Right Rule.** Every route reads IN on the left and OUT on the right, and every station is lit in that order. Nothing on the panel flows right-to-left, and the vertical mobile diagrams keep the same top-to-bottom order.

**The One Panel Rule.** The eleven projects live inside one keylined panel. Adding a twelfth means a twelfth row, never a second panel or a card grid beside it.

## Elevation & Depth

Hybrid, and deliberately so: enamel is printed flat, controls are mounted proud, screens cast a soft shadow. The hard bottom edge on a button is the object's own thickness in a darker shade of its own material (yellow button → `#9a7608` rim; black plate → `#000`), it never exceeds 5px, and it collapses when the control is pressed because the object travels down. Screens (VDU bezels) and the panel itself get long, low-contrast ambient shadows instead. There is no blur-glass, no glow except the lamp ring, and no floating element without a keyline.

### Shadow Vocabulary
- **Plate / panel mount** (`inset 0 1px 0 rgb(255 255 255 / 0.08), 0 1px 2px rgb(0 0 0 / 0.25)`; the panel adds `inset 0 2px 0 rgb(255 255 255 / 0.5), 0 10px 28px rgb(20 30 18 / 0.18)`): every plate, the status bar, the mimic panel and the junction diagram.
- **Control thickness** (`0 3px 0 #000, 0 4px 8px rgb(0 0 0 / 0.2)`): black plate buttons at rest; on `:active` the offset goes to 0 and the button moves down 3px.
- **Push thickness** (`0 4px 0 #9a7608, 0 6px 12px rgb(0 0 0 / 0.22)`): the yellow Email button; `:active` drops to `0 0 0` and travels 4px.
- **Screen cast** (`0 16px 34px rgb(18 26 16 / 0.28), inset 0 1px 0 rgb(255 255 255 / 0.08)`): VDU bezels, 40px for the inset pair.
- **Lamp ring** (`inset 0 -3px 0 rgb(0 0 0 / 0.5), 0 0 0 3px var(--enamel-hi), 0 0 0 5px rgb(18 21 18 / 0.25)`): route-number badges; the ring turns lamp-white when set.

### Named Rules
**The Thickness Rule.** A hard offset is material, not decoration: same-hue darker, ≤5px, on a control that physically depresses. Offset shadows in ink or accent hues under text, cards or headings are not part of this world.

## Shapes

Rectangles with small corners: 3px for plates, chips, tags and buttons; 4px for route rows and SVG junction plates; 6px for structural containers (panel, case cards, sheets, contact plate, ID card, diagram); 10px for VDU bezels and chain nodes. Pills (999px) are reserved for the push button and the auto-route switch; circles for lamps, the toggle knob and the route-number badge. Borders do the work — 2px ink on every container, 1.5px on tags, 1px on nav pills and 30% hairlines. Tracks are 8px black strips with a 1px radius: no dashed rails and no arrows on the line; direction is carried by the IN/OUT labels and the occupancy run.

## Components

### Buttons
Character: physical panel controls — a plate you could press, with a visible edge.
- **Push (primary):** yellow, pill, 2px ink border, 3.25rem min-height, uppercase Archivo 800 at 112% width, letter-spaced 0.04em, icon left. Hover lifts 1px and deepens the cast; `:active` travels 4px and the edge collapses.
- **Plate (secondary):** black traffolyte, 3px radius, 2.75rem min-height, 13px mono, inset highlight plus 3px black edge; hover fills `#232823`.
- **Ghost (tertiary):** transparent with a 2px ink border and no shadow; hover inverts to a black plate. On the contact plate its border is `#b9c1b4` and its focus ring yellow.
- **Focus:** 3px ink outline at 3px offset everywhere; yellow on black.

### Chips
- **Station chips:** black plates, 3px radius, 1px plate border, 11px mono, 0.45/0.55rem padding. Lit state is a lamp-white border only — never a fill.
- **Tags ("Built with"):** 1.5px ink border, 3px radius, 25% white fill, 12px mono, no hover; they are a spec list, not buttons.
- **Route numbers:** 2.5rem circle (3rem in case heads), 3px inset bottom, double ring; the numeral turns lamp-white and the ring lights when the route is set or hovered.

### Cards / Containers
- **Mimic panel:** 2px ink keyline, 6px radius, raised enamel, 20px padding, inner top highlight. Head row: plate heading, legend, auto-route switch.
- **Case sheet / sheet card:** the case sheet has no fill — two columns on enamel, separated by space, the screenshot carrying the weight. The sheet card is a 2px ink box at 6px radius on 20% white, 1–1.5rem padding, link row pushed down with `margin-top: auto` so cards end level.
- **Certificate card:** 2px ink border, 6px radius, clipped image well at 400:283 on `#f4f6f1`; the whole card is the link target via a full-inset `::after`.
- **Contact plate:** black plate, 6px radius, `clamp(1.75rem, 5vw, 3.5rem)` padding, headline left and stacked actions right; the yellow push gains a double ring (4px plate, 6px 35% yellow) because it sits on black.

### Navigation
A mono status plate (green lamp, "Available", location, live PHT clock) on the left, five nav pills on the right: 1px ink border at 35%, 3px radius, 12px uppercase mono, 0.06em. Hover inverts to a black plate. Section headings themselves are plate anchors; at ≤30rem the nav is hidden and the plate headings do the navigating.

### Signature: the route row
The world's core component and the only place motion is authored. Track (8px strip) with station chips spaced along it, `--i` index per chip, IN and OUT terminals flanking it in 10px caps plus 12px values.
- **Hover / focus-within / `.is-set`:** the white centre line scales in over 640ms in `steps(8, end)`; each station border lights after `var(--i) × 150ms + 120ms`; the route number ring turns lamp-white.
- **`.is-run`:** a 2.75rem red occupancy block traverses the track in 1.7s (`cubic-bezier(0.45, 0, 0.35, 1)`, 0.55s delay).
- **Auto-route:** the switch is hidden until JS idles, then cycles one route every 2.6s; it pauses on row hover, when the panel is <20% visible or the tab is hidden, and its `aria-pressed` switch stops it. It never starts under `prefers-reduced-motion`.
- **Scroll-driven (progressive):** VDU bezels and the chain diagram rise 2.5rem and settle to scale 1 on entry; the chain lamp draws in 10 steps; the junction's white routes draw via `stroke-dashoffset`. All gated behind `animation-timeline: view()` support and `no-preference`.

### Signature: the junction diagram
A code-drawn SVG mimic of the Sheets systems: spreadsheet rectangles with cell rules, black track paths with white lamp paths on top, black plates for Apps Script and the directory, three output plates for routes 07–09. Two hand-built viewBoxes (1200×370 horizontal, 360×600 vertical) swap at 47rem; nothing is scaled below legibility.

### Signature: the operator record
Skills are ten numbered black plates in one list, mono numerals, one line each. The service record is a ruled table — mono dates, sans job titles, 12px dash bullets — the one place dense text is allowed, because a recruiter reads it as a CV, not a poster.

## Do's and Don'ts

### Do:
- **Do** draw every project as a route with named IN and OUT terminals, numbered in the same order as the panel (01–11).
- **Do** keep the 24px enamel grid visible behind all content, and mount labels, numbers, dates and status on black plates with mono caps at 3px corners.
- **Do** light routes in steps (150ms stagger, `steps()` easing) and let the red block be the only thing that travels.
- **Do** put every screenshot inside a black VDU bezel at 10px radius with a lamp-dot caption naming the live demo.
- **Do** keep body text on enamel at 17px/1.55 with 36–62ch measures; the panel is dense, not cramped.

### Don't:
- **Don't** put a kicker or eyebrow line above a heading; the plate heading is the label and the name is the headline.
- **Don't** add a dark full-bleed section, neon glow, scanlines, CRT curvature, or a terminal window chrome — the world is an enamel panel, not an IDE.
- **Don't** round a rectangle past 10px, or use pills for anything but the Email push and the auto switch.
- **Don't** colour-code technologies, add gradients or glass, or introduce a fourth signal colour beyond green/red/yellow.
- **Don't** animate lamp light with a smooth fade or bounce, or loop it for attention; only the auto-route cycle repeats, and it must be stoppable.
- **Don't** place a sans-serif label on a plate or a mono paragraph on enamel; the material decides the typeface.
- **Don't** invent metrics, hero copy or a second yellow element to fill space; empty enamel is on-world.
