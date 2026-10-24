# Candidate Assumptions — Guided Shop Setup & Theme Setup (JTL-Shop 6.0)

**Scope:** the onboarding path a merchant walks from empty account to live storefront — dashboard setup checklist, *Add shop*, theme selection, theme editor.
**Date:** 22 Aug 2026
**Status:** candidates for prioritisation. Not validated. Each still needs to be ranked on *impact if wrong* × *evidence we currently have*.

**Sources read**
- `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` — §3.1 initial situation & user profile, §3.2 target vision, §6.3 ease of use, §6.7 AI (BUILD/RUN/IMPROVE), §9.1 MVP scope
- `4 design prototype/Admin Setting+ Theme Setup (update by AnhTruong).html` — setup checklist, *Add shop* modal, theme list, theme editor, domains, roles
- `4 design prototype/Shop Setup Platform-10.08.2026.html`
- `2 define/breakpoint grid spacing/storefront-layout-system.md` — token inheritance across breakpoints
- Figma board *ainavio* → section **Current Screen Flow / Create shop** (dashboard → Add shop → theme editor)

**What the current design actually commits to** (the ground these assumptions sit on)
- A five-item setup checklist: *Create your shop* · *Customize your theme* · *Set up payments* · *Add a shipping zone* · *Connect a custom domain*
- *Add shop* asks for three things only: shop name, "Fetch products from ERP by categories", domain (marked *Optional · set up later*)
- Three built-in themes (Aurora, Meridian, Editorial) plus *Customize*; a *Style reference* panel; global values that pages mark as *Inherits global*
- **No conversational AI assistant is present in the prototype**, though §6.3 and §6.7 make an AI "Shop Lead" central to onboarding. A7 below is where that gap gets tested.

Numbers in the signals are deliberate placeholders — set the real thresholds against 5.0 baselines before anyone runs a test.

**Also on the board:** all ten are placed as sticky notes on the *ainavio* FigJam board, in four clusters below the *Current Screen Flow* section — screen 1 (setup checklist), screen 2 (*Add shop*), screen 3 (theme picker/editor), and a business cluster for the whole flow. Sticky colour = type (blue user, orange problem, green solution, violet business); ⚠ marks A7. The stickies carry the one-line version, this file carries the reasoning and sources.

---

## User assumptions

### A1 — Non-technical merchants can finish setup unaided
We believe **a non-technical JTL merchant (owner-operator or e-commerce manager, 1–50 employees, DACH)** will **complete all five setup tasks and go live without contacting a service partner**, because **the checklist makes explicit the sequence that Shop 5.0 left as implicit knowledge about shop / WaWi / hosting interplay**. We'll know we're right when **≥60% of new shops reach go-live with all five tasks done, and fewer than 1 in 5 open a partner or support ticket during setup**.

- *Type:* User · *Evidence:* §3.1 (setup effort and technical understanding are the top barriers; users "have no technical background", high partner dependency)
- *Test:* instrument checklist completion; 8–10 moderated first-run sessions with 5.0 merchants who currently rely on a partner

### A2 — Merchants start from a built-in theme, not a custom one
We believe **merchants migrating from Shop 5.0** will **launch on one of the three built-in themes with only global-level customisation**, because **their established priority is process stability over branding, and picking a ready theme is the shortest path to a live shop**. We'll know we're right when **>70% of first shops go live on a built-in theme with no per-page overrides, and theme selection takes under 10 minutes in session data**.

- *Type:* User · *Evidence:* §3.1 (branding, storytelling, "highly modern UX concepts" all currently of lesser relevance) against §3.2 (UX as strategic differentiator for the 6.0 target customer) — the two profiles disagree, which is exactly why this needs testing
- *Test:* theme-choice funnel; count overrides at go-live; interview the merchants who *do* go custom about what drove it

---

## Problem assumptions

### A3 — The real barrier is sequencing and vocabulary, not missing capability
We believe **JTL merchants setting up a shop** will **stall primarily on "what comes next" and "what does this term mean" rather than on absent functionality**, because **the customer survey located the pain in overall operational complexity and partner dependency, not in individual feature gaps**. We'll know we're right when **in 10 moderated setup tests, more than half of all hesitation events are sequencing or terminology confusion rather than "the system can't do X"**.

- *Type:* Problem · *Evidence:* §3.1 ("perceived challenges lie less in individual missing features and more in the overall complexity of operations"), §6.7 BUILD (replacing "complex admin menus and assumed e-commerce terminology")
- *Test:* code hesitation events by cause in usability sessions; tag setup support tickets the same way

### A4 — Adding a second storefront stops being a project
We believe **multi-shop operators** will **treat adding a storefront as a routine, low-risk action instead of a project**, because **Add shop reduces a new storefront to a name, an ERP category selection, and an optional domain — where 5.0 multi-shop was used but experienced as complex, maintenance-intensive and error-prone**. We'll know we're right when **median time from *Add shop* to a themed, previewable storefront is under 15 minutes, and ≥30% of accounts create a second shop within 60 days**.

- *Type:* Problem · *Evidence:* §3.1 (multi-shop "used, but perceived as complex, maintenance-intensive, and error-prone"), §6.4, prototype *Add shop* modal
- *Test:* time-to-second-shop cohort metric; follow-up interviews on what they expected to have to configure and didn't

---

## Solution assumptions

### A5 — ERP-category import is the right first product step
We believe **merchants** will **accept "Fetch products from ERP by categories" as the way products enter the shop**, because **WaWi is already their single source of truth and they expect no duplicate data maintenance**. We'll know we're right when **>80% select at least one category on first pass without leaving to check WaWi, and fewer than 10% of shops later need a manual import workaround**.

- *Type:* Solution · *Evidence:* §9.1 (centralised product maintenance, WaWi as lead system, "no duplicate data maintenance"), prototype *Add shop* modal
- *Test:* modal drop-off and re-entry rate; check whether merchants can predict what their category selection will pull in

### A6 — Deferring the domain raises completion instead of stranding shops
We believe **merchants who skip domain setup at *Add shop* time** will **finish the rest of the checklist and connect a domain later**, because **pointing an A record is the step most likely to need external help, and blocking on it would stall everything behind it**. We'll know we're right when **shops that defer the domain complete the remaining tasks at an equal or higher rate, and ≥70% connect a custom domain within 30 days**.

- *Type:* Solution · *Evidence:* prototype (domain marked *Optional · set up later*; separate Domains screen with A-record instruction)
- *Test:* split completion rates by defer/don't-defer; 30/60/90-day domain-attach curve

### A7 — The checklist substitutes for the AI "Shop Lead" *(riskiest — resolve first)*
We believe **first-time merchants** will **reach go-live with the checklist and theme picker alone, without the dialogue-based AI assistant**, because **the checklist already removes the sequencing problem the assistant was designed to solve**. We'll know we're right when **an unassisted cohort reaches go-live within 10 percentage points of an AI-assisted cohort** — and if the gap is wider, conversational BUILD belongs on the MVP critical path rather than in a later phase.

- *Type:* Solution · *Evidence:* §6.3 and §6.7 BUILD both make AI setup assistance central and §9.1 marks AI-assisted theme setup as MVP-relevant, yet the current prototype contains no assistant surface
- *Test:* Wizard-of-Oz a chat-guided setup against the current flow; compare go-live rate, time-to-live and drop-off point. Cheapest way to learn whether the AI is a differentiator or a nice-to-have

### A8 — Merchants will work through inheritance rather than per-page styling
We believe **merchants managing one or more shops** will **change global theme values and let pages inherit, instead of styling pages individually**, because **inheritance is what keeps a multi-shop setup maintainable and the editor surfaces *Inherits global* as the default state**. We'll know we're right when **fewer than 20% of pages carry a local override at go-live, and merchants can correctly predict what a global token change will affect in a comprehension task**.

- *Type:* Solution · *Evidence:* prototype (*Inherits global*, global theme settings, templates management), `storefront-layout-system.md` (responsive vs static token behaviour), §6.4 (file inheritance principle, 60–80% shared core)
- *Test:* override counts per shop; comprehension test on the theme editor; look for merchants who override globally-solvable things — that's an affordance failure, not a user failure

---

## Business assumptions

### A9 — Faster time-to-value carries the SaaS price
We believe **ROI-driven buyers in professionalised retail teams** will **accept SaaS pricing on the strength of time-to-value**, because **today's cost is inflated less by licence fees than by setup time and partner dependency**. We'll know we're right when **median signup → first order drops to single-digit days against a 5.0 baseline measured in weeks, and setup-related partner spend per new shop falls by at least half**.

- *Type:* Business · *Evidence:* §3.1 (higher time-to-market, rising total costs, low time-to-value), §3.2 (management- and ROI-driven decision structure), §5 positioning (time-to-market as a structural advantage)
- *Test:* baseline 5.0 setup cost and duration from partner invoices and merchant interviews before launch, so there is something to compare against

### A10 — Partners don't lose by merchants self-serving
We believe **JTL service partners** will **support a self-service setup flow**, because **it moves them off low-margin setup work toward integration, migration and growth work — the enablement role the target vision assigns them**. We'll know we're right when **partner interviews surface no net revenue objection, and at least a third of new 6.0 shops still arrive via partner referral in the first two quarters**.

- *Type:* Business · *Evidence:* §3.2 Table 8 (partner role shifts from problem-solver/operator to enablement and growth partner; merchant autonomy low-to-medium → medium-to-high), §3.1 (high partner dependency today)
- *Test:* 6–8 partner interviews across sizes; track referral share post-launch. Partner resistance is a distribution risk, not just a sentiment one

---

## Suggested order of attack

| # | Assumption | Type | Why this order |
|---|---|---|---|
| A7 | Checklist substitutes for AI Shop Lead | Solution | Spec and prototype disagree; the answer changes MVP scope |
| A1 | Merchants finish setup unaided | User | The whole positioning rests on it |
| A3 | Barrier is sequencing, not features | Problem | If wrong, the guided-flow strategy is aimed at the wrong pain |
| A9 | Time-to-value carries the price | Business | Needs a 5.0 baseline captured *before* launch or it can't be measured |
| A4 | Second storefront becomes routine | Problem | Core differentiator claim |
| A2, A5, A6, A8 | Flow-level design bets | User / Solution | Cheap to test in usability sessions and instrumentation |
| A10 | Partners don't lose | Business | Slower-burning, but a distribution risk if ignored |
