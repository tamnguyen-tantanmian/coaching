# Audit Findings Log — Heuristic Evaluation

**Reviewed:** the three screens in *Current Screen Flow / Create shop* on the ainavio FigJam board
**Against:** `5 test/heuristic-evaluation-checklist.md` — Nielsen's 10 heuristics (50 criteria) plus project watch-outs W1–W3 (17 criteria)
**Date:** 22 Aug 2026
**Reviewer:** Claude, single-evaluator pass

| Screen | What it is | Source file |
|---|---|---|
| **S1** | Dashboard — setup checklist, Multi-shop management, Team & 2FA, Payment | `Admin Setting+ Theme Setup (update by AnhTruong).html` |
| **S2** | *Add shop* modal over the dashboard | same |
| **S3** | Theme setup — layer tree, storefront preview, element inspector | `Shop Setup Platform-10.08.2026.html` |

**Rating scale**

| Rating | Meaning |
|---|---|
| **Needs fixing** | Breaks the criterion; a user can be misled, blocked, or cause damage |
| **Needs improvement** | Partly satisfied, or satisfied in a way that will not hold up |
| **Good** | Satisfies the criterion as designed |
| *Not assessable* | Cannot be judged from a static screen (error states, timings, tooltip contents) |

**Method note.** Screens were read at full resolution and cross-checked against the prototype HTML, so findings about behaviour (what a control does when clicked, whether an Undo exists) come from the markup rather than being inferred from the picture. Where the markup is silent the finding is marked *Not assessable* rather than guessed.

---

## S1 — Dashboard

### S1-01 · W3.1 · Needs fixing

> "Can a merchant reach 'live' with any legally required element still unset?"

The checklist is *Create your shop · Customize your theme · Set up payments · Add a shipping zone · Connect a custom domain*. Nothing about consent management, legal notice, withdrawal instructions, tax configuration, or price-display mode appears anywhere in it — yet the spec makes all of them mandatory for DE/EU operation. A merchant can complete 5 of 5, see the checklist finish, and be non-compliant on day one. This is the highest-severity finding in the audit.

### S1-02 · W3.2 · Needs fixing

> "Are compliance-critical steps distinguishable from genuinely optional ones?"

All five tasks are styled identically — same checkbox, same *Set up* affordance, same weight. Nothing separates "you legally must" from "you probably want to". Compounding this: the tasks are **manually toggleable** (the panel's own copy reads "Toggle a task to mark it complete"), so completion reflects what the merchant ticked, not what is actually configured.

### S1-03 · H3.5 + H5.5 · Needs fixing

> "Are destructive actions reversible, or at minimum confirmed with what exactly will be lost?"
> "Are irreversible actions separated from routine ones so they can't be hit by accident?"

In the Team table, each member's role is an inline segmented control (`Owner | Staff | External`) and each 2FA state is a clickable pill — both wired to instant-apply handlers, with no confirmation step and no Undo anywhere in the file. Turning off a colleague's 2FA, or demoting an Owner, is a single accidental click sitting in the same visual register as the surrounding read-only table content.

### S1-04 · H1.5 + W1.3 · Needs fixing

> "Are background processes (syncs, imports, publishes) visible while they run and after they finish?"
> "When a value is a synced mirror, is the last sync time or freshness shown?"

The dashboard shows per-shop product counts and status but says nothing about the WaWi connection: no last-sync time, no sync health, no indication that this data is a mirror of the ERP. On a platform whose central premise is ERP-led data, the merchant's home screen gives no answer to "is my data current?"

### S1-05 · H9.5 + H5.3 · Needs fixing

> "Do warnings distinguish 'this will fail' from 'this is unusual but allowed'?"
> "Are constraints shown *before* input, not after submission?"

*Require 2FA for all admins* is toggled **on**, while the table below shows two members with 2FA **Off** (Leo Pham, Staff; Studio Bright, External). Either the rule is not enforced or "admins" excludes those roles — the screen defines neither, and raises no warning about the apparent contradiction. For a security control, an unresolvable state like this is worse than no control.

### S1-06 · W1.1 · Needs fixing

> "Is it visible, per field, whether this value comes from WaWi or lives in the shop?"

No field anywhere on the screen carries an origin marker. Shop-owned settings (payout account, 2FA policy) and ERP-derived values (product counts) are presented with identical treatment.

### S1-07 · W3.5 + W3.6 · Needs fixing

> "When a legal element is missing, does the message explain the obligation rather than just flagging an empty field?"
> "Is the merchant's own tax and legal responsibility stated where they'd assume the platform handles it?"

Neither surface exists on this screen. Given that the product is sold on ease of setup, the absence of any statement about where platform responsibility ends is itself a risk.

### S1-08 · H8.2 + H8.4 · Needs improvement

> "Is the primary task obvious within a couple of seconds of landing?"
> "Is visual weight going to the most important element, not the most decorated one?"

For a merchant who has not gone live, *Finish setting up your shop* is the only task that matters — and it sits in a narrow right rail, visually outweighed by three dense full-width tables. The screen is laid out for the returning operator, not the one still in setup.

### S1-09 · H2.1 + H2.3 · Needs improvement

> "Would the intended user recognise every label and term on this screen without training?"
> "Are internal system names, database field names, or team shorthand showing through?"

"Multiple-shops management" and "Manage every frontend, its configuration and assigned team from one place" — *frontend* is developer vocabulary, and the spec's target user is explicitly non-technical. *Storefront*, used elsewhere in the same product, is the merchant-facing word. "Upgrade Edition" in the top bar names no edition and no benefit.

### S1-10 · H2.5 · Needs improvement

> "Are numbers, dates, currencies and units in the format the user's market expects?"

The search field placeholder is German — "Suche Apps, Hilfe und mehr" — inside an otherwise entirely English interface. Separately, "1 members" is unpluralised.

### S1-11 · H4.1 + H4.2 · Needs improvement

> "Does the same concept use the same word everywhere in the product?"
> "Do the same components behave the same way on every screen they appear on?"

Shops are called "Multiple-shops management" here, "Your shops" in the sibling prototype, and "storefront" in the *Add shop* modal. More consequentially, the segmented control is a passive selector in most of the product but an instant-apply mutator in this table — same component, different consequence, no visual distinction.

### S1-12 · H7.2 + H7.4 · Needs improvement

> "Are there keyboard shortcuts, bulk actions, or duplication for repetitive work?"
> "Can frequent settings be saved, templated, or reused instead of rebuilt?"

⌘K search is present and welcome. But there is no multi-select on members or shops, and no way to duplicate an existing shop's configuration as the starting point for the next one — which is the central promise of the multi-shop model.

### S1-13 · W2.3 + W2.4 · Needs improvement

> "Is inherited-versus-overridden distinguishable at a glance, per property?"
> "Before a global change lands, is the blast radius named ('affects 4 storefronts')?"

The Payment section states its scope well — "Global payment providers and payout settings applied to every shop by default" — but nothing shows which shops have since overridden it. The 2FA toggle says "for all admins" without saying how many people that is.

**Notable Good on S1:** the per-shop `Live`/`Draft` dots, the `2 of 5 complete` counter with progress bar, the per-member `Shops` column (real scope visibility), and 2FA defaulting to on.

---

## S2 — *Add shop* modal

### S2-01 · W3.4 + W3.3 · Needs fixing

> "Do market-specific requirements follow the shop's country, not the admin's UI language?"
> "Are B2C gross and B2B net price displays correct for the market this shop targets?"

The modal collects three things: shop name, category, domain. There is no country, market, currency, or language field. The prototype's own state object holds `language: "German", taxIncluded: true` as defaults — so every new storefront silently inherits a German, tax-inclusive configuration that the merchant never saw and was never asked about. For a product positioning EU expansion as a core requirement, market belongs at creation time.

### S2-02 · H2.1 + W1.1 · Needs fixing

> "Would the intended user recognise every label and term on this screen without training?"
> "Is it visible, per field, whether this value comes from WaWi or lives in the shop?"

The middle field reads only **"Select category"** with an ⓘ icon; the ERP relationship — that these are WaWi categories and this selection determines which products the storefront carries — is hidden behind a tooltip. This is the most consequential decision in the modal and the least explained. The spec's own phrasing ("Fetch products from ERP by categories") is clearer than the UI's.

### S2-03 · H1.4 + H1.3 · Needs improvement

> "After an action completes, is the result visible — or do I have to go looking for it?"
> "Is progress through a multi-step task shown, including how much is left?"

Nothing states what *Create shop* produces: a draft, a live storefront, a background product sync of unknown duration? The modal presents itself as a single self-contained action when it is in fact the first step of a longer sequence.

### S2-04 · H5.2 + H5.3 · Needs improvement

> "Are impossible or invalid options disabled rather than allowed and then rejected?"
> "Are constraints shown *before* input, not after submission?"

Only *Shop name* carries a required marker, leaving category's necessity ambiguous. And since the shop list shows URLs of the form `lalouette.myshop.co`, the name apparently derives a subdomain — but no uniqueness or character rule is stated before typing.

### S2-05 · H3.1 · Needs improvement

> "Is there a visible way out of this screen that doesn't commit the change?"

*Cancel* is present and clearly distinguished from the primary action, which is good. There is no close affordance in the top corner, and the markup shows no Escape handler — so the modal is exitable but only by the one route.

### S2-06 · H7.1 + H7.4 · Needs improvement

> "Is there a fast path for someone doing this for the twentieth time?"
> "Can frequent settings be saved, templated, or reused instead of rebuilt?"

No "duplicate an existing shop" path. For the operator running four storefronts — the target customer — every new shop starts from nothing.

### S2-07 · W2.2 · Needs improvement

> "Does an edit state the scope it will apply at — global, shop, page?"

The modal never names which account or tenant the new storefront joins, or what it inherits from the global level.

**Notable Good on S2:** "Optional · set up later" on the domain field is exactly the right microcopy for the step most likely to need outside help; the dimmed dashboard stays visible behind the modal, preserving context; three fields only, with the primary task unmistakable.

---

## S3 — Theme setup

### S3-01 · W2.3 · Needs fixing

> "Is inherited-versus-overridden distinguishable at a glance, per property?"

The inspector for *Announcement bar* shows Typography values as plain segmented controls — Font `Subheading`, Weight `Default`, Letter spacing `Normal`, Case `Default`. Nothing indicates whether a value is inherited from the global theme or overridden here. The prototype does contain an `Inherits global` state and a `Customized` badge with a *Reset to default* control, but that control is a 24 px icon button whose only label is a `title` tooltip, and none of it is visible in the panel as shown. The assumption that merchants will work through inheritance (A8) cannot hold on a panel that never shows inheritance.

### S3-02 · W2.4 · Needs fixing

> "Before a global change lands, is the blast radius named ('affects 4 storefronts')?"

The primary action is **Apply to storefront** — singular, unqualified. In a product where theme values cascade across storefronts, the merchant cannot tell from this button whether they are changing one shop or every shop that inherits the value they just edited.

### S3-03 · H3.2 + H3.5 · Needs fixing

> "Can the last action be undone — and is the undo discoverable at the moment it's needed?"
> "Are destructive actions reversible, or at minimum confirmed with what exactly will be lost?"

There is no Undo control anywhere in the file, and no confirmation on *Apply to storefront*. The version dropdown (`Aug 06, 2026, 04:42 PM · Draft`) implies recoverable history, which is the right instinct — but recovery through a version picker is not the same as undo at the moment of the mistake, and the AI panel below can restyle many properties at once.

### S3-04 · H1.2 + H1.4 · Needs fixing

> "Does every action that takes more than a moment show that it's working?"
> "After an action completes, is the result visible — or do I have to go looking for it?"

The *AI theme setup* panel offers a prompt textarea ("Describe your brand or paste a reference link…") and an *Import image* button — and **no submit control**. There is no generate button, no processing state, and no summary of what the AI changed once it has run. The single most novel interaction on the screen has no visible way to start it and no way to see what it did.

### S3-05 · W1.1 + W1.3 · Needs fixing

> "Is it visible, per field, whether this value comes from WaWi or lives in the shop?"
> "When a value is a synced mirror, is the last sync time or freshness shown?"

The preview's *Products* section renders four flat coloured tiles — no names, prices, or images. A merchant cannot distinguish "products haven't synced from WaWi yet" from "no category selected" from "this is placeholder art in a preview". Empty product states are exactly where the ERP relationship needs to be legible.

### S3-06 · W3.1 · Needs fixing

> "Can a merchant reach 'live' with any legally required element still unset?"

The layer tree contains a `FOOTER > Footer` node and the preview shows no cookie or consent banner, no legal links. Nothing in the publish path checks for the mandatory DACH/EU elements before *Apply to storefront* commits.

### S3-07 · H2.5 · Needs fixing

> "Are numbers, dates, currencies and units in the format the user's market expects?"

The header reads **"Last publish 11/12/2026"** — ambiguous between 11 December and 12 November, in a DACH-first product where the two conventions collide. It is also inconsistent with the draft timestamp in the same toolbar (`Aug 06, 2026, 04:42 PM`), which uses a different format *and* an earlier date than the "last publish" of a shop still marked Draft.

### S3-08 · H4.2 · Needs fixing

> "Do the same components behave the same way on every screen they appear on?"

The shop is named **Lili** in the top bar, breadcrumb and page header — but the storefront preview's own header renders **L'alouette**. Whatever the cause in the prototype, a preview that shows a different brand than the shop being edited undermines the one thing a preview is for.

### S3-09 · H4.1 · Needs improvement

> "Does the same concept use the same word everywhere in the product?"

Four words for one concept in one toolbar: *Apply to storefront* (button), *Last publish* (header), *Draft* (status chip and version selector), plus `publishShop` in the markup. Decide whether the model is apply/revert or publish/draft and use one vocabulary.

### S3-10 · H7.2 + H4.4 · Needs improvement

> "Are there keyboard shortcuts, bulk actions, or duplication for repetitive work?"
> "Does the screen follow the platform conventions users bring from other tools?"

The preview offers two device widths. The project's own `storefront-layout-system.md` defines four breakpoint tiers — Mobile 360, Tablet 768, Desktop 1024, Wide 1440 — with layout changes at each boundary, including a nav pattern change at 768. A merchant cannot preview two of the four tiers their theme will actually render in.

### S3-11 · H5.5 · Needs improvement

> "Are irreversible actions separated from routine ones so they can't be hit by accident?"

*Apply to storefront* — the one action with public consequences — sits in the same toolbar strip as routine view controls (page selector, device toggles, version picker), differentiated only by fill colour.

### S3-12 · H10.1 + H10.3 · Needs improvement

> "Does the screen work without help — and if not, is help right where the confusion happens?"
> "Are the steps concrete and specific to the user's actual task?"

The AI panel's placeholder text is the only guidance for the least familiar control on the screen. "Describe your brand or paste a reference link" does not say what will change, how much, or whether it can be undone.

**Notable Good on S3:** breadcrumb plus shop name plus `Draft` chip make context unambiguous; the version selector shows an explicit draft timestamp; `Desktop preview` labels the canvas; the layer tree's `HEADER / TEMPLATE / FOOTER` grouping matches how merchants think about a page; typography options are semantic (`Subheading / Heading / Body`) rather than raw values, which protects the design system.

---

## Coverage matrix

All 67 criteria × 3 screens. `—` = criterion does not apply to that surface; `n/a` = not assessable from a static screen.

### Nielsen 1–5

| # | Criterion (abbrev.) | S1 | S2 | S3 |
|---|---|---|---|---|
| H1.1 | State visible without clicking | Good | Good | Good |
| H1.2 | Slow actions show working | n/a | n/a | **Needs fixing** |
| H1.3 | Multi-step progress + remaining | Good | Needs improvement | Good |
| H1.4 | Result visible after action | n/a | Needs improvement | **Needs fixing** |
| H1.5 | Background processes visible | **Needs fixing** | n/a | Needs improvement |
| H2.1 | Labels recognisable untrained | Needs improvement | **Needs fixing** | Needs improvement |
| H2.2 | Order matches real-life task | Good | Good | Good |
| H2.3 | No internal names leaking | Needs improvement | Good | Good |
| H2.4 | Icons/metaphors read correctly | Good | Good | Good |
| H2.5 | Market number/date/unit formats | Needs improvement | — | **Needs fixing** |
| H3.1 | Visible non-committing exit | Good | Needs improvement | Good |
| H3.2 | Undo discoverable when needed | **Needs fixing** | — | **Needs fixing** |
| H3.3 | Pause / save / resume | Good | — | Good |
| H3.4 | Cancel vs confirm distinct | — | Good | — |
| H3.5 | Destructive reversible/confirmed | **Needs fixing** | — | **Needs fixing** |
| H4.1 | One word per concept | Needs improvement | Good | Needs improvement |
| H4.2 | Components behave consistently | Needs improvement | Good | **Needs fixing** |
| H4.3 | Primary/secondary placement | Good | Good | Good |
| H4.4 | Platform conventions | Good | Good | Needs improvement |
| H4.5 | Grid / type from design system | Good | Good | Good |
| H5.1 | Likely mistake is guarded | **Needs fixing** | Needs improvement | Needs improvement |
| H5.2 | Invalid options disabled | Needs improvement | Needs improvement | n/a |
| H5.3 | Constraints shown before input | Needs improvement | Needs improvement | n/a |
| H5.4 | Defaults are safe | Good | Needs improvement | Good |
| H5.5 | Irreversible separated | **Needs fixing** | Good | Needs improvement |

### Nielsen 6–10

| # | Criterion (abbrev.) | S1 | S2 | S3 |
|---|---|---|---|---|
| H6.1 | No cross-screen memory needed | Good | Good | Good |
| H6.2 | Prior values shown not re-asked | Good | Good | Good |
| H6.3 | Options visible not recalled | Good | Good | Good |
| H6.4 | Context always visible | Good | Needs improvement | Good |
| H6.5 | Returning user re-orients | Good | — | Good |
| H7.1 | Fast path for repeat use | Needs improvement | Needs improvement | Needs improvement |
| H7.2 | Shortcuts / bulk / duplicate | Needs improvement | Needs improvement | Needs improvement |
| H7.3 | Beginner path stays clear | Good | Good | Needs improvement |
| H7.4 | Settings saved / templated | Needs improvement | Needs improvement | Good |
| H7.5 | Sensible defaults | Good | Needs improvement | Good |
| H8.1 | Nothing removable | Good | Good | Good |
| H8.2 | Primary task obvious fast | Needs improvement | Good | Good |
| H8.3 | Progressive disclosure of rare detail | Good | Good | Good |
| H8.4 | Visual weight on what matters | Needs improvement | Good | Good |
| H8.5 | Text no longer than needed | Good | Good | Good |
| H9.1 | Plain-language errors, no codes | n/a | n/a | n/a |
| H9.2 | Errors say what to do next | n/a | n/a | n/a |
| H9.3 | Error appears next to cause | n/a | n/a | n/a |
| H9.4 | Work preserved on error | n/a | n/a | n/a |
| H9.5 | Warnings distinguish fail vs unusual | **Needs fixing** | n/a | Needs improvement |
| H10.1 | Works without help / help in place | Good | Needs improvement | Needs improvement |
| H10.2 | Help is contextual | Good | Good | Needs improvement |
| H10.3 | Concrete steps | n/a | n/a | Needs improvement |
| H10.4 | Help without losing state | Good | Good | Good |
| H10.5 | Help matches the product | n/a | n/a | n/a |

### Project watch-outs

| # | Criterion (abbrev.) | S1 | S2 | S3 |
|---|---|---|---|---|
| W1.1 | Field origin: WaWi vs shop | **Needs fixing** | **Needs fixing** | **Needs fixing** |
| W1.2 | WaWi fields read-only | n/a | n/a | n/a |
| W1.3 | Sync time / freshness shown | **Needs fixing** | Needs improvement | **Needs fixing** |
| W1.4 | Warns before an edit is overwritten | n/a | n/a | n/a |
| W1.5 | Points to where the change belongs | n/a | n/a | n/a |
| W2.1 | Active shop always visible | Good | Good | Good |
| W2.2 | Edit states its scope | Good | Needs improvement | **Needs fixing** |
| W2.3 | Inherited vs overridden per property | Needs improvement | — | **Needs fixing** |
| W2.4 | Blast radius named | Needs improvement | — | **Needs fixing** |
| W2.5 | Route back to inherited | n/a | — | Needs improvement |
| W2.6 | Preview vs published distinct | Good | — | Needs improvement |
| W3.1 | Can go live with legal unset | **Needs fixing** | **Needs fixing** | **Needs fixing** |
| W3.2 | Compliance vs optional distinguishable | **Needs fixing** | Needs improvement | n/a |
| W3.3 | Gross/net correct for market | n/a | **Needs fixing** | n/a |
| W3.4 | Market rules follow shop country | n/a | **Needs fixing** | n/a |
| W3.5 | Missing legal explains obligation | **Needs fixing** | n/a | n/a |
| W3.6 | Merchant responsibility stated | **Needs fixing** | n/a | n/a |

### Totals

| | S1 | S2 | S3 | Total |
|---|---|---|---|---|
| Needs fixing | 10 | 5 | 12 | **27** |
| Needs improvement | 12 | 13 | 14 | **39** |
| Good | 24 | 22 | 22 | **68** |
| Not assessable | 12 | 12 | 12 | 36 |
| Not applicable | 9 | 15 | 7 | 31 |

---

## Priority order

1. **Compliance can't be optional** — S1-01, S1-02, S2-01, S3-06. A merchant can complete setup and publish a storefront with no consent management, no legal notice, and a silently inherited German tax configuration. Fix by adding legal/market to the checklist as non-deferrable steps, and a pre-publish compliance gate.
2. **Scope and inheritance are invisible** — S3-01, S3-02, S1-13. Theme edits and *Apply to storefront* give no indication of what else they touch. Fix before multi-shop merchants arrive, or the cascade becomes a liability rather than the feature it is meant to be.
3. **No undo on consequential actions** — S1-03, S3-03. Role changes, 2FA changes and theme publishes all commit on one click with no reversal path.
4. **The ERP is invisible** — S1-04, S1-06, S2-02, S3-05. Nothing on any screen says where data comes from or when it last arrived. This is the platform's core premise and its least represented idea in the UI.
5. **The AI panel is unfinished** — S3-04. A prompt field with no submit, no progress and no result summary.
6. Everything else: vocabulary consistency, market formats, breakpoint coverage, bulk actions.

---

## Impact on the assumptions log

Two corrections to `2 define/shop-setup-candidate-assumptions.md`:

- **A7 needs narrowing.** An AI surface *does* exist — the *AI theme setup* panel on S3 — which matches the spec's MVP-relevant "AI-assisted theme setup". What is absent is §6.7's cross-cutting "Shop Lead" reachable from anywhere in the admin. A7 should read as "theme-scoped AI is enough; merchants don't need a setup-wide assistant", not "no AI is present".
- **A6 acquires a caveat.** Deferring the domain is sound (S2's microcopy is a strength). Deferring anything legally required is not. Whatever gets made deferrable needs an audit against W3.1 before A6 is tested.

---

*Criteria quoted from `5 test/heuristic-evaluation-checklist.md`. Screens read from the ainavio board, section `Current Screen Flow`, and cross-checked against the prototype HTML in `4 design prototype/`. Single-evaluator pass — Nielsen's method assumes 3–5 independent evaluators, so treat the Good ratings as least reliable.*
