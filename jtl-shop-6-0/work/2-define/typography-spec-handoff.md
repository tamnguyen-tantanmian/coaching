# Typography Spec v2 — Storefront Text Tokens

**Version:** 2.0 · 30 Aug 2026 · supersedes v1 (7 tokens) and the 17-row PrimeVue role table
**Scope:** JTL-Shop 6.0 storefront default theme · feeds `[UI/UX] Create Themes Setting UI Page (AD)`, Workstream B
**Face:** Inter (heading + body), merchant-swappable

---

## 0. Why v2

Two typography specs were in circulation and they disagreed on h4, on whether an 18px step exists, on weights, and on h1 line height. The 17-row role table also carried duplicates: three tokens shared `12/16 bold`, two shared `14/18 bold`, and two encoded a component's height (`12/32`) as a text token.

v2 collapses to **12 tokens**, adds the one role e-commerce cannot ship without (price), and states one rule per decision so the set can be extended without a meeting.

**Headline changes**

| | v1 / role table | v2 |
|---|---|---|
| Token count | 7 / 17 | 12 |
| Body size | 14 | **16** |
| `text-base` primitive | 14 | **16** ⚠ breaking rename |
| Heading steps | h1–h4 / h1–h5 | display + h1–h4 |
| Price | — | `price-m`, `price-s` |
| Italic / breadcrumb / tag | tokens | modifiers |
| Line height | mixed px + ratio | ratio only |
| Weights | 400/600/700/800 | 400/600/700 |
| Mode switch | 768px | **1024px** (see §6) |

---

## 1. The token set

Semantic roles. This is the public API — components reference these, never the primitives in §2.

| Token | Desktop | Compact | Line height | Weight | Tracking | Applies to |
|---|---|---|---|---|---|---|
| `type.display` | 56 | 40 | 1.10 | 700 | −0.02em | Hero headline. One per page, or none |
| `type.h1` | 40 | 32 | 1.15 | 700 | −0.02em | Page title — PDP product name, PLP category name |
| `type.h2` | 32 | 24 | 1.20 | 700 | −0.02em | Section title inside a page |
| `type.h3` | 24 | 18 | 1.30 | 600 | 0 | Card title, block header, accordion header |
| `type.h4` | 18 | 16 | 1.40 | 600 | 0 | Sub-section, supporting line under a heading |
| `type.body` | 16 | 16 | 1.60 | 400 | 0 | Product copy, CMS pages, **input values** |
| `type.body-sm` | 14 | 14 | 1.50 | 400 | 0 | Dense UI, secondary copy, table cells |
| `type.caption` | 12 | 12 | 1.40 | 400 | 0 | Helper text, meta, breadcrumb, legal |
| `type.label` | 14 | 14 | 1.40 | 600 | 0 | Form labels, small buttons, filter chips, nav |
| `type.cta` | 16 | 16 | 1.20 | 600 | 0 | Primary / secondary button text |
| `type.price-m` | 24 | 24 | 1.20 | 700 | 0 | PDP price, cart total |
| `type.price-s` | 16 | 16 | 1.30 | 600 | 0 | Card price, line-item price |

### Computed line boxes

For visual verification only. The **ratio is the source of truth** — do not round these to a 4pt grid.

| Token | Desktop | Compact |
|---|---|---|
| `display` | 56 / 61.6 | 40 / 44 |
| `h1` | 40 / 46 | 32 / 36.8 |
| `h2` | 32 / 38.4 | 24 / 28.8 |
| `h3` | 24 / 31.2 | 18 / 23.4 |
| `h4` | 18 / 25.2 | 16 / 22.4 |
| `body` | 16 / 25.6 | 16 / 25.6 |
| `body-sm` | 14 / 21 | 14 / 21 |
| `caption` | 12 / 16.8 | 12 / 16.8 |
| `label` | 14 / 19.6 | 14 / 19.6 |
| `cta` | 16 / 19.2 | 16 / 19.2 |
| `price-m` | 24 / 28.8 | 24 / 28.8 |
| `price-s` | 16 / 20.8 | 16 / 20.8 |

### Two rules that justify the odd ones

**`body` is 16, not 14.** iOS Safari auto-zooms any input whose text is below 16px. At 14 every form on the storefront — search, address, checkout — jump-zooms on focus. 16 is also the comfortable reading floor for product descriptions and CMS pages. 14 remains available as `body-sm` for dense UI.

**Price is a token, not a styled body.** It carries a mandatory technical property: `font-variant-numeric: tabular-nums`. Without it, prices in a PLP grid do not align vertically and the PDP price visibly jitters when quantity changes. A token is the only place that property cannot be forgotten.

---

## 2. Primitives

Internal layer. PrimeVue spelling retained so the mapping survives.

| Primitive | Value | Used by |
|---|---|---|
| `text-xs` | 12 | caption |
| `text-sm` | 14 | body-sm, label |
| `text-base` | **16** | body, cta, price-s, h4 (compact) |
| `text-lg` | 18 | h4, h3 (compact) |
| `text-2xl` | 24 | h3, price-m, h2 (compact) |
| `text-3xl` | 32 | h2, h1 (compact) |
| `text-4xl` | 40 | h1, display (compact) |
| `text-5xl` | 56 | display |

> ⚠ **`text-base` changes from 14 → 16.** Any component already referencing `text-base` will grow 2px. Sweep before merging; do not silently reuse the name.

Eight steps, no `text-xl` (20). 20 sat two pixels from 18 and produced an invisible step. The ramp is deliberately gapped so every adjacent pair is visually distinguishable at arm's length.

---

## 3. Modifiers — not tokens

Applied on top of a token. Adding a token for each combination is what produced 17 rows from 9 distinct specs.

| Modifier | Value | Typical use |
|---|---|---|
| `case.upper` | uppercase | Badges, overlines |
| `ls.wide` | +0.08em | Always paired with `case.upper` |
| `num.tabular` | `tabular-nums` | Baked into both price tokens; also apply to quantities, order numbers, dates in tables |
| `deco.strike` | line-through | Compare-at price (+ muted colour) |
| `deco.underline` | underline | Inline links in body copy |
| `emphasis.italic` | italic | Editorial pull-quotes only |

**Overline recipe:** `caption` + `case.upper` + `ls.wide` + weight 600. Covers badges, tags, eyebrow labels, `NEW ARRIVAL`, `SALE`.

**Italic is never used for placeholders or helper text.** Synthesised obliques in fallback faces are a legibility problem, and italic placeholder text tests badly for anyone with low vision or dyslexia.

---

## 4. Weights

| Token | Value | Applied to |
|---|---|---|
| `fw.regular` | 400 | body, body-sm, caption |
| `fw.semibold` | 600 | h3, h4, label, cta, price-s, overline |
| `fw.bold` | 700 | display, h1, h2, price-m |

Three weights, not four. `fw.extrabold` (800) is dropped: it existed for one token, and each extra weight is 2 more font files per face across a merchant-swappable stack. `fw.medium` (500) stays excluded — nothing uses it.

**Fallback rule (new, required by the theme builder):** merchants can pick a face that ships no 600. Never let the browser synthesise. Resolve to the nearest available weight, rounding **up** (600 → 700), and surface a quiet notice in the font picker: *"This font has no Semibold — headings will use Bold."*

---

## 5. Faces

| Token | Applies to | Default |
|---|---|---|
| `font.heading` | display, h1–h4 | Inter |
| `font.body` | body, body-sm, caption, label, cta, price-m, price-s | Inter |

**Two faces, not four.** The theme panel currently offers four dropdowns (Body / Subheading / Heading / Accent). Recommend cutting to Heading + Body for MVP:

- `Subheading` has exactly one consumer (`h4`) — a whole webfont download for one token.
- `Accent` has **no** consumer at all. It is a control with nothing behind it.
- Each additional face costs 3 files (400/600/700) × 2 formats. Four faces is a ~400KB font budget before any content loads.

If `Accent` survives review, it must be bound to a defined set — the proposal is `display` + `h1` only — or it will be wired to something arbitrary during build.

---

## 6. Modes and the breakpoint

Two modes: **Default** (≥ 1024px) and **Compact** (< 1024px).

### Scaling rule

> On Compact, every heading drops **one step down the §2 ramp**. Body, body-sm, caption, label, cta and price do not scale.

That is the whole rule, and it is self-verifying — no multiplier, no rounding, no floor. `display` 56 → 40, `h1` 40 → 32, `h2` 32 → 24, `h3` 24 → 18, `h4` 18 → 16.

It replaces v1's "×0.75 rounded to nearest even", which did not reproduce v1's own table:

```
h1  56 × 0.75 = 42   v1 table said 36   ✗
h2  40 × 0.75 = 30   v1 table said 30   ✓
h3  32 × 0.75 = 24   v1 table said 26   ✗
h4  24 × 0.75 = 18   v1 table said 20   ✗
```

Prices do not scale because price is a conversion element, not a heading — shrinking it on the device where most traffic converts is the wrong trade.

### ⚠ Boundary moved 768 → 1024 — confirm

v1 switched type at 768px. `storefront-layout-system.md` concentrates its layout switch at **1024px** (8 → 12 columns, 16 → 24 gutter, 24 → 32 margin). With type at 768, the 768–1023 tablet band renders **desktop type inside a tablet grid** — a 56px hero across 8 columns at 24px margins, the tightest measure anywhere in the system.

Aligning both at 1024 removes that band. Mode names changed from Desktop/Mobile to **Default/Compact** so it is not misread as "phones only" — Compact covers phone *and* tablet.

**Decision needed** from whoever owns `storefront-layout-system.md` before Figma variables are built.

---

## 7. Units

Three properties, three units. Deliberate.

| Property | CSS | Figma | Reason |
|---|---|---|---|
| Font size | `rem` | px | Respects the browser's user font-size setting; hard px breaks accessibility zoom |
| Line height | **unitless** | % | Inherits as a ratio. `em` is a trap — a child re-inherits the parent's *computed* line height, not the ratio |
| Letter spacing | `em` | % | Scales with font size, so tracking stays proportional at every step |

Unitless and Figma's % are the same number (`1.60` = `160%`) — one value per token, not two. **Base:** `1rem = 16px`, so `type.display` = `3.5rem`, `type.body` = `1rem`.

### No fixed px line heights — this is a hard constraint now

The role table used `lineheight-fixed` (e.g. `14/18`, `12/32`). In a theme builder that is a defect, not a style choice: a px leading tuned to Inter's x-height breaks the moment a merchant selects Playfair, Noto Sans, or an uploaded face. Text line heights are ratios. Fixed heights belong to **components** (`nav-height`, button min-height, breadcrumb bar) and are specified in the layout system, not here.

This also resolves the v1 ambiguity where `text-m` (14/20 auto) and `label-m` (14/20 fixed) computed identically today and diverged the first time anything changed.

---

## 8. Component mapping

Exclusive assignments. If a surface is not listed, it inherits `body`.

| Surface | Token |
|---|---|
| Hero headline | `display` |
| PDP product name · PLP category title | `h1` |
| Section header ("Related products") | `h2` |
| Product card title · accordion header · tab | `h3` |
| Filter group title · supporting line | `h4` |
| Product description · CMS page body | `body` |
| Input value and placeholder | `body` |
| Spec table cell · footer link | `body-sm` |
| Form label · nav link · filter chip · small button | `label` |
| Helper text · error text · legal · cookie notice | `caption` |
| Breadcrumb parent | `caption` |
| Breadcrumb current page | `caption` + weight 600 |
| Badge · tag | `caption` + `case.upper` + `ls.wide` + 600 |
| Primary / secondary button | `cta` |
| PDP price · cart total | `price-m` |
| Card price · line-item price | `price-s` |
| Compare-at price | `price-s` + `deco.strike` + muted colour |

Breadcrumb active/disabled is a **colour and weight state**, not two type tokens. The old `12/32` came from the breadcrumb bar's 32px height — that lives in the layout system.

---

## 9. What the merchant may edit

Feeds Workstream B of the theme-setting ticket.

**Editable**

- `font.heading` and `font.body` (picker, upload, fallback stack)
- One global **scale multiplier**: S 0.9 · M 1.0 · L 1.1, applied to every size, rounded to whole px

**Not editable**

- Line-height ratios, per-token weights, tracking presets, the ramp itself, the compact-mode rule

**Why no per-step editing:** seven independent size fields let a merchant set h2 below h3. The hierarchy stops being a hierarchy, every downstream template breaks, and support absorbs it. One multiplier gives the same felt control — "bigger type" — while the ramp stays monotonic by construction.

---

## 10. Accessibility floor

- Minimum rendered size anywhere: **12px**. The old `tag-s` at 10/12 is removed.
- Input text ≥ 16px (see §1).
- Ratios must survive 200% browser zoom without clipping or horizontal scroll.
- Relevant for the German market: BFSG / EN 301 549 apply to this storefront.

---

## 11. Implementation

**One implementation only.** Build a `Typography` variable collection with two modes:

- `Default` — Desktop column
- `Compact` — Compact column

Switch at **1024px** (pending §6 confirmation). Bind text styles to the variables rather than duplicating styles per mode — a frame switched to Compact should reflow with no style swapping.

Do **not** also add fluid `clamp()` values. Modes and clamps disagree at every viewport between breakpoints, leaving the handoff with no single source of truth. FE consumes the exported tokens and hard-switches.

**Naming**, following `storefront-layout-system.md` §4:

```
storefront - type - h1 - size
  scope     property element attribute
```

Composite style: `storefront-type-h1`. Parts: `-size`, `-line`, `-weight`, `-tracking`.

---

## 12. Panel labels

The Style Reference preview prints its own spec labels. After this change:

- `DISPLAY · 56PX · TIGHT · BOLD` → Default; `· 40PX ·` on Compact
- `HEADING 1 · 40PX · TIGHT · BOLD` → `· 32PX ·`
- `HEADING 2 · 32PX · TIGHT · BOLD` → `· 24PX ·`
- `HEADING 3 · 24PX · NORMAL · SEMIBOLD` → `· 18PX ·`
- `HEADING 4 · 18PX · NORMAL · SEMIBOLD` → `· 16PX ·`
- `BODY · 16PX · NORMAL · REGULAR` → unchanged both modes
- `PRICE · 24PX · TABULAR` → unchanged both modes

**Open bug, still unfixed:** the mobile preview renders Default sizes — its top heading label reads the desktop value. Compact must read the Compact column.

---

## 13. Migration map

| Old token | v2 | Note |
|---|---|---|
| `h1` 56/64 | `display` | Was doing hero *and* module header — two jobs |
| `h2` 40/48 | `h1` | Page title is the real h1 |
| `h3` 32/40 | `h2` | |
| `h4` 20/28 | `h3` (24) | 20 was 2px from its neighbour |
| `h5` 14/18 | **removed** → `h4` (18) | Was body-sized; identical spec to `cta-m` |
| `cta-m` 14/18 | `cta` (16) | 14px label under-reads on a 44px target |
| `cta-s` 12/16 | **removed** → `label` | Identical to `label-s` and `tag-m` |
| `label-m` 14/20 | `label` | |
| `label-s` 12/16 | **removed** → `label` | Named `text-base`, valued 12. 12px form labels fail review |
| `text-m` 14/20 | `body` (16) | |
| `text-s` 12/16 | `caption` | |
| `accent-m` 14/20 italic | **removed** | Italic is a modifier |
| `accent-s` 12/16 italic | **removed** | |
| `bread-m` 12/32 | **removed** → `caption` + 600 | 12/32 = ratio 2.67 — component height in a text token |
| `bread-s` 12/32 | **removed** → `caption` | State, not token |
| `tag-m` 12/16 | **removed** → overline recipe | |
| `tag-s` 10/12 | **removed** | Below the 12px floor |
| — | `price-m` **new** | |
| — | `price-s` **new** | |

**17 → 12.**

---

## 14. Do not add

Additive later only against a named, shipped use case:

- `h5` / `h6` — nothing below 18 is a heading
- Any size under 12px
- Italic, breadcrumb, or tag tokens — modifiers cover them
- Fixed px line heights (§7)
- `fw.medium` (500), `fw.extrabold` (800)
- Per-component tokens (`type.card-title`, `type.checkout-label`) — this is how a 12-token set becomes 60

---

## 15. Open questions

1. **Mode boundary 768 or 1024?** (§6) — blocks the Figma variable build.
2. **Does `Accent` font survive?** (§5) — it currently has no consumer. Cut, or bind to display + h1.
3. **Is the scale multiplier in MVP?** (§9) — if not, merchants get faces only, and the panel needs one fewer control.
