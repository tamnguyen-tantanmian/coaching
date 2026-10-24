# Shop Settings — Spec Trace & Assumptions (JTL-Shop 6.0)

**Question this answers:** for every function on the shop settings screens, what does the Pflichtenheft already specify — and what is the design assuming on top of, or against, it?

**Scope:** *Shop Admin shell* and *Settings* as designed on the Figma board section **Shop settings** (18 Sep 2026), plus the domains surface both prototypes carry.
**Date:** 18 Sep 2026 · **Numbering:** C1–C10 (A-series = setup & theme, B-series = settings behaviour, C-series = spec coverage)

**Sources**
- `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` — §6.2, §6.4, §8.12, §8.13, §8.17, §9.1, §9.2
- `4 design prototype/Shop Setup Platform-10.08.2026.html` and `Admin Setting+ Theme Setup…html` — the state objects behind the toggles
- `5 test/audit-findings-log.md` · `2 define/storefront-checkout-ui-brief.md`

---

## 1. Coverage at a glance

| # | Function as designed | Pflichtenheft status | Reference |
|---|---|---|---|
| 1 | Currency — `USD · EUR · GBP` picker | **Diverges** — currency is *derived*, not chosen | §8.12 Currency Strategy |
| 2 | Language — single select `EN · DE · FR` | **Diverges** — shops support *multiple* locales with a default | §8.12 Locale Strategy |
| 3 | Tax included in prices — boolean | **Under-modelled** — spec requires a tax *model* | §9.1 Taxes, §6.2 |
| 4 | Guest checkout — boolean | **Specified and matched** — funded as a UI toggle | §9.2 (6 FE days) |
| 5 | Inventory tracking — boolean, per shop | **Diverges** — spec places it per *product*, non-MVP | §9.1 Inventory & availability |
| 6 | Product reviews — boolean | **Not specified** — no review function anywhere in the feature table | — |
| 7 | Wishlist — boolean, off | **Specified as non-MVP** — Must-have, MVP column blank | §9.1 Customer Retention |
| 8 | Maintenance mode — boolean | **Not specified** — no offline state anywhere in the document | — |
| 9 | Payment (this shop), overrides global | **Specified and matched** | §"Payment Processing" |
| 10 | Roles & 2FA (this shop) | **Extends** — roles are specified at *tenant* level; admin 2FA isn't specified at all | §8.12, §8.17 |
| 11 | Products / Categories counts | Specified as WaWi-led; origin not distinguished in UI | §9.1 Central article mgmt |
| 12 | Content pages count | Shop-owned; correct, but presented identically to #11 | §9.1 |
| 13 | Storefront pages — create with template | **Specified as non-MVP** — CMS/template management is Must-have, MVP blank | §9.1 CMS Elements & Templates |
| 14 | Connected domains — plural, *Add domain* | **Contradicts** — "Only one domain per shop in the MVP" | §8.13 Custom Domain Mgmt |

Four functions match the spec. Five diverge from it. Two are toggles for things the spec does not describe at all. Three are toggles for things the spec explicitly places outside MVP.

---

## 2. The assumptions

### C1 — A currency picker stands in for a region group
We believe **the platform team** can **let merchants choose currency directly from a three-option control**, because **merchants think in currencies and the region-group mechanism is an implementation detail**. We'll know we're right when **no shop ends up with a currency its region group would not have produced, and no merchant asks why prices did not convert**.

> §8.12: "Currency is derived from the region group… Region group resolution based on the country identifiers configured in the shop… Currency affects price display only… The platform does not introduce uncontrolled currency conversion logic in the MVP."

The architecture derives currency from a region group, which derives from country identifiers configured on the shop. **No country or region-group control exists anywhere in the design.** Two consequences the screen does not carry: currency changes price *display* without converting any amount, and the German market is the specified fallback when a region cannot be resolved — while the screen ships defaulting to `USD`.

- *Type:* Solution · *Test:* ask engineering what happens when a merchant picks `USD` on a EUR-priced catalogue. If the answer is "labels change, numbers don't", the control is mislabelled and needs to become a market/country selector.

### C2 — One language per shop is close enough to a locale model
We believe **merchants** will **treat a shop as having one language**, because **the early cohort runs one market per storefront**. We'll know we're right when **fewer than 10% of shops need a second locale in the first two quarters**.

> §8.12: "Shops can support multiple locales. Each shop defines a default locale… The locale is expressed via a path prefix… hreflang generation is strictly locale-based. SEO identity is derived exclusively from shop and locale."

The spec models *many locales with a default*; the control models *one language*. It is also silent about the consequence: changing it changes URL paths, cache scope and hreflang. And §9.1 separately requires "support for multiple languages in the shop administration, at minimum DE and EN" — an admin-language setting that is a different thing from storefront locale and appears nowhere. Your own checkout brief already flagged this: "locale is a theme-level switch, not a copy decision — decide where it lives before build."

- *Type:* Problem · *Test:* decide first whether this control is storefront locale or admin language; they cannot be one control.

### C3 — A boolean is an adequate tax control for MVP
We believe **a single "Tax included in prices" switch** will **carry the tax decision for MVP merchants**, because **most early shops are German B2C, where gross display is the only correct answer**. We'll know we're right when **no pilot merchant needs a tax behaviour the boolean cannot express in their first month**.

> §9.1 Taxes: "Configuration of input tax for CH and GB, integration of OSS with automatic tax calculation, tax exemptions, reduced tax rates."
> §6.4: one merchant running "a shop for private end customers with gross prices… as well as a shop for business customers with net prices."
> §6.2: "Preconfigured systems enable an immediate sales launch for the German market with minimal initial setup effort. These concern in particular tax logic…"

The strongest signal here is §6.2: tax logic is supposed to be *preconfigured and correct by default*. A merchant-facing boolean invites a merchant to set it wrong — which is the opposite of what the regulatory section promises.

- *Type:* Problem · *Test:* express the tax treatment of ten real JTL catalogues using only this control.

### C4 — Inventory tracking belongs to the shop
We believe **a shop-level inventory-tracking switch** is **a reasonable simplification**, because **merchants think about tracking as a shop-wide policy**. We'll know we're right when **no merchant needs tracking on for part of the catalogue and off for the rest**.

> §9.1: "Configuration options per product: continue selling at ≤0 availability or mark as non-inventory-tracked" — *per product*, and in a row with the MVP column blank.
> §9.1 (MVP, Yes/Yes): "Prevention of overselling — the sync ensures that only available quantities are offered in the shop."

Two divergences at once: the spec scopes this per product, not per shop, and does not place it in MVP. More importantly, WaWi is the lead system for inventory, and overselling prevention *is* MVP — so a shop-level switch that disables tracking sits directly against a committed MVP guarantee.

- *Type:* Solution · *Test:* ask what this toggle does to the overselling guarantee. If it cannot disable it, the label is wrong; if it can, it breaks an MVP commitment.

### C5 — Product reviews are in scope
We believe **product reviews** are **part of the product**, because **a settings toggle exists for them**. We'll know we're right when **reviews appear in a scope document, a person owns them, and moderation and WaWi handling are defined**.

Reviews appear nowhere in the Pflichtenheft's requirement tables. The only mentions in the whole document are competitor analysis — Shopware's AI generating "review summaries". A toggle exists for a feature with no requirement, no data model, no moderation story, and no stated relationship to WaWi.

- *Type:* Problem · *Test:* find the requirement. If there isn't one, either it gets specified or the toggle comes off the screen.

### C6 — Wishlist can ship as a toggle despite being non-MVP
We believe **a toggle resolves the wishlist question**, because **merchants who want it can switch it on**. We'll know we're right when **turning it off removes the wishlist from every storefront surface, and someone has decided whether it ships at all**.

> §9.1 Customer Retention: "Wish List Function — customers can save products to a wish list; saved items are stored in the customer account." Must-have column marked; **MVP column blank.**

This is now a three-way contradiction: the spec says not-MVP, the settings screen offers a toggle (defaulted off), and your checkout brief records a wishlist heart on every product card. The brief's own words: "Cannot stay ambiguous — the heart is on screen today."

- *Type:* Problem · *Test:* one decision, not a test. Ships or doesn't.

### C7 — Maintenance mode is a safe addition
We believe **adding maintenance mode** is **low-risk**, because **taking a storefront offline is a simple, well-understood control**. We'll know we're right when **it interacts correctly with the edge cache and the domain layer, and someone owns what a visitor actually sees**.

Maintenance mode appears nowhere in the Pflichtenheft. It is not a small feature in this architecture: §8.9 and §8.15 put CDN caching and TTL-driven revalidation in front of every storefront, and §8.13 enforces host-based resolution with "immediate rejection of unbound domains". An offline state has to define what the edge serves, what status code it returns, what happens to SEO, and whether the merchant's own preview still works.

- *Type:* Solution · *Test:* an engineering answer on cache and status-code behaviour before this is drawn any further.

### C8 — Per-shop roles extend the tenant role model cleanly
We believe **per-shop role scoping with "graduated permissions inherited from global roles"** will **work within the specified identity model**, because **it is a refinement of role-based permissions rather than a new mechanism**. We'll know we're right when **engineering confirms the control plane can express shop-scoped roles, and every role change is auditable**.

> §8.12: "Users belong to a tenant and are granted role-based permissions. Permission checks are enforced in the control plane and management APIs."
> §8.17: "Tenant admin tokens scoped to the tenant context and administrative roles… Changes to roles and permissions are traceable."

The spec scopes users and roles to the **tenant**; the design scopes them to the **shop**, with inheritance. That may be fine, but it is an extension, not a restatement. Two specifics: the only multi-factor authentication in the document is under *Customer account · Identity & security* — that is buyers, not admins, so **admin 2FA is unspecified** — and §8.17 mandates that role and permission changes be traceable, while the design offers no audit or history surface anywhere.

- *Type:* Solution · *Test:* confirm shop-scoped roles are expressible in the control plane; add an audit trail to the design, since the spec already requires one.

### C9 — "Inherits global" means to merchants what it means to the system
We believe **merchants** will **read the *Inherits global* badge as "this shop follows the default until I change it"**, because **that is what the platform actually does**. We'll know we're right when **merchants correctly predict what happens to this shop when the global payment default changes**.

> §"Payment Processing": "Different payment methods and risk profiles can be configured in a differentiated manner per shop, target group, or market segment, without fragmenting the central logic of order and financial processes in the ERP."

This is the cleanest match on the board — the design and the spec agree. The remaining assumption is purely comprehension, and it is worth protecting: the badge is the only place the inheritance model is visible to a merchant anywhere in the product.

- *Type:* User · *Test:* comprehension task — change the global default, ask what happens to each shop.

### C10 — The screen can promise pages and domains
We believe **Settings can offer storefront page creation and multiple connected domains**, because **both read as ordinary shop configuration**. We'll know we're right when **both survive contact with the MVP scope**.

> §9.1: "Management of CMS Elements and Templates — central control of all page templates, CMS building blocks, and design variants… including inheritance logic for content and settings." Must-have; **MVP column blank.**
> §8.13: "The MVP supports one custom domain per shop… **Only one domain per shop in the MVP version.** No platform-managed subdomain hierarchy. Tenants manage DNS configuration externally."

Page creation with a template picker is the CMS-management row, which is not MVP. And both prototypes carry a **Connected domains** list with an *Add domain* action — a plural affordance against an explicitly singular MVP constraint. The domain *verification* step the prototypes show does match §8.13.

- *Type:* Solution · *Test:* neither needs research. Both need a scope decision.

---

## 3. Specified in the Pflichtenheft, missing from the settings screens

The trace runs both ways. These are functions the spec explicitly assigns to shop administration and that the current Settings screens do not surface:

| Specified function | What the spec says | Reference |
|---|---|---|
| **Integrated consent manager** | "Legally compliant collection and management of consents for cookies, tracking services and third-party tools. **Settings can be adjusted in the admin.**" | §9.1 Regional DE |
| **Central legal texts** | Provision and maintenance of "privacy policies, legal notices and other legally required information" | §6.2 |
| **Admin language** | "Support for multiple languages in the shop administration, at minimum DE and EN" | §9.1 Shop Admin |
| **Shipping / delivery terms** | A checklist step at setup, with regional shipping methods and country-specific settings — no settings home | §9.1 Regional DE |
| **Customer groups & price visibility** | Customer-specific prices, tiered pricing; hiding prices from non-logged-in visitors | §9.1 B2B Logic |
| **Notifications** | Shop notifications and message formats | §9.1 Shop Notifications |
| **Block lists, sanctions & fraud checks** | "Checks against sanctions lists, procedures for detecting potential fraud attempts, and the ability to maintain customer block lists" | §6.2 |

The consent manager is the sharpest of these: the spec places it in the admin *by name*, and the audit already found no legal surface anywhere in the merchant flow. It is not a gap that needs validating — it is a specified requirement with no design.

---

## 4. Questions the spec owner should answer before this is built

1. **Is currency chosen or derived?** If derived (§8.12), the Regional group needs a country/market selector and the currency control goes away.
2. **Is the Language control storefront locale or admin language?** The spec treats them as separate; the screen has one control.
3. **Does "Tax included in prices" survive §6.2's promise of preconfigured, legally correct DE defaults?**
4. **Do reviews exist as a requirement?** If not, the toggle has no product behind it.
5. **Wishlist: in or out?** Three artefacts currently disagree.
6. **One domain per shop, or several?** §8.13 says one, twice. The UI says several.
7. **Are shop-scoped roles expressible in the control plane,** and where does the audit trail §8.17 mandates appear in the UI?
8. **Where does the consent manager live?** It is specified as an admin setting and designed nowhere.

---

*Spec quotations are verbatim from `JTL_Shop_6.0_Pflichtenheft_EN.md`. "MVP column blank" refers to the Table 19 feature overview in §9.1, where a Must-have marking without an MVP marking places the feature in a later expansion stage.*
