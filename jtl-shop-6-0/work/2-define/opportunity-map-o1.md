# Opportunity Map — O1 · Nothing reaches customers unchecked

**Method:** opportunity solution tree (outcome → opportunities → solutions → assumption tests).
**Scope:** the Publish phase of `2 define/customer-journey-map.md`, plus the Setup moments that feed it.
**Date:** 19 Sep 2026 · **Numbering:** OPP-A…D and their sub-branches; SOL-1…4; AT-1…4.
**Status:** hypothesised. See *How to read this* — no opportunity here came from a merchant.

---

## The outcome

> **Merchants publish only what they have been shown is ready.**

- **Product metric** — shops published with a mandatory element unset (target: zero); share of publishes preceded by a cleared readiness check
- **Business result** — compliance exposure moves off the merchant; setup-related partner and support tickets fall; "go live without a partner" becomes defensible rather than asserted
- **Today** — a merchant can complete 5 of 5 checklist items, publish, take real orders, and be non-compliant from the first hour, having been shown nothing

---

## How to read this

An opportunity solution tree is normally built from **interview snapshots** — opportunities are things real customers said they needed. This one is not. Discovery has had zero merchant contact, so every opportunity below is derived from the build, the Pflichtenheft and the heuristic audit.

That makes the evidence tag the most important thing on the tree:

| Tag | Means | Confirmable by |
|---|---|---|
| **[gap]** | The spec requires something the build does not do | Reading the spec and the build. No merchant needed. |
| **[need?]** | Assumes merchants *experience* that gap as a need | An interview. Not yet run. |

**Every opportunity is at least a [gap]. None is yet a confirmed [need?].** Treat the tree as a map of where to look, not a map of what is true. The first five merchant interviews should reorder it.

**Opportunities are short need phrases in the merchant's terms** — verb first, four to ten words, with a *without…* qualifier where the condition matters. Reference shape: *make local groceries affordable* · *buy local food without changing their existing shopping routine* · *help consumers live more sustainably*.

Two rules keep them honest:

- **No barrier in the statement.** It goes in the evidence line underneath. That is what separates these from `problem-statements.md`, which uses the POV template *[user] needs a way to [goal] because [barrier]* — a problem statement names the design gap; an opportunity names the need the merchant would recognise as theirs.
- **No solution in the statement.** *"Know what's still missing"* is an opportunity; *"see a readiness checklist"* is SOL-2 wearing an opportunity's clothes.

---

## The tree

```
OUTCOME  Merchants publish only what they have been shown is ready
│
├── OPP-A ★ TARGET  Know what's still missing, without working it out myself
│   ├── A1  Know which legal rules apply to my shop            [gap]
│   ├── A2  Tell required steps from optional ones             [gap]
│   └── A3  Get the rules for the market I sell in             [gap]
│
├── OPP-B  See what customers will see, before they see it
│   ├── B1  Trust the preview is my shop                       [gap]
│   ├── B2  Check every screen size customers use              [gap]
│   ├── B3  Tell a draft from the live shop                    [gap]
│   └── B4  See my real products, not stand-ins                [gap]
│
├── OPP-C  Know what publishing changes, before committing
│   ├── C1  Tell the public action from the routine ones       [gap]
│   ├── C2  Be told what's about to change                     [gap]
│   ├── C3  Take a publish back              → outcome O2      [gap]
│   └── C4  Know how many storefronts it reaches               [gap]
│
└── OPP-D  Know the change landed, without going to look
    ├── D1  See what the publish changed                       [gap]
    └── D2  Know something's happening while I wait            [gap]

TARGET BRANCH  OPP-A
├── SOL-1  Pre-flight gate at publish
├── SOL-2  Requirements as non-deferrable checklist items
├── SOL-3  Market-derived requirement set
└── SOL-4  Persistent readiness panel
```

---

## OPP-A ★ TARGET

> ### Know what's still missing, without working it out myself

**A1 · Know which legal rules apply to my shop**
**[gap]** — no screen names consent management, legal notice, right of withdrawal or unit pricing. S1-01, S1-07, W3.1/W3.5/W3.6 *Needs fixing*; §9.1 mandates all four for DE.

**A2 · Tell required steps from optional ones**
**[gap]** — the checklist styles required and optional identically. S1-02, W3.2 *Needs fixing*.

**A3 · Get the rules for the market I sell in**
**[gap]** — no country or market is ever collected. S2-01, W3.3/W3.4 *Needs fixing*; the prototype defaults `language:"German", taxIncluded:true` unasked; §8.12 derives currency from a region group that has no control anywhere (C1).

**Journey moment.** *"When I think the shop is ready, I want a check that flags what is missing or broken, so I can go live without an embarrassing first day."* — a job with **no surface in the product at all**.

---

## OPP-B

> ### See what customers will see, before they see it

**B1 · Trust the preview is my shop**
**[gap]** — the top bar reads **Lili** while the preview header renders **L'alouette**. S3-08. A five-minute check: prototype data bug, or a real binding error?

**B2 · Check every screen size customers use**
**[gap]** — two of four defined tiers can't be previewed. S3-10; `storefront-layout-system.md` defines 360 / 768 / 1024 / 1440, with a nav pattern change at 768.

**B3 · Tell a draft from the live shop**
**[gap]** — W2.6 *Needs improvement*.

**B4 · See my real products, not stand-ins**
**[gap]** — product areas render as flat coloured tiles. S3-05. This is the P4 dependency: a merchant cannot judge readiness against placeholder art.

---

## OPP-C

> ### Know what publishing changes, before committing

**C1 · Tell the public action from the routine ones**
**[gap]** — *Apply to storefront* shares a toolbar strip with the page selector, device toggles and version picker, differentiated only by fill colour. S3-11.

**C2 · Be told what's about to change**
**[gap]** — no confirmation step. S3-03.

**C3 · Take a publish back**
**[gap]** — no undo exists anywhere in the build; a version picker is not undo at the moment of the mistake. S3-03, H3.2/H3.5 *Needs fixing*. **Belongs to outcome O2** — listed because it shapes this branch, not solved here.

**C4 · Know how many storefronts it reaches**
**[gap]** — blast radius is never named. S3-02, W2.4 *Needs fixing*.

---

## OPP-D

> ### Know the change landed, without going to look

**D1 · See what the publish changed**
**[gap]** — no result summary appears. H1.4 *Needs fixing* on the theme editor.

**D2 · Know something's happening while I wait**
**[gap]** — no action shows it is working. H1.2 *Needs fixing*.

---

## Why OPP-A is the target

Not because it is the biggest branch — B and C have more sub-opportunities. Three reasons:

1. **It is the only branch that fails silently.** A merchant notices a wrong preview (B), an accidental publish (C) and a publish that seems not to land (D) — all self-reporting failures. A's failure surfaces weeks later, via a customer complaint or a regulator, by which point the exposure has happened.
2. **It carries the only legal and financial consequence** in the whole outcome. P1 scored 20/20 and is the heuristic audit's own #1 of 32 findings, independently reached.
3. **It is the branch the outcome is named after.** "Shown it is ready" is A. B, C and D make publishing *trustworthy*; A makes it *correct*. Without A, solving B–D produces a merchant who is confidently non-compliant.

**Explicitly deferred, not dismissed:** B1 is a five-minute check (is it a prototype data bug or a real binding error?) and should be done regardless. C3 belongs to outcome O2, where undo is the whole point — solving it here would duplicate that work.

---

## Four competing solutions for OPP-A

> ### Know what's still missing, without working it out myself

These compete — they act at different moments with different mechanisms. SOL-1 and SOL-2 can combine; SOL-3 is the only one that addresses the root; SOL-4 is the weakest alone.

| | Acts at | Blocks the merchant? | Fixes the root? | Effort |
|---|---|---|---|---|
| **SOL-1** Pre-flight gate | Publish | Yes, for mandatory items | No — catches, doesn't prevent | Medium |
| **SOL-2** Non-deferrable checklist items | Setup | Yes, by sequence | No — still a hand-kept list | Low |
| **SOL-3** Market-derived requirement set | Create → everywhere | No | **Yes** | High |
| **SOL-4** Persistent readiness panel | Always | No | No | Low |

### SOL-1 · Pre-flight gate at publish
*Apply to storefront* runs a check, lists what is unmet, and refuses to publish while a mandatory element is unset — the audit's own recommended fix alongside SOL-2.

- **Also solves** — C1 and C2 come along free: a gate turns publish into a decision with a confirmation
- **Doesn't solve** — a merchant who reaches the gate with six things unset has still wasted the whole setup; and it says nothing about *which* market's rules apply (A3)
- **Blocking question, not an assumption** — a gate implies the platform is vouching for legal readiness. **Who carries that liability?** W3.6 ("merchant responsibility stated") is rated *Needs fixing* precisely here. This needs a legal answer before a design one.

### SOL-2 · Requirements as non-deferrable checklist items
Extend the five-item checklist with the legal and market steps, marked as required, so the gap never opens.

- **Also solves** — A2 directly: required vs optional becomes a visible property of the list
- **Doesn't solve** — completion pressure. The audit's own caveat on A6: deferring a domain is sound, deferring a legal requirement is not — but a longer mandatory list is exactly what A1's 60% completion bet is exposed to
- **Cheapest of the four**, and the one that could ship first

### SOL-3 · Market-derived requirement set
Collect country/market at shop creation, and derive the required element list — and currency, tax treatment and locale — from it, per shop.

- **Also solves** — A3 at the root, C1's currency/region-group divergence (§8.12), part of C2's locale problem, and S2-01's silent German default
- **Doesn't solve** — anything on its own: it produces a correct list that still needs SOL-1 or SOL-2 to be *shown*
- **The real argument for it** — SOL-1 and SOL-2 both assume someone hand-maintains a list of what DE, AT, CH and GB require. SOL-3 is the only version that survives the second market.
- **Cost** — it touches creation, settings and the tax model at once, and collides with A4's 15-minute target

### SOL-4 · Persistent readiness panel
A "what this shop still needs" surface on the Shop Admin shell, updating as configuration lands.

- **Also solves** — S1-08, the dashboard being laid out for the returning operator rather than the merchant still in setup
- **Doesn't solve** — anything if merchants don't read it. This is the solution most dependent on B4 being wrong.

---

## Assumption tests

The leave-behind assumption under each solution, and the cheapest way to find out.

| # | Solution | Riskiest assumption | Test | Cost |
|---|---|---|---|---|
| **AT-1** | SOL-1 | Merchants accept being blocked from publishing rather than working around it | Add the gate to a prototype and run 6 moderated go-live tasks; watch for workaround-seeking | Medium |
| **AT-2** | SOL-2 | A longer mandatory list doesn't depress completion | Split completion rates by list length in the prototype; compare against A1's ≥60% placeholder | Low |
| **AT-3** | SOL-3 | Market can be collected at creation without breaking the three-field moment | Add the field to the *Add shop* modal and re-time it against A4's 15-minute placeholder. Separately: ask engineering C1's question — *what happens when a merchant picks `USD` on a EUR-priced catalogue?* If the answer is "labels change, numbers don't", the control is mislabelled and SOL-3 is mandatory, not optional | Low |
| **AT-4** | SOL-4 | Merchants read an ambient panel they were not sent to | Instrument it; or cheaper, infer from B4 — merchants who believe compliance is handled have no reason to look | Low |

### The one question that decides the shape

**B4, verbatim, to eight merchants: *"What makes this shop legally ready to sell in Germany?"***

- If they point at the tax toggle or say *"the platform does it"* → they will not seek this information out. **SOL-4 is dead and SOL-1's gate is required**, because only an interruption reaches someone who isn't looking.
- If they name consent management, legal notice, right of withdrawal and unit pricing → they are already looking, and **SOL-2 plus SOL-4** may be enough without blocking anyone.

One question, eight merchants, and it selects between a blocking gate and an ambient panel. Run it before designing either.

---

## What is deliberately not on this tree

- **Undo (C3)** — belongs to outcome O2. Listed as an opportunity because it shapes the branch; not solved here.
- **The AI "Shop Lead"** — a readiness check is one of the two shapes A7's assistant could take. Until A7 has an owner and a date, designing the check as an AI surface would pre-decide it.
- **Anything in Onboarding or Create** except A3, which has to be there because the market must be collected at creation to be derivable later.
- **Numbers.** A1's 60%, A4's 15 minutes — placeholders, both. Capturing real 5.0 baselines is still one of the four things blocking discovery. Present the indicators; leave the targets blank.

---

## Sources

`2 define/customer-journey-map.md` · `2 define/problem-statements.md` (P1, P2, P9) · `5 test/audit-findings-log.md` (S1-01, S1-02, S1-07, S1-08, S2-01, S3-02, S3-03, S3-05, S3-08, S3-10, S3-11; W2.4, W2.6, W3.1–W3.6; H1.2, H1.4, H3.2, H3.5) · `2 define/assumptions/` (A1, A4, A6, A7, B4, C1, C2) · `2 define/breakpoint grid spacing/storefront-layout-system.md` · `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` §8.12, §9.1 · `4 design prototype/*.html` · FigJam `Z8PycuHpuIAHW2GxOwC5Az` → **JTBDs** (`53:436`)
