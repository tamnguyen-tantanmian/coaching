# Storefront Layout System

Combined reference covering breakpoint tiers, the column grid, the spacing scale, and token resolution across breakpoints.

**Contents**

1. [Breakpoint Tiers](#1-breakpoint-tiers)
2. [Column Grid](#2-column-grid)
3. [Spacing Scale](#3-spacing-scale)
4. [Token Behavior per Breakpoint](#4-token-behavior-per-breakpoint)

---

## 1. Breakpoint Tiers

Defines the four responsive breakpoints used across the Storefront. Each tier maps to a viewport-width range, a target device class, and a recommended column grid.

### Tier Overview

| Tier | Range | Columns | Gutter | Margin |
|---|---|---|---|---|
| Mobile | 360 – 767 px | 4 | 16px | 16px |
| Tablet | 768 – 1023 px | 8 | 16px | 24px |
| Desktop | 1024 – 1439 px | 12 | 24px | 32px |
| Wide | 1440+ px | 12 | 24px | 48px |

### Breakpoint Range Diagram

Viewport widths map to each tier. Boundaries are inclusive on the left, exclusive on the right.

```
0        360        768       1024       1440       1920
         |───────────Mobile────────|
                    |──────Tablet──────|
                               |─────Desktop─────|
                                          |────Wide────▸
```

| Boundary | Meaning |
|---|---|
| 360px | Mobile floor — smallest supported viewport |
| 768px | Tablet breakpoint — switches to 8-col grid |
| 1024px | Desktop breakpoint — switches to 12-col grid |
| 1440px | Wide breakpoint — content max-width caps |

### Behavior at Boundaries

What happens at each breakpoint transition — layout shifts, grid changes, and component adaptations.

**Mobile → Tablet (at 768px)**

- Grid changes from 4 to 8 columns
- Side margins increase 16 → 24px
- Nav switches from bottom bar to sidebar
- Cards switch from stacked to 2-up grid

**Tablet → Desktop (at 1024px)**

- Grid changes from 8 to 12 columns
- Gutter increases 16 → 24px
- Sidebar becomes persistent (not collapsible)
- Typography scale shifts up one step

**Desktop → Wide (at 1440px)**

- Content area max-width caps at 1200px
- Side margins become auto (centered)
- No grid column change
- Hero sections can go full-bleed

### Device Coverage Matrix

| Device | Viewport | Tier | Columns | Gutter |
|---|---|---|---|---|
| iPhone SE | 375×667 | Mobile | 4 | 16px |
| iPhone 14 Pro | 393×852 | Mobile | 4 | 16px |
| iPad Mini | 768×1024 | Tablet | 8 | 16px |
| iPad Pro 11" | 834×1194 | Tablet | 8 | 16px |
| MacBook Air 13" | 1280×800 | Desktop | 12 | 24px |
| Desktop 1080p | 1920×1080 | Wide | 12 | 24px |
| Ultrawide | 2560×1440 | Wide | 12 | 24px |

---

## 2. Column Grid

The Storefront uses a responsive column grid that adapts columns, gutters, and margins per breakpoint tier. All layout content should align to these grid tracks.

### Grid Anatomy

Three core concepts:

- **Columns** — content tracks
- **Gutters** — gaps between columns
- **Margins** — outer spacing from the viewport edge

```
← Margin →   ← Columns + Gutters →   ← Margin →
```

### Grid Configuration per Breakpoint

| Tier | Range | Columns | Column width | Gutter | Margin |
|---|---|---|---|---|---|
| Mobile | 360–767px | 4 | 260px (fluid) | 16px (fixed) | 16px (fixed) |
| Tablet | 768–1023px | 8 | 120px (fluid) | 16px (fixed) | 24px (fixed) |
| Desktop | 1024–1439px | 12 | 66px (fluid) | 24px (fixed) | 32px (fixed) |
| Wide | 1440+px | 12 | 63px (fluid) | 24px (fixed) | 48px (fixed) |

### Common Layout Patterns

| Pattern | Spans | Description |
|---|---|---|
| Full-width hero | 12/12 | Hero banners, full-bleed images |
| Content + sidebar | 8 + 4 | Article page with right sidebar |
| 3-up card grid | 4 × 3 | Product cards, feature blocks |
| 2-up split | 6 × 2 | Comparison views, dual content |
| Centered content | 8 centered | Blog posts, forms |

---

## 3. Spacing Scale

A geometric spacing ramp (base 4 / 8) used for all margins, padding, and gaps. Tokens are referenced by t-shirt size.

### Scale Ramp

| Token | Value | Factor | Usage |
|---|---|---|---|
| XS | 4px | ×1 | Icon gaps, hairline separators |
| S | 8px | ×2 | Inline element gaps, tight card padding |
| M | 16px | ×4 | Default content spacing, card padding |
| L | 24px | ×6 | Section padding (mobile), form field gaps |
| XL | 32px | ×8 | Section padding (desktop), card group gaps |
| XXL | 48px | ×12 | Section padding (wide), page-level vertical rhythm |
| XXXL | 64px | ×16 | Hero vertical spacing, max breathing room |

### Spacing in Context

**Card component**

- `M` = 16px padding
- `M` = 16px gap between internal blocks

**Section spacing**

- `XL` = 32px between Section 1 and Section 2
- `XXL` = 48px between Section 2 and Section 3

**Inline & icon spacing**

- `S` = 8px between label text and icon
- `S` = 8px between stacked buttons (Primary / Secondary)
- `XS` = 4px for icon-internal gaps

### Scale Formula

**Base unit = 4px.** All spacing tokens are multiples of the 4px base unit, ensuring consistent vertical and horizontal rhythm.

```
XS ×1 · S ×2 · M ×4 · L ×6 · XL ×8 · XXL ×12 · XXXL ×16
```

---

## 4. Token Behavior per Breakpoint

Shows how each design token resolves differently across breakpoint tiers. Responsive tokens change value at each boundary; static tokens remain constant.

### Resolution Table

| Token | Mobile | Tablet | Desktop | Wide | Behavior |
|---|---|---|---|---|---|
| base-width | Full width | Full width | Bounded | Bounded | Responsive |
| grid-columns | 4 | 8 | 12 | 12 | Responsive |
| grid-gutter | 16px | 16px | 24px | 24px | Responsive |
| grid-margin | 16px | 24px | 32px | auto | Responsive |
| section-padding | 24px (L) | 24px (L) | 32px (XL) | 48px (XXL) | Responsive |
| content-gap | 16px (M) | 16px (M) | 16px (M) | 16px (M) | Static |
| card-padding | 16px (M) | 16px (M) | 16px (M) | 16px (M) | Static |
| nav-height | 56px | 56px | 64px | 64px | Responsive |
| hero-spacing | 32px (XL) | 48px (XXL) | 64px (XXXL) | 64px (XXXL) | Responsive |
| inline-gap | 8px (S) | 8px (S) | 8px (S) | 8px (S) | Static |

### Token Switching at 1024px

When the viewport crosses the 1024px boundary, several tokens change simultaneously.

| Property | Tablet (< 1024px) | Desktop (≥ 1024px) |
|---|---|---|
| Grid | 8 columns | 12 columns |
| Gutter | 16px | 24px |
| Margin | 24px | 32px |
| Section padding | 24px (L) | 32px (XL) |

### Token Naming Convention

Responsive tokens follow a structured naming pattern:

```
storefront - spacing - section - padding
  scope      property  element   attribute
```

**Examples**

- `storefront-spacing-section-padding` → L (24px) mobile, XL (32px) desktop
- `storefront-grid-column-count` → 4 mobile, 8 tablet, 12 desktop
- `storefront-grid-gutter` → 16px mobile/tablet, 24px desktop/wide
