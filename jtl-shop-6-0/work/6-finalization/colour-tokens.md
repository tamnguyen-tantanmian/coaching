# Colour Tokens — JTL-Shop 6.0 Storefront

Four roles the merchant sets. Primary and Secondary each generate a brand ramp; Background and Text are the two poles the neutral scale is mixed between. Nothing else is stored.

**Source of truth:** Figma boards *Colour tokens — Tangerine* and *Colour tokens — Indigo*.
Tangerine and Indigo are **two separate themes**, each storing its own four roles. They share the system — same roles, same ramp formula, same neutral mix — not the values. Shown side by side below as one specification against two sets of inputs.

---

## Layer 1 — Roles (merchant-set)

| Role | Tangerine | Indigo | Applies to |
| --- | --- | --- | --- |
| **Primary** | `#FF6633` | `#6366F1` | Fill only — button and chip backgrounds, active nav, focus ring. Never text or an icon on a light surface |
| **Secondary** | `#111827` | `#111827` | Fill only — secondary actions. Same rule |
| **Background** | `#FFFFFF` | `#FFFFFF` | The page ground |
| **Text** | `#111827` | `#111827` | Body copy and headings |

Only these four are stored. Everything below is computed at runtime, in **OKLCH** — never in sRGB, which gives muddy mid-tones and uneven steps.

```
Tangerine primary   L 69.8%  C 0.197  H  38°
Indigo primary      L 58.5%  C 0.204  H 277°
Secondary (both)    L 21.0%  C 0.032  H 265°
```

---

## Layer 2 — Brand ramps (generated)

Hue is held; lightness is pinned to a target; chroma scales relative to the base.

| Step | L target | Chroma | Tangerine | Indigo | Applies to |
| --- | --- | --- | --- | --- | --- |
| `primary-subtle` | 96.6% | × 0.10 | `#FFF0EB` | `#F1F3FF` | Tinted backgrounds — badge fill, selected row, hover wash |
| `primary-muted` | 84.2% | × 0.43 | `#FDB9A3` | `#BEC7FF` | Disabled fill, borders on tinted surfaces |
| `primary` | — | — | `#FF6633` | `#6366F1` | **Stored.** Button fill, active nav, focus ring |
| `primary-strong` | 54.3% | × 0.92 | `#C03B00` | `#595CD9` | Hover and pressed states, text links on background |
| `primary-deep` | 30.9% | × 0.44 | `#531C0A` | `#26295C` | Text and icons sitting on `primary-subtle` |

Secondary runs the identical formula on its own hue. Because Secondary is near-black in both of these themes, the guard compresses the dark end — `secondary-strong` comes out *darker* than the base, which is the correct hover for a dark button.

**The guard.** The lightness targets assume a mid-lightness base. If a merchant picks near-white or near-black, the targets compress toward their base instead of inverting the ramp.

---

## Layer 3 — Neutral scale (system-owned)

**Fixed values, identical in every theme. Not merchant-editable, and not derived from a brand role.** The mix column below records how the scale was originally derived from the Background → Text poles — it documents where the values came from, not a live computation.

| Token | Mix | Value | L · C · H | Applies to |
| --- | --- | --- | --- | --- |
| `neutral-white` | 0% | `#FFFFFF` | L 100.0% C 0.000 | The page ground — alias to Role/background |
| `neutral-01` | 2% | `#F9FAFA` | L 98.4% C 0.001 H 197° | Raised surfaces — cards, sheets, menus |
| `neutral-02` | 9% | `#E6E7E9` | L 92.8% C 0.003 H 265° | Decorative rules and card outlines. Carries no meaning, so no contrast floor |
| `neutral-03` | 45% | `#898E97` | L 64.5% C 0.015 H 262° | Input and control outlines. **Must clear 3:1** — the border is what identifies the field (WCAG 1.4.11) |
| `neutral-04` | 70% | `#4E5561` | L 44.8% C 0.022 H 261° | Placeholder, helper text, captions, timestamps |
| `neutral-black` | 100% | `#111827` | L 21.0% C 0.032 H 265° | Body copy and headings — alias to Role/text |

Identical in every theme, because the scale is system-owned. That is what makes a theme swap predictable: the only thing that moves between Tangerine and Indigo is the brand colour.

---

## Layer 4 — Status (system-owned)

Fixed values. Never derived from a brand role, never merchant-editable — red meaning error is a safety affordance, not a brand decision. **Identical in every theme**, not just these two.

| Token | Value | L · C · H | Applies to |
| --- | --- | --- | --- |
| `Status/info-bg` | `#D6E4FF` | L 91.7% C 0.040 H 264° | Banner and alert background |
| `Status/info` | `#0055FF` | L 53.3% C 0.260 H 263° | Badge and chip fill only |
| `Status/info-fg` | `#0041CD` | L 45.0% C 0.222 H 263° | Icons and coloured text |
| `Status/success-bg` | `#C5FCE8` | L 94.8% C 0.062 H 171° | Banner and alert background |
| `Status/success` | `#10C683` | L 73.0% C 0.163 H 160° | Badge and chip fill only |
| `Status/success-fg` | `#006641` | L 45.0% C 0.102 H 160° | Icons and coloured text |
| `Status/warning-bg` | `#FFF0C2` | L 95.6% C 0.061 H 92° | Banner and alert background |
| `Status/warning` | `#FFBF00` | L 84.0% C 0.172 H 84° | Badge and chip fill only |
| `Status/warning-fg` | `#6D5000` | L 45.0% C 0.092 H 84° | Icons and coloured text |
| `Status/error-bg` | `#FFDEDB` | L 92.7% C 0.037 H 24° | Banner and alert background |
| `Status/error` | `#F21C0D` | L 61.1% C 0.240 H 30° | Badge and chip fill only |
| `Status/error-fg` | `#A30300` | L 45.0% C 0.183 H 29° | Icons and coloured text |

**The rule that keeps this compliant:** a status solid is a **fill**, always with a computed label colour. Never an icon or text on a light surface — `#FFBF00` on white is 1.65:1. That job belongs to `-fg`.

---

## Contrast — checked pairings

| Pair | Used by | Tangerine | Indigo | Target |
| --- | --- | --- | --- | --- |
| text on background | Body copy | 17.74:1 | 17.74:1 | 4.5 |
| text-muted on background | Helper, captions | 7.51:1 | 7.51:1 | 4.5 |
| computed label on primary | Button label | 7.20:1 *(black)* | 4.70:1 *(black)* | 4.5 |
| white on primary-strong | Hover label | 6.04:1 | 5.31:1 | 4.5 |
| primary-deep on primary-subtle | Badge text | 12.30:1 | 12.23:1 | 4.5 |
| primary-strong on background | Text links | 6.04:1 | 5.31:1 | 4.5 |
| primary on background | Focus ring | 3.68:1 | 4.47:1 | 3 |
| border on background | Input outline | 3.29:1 | 3.29:1 | 3 |
| banner copy on each status-bg | Banner copy | 13.9 – 15.6:1 | 13.9 – 15.6:1 | 4.5 |
| each status-fg on background | Icons, coloured text | 7.0 – 8.2:1 | 7.0 – 8.2:1 | 4.5 |

Every pairing clears AA. **AA is guaranteed by construction** across any hue a merchant picks, because the generated steps sit at fixed lightness targets — the worst case for a label on any fill is 4.58:1. AAA is not reachable for button labels at any hue, and is not the standard: BFSG and EN 301 549 both reference WCAG 2.1 AA.

### Indigo's label resolves to black

`#6366F1` scores **4.70:1 with black** and **4.47:1 with white**, so black is the only one clearing AA at body size. This sits almost exactly on the crossover where neither choice has margin. White is defensible at 18px and above, where the bar drops to 3:1 — but that has to be a decision, not an accident.

---

## Implementation

```css
/* the four the merchant sets */
--primary: #ff6633;
--secondary: #111827;
--background: #ffffff;
--text: #111827;

/* brand ramps — same formula, own hue */
--primary-subtle: oklch(from var(--primary) 97% calc(c * 0.10) h);
--primary-muted:  oklch(from var(--primary) 84% calc(c * 0.43) h);
--primary-strong: oklch(from var(--primary) 54% calc(c * 0.92) h);
--primary-deep:   oklch(from var(--primary) 31% calc(c * 0.44) h);

/* neutral scale — mixed between the poles */
--neutral-01: color-mix(in oklab, var(--text)  2%, var(--background));
--neutral-02: color-mix(in oklab, var(--text)  9%, var(--background));
--neutral-03: color-mix(in oklab, var(--text) 45%, var(--background));
--neutral-04: color-mix(in oklab, var(--text) 70%, var(--background));
```

Or compute the same values in `resolveTheme` and inject them as `--t-*`, which fits ARC-17's existing token flow and avoids browser-support questions.

**Derived tokens are never written to `tokenOverrides`.** `Partial<ThemeTokens>` currently permits overriding any token, so this needs an `EditableTokens` subset type or write validation — otherwise the three-layer model is only a wish.

---

## Open items

1. **Figma cannot compute.** The brand and neutral hexes above are a snapshot of the formula on the default theme, not a live derivation. Treat the formula as the spec, not the literals.
2. **Neutral naming is positional.** `neutral-01…04` doesn't tell a developer when to reach for which — the "applies to" column does all that work. If FE finds it ambiguous in review, semantic names (`surface`, `divider`, `border`, `text-muted`) map one-to-one.
3. **Dark mode has nowhere to live.** `StoreCustomisation.tokenOverrides` is a single flat map with no mode axis, so a merchant's brand override applies to both light and dark unchanged. Blocks all dark-theme colour work — for whoever owns ARC-17.
