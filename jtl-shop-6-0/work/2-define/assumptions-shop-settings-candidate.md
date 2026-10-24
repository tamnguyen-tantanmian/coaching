# Candidate Assumptions — Shop Settings (JTL-Shop 6.0)

**Scope:** the per-shop administration area — *Shop Admin shell* (products, categories, content, configuration, per-shop roles, per-shop payment) and *Settings* (regional, checkout, catalogue, status, storefront pages).
**Date:** 18 Sep 2026
**Numbering:** B1–B10. The A-series in `shop-setup-candidate-assumptions.md` covers guided setup and theme setup; these are deliberately non-overlapping.
**Status:** candidates for prioritisation. None validated.

**Sources read**
- Figma board *Tam-Analyze-Session* → section **Shop settings** (4 screens, 18 Sep 2026)
- `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` — §6.3, §6.4 multi-tenancy and inheritance, §9.1 regional/tax/B2B requirements
- `5 test/audit-findings-log.md` — watch-outs W1 (data origin), W2 (scope), W3 (compliance)
- `2 define/storefront-checkout-ui-brief.md` — where settings toggles surface on the buying flow
- `2 define/assumptions/shop-setup-candidate-assumptions.md` — the A-series

## What the new screens commit to

Two of the four screens are new since the August audit, and both respond to it.

**Shop Admin shell** — Products (42 items) · Categories (18) · Content (6 pages) · Configuration. Below: *Roles & 2FA (this shop)* — "3 members assigned · graduated permissions inherited from global roles" — and *Payment (this shop)* — "Overrides the global payment defaults for this shop only", carrying an **Inherits global** badge.

**Settings** — "Shop-specific configuration, pages and domains for this shop only."

| Group | Controls |
|---|---|
| Regional | Currency `USD · EUR · GBP` · Language `English · German · French` |
| Checkout | Tax included in prices *(on)* · Guest checkout *(on)* |
| Catalog | Inventory tracking *(on)* · Product reviews *(on)* · Wishlist *(off)* |
| Status | Maintenance mode *(off)* — "Temporarily take this storefront offline" |
| Pages | Storefront pages — page title + template, Create page |

The scope language the audit asked for is now present — *this shop*, *Inherits global*, *inherited from global roles*. What is still absent: any legal or consent group, and any indication of when WaWi data last arrived.

Numbers in the signals are placeholders. Set real thresholds against Shop 5.0 baselines before testing.

---

## User assumptions

### B1 — Merchants override rather than rebuild
We believe **merchants running more than one storefront** will **configure a new shop by overriding a handful of global defaults rather than setting it up from scratch**, because **the "this shop" framing and the *Inherits global* badge make the relationship between the two levels legible at the moment of change**. We'll know we're right when **the median shop shows two or fewer overridden sections, and merchants can answer "where does this value come from?" correctly for a given setting in a comprehension task**.

- *Type:* User · *Evidence:* the new per-shop framing on both screens; §6.4 (60–80% shared core, file inheritance principle); audit W2.2
- *Test:* count overridden sections per shop; comprehension task on a settings page with mixed inherited and overridden values

### B2 — Toggles get flipped without checking the storefront
We believe **merchants** will **flip catalogue and checkout toggles without previewing the storefront**, because **a toggle reads as reversible and the screen shows no consequence — nothing next to *Wishlist* or *Guest checkout* says what disappears from the buying flow**. We'll know we're right when **session data shows toggles flipped and reverted inside one session, and fewer than a third of merchants can predict the storefront change before flipping**.

- *Type:* User · *Evidence:* the checkout brief notes the wishlist heart sits on every product card while the Pflichtenheft marks it non-MVP, and that guest checkout removes an entire card from the identify step — neither consequence is visible here
- *Test:* moderated "what will this do?" task per toggle; instrument flip-and-revert rates
- *Note:* this is the settings-side version of the audit's no-undo finding. A toggle is reversible; its effect on a live storefront may not be.

---

## Problem assumptions

### B3 — The difficulty is level, not volume
We believe **multi-shop operators** will **make mistakes about which level a value lives at rather than about the value itself**, because **the audit found inheritance invisible on every screen, and the platform's whole reuse model depends on that distinction being clear**. We'll know we're right when **in eight moderated sessions, more than half of settings errors are wrong-level changes rather than wrong-value changes**.

- *Type:* Problem · *Evidence:* audit W2.3/W2.4 rated *Needs fixing* on the theme editor; §6.4
- *Test:* code settings errors by type in usability sessions; look for the same in support tickets

### B4 — Merchants assume compliance is handled
We believe **DACH merchants** will **assume the platform has taken care of legal configuration**, because **Settings presents Regional, Checkout, Catalog and Status with no legal group at all, and "Tax included in prices" reads like *the* tax decision**. We'll know we're right when **most merchants, asked what makes this shop legally ready to sell in Germany, point at the tax toggle or say "the platform does it", and fewer than one in four name consent management, legal notice, right of withdrawal and unit pricing**.

- *Type:* Problem · *Evidence:* §9.1 requires all four for DE; audit W3.1/W3.5/W3.6 rated *Needs fixing*; the checkout brief's own warning — "the project's own audit already found compliance elements missing from the merchant setup flow — do not repeat it on the buying flow"
- *Test:* the question above, verbatim, in eight interviews. Cheap, and the answer decides whether a legal group is MVP

### B5 — One tax boolean won't survive a real catalogue
We believe **merchants with real DACH catalogues** will **need a tax setting that "Tax included in prices" cannot express**, because **the spec requires reduced rates, tax exemptions, OSS automatic calculation, CH and GB input tax, and gross B2C alongside net B2B in the same tenant**. We'll know we're right when **more than 30% of pilot merchants hit a tax case the toggle cannot express within their first month, and support tickets name reduced rates or net pricing**.

- *Type:* Problem · *Evidence:* §9.1 Taxes and B2B Logic; §6.4's own worked example — one merchant running gross B2C and net B2B storefronts from one WaWi
- *Test:* take ten representative JTL catalogues and try to express their tax treatment with the current control

---

## Solution assumptions

### B6 — A short fixed list covers the MVP cohort
We believe **shops created in the first quarter** will **be served by the three currencies and three languages offered as segmented controls**, because **the early cohort is DACH-first with limited European expansion**. We'll know we're right when **fewer than 10% of new shops need a currency or language outside `USD · EUR · GBP` and `English · German · French`**.

- *Type:* Solution · *Evidence:* the Regional group as designed; §3.2 (DACH + European expansion as the 6.0 target)
- *Test:* market distribution of pilot shops
- *Note:* the control type carries the bet. A segmented control cannot grow into twenty locales — if this is wrong, it is a component change, not a content change. Worth noting the defaults ship as `USD` and `English` in a DACH-first product.

### B7 — Per-shop overrides stop payment duplication
We believe **merchants** will **leave payment configured globally and override only where a storefront genuinely differs**, because **the panel presents itself as a diff from a global default rather than as an independent setup**. We'll know we're right when **the median shop carries zero payment overrides, and merchants can say which of their shops deviate without opening each one**.

- *Type:* Solution · *Evidence:* *Payment (this shop)* with the *Inherits global* badge; audit W2.3 on S1 rated *Needs improvement* precisely because nothing showed which shops had overridden the global default
- *Test:* override counts; a "which shops differ?" recall task

### B8 — Maintenance mode becomes the safety net
We believe **merchants making risky changes** will **take the storefront offline first**, because **maintenance mode is the only reversible storefront-wide control in a product that still has no undo**. We'll know we're right when **maintenance mode precedes large theme or catalogue changes in more than a fifth of such sessions, and "published something broken" incidents fall**.

- *Type:* Solution · *Evidence:* the Status group; audit S1-03 and S3-03 (no undo anywhere in the build)
- *Test:* sequence analysis — does maintenance mode get used before publishes, or only after something breaks?
- *Note:* if merchants only reach for it *after* a bad publish, it is a recovery tool, not a safety net, and the undo gap stays open.

---

## Business assumptions

### B9 — Settings depth is what makes multi-shop an expansion driver
We believe **a single merchant** will **run materially different business models on one subscription — DE B2C gross alongside B2B net, guest checkout on in one shop and off in another — because settings are where those models actually diverge**, turning additional storefronts into expansion revenue rather than support load. We'll know we're right when **at least a quarter of multi-shop accounts run shops with materially different settings profiles, and support contacts per account stay flat as shop count grows**.

- *Type:* Business · *Evidence:* §6.4's two worked examples; §3.1's finding that 5.0 multi-shop was "complex, maintenance-intensive, and error-prone"
- *Test:* settings-profile divergence per account; support contacts normalised by shop count

### B10 — Settings move partners out of routine configuration
We believe **JTL service partners** will **stop being needed for routine shop configuration**, because **the surface is now toggles and segmented controls rather than files, templates and plugins**. We'll know we're right when **partner hours per configuration change fall against a 5.0 baseline, and fewer than 15% of settings changes in pilot accounts are made by a user holding the External role**.

- *Type:* Business · *Evidence:* §3.2 Table 8 (partner role moves to enablement; merchant autonomy low-to-medium → medium-to-high); the *Roles & 2FA (this shop)* panel makes External a first-class, per-shop role
- *Test:* attribute settings changes by role — the role column makes this measurable without asking anyone

---

## Suggested order of attack

| # | Assumption | Type | Why this order |
|---|---|---|---|
| B4 | Merchants assume compliance is handled | Problem | One interview question answers it, and the answer decides whether a legal group is MVP |
| B5 | One tax boolean won't hold | Problem | Testable against real catalogues today, before the control ships |
| B3 | Errors are about level, not value | Problem | Validates or kills the whole inheritance model |
| B1, B7 | Override rather than rebuild | User / Solution | The two halves of the same bet; cheap to instrument |
| B6 | A short fixed list is enough | Solution | Answer changes the component, so it wants an early answer |
| B2, B8 | Toggle consequences and the safety net | User / Solution | Both are downstream of the missing undo — test together |
| B9, B10 | Expansion revenue, partner shift | Business | Slower-burning; need a pilot cohort |

## Carried over from the audit, still open on these screens

Two findings from `5 test/audit-findings-log.md` are untouched by the new work and are assumed rather than resolved:

- **W1 · data origin.** Products (42 items) and Categories (18) are WaWi-derived; Content (6 pages) is shop-owned. Nothing distinguishes them, and no screen shows when the sync last ran.
- **W3 · legal configuration.** Settings still has no legal or consent group. B4 tests whether merchants notice; it does not make the gap smaller.

One new ambiguity worth a decision rather than an assumption: **where locale lives**. Language is a per-shop setting here, but the checkout brief concluded locale is "a theme-level switch, not a copy decision". Two homes for one concept — decide before build.
