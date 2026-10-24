# Font Model Spec — Update Request

**For:** Claude Design
**Target:** Theme panel → Fonts + Text styles, in `4 design prototype/Admin Setting+ Theme Setup (update by AnhTruong).html`
**Direction chosen:** Option 3 — font slots with a `Custom…` escape hatch
**Companion specs:** `typography-spec-handoff.md` (v2 token set) · `ARC-17 Theme & Preset System` (token architecture)
**Rationale, if needed:** `1 discovery/how-merchants-pick-fonts.html`

---

## 1. What is wrong today

The panel has four font dropdowns and **no font control on individual heading levels**. A merchant who picks a display face for the hero gets that same face on product card titles, where it is too heavy. Their only remaining lever is size, so they shrink H3 to hide it and the heading scale stops being a scale.

The `Accent` slot has no consumer at all — a control that changes nothing.

Both are fixed by the same change: **give every text style a font control, and make that control point at a slot.**

---

## 2. The model

Three layers. Only the first two appear in the panel.

```
LAYER 1   FONT SLOTS (4)     Body · Subheading · Heading · Accent
                             each holds one font family
                                     ↑ pointed at by
LAYER 2   TEXT STYLES (5)    Paragraph · H1 · H2 · H3 · H4
                             font pointer + size + line height + tracking + case
                                     ↓ derives
LAYER 3   DERIVED            buttons · labels · badges · prices · captions
                             no controls, never shown
```

**A slot holds a family, not a weight.** The system pulls Regular / Semibold / Bold from whatever family the slot holds, mapped per token. If the family ships no Semibold, resolve **upward** to Bold and show a quiet note on the slot row: *"Inter Tight has no Semibold — those styles will use Bold."* Never let the browser synthesise a weight.

---

## 3. Fonts section — changes

Keep the four rows in their current order (Body, Subheading, Heading, Accent). Add to each row:

- The family name **rendered in that family**, as now
- A usage line beneath, small and muted: `Used by H1, H2` — or `Not used` when nothing points at it
- On a `Not used` row only: a **Remove** action that clears the slot

The usage line is doing the teaching. It is the only place the slot concept becomes visible, and without it a merchant has no way to understand why the dropdown in section 4 offers these four names.

---

## 4. Text styles section — new

Add below Fonts. Header: **Text styles**, with helper text beneath: *Sizes scale automatically for all screen sizes.*

Five groups in this order, each labelled with its name as a small heading:

| Group | Controls |
| --- | --- |
| Paragraph | Font · Size · Line height |
| H1 | Font · Size · Line height · Letter spacing · Case |
| H2 | Font · Size · Line height · Letter spacing · Case |
| H3 | Font · Size · Line height · Letter spacing · Case |
| H4 | Font · Size · Line height · Letter spacing · Case |

Paragraph deliberately has no letter spacing and no case — body copy needs neither, and offering them invites unreadable body text.

### Control specs

**Font** — a dropdown, not a font picker. Options, in order:

```
Body            Inter
Subheading      Inter
Heading         Inter
Accent          — not set —
────────────────────────
Custom…
```

Render each slot name in that slot's actual face, with the family name as secondary text on the right. An empty slot shows `— not set —` and is still selectable.

**Size** — a numeric stepper in px, clamped per style:

| Style | Min | Default | Max |
| --- | --- | --- | --- |
| Paragraph | 14 | **16** | 20 |
| H1 | 32 | **56** | 72 |
| H2 | 28 | **40** | 56 |
| H3 | 22 | **32** | 44 |
| H4 | 18 | **24** | 32 |

**Line height** — three segmented options. The value depends on the style's role:

| | Tight | Normal | Loose |
| --- | --- | --- | --- |
| H1–H4 | 1.10 | 1.20 | 1.35 |
| Paragraph | 1.40 | 1.60 | 1.80 |

**Letter spacing** — three segmented options: Tight `−0.02em` · Normal `0` · Loose `+0.04em`

**Case** — two segmented options: Default · Uppercase

Show the numeric value in a tooltip on hover for every relative step. Merchants do not need it; whoever files a bug does.

### Defaults on first load

| Style | Font | Size | Line height | Tracking | Case |
| --- | --- | --- | --- | --- | --- |
| Paragraph | Body | 16 | Normal | — | — |
| H1 | Heading | 56 | Tight | Normal | Default |
| H2 | Heading | 40 | Tight | Normal | Default |
| H3 | Heading | 32 | Normal | Normal | Default |
| H4 | Heading | 24 | Normal | Normal | Default |

All four slots default to Inter, so the panel looks unchanged until the merchant diverges.

---

## 5. The `Custom…` flow

This is the only genuinely new mechanism. Build it exactly.

**Selecting `Custom…`** opens the font family picker (search, grouped Recommended / Google / System / Uploaded, names rendered live).

**On choosing a family**, three things happen at once:
1. The family is filed into the first free slot, in the order **Accent → Subheading →** any slot nothing points at
2. The text style's font pointer is set to that slot
3. An inline note appears under the dropdown: *"Canela added to the Accent font slot."* with an **Undo** link. Auto-dismiss after 6 seconds; Undo reverses both the slot assignment and the pointer.

The note is not optional. Filing a family into a named slot silently is invisible magic, and the merchant will not find it later in the Fonts section.

**When all four slots are in use**, `Custom…` still opens the picker, with a banner pinned at the top:

> All four font slots are in use. Pick one of them below, or free a slot in **Fonts** above.

In this state the picker lists only the four families already in slots. Selecting one points at that slot. This is where the cap becomes visible, and it is the right moment for it — not on first load.

**Freeing a slot:** a slot with no text style pointing at it shows `Not used` plus **Remove** in the Fonts section (section 3). Removing clears the family and makes the slot available to `Custom…` again.

---

## 6. Behaviour

- Changing a slot's family in the Fonts section updates **every** text style pointing at it, live in the preview. This is the payoff of the whole model — make sure the prototype demonstrates it.
- A text style whose font differs from its default shows a small reset affordance on the row.
- Hierarchy warning: if a heading's size is set at or below the level beneath it, show an inline caution on that row — *"H2 is smaller than H3."* Warn, never block. Agencies occasionally want it.
- No mobile size controls anywhere. Sizes are fluid (section 7).

---

## 7. Fluid sizing

The merchant sets one number. The responsive value is computed, never authored:

```
min  = base × 0.75      for base ≥ 24px
min  = base             for base < 24px  (Paragraph never shrinks)
size = clamp(min, fluid between 360px and 1024px viewport, base)
```

Against the defaults: 56→42, 40→30, 32→24, 24→18, and Paragraph holds at 16.

Paragraph stays at 16 at every width because iOS Safari auto-zooms any input below 16px, and input values use the Paragraph style.

---

## 8. Derived — build no controls for these

`body-sm` (Paragraph × 0.875) · `caption` (max(12, Paragraph × 0.75)) · `label` · `cta` · `price-m` · `price-s` · internal `h5` (H4 × 0.75).

Prices carry `font-variant-numeric: tabular-nums`. If the specimen shows a price, it must be tabular — misaligned prices in a column are the visible symptom of getting this wrong.

---

## 9. Style Reference specimen — update

The centre preview currently shows two heading rows (56px, 32px). Update to match the new set:

- `DISPLAY · 56PX · TIGHT · BOLD`
- `HEADING 1 · 40PX · TIGHT · BOLD`
- `HEADING 2 · 32PX · TIGHT · BOLD`
- `HEADING 3 · 24PX · NORMAL · SEMIBOLD`
- `HEADING 4 · 18PX · NORMAL · SEMIBOLD`
- `PARAGRAPH · 16PX · NORMAL · REGULAR`
- `PRICE · 24PX · TABULAR`

**Known bug to fix:** the mobile preview renders desktop sizes — its top heading label reads the desktop value. Mobile must render the fluid minimum from section 7.

Note the panel labels H1–H4 while the specimen labels Display + H1–H4. That is intentional: the panel's H1 drives the internal `display` token. If this reads as confusing in the built prototype, say so — it is the one naming decision I am unsure about.

---

## 10. Token naming

Follow `storefront-layout-system.md` §4: `storefront-type-h1-size`, with parts `-size`, `-line`, `-weight`, `-tracking`.

Font pointers are stored as CSS `var()` references — `--font-h3: var(--t-font-slot-body)` — and **must never be resolved to a literal family name**. ARC-17's `resolveTheme` is a flat spread; a resolved literal silently breaks store-level rebranding.

---

## 11. Out of scope

Not part of this update: the colour panel, AI theme setup, save/publish states, the theme list in the left rail. Do not change them.

---

## 12. Terminology

**Text styles**, not "text presets". In ARC-17 a *preset* already means a theme's named token variation. The Shopify reference screenshots say "text presets"; ours do not.
