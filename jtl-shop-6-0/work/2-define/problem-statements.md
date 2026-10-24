# Problem Statements — Merchant setup & administration (JTL-Shop 6.0)

**Scope:** the journey mapped in `2 define/customer-journey-map.md` — Onboarding · Create · Setup · Modify · Publish · Manage, both personas.
**Date:** 19 Sep 2026 · **Numbering:** P1–P10 (A = setup bets, B = settings behaviour, C = spec coverage, S = audit findings, W = watch-outs).
**Status:** prioritised, not validated. No merchant contact yet — the ranking is a reasoned bet, not a measurement.

---

## The problem statement

> **Shop owners and their staff need a way to see what a change will affect, where a value came from, and whether it can be undone — because the product states none of these at the moment of the change.**

The four highest-scoring problems are that same gap on four screens: what the shop still needs before it may legally sell (P1) · what this click is about to do (P2) · which level this value lives at (P3) · where this data came from (P4). P5 is the same gap applied to people.

So they are not four projects. They are one principle — **no consequential control without its consequence stated** — applied at five surfaces.

---

## Scoring

Four axes, 1–5, 20 max, all running the same direction: higher = more urgent.

| Axis | 1 | 5 |
|---|---|---|
| **Severity** | An annoyance; the task still completes | Legal, financial or security exposure |
| **Reach** | One phase, no job blocked | Most phases, blocking jobs both personas need |
| **Evidence** | Inferred from the map | Verifiable spec-vs-build gap + audit *Needs fixing* |
| **Recoverability** | Fully reversible | Not recoverable once it has happened |

**Evidence never scores 5 on merchant behaviour**, because there is none. A 5 means confirmable without talking to anyone. A 3 means the absence is verifiable but whether merchants care is not.
**Tiebreak:** higher Severity → more board jobs blocked → blocks a scope decision.

| # | Problem | Sev | Reach | Evid | Recov | **Total** |
|---|---|:--:|:--:|:--:|:--:|:--:|
| **P1** | Go-live with legal elements unset | 5 | 5 | 5 | 5 | **20** |
| **P2** | No undo on consequential actions | 4 | 4 | 5 | 5 | **18** |
| **P3** | Inheritance and scope invisible | 4 | 5 | 5 | 3 | **17** |
| **P4** | ERP origin and freshness invisible | 4 | 5 | 5 | 2 | **16** |
| **P5** | Permissions have no home | 4 | 5 | 3 | 3 | **15** |
| **P6** | Setup has no sequence or end | 3 | 4 | 3 | 2 | **12** |
| **P7** | No fast path for repeat work | 3 | 4 | 4 | 1 | **12** |
| **P8** | AI panel unfinished and unscoped | 3 | 3 | 4 | 1 | **11** |
| **P9** | Preview is not trustworthy | 3 | 3 | 3 | 2 | **11** |
| **P10** | Two vocabularies | 2 | 3 | 4 | 1 | **10** |

---

## P1 — 20/20

> **A DACH shop owner needs a way to know what the shop still needs before it may legally sell, because setup lists five operational tasks and no legal ones, and nothing is checked before publish.**

- **Evidence** — S1-01 (5 of 5 complete, non-compliant day one — highest-severity finding), S1-02, S1-07, S2-01 (no market field; silent `language:"German", taxIncluded:true`), S3-06, W3.1–W3.6 *Needs fixing*, §9.1
- **Blocks** — *each step confirms it is verified* · *a check that flags what is missing* (**no surface exists**)
- **Bets** — B4, B5, C3; A6 needs the audit's caveat: deferring a domain is sound, deferring a legal requirement is not
- **Solved when** — a shop cannot publish with a mandatory element unset, and merchants can name what makes their shop legally ready
- **Next** — B4's question verbatim to eight merchants: *"What makes this shop legally ready to sell in Germany?"*

## P2 — 18/20

> **A shop owner or staff member needs a way to undo a change to a live storefront, because role, 2FA and publish controls commit on one click and there is no undo anywhere in the build.**

- **Evidence** — S1-03 (instant-apply role and 2FA, no confirmation), S3-03 (version picker ≠ undo at the moment of the mistake), S3-11, S2-03, H3.2/H3.5/H5.5 *Needs fixing*
- **Blocks** — staff: *daily upkeep quick and reversible* — the job names reversibility the product lacks
- **Bets** — B8 (maintenance mode is currently the only reversible storefront-wide control), B2
- **Solved when** — every public or security action is reversible or confirmed with what will change
- **Next** — inventory every instant-apply control in the two prototypes; sort into reversible / confirm / needs undo. A reading exercise, not research.

## P3 — 17/20

> **A multi-shop merchant needs a way to tell whether a value is inherited or overridden and what else a change touches, because no screen marks inheritance per property or names a blast radius.**

- **Evidence** — S3-01 (the `Inherits global` state exists in the prototype, behind a 24 px tooltip-only icon), S3-02, S1-13, W2.2/W2.3/W2.4 *Needs fixing*, §6.4
- **Blocks** — *see what still inherits* · *change the shared basis once* · *one view of each shop* · staff: *know what I may change*
- **Bets** — **A8 is untestable today** (inheritance can't be worked through on a panel that never shows it), B1, B3, B7, C9
- **Solved when** — inherited vs overridden readable per property; global changes name what they affect
- **Next** — surface the inheritance state the prototype data **already holds**. Affordance problem before feature problem.

## P4 — 16/20

> **A merchant needs a way to tell which values come from WaWi and when they last arrived, because no field carries an origin marker and no screen shows sync freshness.**

- **Evidence** — S1-04, S1-06, S2-02 (*"Select category"* — most consequential decision, least explained), S3-05 (four grey tiles: unsynced, unselected and placeholder are indistinguishable), W1.1 *Needs fixing* on all three screens
- **Blocks** — *connect the ERP on day one* · *preview with my own products* · *one view of each shop*
- **Bets** — A5 (can merchants predict what a category selection pulls in? today, no)
- **Solved when** — every field states origin; every mirror states freshness; empty states say which empty they are
- **Next** — add origin and freshness to the three states that already exist. No new screens.

## P5 — 15/20

> **A shop owner needs a way to hand the shop to a colleague with scoped access, because setup has no invitation step and no screen states what a role may change.**

The observed workaround is sharing the login. Six of seven staff jobs depend on a permission model the product does not visibly have.

- **Evidence** — no "invite your team" step on the checklist, W2.2 *Needs fixing*, no approval state, no owner-only markers, S1-03/S1-05 (*Require 2FA for all admins* on while two members show 2FA off), C8
- **Blocks** — 2 owner jobs + 6 of 7 staff jobs
- **Bets** — B10; the board's split: *Setup* defines access, *Manage* maintains it
- **Solved when** — handoff without shared credentials; a staff member can answer "what may I change here?" from the screen they're on
- **Next** — **decision before design:** is a roles model in MVP? It gates six jobs.

## P6 — 12/20

> **A first-time merchant needs a way to work through setup in a sequence that ends, because Setup holds four unrelated jobs — branding, commerce, access, compliance — with no order and no completion state.**

- **Evidence** — 5 of 16 owner jobs, 6 of 7 staff jobs and the densest audit cluster in one column; S1-08 (the checklist sits in a narrow rail behind three dense tables — laid out for the returning operator); S3-12; §3.1; §6.7 BUILD
- **The comparison is the finding** — everything that makes *Create* work (three fields, a safe default, explicit permission to defer) is absent one phase later
- **Bets** — A3, A1, A7
- **Next** — split the stage on the board: *Brand* / *Commerce readiness* / *Access*. An hour's work that changes what the next statements are about.

## P7 — 12/20

> **A merchant adding a second storefront needs a way to start from an existing shop, because nothing in the product duplicates a configuration.**

- **Evidence** — S1-12 ("the central promise of the multi-shop model"), S2-06, S2-07, H7.1/H7.2 *Needs improvement* on all three screens, §3.1
- **Blocks** — *reuse my first shop's setup* · staff: *create a campaign shop from an existing one* · the ARC-17 preset-reuse jobs for Modify and Manage, **not yet drafted**
- **Bets** — A4 (cannot be tested as written while no duplicate action exists), B9
- **Next** — draft the two missing preset-reuse jobs. ARC-17 already tells you their shape.

## P8 — 11/20

> **A merchant describing their brand needs a way to run the AI theme setup, because the panel has no submit control, no progress state and no summary of what changed.**

- **Evidence** — S3-04; §6.3/§6.7 BUILD (setup-wide "Shop Lead") against §9.1 (theme-scoped AI is the MVP line)
- **Bets** — **A7 as narrowed by the audit:** theme-scoped AI is enough. Riskiest bet in the programme; changes MVP scope; ⚑ ask first
- **Next** — two separate moves: **fix the button now** (a bug), and Wizard-of-Oz a chat-guided setup to answer A7. Don't let the second block the first.

## P9 — 11/20

> **A merchant about to publish needs a way to see exactly what customers will get, because the preview renders a different brand than the shop being edited and offers two of the four defined breakpoints.**

- **Evidence** — S3-08 (header says *Lili*, preview renders *L'alouette*), S3-10 (2 of 4 tiers: 360 / 768 / 1024 / 1440, with a nav change at 768), W2.6
- **Blocks** — *preview exactly what customers see before it hits real traffic*
- **Next** — confirm whether S3-08 is a prototype data bug or a real binding error. Five minutes, and it decides whether this is a defect or a design problem.

## P10 — 10/20

> **A non-technical merchant needs a way to understand every label without training, because the interface mixes developer vocabulary, two languages and inconsistent naming.**

- **Evidence** — S1-09 ("frontend"; "Upgrade Edition" names no edition), S1-10 (German placeholder in an English UI; "1 members"), S1-11, S3-09, S3-07, H2.1/H2.3/H4.1/H2.5; C2 (storefront locale and admin language share one control)
- **Next** — worth doing, but *after* P6 splits Setup, since that renames things anyway.

---

## What to do with this

**Sequencing.** P1–P4 are one workstream, not four — same principle, four surfaces. Cheaper together, and it produces a consistent product rather than four patched screens.

**Blocked on a decision, not design:** P5 (roles in MVP?) · P8 (A7 — theme-scoped or setup-wide? ⚑) · P7 (theme vs preset — confirmed as preset, needs sign-off).

**Testable this week:** B4 (eight merchants, one question) · B5 (ten real catalogues against the tax control) · B3 (code settings errors by type).

**Agreement with the audit.** P1–P4 reproduce its own top four in the same order — two methods, same answer. Two changes: **P5 is new**, visible only once the staff lane is on the map; **the AI panel drops from audit #5 to P8**, because the missing button is a bug while A7 is a decision.

**What this cannot tell you.** Whether any of these stops a merchant. Every Severity score is reasoned from the spec and the build, not observed. The first moderated session will reorder this table — that is the point of running one.

**Coverage.** 30 of the audit's 32 numbered findings are clustered here. S2-04 (no name/subdomain rule stated before typing) and S2-05 (no corner close or Escape on the *Add shop* modal) are deliberately below threshold — backlog items, not problem statements.

---

## Sources

`2 define/customer-journey-map.md` · `5 test/audit-findings-log.md` · `5 test/heuristic-evaluation-checklist.md` · `2 define/assumptions/` (A1–A10, B1–B10, C1–C10) · `2 define/ARC-17 Theme & Preset System.md` · `2 define/breakpoint grid spacing/storefront-layout-system.md` · `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` §3.1, §3.2, §6.3, §6.4, §6.7, §8.12, §8.13, §8.17, §9.1, §9.2 · `4 design prototype/*.html` · FigJam `Z8PycuHpuIAHW2GxOwC5Az` → **JTBDs** (`53:436`)
