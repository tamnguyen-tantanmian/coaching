# Heuristic Evaluation Checklist

Jakob Nielsen's 10 usability heuristics, written as review prompts you can run against a single screen — plus watch-outs specific to the JTL-Shop 6.0 admin and setup flow.

**How to use it.** Take one screen at a time. Walk the ten sections in order, note what fails rather than what passes, and rate each finding. The heuristics are rules of thumb, not pass/fail rules — a deliberate violation with a good reason is a decision, not a defect, so record the reasoning next to it.

**Severity scale**

| Rating | Meaning |
|---|---|
| 0 | Not a problem — disagree that this is an issue |
| 1 | Cosmetic — fix if there's spare time |
| 2 | Minor — low priority fix |
| 3 | Major — important to fix, high priority |
| 4 | Catastrophe — must fix before release |

**Finding format:** `[Screen] · [Heuristic #] · [Severity] · What breaks · Who it hits · Suggested fix`

---

## 1. Visibility of system status

The design should always keep the user informed about what is going on, through appropriate feedback within a reasonable time.

- [ ] Can I tell, without clicking, what state this screen is in right now?
- [ ] Does every action that takes more than a moment show that it's working?
- [ ] Is progress through a multi-step task shown, including how much is left?
- [ ] After an action completes, is the result visible — or do I have to go looking for it?
- [ ] Are background processes (syncs, imports, publishes) visible while they run and after they finish?

## 2. Match between the system and the real world

Speak the user's language. Use words, phrases and concepts familiar to them rather than internal jargon, and follow real-world conventions.

- [ ] Would the intended user recognise every label and term on this screen without training?
- [ ] Does the order of things on screen match the order the user does them in real life?
- [ ] Are internal system names, database field names, or team shorthand showing through?
- [ ] Do icons and metaphors mean the same to the user as to us?
- [ ] Are numbers, dates, currencies and units in the format the user's market expects?

## 3. User control and freedom

Users perform actions by mistake. They need a clearly marked emergency exit to leave an unwanted state without an extended process.

- [ ] Is there a visible way out of this screen that doesn't commit the change?
- [ ] Can the last action be undone — and is the undo discoverable at the moment it's needed?
- [ ] Can a long task be paused, saved, and resumed later without losing work?
- [ ] Is *Cancel* clearly distinguishable from the confirming action?
- [ ] Are destructive actions reversible, or at minimum confirmed with what exactly will be lost?

## 4. Consistency and standards

Users should not have to wonder whether different words, situations, or actions mean the same thing. Follow both internal and platform conventions.

- [ ] Does the same concept use the same word everywhere in the product?
- [ ] Do the same components behave the same way on every screen they appear on?
- [ ] Are primary and secondary actions in the same position and style as elsewhere?
- [ ] Does the screen follow the platform conventions users bring from other tools?
- [ ] Do spacing, grid and type match the design system rather than being hand-tuned here?

## 5. Error prevention

Good error messages matter, but the best designs stop the problem happening at all — remove error-prone conditions, or confirm before committing.

- [ ] What's the most likely mistake on this screen, and what stops it?
- [ ] Are impossible or invalid options disabled rather than allowed and then rejected?
- [ ] Are constraints shown *before* input, not after submission?
- [ ] Do defaults lead to a safe, sensible outcome for someone who changes nothing?
- [ ] Are irreversible actions separated from routine ones so they can't be hit by accident?

## 6. Recognition rather than recall

Minimise memory load. Make elements, actions and options visible rather than requiring the user to remember information from a previous screen.

- [ ] Does this screen require anything remembered from an earlier step, or held in another window?
- [ ] Are previously entered values shown rather than re-asked?
- [ ] Are available options visible or one click away, instead of needing to be typed from memory?
- [ ] Is context — which item, which shop, which mode — visible on screen at all times?
- [ ] Would a user returning after a week know where they left off?

## 7. Flexibility and efficiency of use

Accelerators, hidden from the novice, can speed up the expert. Let people tailor frequent actions.

- [ ] Is there a fast path for someone doing this for the twentieth time?
- [ ] Are there keyboard shortcuts, bulk actions, or duplication for repetitive work?
- [ ] Does the beginner path stay clear and unhurried despite the accelerators existing?
- [ ] Can frequent settings be saved, templated, or reused instead of rebuilt?
- [ ] Are sensible defaults doing the work for people who don't want to configure?

## 8. Aesthetic and minimalist design

Interfaces should not contain information that is irrelevant or rarely needed. Every extra unit of content competes with the relevant units.

- [ ] What can be removed from this screen without losing meaning?
- [ ] Is the primary task obvious within a couple of seconds of landing?
- [ ] Is rarely-needed detail tucked behind progressive disclosure rather than shown by default?
- [ ] Is visual weight going to the most important element, not the most decorated one?
- [ ] Is any text here longer than it needs to be?

## 9. Help users recognise, diagnose and recover from errors

Error messages should be in plain language, state the problem precisely, and suggest a solution constructively.

- [ ] Does every error say what happened, in words the user understands — no codes?
- [ ] Does it say what to do next, specifically?
- [ ] Does the message appear next to the thing that caused it?
- [ ] Is the user's work preserved when an error occurs?
- [ ] Do warnings distinguish "this will fail" from "this is unusual but allowed"?

## 10. Help and documentation

Ideally no explanation is needed; where it is, help should be easy to search, in context, listing concrete steps, and not too long.

- [ ] Does the screen work without help — and if not, is help right where the confusion happens?
- [ ] Is help contextual rather than a link to a general manual?
- [ ] Are the steps concrete and specific to the user's actual task?
- [ ] Can help be reached without losing the current state?
- [ ] Does the help text still match what the product actually does?

---

## Project watch-outs — JTL-Shop 6.0 admin & setup

Three failure modes specific to a multi-shop admin sitting on top of an ERP. They cut across the ten heuristics above and are easy to miss when reviewing screens in isolation.

### W1. Data ownership: which system wins?

JTL-WaWi stays the lead system for products, prices, inventory, customers and orders — the shop is not supposed to hold duplicate master data. Any field that mirrors WaWi looks identical on screen to a field the merchant genuinely owns, and a merchant who edits the wrong one loses the edit at the next sync. That's a trust failure, and no single Nielsen heuristic names it.

- [ ] Is it visible, per field, whether this value comes from WaWi or lives in the shop?
- [ ] Are WaWi-owned fields read-only here rather than editable-then-reverted?
- [ ] When a value is a synced mirror, is the last sync time or freshness shown?
- [ ] If an edit here will be overwritten by the next sync, does the UI say so *before* the user types?
- [ ] When a change belongs in WaWi, does the screen say where to make it instead of failing silently?

### W2. Scope: which shop, which page, which level am I changing?

Multi-shop is a first-class feature, and theme values cascade — global settings, per-shop overrides, per-page overrides marked *Inherits global*. The same editor can therefore change one page or every storefront, and the two look nearly identical. Get this wrong and a merchant restyles four live shops while trying to fix one banner.

- [ ] Is the active shop visible at all times, not just on the screen where it was chosen?
- [ ] Does an edit state the scope it will apply at — global, shop, page?
- [ ] Is inherited-versus-overridden distinguishable at a glance, per property?
- [ ] Before a global change lands, is the blast radius named ("affects 4 storefronts")?
- [ ] Is there a way back to inherited state without manually restoring the old value?
- [ ] Do preview and published state read clearly as different things?

### W3. Regulated content is not optional configuration

DACH and EU rules make certain shop content mandatory, not a preference: consent management, withdrawal instructions, legal notice, gross-versus-net price display, and unit prices such as €/kg. The setup flow deliberately lets steps be deferred — good for completion, bad if the deferrable set includes something that makes going live non-compliant.

- [ ] Can a merchant reach "live" with any legally required element still unset?
- [ ] Are compliance-critical steps distinguishable from genuinely optional ones?
- [ ] Are B2C gross and B2B net price displays correct for the market this shop targets?
- [ ] Do market-specific requirements follow the shop's country, not the admin's UI language?
- [ ] When a legal element is missing, does the message explain the obligation rather than just flagging an empty field?
- [ ] Is the merchant's own tax and legal responsibility stated where they'd assume the platform handles it?

---

## Review log

| # | Screen | Heuristic | Sev | Finding | Suggested fix |
|---|---|---|---|---|---|
| 1 |  |  |  |  |  |
| 2 |  |  |  |  |  |
| 3 |  |  |  |  |  |

---

*Heuristics: Jakob Nielsen, "10 Usability Heuristics for User Interface Design", Nielsen Norman Group (1994, updated) — https://www.nngroup.com/articles/ten-usability-heuristics/*
*Project watch-outs derived from `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md` §6.4, §9.1 and the Admin Setting / Theme Setup prototypes.*
