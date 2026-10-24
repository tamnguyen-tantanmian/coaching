# Font Tokens — JTL-Shop 6.0 Storefront

Seven text styles, each pointing at one of four font slots. This is the shared contract between Figma, the front end, and the theme panel — one row per thing, three names for it.

**Source of truth:** Figma board *Font Token Mapping*.

---

## Layer 1 — Font slots

A slot holds a **family, not a weight**. Regular / Semibold / Bold are pulled from whatever family sits in the slot; a missing weight resolves upward with a notice, never a browser-synthesised one.

| Slot | Default | Selectable families (MVP) | Referenced by |
| --- | --- | --- | --- |
| **Heading** | Inter | Inter · Montserrat · Roboto · Playfair Display | H1, H2 |
| **Subheading** | Inter | Inter · Montserrat · Roboto · Playfair Display | H3, H4 |
| **Body** | Inter | Inter · Montserrat · Roboto · Playfair Display | Paragraph |
| **Special** | Inter | Inter · Montserrat · Roboto · Playfair Display | S1, S2 |

Every slot has at least one style pointing at it, so none ships as a dead control. Only referenced slots are downloaded.

---

## Layer 2 — Text styles (merchant-configurable)

`FE-DES` is the name the front end and design share. `Theme settings` is what the merchant sees in the panel.

| FE-DES | Description | Theme settings | Font slot | Size | Line height | Weight | Case |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `H1` | Headline 1 | H1 | Heading | 48 | 1.2 | 700 | Default |
| `H2` | Headline 2 | H2 | Heading | 32 | 1.2 | 700 | Default |
| `H3` | Headline 3 | H3 | Subheading | 24 | 1.4 | 600 | Default |
| `H4` | Headline 4 | H4 | Subheading | 20 | 1.4 | 600 | Default |
| `P1` | Paragraph 1 | Paragraph | Body | 16 | 1.5 | 400 | Default |
| `Span 1` | Special 1 | S1 | Special | 14 | 1.5 | 400 | Default |
| `Span 2` | Special 2 | S2 | Special | 12 | 1.5 | 400 | Default |

**A text style's font control selects a slot, never a family.** Changing a slot updates every style pointing at it, live; changing one style's control moves that style only.

---

## Layer 3 — Derived (no merchant controls)

System-managed, available in the default only. Not exposed as configurable settings.

| FE-DES | Description | Theme settings | Family | Size | Line height | Weight | Case |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `H5` | Headline 5 (= H3) | Default | Inter | 24 | 1.4 | 600 | Default |
| `H6` | Headline 6 (= H4) | Default | Inter | 20 | 1.4 | 600 | Default |
| `P2` | Paragraph 2 | Default | Inter | 14 | 1.5 | 400 | Default |
| `P3` | Paragraph 3 | Default | Inter | 12 | 1.5 | 400 | Default |
| `Cap` | Caption | Default | Inter | 11 | 1.5 | 400 | Default |

---

## Implementation notes

**Font pointers are stored as `var()` references** — `--type-h1-family: var(--t-font-heading)` — and must **never** be resolved to a literal family name at merge time. ARC-17's `resolveTheme` is a flat spread; a resolved literal silently breaks store-level rebranding.

**No fixed px line heights.** Merchants swap fonts; px leading tuned to one face breaks on another. Line heights are unitless ratios; fixed heights belong to components in the layout system.

**Weight is not a merchant control.** It comes from the style's role, resolved out of the slot's family.

---

## Open items

1. **`H5` duplicates `H3`, `H6` duplicates `H4`.** Deliberate — HTML needs a style for `<h5>` and `<h6>` even when they render identically to h3/h4. Worth stating in the FE docs so nobody "cleans up" the duplication.
2. **`Span 1` = `P2` and `Span 2` = `P3`** at the same values. Also deliberate: Span 1/2 are merchant-configurable, P2/P3 are system defaults that never move. Same default, different editability.
3. **No price token.** Price is the most brand-expressive element after the logo and carries a mandatory `font-variant-numeric: tabular-nums` — without it PLP prices misalign and the PDP price jitters on quantity change. Currently nothing in the set carries it. Either S1 becomes Price, or a derived `price` token is added.
4. **No `input` token.** iOS Safari auto-zooms any input under 16px. P1 at 16 covers it today, but if a merchant lowers P1 the guard disappears. A derived `input` token floored at 16 removes the risk.
5. **No `cta` token.** Button labels currently have no named style.
