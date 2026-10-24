# Theme Editor — Theme Settings

JTL-Shop 6.0 · Storefront theming · Design documentation

---

## 1. Context

### 1.1 The platform

JTL-Shop 6.0 ships as two applications against one data layer.

| Application | Audience | Purpose |
| --- | --- | --- |
| **Admin Dashboard** | Merchant, shop staff | Runs the shop — catalogue, orders, customers, content, and the appearance of the storefront |
| **Storefront** | Shopper | The public shop. Every pixel of it is produced from configuration held in the Admin Dashboard |

The storefront has no design surface of its own. A merchant never edits storefront markup or CSS; they change values in the Admin Dashboard and the storefront re-renders from those values. The tool that holds those values is the **Theme Editor**.

### 1.2 The Theme Editor

The Theme Editor is one tool with **two scopes**.

> **On the wording.** "Layer" is already used inside the token model (slots → styles → derived), and "function" understates it. The two halves are distinguished by *how far a change reaches*, which makes **scope** the accurate term: one edits the whole shop, the other edits one thing. Suggested labels in the UI: **Theme Settings** and **Theme Builder**, with the relationship described as global scope vs. composition scope.

| Scope | Name | What a merchant changes | Reach of one change |
| --- | --- | --- | --- |
| **Global** | **Theme Settings** | The shop's design foundation — colour roles, text styles, and the theme's identity and version history | Every page, every section, every component at once |
| **Composition** | **Theme Builder** | Page structure and content — which sections appear on a page, in what order, and the settings of each section, block, and item inside it | Only the object being edited |

They are not alternatives. **Theme Settings defines the vocabulary; Theme Builder composes with it.**

The two are not symmetrical, and the asymmetry is deliberate:

| In the Theme Builder | Can reference a token | Can take a literal value |
| --- | --- | --- |
| **Colour** | Yes — any colour token | **Yes** — a raw hex can be entered directly |
| **Type** | Yes — a text style | **No** — a font family cannot be typed in |

**Colour has an escape hatch. Type does not.** A section can take a hex because some colours genuinely belong to one block and should *not* follow the brand — a seasonal banner, a campaign strip, a partner logo lockup. Type has no equivalent field because families are loaded as web fonts: a family named inside a section would either fail to render or force a download the theme never planned for. Text carries a token reference, always.

The consequence is the thing to hold on to: **what is expressed as a token survives a rebrand; what is typed as a literal does not.** Change Primary in Theme Settings and every token reference across every page moves at once. A hand-typed hex does not move — it sits there until somebody finds it.

That is the trade the hex field buys: local freedom now, a manual sweep later. So the working rule for design and content is **reference by default, and reach for the hex field only when the colour is deliberately outside the brand** — not when it merely happens to match today.

```
Theme Settings
    └─▶ tokens (colour roles, text styles)
           │
           ▼
Theme Builder
    └─▶ Section ─▶ Block ─▶ Item
           │   each references tokens,
           │   never literals
           ▼
      Storefront
```

**Scope of this document: Theme Settings.** The Theme Builder is documented separately.

---

## 2. Flow and logic

### 2.1 Flow

#### Page anatomy

Three regions, fixed widths on the two side panels.

| Region | Contents | Behaviour |
| --- | --- | --- |
| **Theme rail** (left) | `THEMES` list — one row per installed theme with its active preset (*Tangerine · Default*, *Indigo · Default*) | Selecting a row loads that theme into the preview and the config panel |
| **Preview** (centre) | Rendered storefront page, plus a page selector | **Read-only.** Not an editor — no click-to-select, no inline editing. That behaviour belongs to the Theme Builder |
| **Config panel** (right) | The full configuration tree for the selected theme | Every control writes to the working copy, never straight to live |

The page selector (Home page · Default page · Product page · Cart · Check out · Login / Register · Account settings) changes **what the preview renders**, not what is being edited — the configuration is theme-wide. The preview pulls the latest saved version of the selected page, so content edited elsewhere in the admin appears here without republishing the theme.

#### Version model

A theme carries **one draft** plus **up to five saved versions**. The default theme, as shipped, already counts as Version 1.

| Row action | Available on | Result |
| --- | --- | --- |
| **Reset** | any version | Loads that version into the default of the selected theme. **Does not make it applicable** |
| **Delete** | any unbadged version | Removes it from the stack, freeing a slot |
| **Apply** | latest version only | Publishes it to the storefront |

An older version therefore cannot go live directly. The path is **Reset → Save as new version → Apply that new version.** This is deliberate: the storefront is only ever fed from the top of the stack, so nobody can quietly publish something that sits behind newer work.

#### Protected versions

Two versions in the list are doing a job right now, and both are marked with a badge on their row.

| Badge | Marks | There is |
| --- | --- | --- |
| **Live** | The version currently published to the storefront | Exactly one, always |
| **Active** | The version loaded in the current Theme Builder working session | At most one |

A version can carry **both badges at once** — the usual case, where the merchant is working on the same version that shoppers are seeing. It shows `Live` and `Active` together rather than either one alone.

**Neither badged version can be deleted.** `Delete` is disabled on those rows, not merely warned about: deleting the live version would leave the storefront rendering something with no entry in the list, and deleting the active one would cut the working session out from under the merchant.

#### Save and apply

```
Start
 └─ default theme = Version 1
      │
      ├─▶ Apply this theme
      │      └─ toast "Theme applied successfully"
      │         [Open in editor]
      │
      └─▶ Make changes
             │
             ├─▶ Save as Draft
             │      └─ overwrites the existing draft
             │
             └─▶ Save as Version
                    ├─ "Saved as Version X"
                    │
                    └─ at 5 of 5
                         └─▶ "Exceed 5 versions limitation"
                                ├─ [Cancel] ......... no write
                                └─ [Save anyway] .... drops the
                                     oldest unbadged version,
                                     saves as the next number
```

**Save as Draft** is a split button; the caret opens *Save as Version*. The draft is a single scratch slot — never live, and overwritten without a confirm.

**Apply publishes. Save records.** Applying never creates a version.

#### Version numbering

At five of five, saving another version drops the oldest. It does **not** renumber the survivors — the counter only ever climbs, and a number, once used, is never reused.

| Save | Stack after | Dropped |
| --- | --- | --- |
| Version 5 | 1 · 2 · 3 · 4 · 5 | — |
| Version 6 | 2 · 3 · 4 · 5 · 6 | Version 1 |
| Version 7 | 3 · 4 · 5 · 6 · 7 | Version 2 |

So a full stack is not necessarily `1…5`; after a while it reads `12…16`. The dropdown always shows five rows, but the numbers on them are history, not positions. Because the drop is destructive and not undoable, the confirmation modal is mandatory — the cap must never be enforced silently.

**A version still doing a job is never dropped.** The version live on the storefront is marked `Live`; the version applied in the Theme Builder is marked `Active`. Neither is ever removed — if the oldest version carries either badge it stays where it is, and the oldest version with no badge goes in its place.

---

### 2.2 Colour settings

**Four roles are merchant-set. The neutral scale and the status set are system-owned. Nothing else is defined yet.**

| Role | Tangerine | Indigo | Applies to |
| --- | --- | --- | --- |
| **Primary** | `#FF6633` | `#6366F1` | Fill only — button and chip backgrounds, active nav, focus ring |
| **Secondary** | `#111827` | `#111827` | Fill only — secondary actions |
| **Background** | `#FFFFFF` | `#FFFFFF` | The page ground |
| **Text** | `#111827` | `#111827` | Body copy and headings |

**Tangerine and Indigo are two separate themes**, listed as separate rows in the theme rail and each holding its own four stored roles. They are not two modes of one theme, and a merchant does not switch between them inside a theme — they select one.

What they share is the **system**, not the values: the same four roles, the same neutral scale, the same status set. That is why the table above can sit side by side — it is one specification shown against two sets of inputs, and any third theme fills the same four cells.

#### Scope: brand variants are not defined yet

**Primary and Secondary are each a single stored value.** No `-subtle`, `-muted`, `-strong` or `-deep` step is specified at this stage, and none should be built.

This is a scope decision, not an omission: the variant set is easier to get right once real components are using the base colours and the actual demand for each step is visible, rather than specified up front and then bent to fit.

What it defers, and what fills the gap in the meantime:

| Needs a variant | Currently resolves to |
| --- | --- |
| Button hover and pressed | To be decided — see note 3 |
| Disabled fill | `neutral-02` |
| Tinted background — badge, selected row | `neutral-01` |
| Text link colour | `Text`, differentiated by underline rather than hue |

When the variant set is defined, it will be **generated from the stored value, not hand-picked** — held hue, pinned lightness, scaled chroma, computed in **OKLCH**, which is perceptually uniform. sRGB and HSL are not usable for this: in HSL, "50% lightness" is a bright yellow and a dark blue at the same number. Generating rather than hand-picking is what keeps a merchant's own brand colour accessible without anyone checking it by hand.

#### System-owned colours

Two sets sit outside the merchant's reach entirely. They are **fixed values, identical in every theme** — not derived from a brand role, not editable, not part of what a merchant is choosing when they pick a theme.

**Neutral scale** — the greys that carry structure rather than brand.

| Token | Applies to |
| --- | --- |
| `neutral-01` | Raised surfaces — cards, sheets, menus |
| `neutral-02` | Decorative rules and card outlines. Carries no meaning, so no contrast floor |
| `neutral-03` | Input and control outlines. **Must clear 3:1** — the border is what identifies the field |
| `neutral-04` | Placeholder, helper text, captions |

**Status** — twelve tokens in four families (info / success / warning / error), each as `-bg` / solid / `-fg`. Red meaning error is a safety affordance, not a brand decision, so it cannot move with the theme.

The rule that keeps status compliant: a status solid is a **fill**, always paired with a computed label colour — never an icon or text on a light surface. `#FFBF00` on white is 1.65:1.

Keeping both sets fixed is what makes a theme swap predictable: **changing a theme moves the brand colours and nothing else.** Structure, legibility and meaning stay where they are.

#### Accessibility

Every pairing in the defined set clears **WCAG 2.1 AA**.

For a **label on a brand fill**, AA holds for any colour a merchant picks, without anyone checking: whichever of black or white contrasts better with a given fill is never worse than **4.58:1**. The label colour is therefore computed from the fill, never stored — that one rule is what makes merchant-chosen brand colours safe.

AAA is not reachable for button labels at any hue, and is not the target: BFSG and EN 301 549 both reference AA.

---

### 2.3 Text styles settings

**Seven configurable text styles, each pointing at one of four font slots.**

#### Layer 1 — Font slots

A slot holds a **family, not a weight**.

| Slot | Default | Referenced by |
| --- | --- | --- |
| **Heading** | Inter | H1, H2 |
| **Subheading** | Inter | H3, H4 |
| **Body** | Inter | Paragraph |
| **Special** | Inter | S1, S2 |

Selectable families at MVP: Inter · Montserrat · Roboto · Playfair Display. Every slot has at least one style pointing at it, so none ships as a dead control, and only referenced slots are downloaded.

#### Layer 2 — Text styles (merchant-configurable)

| FE-DES | Theme settings | Font slot | Size | Line height | Weight |
| --- | --- | --- | --- | --- | --- |
| `H1` | H1 | Heading | 48 | 1.2 | 700 |
| `H2` | H2 | Heading | 32 | 1.2 | 700 |
| `H3` | H3 | Subheading | 24 | 1.4 | 600 |
| `H4` | H4 | Subheading | 20 | 1.4 | 600 |
| `P1` | Paragraph | Body | 16 | 1.5 | 400 |
| `Span 1` | S1 | Special | 14 | 1.5 | 400 |
| `Span 2` | S2 | Special | 12 | 1.5 | 400 |

**A text style's font control selects a slot, never a family.** Changing a slot updates every style pointing at it, live; changing one style's control moves that style only. This indirection is what lets a merchant set two families for the whole shop in two clicks, and still override one level if they want to.

#### Layer 3 — Derived

`H5` (= H3), `H6` (= H4), `P2`, `P3`, `Caption`. System-managed, not exposed as controls. `H5`/`H6` duplicating `H3`/`H4` is deliberate — HTML needs a style for `<h5>` and `<h6>` even when they render identically.

#### Implementation constraints

- **Font pointers are stored as `var()` references**, never resolved to a literal family at merge time. A resolved literal silently breaks store-level rebranding.
- **No fixed px line heights.** Merchants swap fonts; px leading tuned to one face breaks on another. Line heights are unitless ratios.
- **Weight is not a merchant control.** It comes from the style's role, resolved out of the slot's family.

---

## 3. Summary

The whole of Theme Settings rests on three ideas:

1. **A small editable surface, a fixed frame around it.** Four colour roles and four font slots are everything a merchant sets. Neutrals and status are system-owned, label colours are computed from the fill they sit on, and per-style families come from a slot. This is what makes accessibility provable rather than checked case by case, and a rebrand a four-value edit.
2. **Reference, never literal.** Sections and components hold token references. The moment a literal hex or family name is written into a component, the theme stops being a theme.
3. **Publishing is always forward.** Apply publishes, Save records, and only the newest version can be applied — so nothing behind current work can be pushed to shoppers by accident. What is live is marked, not inferred, and it cannot be deleted while it is serving.
