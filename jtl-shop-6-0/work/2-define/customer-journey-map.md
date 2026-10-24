# Customer Journey Map — Setting up a shop on JTL-Shop 6.0

**Primary persona:** Shop owner (User 1 on the JTBD board)
**Secondary persona:** Shop staff (User 2) — shown as a band under the phases they appear in
**Stages:** Onboarding · Create · Setup · Modify · Publish · Manage
**Date:** 19 Sep 2026 · **Status:** current-state map, assembled from existing artefacts. Not validated with merchants.

---

## How to read this — and what it is not

This map **groups material that already exists**. Nothing in it is new research.

| Row | Where it comes from | How solid |
|---|---|---|
| Jobs to be done | FigJam *Tam-Analyze-Session* → section **JTBDs** (`53:436`), one sticky per job | Team-authored, unvalidated |
| Doing | The two prototype HTMLs in `4 design prototype/` | Observed in the build |
| Thinking / feeling | **Inferred** from audit findings + the Pflichtenheft | ⚠ Not merchant quotes |
| Pain points | `5 test/audit-findings-log.md` (27 *Needs fixing*, 39 *Needs improvement*) | Single-evaluator expert audit |
| Opportunities & open bets | A/B/C assumption sets in `2 define/assumptions/` | Candidates, none validated |
| Duration | Design targets stated in the A-series signals | Targets, not measurements |

**The honest caveat.** Stage 1 of the design process has had **zero user contact** — discovery is the Pflichtenheft plus one desk article, and Stage 5 is a single-evaluator audit. So the emotion curve below is a *hypothesis about where friction concentrates*, not an observation. Treat every quote as a testable statement, not a finding. The map's real job is to show **which phases carry the most unvalidated weight** — and that is Setup, by a wide margin.

**Source of truth for the jobs stays the FigJam board.** This file is a grouping of it, not a replacement.

---

## Persona header

### Shop owner — the merchant who bought the licence

Owner-operator or e-commerce manager, 1–50 employees, DACH, migrating from JTL-Shop 5.0. Non-technical by the spec's own description (§3.1: "no technical background", high partner dependency). Buys on ROI and time-to-value, not on branding — though §3.2 describes a 6.0 target customer who cares about UX as a differentiator. **Those two profiles disagree, and that disagreement is A2.**

**Scenario.** Has just bought JTL-Shop 6.0 and logged in for the first time. The products already live in WaWi. Wants a storefront that looks like the brand and can take real orders — without calling a service partner.

**Expectations**

- See every step between this login and a live shop, before starting
- Connect the ERP on day one and work with the real assortment, not demo data
- Put logo, colours and type on the storefront without opening a design tool
- Be told the shop is genuinely ready — before it takes real traffic

### Shop staff — the colleague who will actually run it

Invited into a shop someone else set up. Needs to know what is theirs to touch. **Has no invitation step anywhere in the current five-item checklist** — which is why owners share credentials today.

---

## Stage 1 · Onboarding

**Duration target:** first session · **Emotion:** cautiously positive, then flat

### Jobs to be done (owner)

- When I first log in after buying JTL-Shop, I want to **see every step between me and a live shop**, so I can judge the effort before I start.
- When my products already live in WaWi, I want to **connect the ERP on day one**, so I can work with my real assortment, not demo data.

### Doing

1. Lands on the dashboard after purchase
2. Finds the five-item setup checklist — *Create your shop · Customize your theme · Set up payments · Add a shipping zone · Connect a custom domain*
3. Scans the shop list and the per-shop product counts
4. Looks for where WaWi connects — and does not find a status for it

### Thinking *(inferred)*

> "Good — someone has written down the order. I was expecting to have to work that out."

> "It says 42 products. From when? Is that today's WaWi or a snapshot?"

> "Five items and I'm live? That feels short for a German shop."

### Pain points

- **S1-08 ·** The checklist — the only thing that matters pre-launch — sits in a narrow right rail, outweighed by three dense full-width tables. The screen is laid out for the returning operator, not the one still in setup.
- **S1-04 / S1-06 ·** No last-sync time, no sync health, no per-field origin marker. On a platform whose premise is ERP-led data, the home screen cannot answer "is my data current?"
- **S1-01 ·** A merchant can complete 5 of 5, see the checklist finish, and be non-compliant on day one. Consent, legal notice, withdrawal, tax mode, price display — none appear. *Highest-severity finding in the audit.*
- **S1-09 ·** "Manage every **frontend**…" — developer vocabulary in a product whose target user is explicitly non-technical. *Storefront* is the merchant-facing word used elsewhere in the same product.
- **Structural ·** §6.3 and §6.7 BUILD make a dialogue-based AI "Shop Lead" central to onboarding. **The prototype contains no assistant surface at all.**

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **A7** ⚑ | The checklist substitutes for the AI "Shop Lead" | **Riskiest in the set.** Spec and prototype disagree; the answer changes MVP scope. Wizard-of-Oz a chat-guided setup against the current flow. |
| **A1** | Non-technical merchants finish setup unaided | The whole positioning rests on it |
| **A3** | The barrier is sequencing and vocabulary, not missing capability | If wrong, the guided-flow strategy is aimed at the wrong pain |
| **B1** | Merchants override rather than rebuild | First encounter with the global/per-shop split happens here |

---

## Stage 2 · Create

**Duration target:** under 15 minutes to a themed, previewable storefront (A4) · **Emotion:** highest point in the journey, then a drop

### Jobs to be done (owner)

- When I create a shop, I want to **set name, categories and domain in one pass**, so I can get a working storefront before I think about design.
- When I add a second shop for another brand or market, I want to **reuse my first shop's setup**, so I can launch without repeating everything.

### Jobs to be done (staff)

- When we need a shop for a seasonal campaign, I want to **create it from an existing one**, so I can hand my manager a near-finished storefront.

### Doing

1. Opens the *Add shop* modal
2. Types a shop name — which apparently derives the subdomain (`lalouette.myshop.co`)
3. Selects ERP categories through *Select category*
4. Skips the domain — *Optional · set up later*
5. Hits *Create shop*

### Thinking *(inferred)*

> "Three fields. That's it? After 5.0 I was braced for an afternoon."

> "Which categories pull which products? I'd have to open WaWi to be sure."

> "Did that create a draft or a live shop? Is something syncing right now?"

### What works — keep it

- **"Optional · set up later"** on the domain field is exactly the right microcopy for the step most likely to need outside help
- Three fields only, primary task unmistakable, dimmed dashboard preserving context behind the modal

### Pain points

- **S2-01 ·** No country, market, currency or language field. The prototype's own state object holds `language: "German", taxIncluded: true` — so **every new storefront silently inherits a German, tax-inclusive configuration the merchant never saw**. For a product positioning EU expansion as core, market belongs at creation time.
- **S2-02 ·** *"Select category"* with a tooltip ⓘ. The most consequential decision in the modal is the least explained — the spec's own phrasing ("Fetch products from ERP by categories") is clearer than the UI's.
- **S2-03 ·** Nothing states what *Create shop* produces: a draft, a live storefront, a background sync of unknown duration? It presents as a self-contained action when it is the first step of a longer sequence.
- **S1-12 ·** No way to duplicate an existing shop's configuration — **which is the central promise of the multi-shop model**, and is exactly the owner's second job and the staff job above.
- **S2-07 ·** The modal never names which account or tenant the storefront joins, or what it inherits.

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **A4** | Adding a second storefront stops being a project | Core differentiator claim — and currently unsupported by any duplicate action |
| **A5** | ERP-category import is the right first product step | Test whether merchants can predict what a category selection pulls in |
| **A6** | Deferring the domain raises completion instead of stranding shops | Split completion rates by defer / don't-defer |
| **B10** | Settings move partners out of routine configuration | Board places it on the Create/Setup boundary |

---

## Stage 3 · Setup — the long pole

**Duration target:** the bulk of signup → first order (A9 targets single-digit days) · **Emotion:** lowest point in the journey

Five of the sixteen owner jobs and **six of the seven staff jobs** land in this one phase. So does the densest cluster of audit findings and every open compliance question. If the map says one thing, it is this: **Setup is carrying more unvalidated weight than the other five phases combined.**

### Jobs to be done (owner)

- When I choose a theme, I want to **preview it with my own products**, so I can tell whether it fits my assortment instead of a demo catalogue.
- When I am setting up, I want to **put my logo, colours and type on the storefront without opening a design tool**, so I can launch something that looks like my brand, not a demo.
- When I set up payment, shipping and domain, I want **each step to confirm it is verified**, so I can trust the shop can really take orders.
- When I am setting up, I want to **invite the colleague who will run the shop and scope what they can touch**, so I can hand off the rest of setup without sharing my login.

### Doing

1. Opens the theme picker — Aurora / Meridian / Editorial, plus *Customize*
2. Opens the theme editor; adjusts Typography in the inspector (Font, Weight, Letter spacing, Case)
3. Tries the *AI theme setup* panel — pastes a brand description or a reference link
4. Checks the storefront preview at the two available device widths
5. Sets up payments, adds a shipping zone, points an A record at the domain
6. Opens *Roles & 2FA* to add the colleague who will run the shop

### Thinking *(inferred)*

> "I've described my brand in the box. Now what — where's the button?"

> "Those four grey tiles where my products should be. Haven't they synced, or did I pick the wrong category?"

> "The header says L'alouette. My shop is called Lili. Which one is the customer going to see?"

> "I changed the font here. Did that change it on every page, or only this one?"

> "I'll just send her my password — there's no step for adding her."

### Pain points

- **S3-04 ·** The *AI theme setup* panel has a prompt box and an *Import image* button and **no submit control** — no generate, no processing state, no summary of what changed. The single most novel interaction on the screen has no visible way to start it.
- **S3-05 ·** The preview's Products section renders four flat coloured tiles. A merchant cannot distinguish "not synced from WaWi" from "no category selected" from "placeholder art".
- **S3-01 ·** The inspector shows typography as plain segmented controls with **no inherited-vs-overridden state**. The `Inherits global` state and `Customized` badge exist in the prototype — behind a 24 px icon button labelled only by a `title` tooltip. **A8 cannot hold on a panel that never shows inheritance.**
- **S3-08 ·** The preview renders a different brand name than the shop being edited — undermining the one thing a preview is for.
- **S3-10 ·** Two device widths previewable against the **four** breakpoint tiers `storefront-layout-system.md` actually defines (360 / 768 / 1024 / 1440), including a nav pattern change at 768.
- **S1-03 / S1-05 ·** Role is an inline segmented control and 2FA a clickable pill, both instant-apply, no confirm, no undo. Meanwhile *Require 2FA for all admins* is **on** while two members show 2FA **Off** — an unresolvable state on a security control.
- **Structural ·** There is **no "invite your team" step on the checklist at all.** Three staff jobs already depend on a permission model the product does not visibly have.
- **Compliance ·** No legal or consent group exists anywhere. "Tax included in prices" is one boolean against a spec requiring reduced rates, exemptions, OSS, CH/GB input tax, and gross B2C alongside net B2B in one tenant.

### Shop staff band — this is where staff live

| Job | What blocks it today |
|---|---|
| When I am invited into a shop someone else set up, I want to **see what is done and what is mine to do** | No shared progress view; the checklist is owner-scoped |
| When I am given access, I want **my role to make clear what I may change** | Roles exist as a table; nothing expresses scope at the point of editing (**W2.2**) |
| When I am asked to finish setup steps, I want to see **which need the owner's decision or credentials** | No step carries an owner-only marker |
| When I am asked to tweak the storefront, I want to **edit only what I am allowed and preview it first** | Preview vs published is only *Needs improvement*-grade distinct (**W2.6**) |
| When I have finished a change, I want to **submit it for the owner's approval** | No approval or review state exists |
| When I do daily upkeep of banners, content and visibility, I want changes to be **quick and reversible** | No undo anywhere in the build (**S3-03**) |

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **B4** | Merchants assume compliance is handled | **Cheapest high-value test in the set** — one verbatim interview question decides whether a legal group is MVP |
| **B5** | One tax boolean won't survive a real catalogue | Testable against ten real JTL catalogues today, before the control ships |
| **B3** | Errors are about *level*, not value | Validates or kills the whole inheritance model |
| **A2** | Merchants start from a built-in theme, not a custom one | §3.1 and §3.2 disagree about this customer — which is why it needs testing |
| **A8** | Merchants work through inheritance rather than per-page styling | Currently untestable: the panel never shows inheritance |
| **B7** | Per-shop overrides stop payment duplication | Nothing shows which shops have overridden the global default |
| **C1** | A currency picker stands in for a region group | §8.12 derives currency from a region group from country identifiers — **no country control exists**, and the screen defaults to `USD` in a DACH-first product |
| **C2** | One language per shop is close enough to a locale model | Spec models many locales with a default; and storefront locale vs admin language are two different things in one control |
| **C3** | A boolean is an adequate tax control for MVP | See B5 |
| **C4** | Inventory tracking belongs to the shop | Spec places it per *product*, non-MVP |
| **C8** | Per-shop roles extend the tenant role model cleanly | Roles are specified at tenant level; admin 2FA is not specified at all |
| **C9** | *Inherits global* means to merchants what it means to the system | The load-bearing phrase of the whole product |
| **C10** | The screen can promise pages and domains | CMS/templates are non-MVP; §8.13 says **one** domain per shop in MVP while the UI says *Add domain* |

---

## Stage 4 · Modify

**Duration target:** ongoing · **Emotion:** low, recovering slowly

### Jobs to be done (owner)

- When I change my brand colour or font, I want it **applied everywhere consistently**, so I can rebrand without hunting for stragglers.
- When I have customised parts of a theme, I want to **see what still inherits the global settings**, so I can reset one thing without losing the rest.
- When I run several shops on one theme, I want to **change the shared basis once and keep per-shop exceptions**, so I can stay consistent without editing each shop.

### Doing

1. Returns to the theme editor to change a global token
2. Clicks through pages hunting for values that did not follow
3. Tries to reset one property back to the global value
4. On a second shop, tries to work out which values are local and which are shared

### Thinking *(inferred)*

> "I changed it globally. Why is the footer still the old blue?"

> "If I reset this, do I lose the other three things I customised?"

> "Which of my four shops have I overridden payment on? I'd have to open each."

### Pain points

- **S3-01 / S3-02 ·** Inheritance is invisible per property and blast radius is never named. No "affects 4 storefronts" anywhere before a global change lands.
- **S1-13 ·** The global Payment section states its scope well — but nothing shows which shops have since overridden it.
- **S3-03 ·** No undo anywhere in the file. The version dropdown implies recoverable history, which is the right instinct — but recovery through a version picker is not undo at the moment of the mistake, and the AI panel can restyle many properties at once.
- **Reset is hidden ·** *Reset to default* is a 24 px icon button whose only label is a `title` tooltip.

### Open decision — carried from ARC-17

Merchant "theme creation" is **preset-shaped, not theme-shaped**. For MVP, a merchant creating "their own theme" means tweaking tokens and saving the result to reuse — a *preset*. Authoring structurally new themes is a separate lifecycle and a third persona (agency / partner / developer) the board does not have.
**Consequence:** the reuse jobs belong in *Modify* (save it) + *Manage* (apply it across shops). **Neither is drafted on the board yet.**

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **A8** | Work through inheritance, not per-page styling | Override counts per shop; comprehension test on the editor |
| **B1** | Override rather than rebuild | "Where does this value come from?" comprehension task |
| **B3** | The difficulty is level, not volume | Code settings errors by type in eight sessions |
| **B6** | A short fixed list covers the MVP cohort | The control type carries the bet — a segmented control cannot grow into twenty locales |
| **B8** | Maintenance mode becomes the safety net | If merchants reach for it only *after* a bad publish, it is a recovery tool, not a safety net |

---

## Stage 5 · Publish

**Duration target:** one action, minutes · **Emotion:** rising — on a shaky base

### Jobs to be done (owner)

- When I think the shop is ready, I want **a check that flags what is missing or broken**, so I can go live without an embarrassing first day.
- When I publish a change, I want to **preview exactly what customers see on mobile and desktop**, so I can be sure before it hits real traffic.

### Doing

1. Checks the storefront preview at the two available widths
2. Hits *Apply to storefront*
3. Opens the live URL to see what customers got

### Thinking *(inferred)*

> "Is that it? Nothing asked me to confirm."

> "I'd like something to tell me I haven't forgotten anything legal."

> "It looks right on the two sizes I can see here."

### Pain points

- **The readiness job has no surface at all.** Nothing in the publish path checks for mandatory DACH/EU elements before *Apply to storefront* commits (**S3-06**). The owner's first Publish job is, today, entirely unbuilt.
- **S3-11 ·** *Apply to storefront* — the one action with public consequences — sits in the same toolbar strip as routine view controls, differentiated only by fill colour.
- **S3-03 ·** No confirmation on apply, and no undo after it.
- **S3-10 ·** Half the defined breakpoint tiers are unpreviewable, so "exactly what customers see" is not available even in principle.
- **W2.6 ·** Preview vs published distinctness rates only *Needs improvement*.

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **B8** | Maintenance mode is the safety net | It is currently the *only* reversible storefront-wide control in a product with no undo |
| **B2** | Toggles get flipped without checking the storefront | A toggle is reversible; its effect on a live storefront may not be |
| **A7** ⚑ | (revisited) | A pre-flight readiness check is the other shape the "AI Shop Lead" could take — decide A7 before designing it |

---

## Stage 6 · Manage

**Duration target:** continuous · **Emotion:** flat

### Jobs to be done (owner)

- When I run several shops, I want **one view of the state of each**, so I can spot the one that needs attention without opening them all.
- When someone joins, leaves or changes role, I want to **change their access in one place**, so I can keep the shop safe without rebuilding anything.
- When a theme or platform update lands, I want to **know what it changes in my storefront first**, so I can update without breaking my customisations.

### Doing

1. Scans the dashboard shop list
2. Edits the roles table when someone joins or leaves
3. Receives a theme or platform update — with no impact preview

### Thinking *(inferred)*

> "Four shops, four green dots. Green because they're fine, or green because nothing's checking?"

> "An update is available. Will it touch the things I customised?"

### Pain points

- **No update-impact surface exists anywhere in the build.** The owner's third Manage job is unbuilt, same as the readiness check.
- **S1-13 / B7 ·** No cross-shop view of which shops have overridden a global default.
- **S1-04 ·** No sync health per shop, so "state of each shop" cannot include the thing the platform is built on.
- **S1-03 ·** Role changes are instant-apply with no confirmation — including demoting an Owner.
- **S1-12 ·** No duplication of an existing shop's configuration as the start of the next one.

### Opportunities & open bets

| ID | Bet | Why here |
|---|---|---|
| **B9** | Settings depth makes multi-shop an expansion driver | Divergence of settings profiles per account; support contacts normalised by shop count |
| **B10** | Settings move partners out of routine configuration | The role column makes this measurable without asking anyone |
| **B7** | Per-shop overrides stop payment duplication | "Which shops differ?" recall task |
| **ARC-17** | Preset reuse across shops | The Manage half of the preset decision — not drafted yet |

---

## Emotion curve — hypothesis, not observation

| Phase | Entry | Exit | What moves it |
|---|---|---|---|
| Onboarding | +0.6 | −0.3 | Relief at an explicit checklist → unanswerable "is my data current?" |
| Create | **+1.2** | +0.2 | Three fields and done → "what did that actually produce?" |
| Setup | −0.8 | **−1.6** | AI panel with no button, preview showing the wrong brand, invisible inheritance, no legal group, no way to invite anyone |
| Modify | −1.1 | −0.9 | Hunting stragglers with no blast radius and no undo |
| Publish | −0.4 | +0.5 | Going live feels good; nothing checked that it should |
| Manage | +0.3 | 0.0 | Steady state, but blind to sync health and update impact |

The shape to notice: **the peak is Create and the trough is Setup, and they are adjacent.** The product's best moment is immediately followed by its worst, and the drop is not gradual.

---

## Three things this grouping makes visible

**1. Setup is not one phase — it is four jobs wearing one label.**
Branding, verification, permissions and compliance all sit under *Setup*, and each has a different owner, a different failure mode and a different spec section. Five owner jobs, six staff jobs, and the densest audit cluster all land in one column. Splitting it is probably the single highest-value change to the board itself.

**2. Three jobs on the board have no surface in the product at all.**

| Job | Phase | Status |
|---|---|---|
| A readiness check that flags what is missing or broken | Publish | Nothing exists |
| Know what an update changes before applying it | Manage | Nothing exists |
| Invite the colleague who will run the shop and scope access | Setup | Not on the checklist; roles table exists but no invitation step |

These are not usability problems. They are missing features that the JTBD exercise surfaced and the prototype does not answer — which is exactly what a current-state map is for.

**3. The permission model is assumed by six staff jobs and built by none of them.**
Every staff job depends on scope being legible at the moment of editing. **W2.2** ("edit states its scope") rates *Needs fixing* on the theme editor. Until roles and permissions get a home in *Setup* (define) and *Manage* (maintain), the staff lane is a map of a journey nobody can currently take.

---

## What to do with this

**Before the next board session**

- Split *Setup* into at least *Brand* / *Commerce readiness* / *Access* — or accept that the stage no longer names one thing
- Draft the missing Modify + Manage preset-reuse jobs (the ARC-17 decision already tells you their shape)
- Decide the *Create* naming snag: if theme creation ever lands there, the stage stops naming one thing

**Four decisions that need an owner and a date** (from the stakeholder check-in plan, section `71:335`)

1. **A7** — is the AI "Shop Lead" on the MVP critical path? ⚑ ask first
2. Roles & permissions in MVP — yes or no
3. Theme vs preset — confirmed as preset for MVP, needs sign-off
4. Light/dark in the data model

**Two tests that cost almost nothing and change scope**

- **B4** — ask eight merchants, verbatim: *"What makes this shop legally ready to sell in Germany?"* If they point at the tax toggle, a legal group is MVP.
- **B5** — take ten representative JTL catalogues and try to express their tax treatment with the current control.

---

## Sources

- FigJam **Tam-Analyze-Session**, `Z8PycuHpuIAHW2GxOwC5Az` → section **JTBDs** (`53:436`) — 16 owner jobs, 7 staff jobs, 6 stages
- `2 define/assumptions/shop-setup-candidate-assumptions.md` — A1–A10
- `2 define/assumptions/shop-settings-candidate-assumptions.md` — B1–B10
- `2 define/assumptions/shop-settings-spec-assumptions.md` — C1–C10 and the 14-function coverage table
- `5 test/audit-findings-log.md` — S1/S2/S3 findings, watch-outs W1–W3
- `2 define/ARC-17 Theme & Preset System…md` — the preset-vs-theme constraint
- `2 define/breakpoint grid spacing/storefront-layout-system.md` — the four breakpoint tiers
- `2 define/storefront-checkout-ui-brief.md` — toggle consequences on the buying flow
- `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` — §3.1, §3.2, §6.3, §6.4, §6.7, §8.12, §8.13, §9.1, §9.2
- `4 design prototype/*.html` — the build the *Doing* rows describe
