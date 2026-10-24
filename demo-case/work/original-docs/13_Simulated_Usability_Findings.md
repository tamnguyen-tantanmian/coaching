# Moderated Usability Test Findings — Travel Buddy

**Project:** Travel Buddy | **Phase:** Test (Section 7)
**Related documents:** `12_Unmoderated_Usability_Test_Plan.md` · `06_User_Personas.md` · `10_Prototype_Plan.md` · `01_Research_Hypotheses.md` · `11_Explore_Requirements.md` · `Submission_Outline_TravelBuddy.md` §7.1–7.2
**Prototype under test:** *Travel Buddy* interactive prototype (`Travel Buddy (Standalone).html`), 32 screens, 4 flows
**Method:** Moderated usability testing, task-based, think-aloud protocol (Dippner, 2022, Ch. 9.1)
**Sample:** n = 3 (one participant per primary persona)

---

## Executive Summary

This report presents findings from a moderated usability test of the Travel Buddy prototype, conducted with three participants representing the product's three primary personas — Aisha (Explorer/Pragmatic Planner), Marco (Connector), and Ji-yeon (Documenter) — as defined in `06_User_Personas.md`. Each participant completed a subset of the five core tasks defined in `12_Unmoderated_Usability_Test_Plan.md` §6 while thinking aloud, followed by a Single Ease Question (SEQ) per task and a full System Usability Scale (SUS) questionnaire.

**Key insight:** Travel Buddy's content-discovery and passive-automation experiences performed strongly (mean SEQ 6.3/7 across the discovery, planning, and journal tasks), while every task requiring the participant to find or select a specific named person — a local to message, a friend to share with — failed or nearly failed (mean SEQ 2/7 across the connect and share tasks). This is not evidence of two unrelated feature weaknesses; once a person was actually reached, both the messaging and sharing experiences scored well qualitatively. It is evidence of a single missing interaction pattern — person search and invite — that recurs across two otherwise-unrelated flows, and should be prioritized as one fix rather than two.

A methodological note precedes the findings below: due to time constraints, this round was conducted with the researcher role-playing each persona in character against the live prototype rather than with independent human participants. It is presented here in the moderated-test format required by §7.1, but should be read as a structured pilot that surfaces hypotheses for a real moderated round, not as a substitute for one (see Section 6, Limitations).

---

## 1. Introduction and Purpose

Following the research-to-design process outlined in Dippner (2022), usability testing serves to validate whether the interface decisions made during the Discovery phase (personas, information architecture, solution pool) actually hold up when a user attempts real tasks. This test was designed to answer, per persona, whether the core journey each persona was built around — Discover & Plan (Aisha), Connect (Marco), and Journal (Ji-yeon) — could be completed without external help, and where the interface caused hesitation or failure.

Per `Submission_Outline_TravelBuddy.md` §7.1, the method specified for this section is a moderated usability test with 3 or more participants, given tasks, using a think-aloud protocol. Moderated testing is defined in contrast to the unmoderated method already planned in `12_Unmoderated_Usability_Test_Plan.md` (Ch. 9.2) by the presence of a live observer able to capture not only *what* a participant does, but *why* — their reasoning, hesitation, and in-the-moment reaction to the interface (Dippner, 2022, Ch. 9.1). This distinction is the reason moderated testing was chosen for this section: it produces the causal, qualitative detail an unmoderated round cannot.

---

## 2. Method

### 2.1 Participants

Three participants were tested, one representing each of the three personas defined during Discovery. A sample of three sits at the lower bound of what moderated usability testing literature recommends: Nielsen (2000) finds that five participants are typically sufficient to surface the majority of usability problems in a single user group, with three participants understood as adequate for an early, low-stakes formative round intended to catch major flow issues before a larger test (as reflected in `12_Unmoderated_Usability_Test_Plan.md` §1, which uses the same Nielsen benchmark to justify its own sample size). Given this round's purpose — a fast, pre-milestone check rather than a definitive validation — three was judged sufficient.

| Participant | Persona represented | Primary flow tested | Tasks completed |
|---|---|---|---|
| P1 | Aisha — Explorer / Pragmatic Planner | Discover & Plan | T1, T2 |
| P2 | Marco — Connector | Connect | T3 |
| P3 | Ji-yeon — Documenter | Journal | T4, T5 |

### 2.2 Materials and Procedure

Each session followed the same structure: a brief warm-up question to establish traveler type, the assigned tasks from `12_Unmoderated_Usability_Test_Plan.md` §6 performed against the live interactive prototype, a Single Ease Question (1–7 scale) immediately after each task, and the full 10-item System Usability Scale (Brooke, 1996) administered at the end of the session. Participants were asked to narrate their reasoning continuously (think-aloud protocol), including moments of hesitation, confusion, or delight, consistent with moderated-method practice (Dippner, 2022, Ch. 9.1).

### 2.3 Note on Execution

Given time constraints ahead of a submission milestone, all three sessions were conducted as an AI-simulated proxy: the researcher (via an AI tool) role-played each persona against the live prototype rather than recruiting independent human participants. The procedure, instruments, and reporting format above are identical to what a real moderated round would use. This substitution is a limitation, addressed directly in Section 6, and the findings below should be treated as a formative pilot rather than validated research data.

| Persona | Tasks run | SEQ scores | SUS score | Outcome |
|---|---|---|---|---|
| Aisha (Explorer/Pragmatic Planner) | T1, T2 | T1: 6/7 · T2: 6/7 | **80/100** | Both completed, minor friction |
| Marco (Connector) | T3 | T3: 3/7 | **62.5/100** | Completed, but only via workaround |
| Ji-yeon (Documenter) | T4, T5 | T4: 7/7 · T5: 1/7 | **65/100** | T4 completed cleanly; T5 blocked, could not complete as scripted |

**Average SEQ: 4.6/7 · Average SUS: 69.2/100** — nominally "above average," but this average is propped up by Aisha's strong run and hides that 2 of 5 tasks had serious friction; don't read it as "healthy" without the per-task breakdown above.

---

## 3. What Went Well

To avoid the common bias of a usability report reading only as a defect list, these moments performed well and directly resolved open product questions from `11_Explore_Requirements.md` §10 — they should be preserved through any redesign addressing Section 4.

- **All three concepts were desired, not just tolerated.** Each participant's spontaneous reaction to a flow's *concept* — independent of how the task itself went — closely matched the top-ranked desires already captured in `06_User_Personas.md`'s survey data: the Explorer called AI-import *"exactly my workflow"* (matching the #1-rated planning pain point, fragmentation), the Documenter called the auto-journal *"exactly the fantasy I have and never get"* (matching the most-wanted journal feature, auto-capture, 7 of 8 respondents), and the Connector's relief at "Free exchange" matched the near-unanimous openness to non-transactional local connection (12 of 13 respondents). None of the three participants expressed doubt about wanting the underlying feature — including the two who hit the Critical issues in Section 4. That is a meaningfully different, more fixable problem than a desirability failure would be.
- **Save → Plan auto-slotting.** Saving a tip immediately placed it into a specific day in the itinerary rather than a flat list, validating the "plan that builds itself as you save" positioning.
- **Live AI-import preview.** Detected places updated in real time as text was entered, building confidence before commitment.
- **Contextual first message on Connect.** The initial message to a local referenced the specific tip that prompted contact, rather than a generic greeting.
- **"Free exchange · no fees" label.** Placed directly under the local's name in the message thread, this proactively resolved the reciprocity/cost question central to hypotheses H4/H5, before the participant had to ask.
- **Zero-setup auto-capture journal.** "Your trips, captured automatically. Private by default" was already running with no configuration needed — matched persona Ji-yeon's core goal almost exactly and was the single strongest moment across all three sessions.
- **Visible trust signals before first contact.** Every Browse profile card shows a verified checkmark and a match-percentage badge, and this registered immediately: *"That verified badge is reassuring right away — that's exactly the safety signal I'd want before messaging a stranger."* This addresses a separate concern from cost (is this person who they say they are?) and directly supports hypothesis H4 (verified identity rated as a near-required condition by 11 of 13 respondents in `06_User_Personas.md`'s survey data).

---

## 4. What Needs to Improve

Two cross-cutting patterns explain most of what follows, rather than twelve unrelated bugs:

1. **One missing interaction pattern causes two separate Critical failures.** Neither Connect → Browse nor the Journal share sheet lets a participant find or select one specific named person — the only path to a specific local is backtracking through content they authored, and the share sheet offers a fixed 3-person list with no search or invite option. Every task that involved *browsing* an open feed scored SEQ ≥ 6/7; every task that instead required *finding a specific known person* scored SEQ ≤ 3/7 — this is one gap, not two.
2. **Strong trust copy without the functional means to act on it risks reading as a broken promise, not neutral friction.** The Documenter participant trusted the Journal's privacy messaging completely — "Only you can see this," "Never posted publicly" — before attempting to share, then immediately hit the wall above. The privacy *promise* was never in question; the ability to *act* on it was what failed. Pairing trustworthy copy with a flow that can't fulfil it risks the participant generalizing the failure to the trust claim itself.

| Issue observed | Participant behavior / quote | Screen | Severity | Recommended fix |
|---|---|---|---|---|
| Connect → Browse has no search or filter and does not surface locals already encountered elsewhere (e.g., a tip author). The only path to a specific named local is backtracking through their tip. | *"I only found him by backtracking through a tip I'd already saved."* | S22 Local Browse | **Critical** | See Recommendation #1 |
| Journal share sheet offers a fixed 3-person list with no search or invite-by-name option; a recipient outside that list cannot be selected. | *"I'm stuck; the exact task I was given can't be completed as written."* | S30 Share sheet | **Critical** | See Recommendation #2 |
| Connect → Browse mixes locals from unrelated destinations (Hanoi, Lisbon) in with Chiang Mai locals, with no location or trip filter — even after scrolling, most visible profiles are irrelevant to the trip actually being planned. | Observed directly during the Connect session while scrolling for Niran; compounds the search gap above. | S22 Local Browse | **Major** | See Recommendation #3 |
| AI-import parser retains the pasted day label as part of the place title instead of using it to sort into the existing day structure; imported items sit in a separate block rather than merging into the itinerary. | *"I expected the imported places to drop into Day 3/Day 4 automatically."* | S17 Import / S18 Trip plan | **Major** | See Recommendation #4 |
| Local profile shows an unrendered "% interest match" placeholder and empty "Interests"/"Recently shared tips" sections for a local who has authored a tip. | Observed directly during the Connect session; not raised spontaneously. | S24 Local profile | **Minor** | See Recommendation #5 |
| The "X% match" badge shown on every Browse card has no visible explanation of what it's based on — the metric is opaque to a first-time user even though it visually implies precision. | Observed directly during the Connect session; not raised spontaneously. | S22 Local Browse | **Minor** | See Recommendation #6 |
| Browse profile cards use a generic "Say hello" CTA, while the tip-detail entry point uses "Connect" and produced a contextual, tip-referencing first message. Whether "Say hello" produces the same message quality is untested, since Niran was unreachable via Browse. | Inferred from comparing card CTAs against the actual message sent via the tip-detail page. | S22 Local Browse vs. S24 profile | **Minor** | See Recommendation #7 |
| A "Copy view-only link" fallback exists in the Journal share sheet that could technically route around the fixed 3-person list, but it is not framed as the answer to "share with someone not listed," so it did not prevent the participant from reporting she was fully stuck. This meaningfully softens, but does not resolve, the Critical severity above. | *"I'm stuck; the exact task I was given can't be completed as written."* (workaround not attempted) | S30 Share sheet | **Minor** | See Recommendation #8 |
| Imported AI-itinerary items show a blank grey placeholder image and a dash ("Imported · —") instead of a duration estimate, unlike manually-saved tips, which display a real photo and a time estimate — imported items visually read as lower-quality than organically discovered content. | Observed directly during the Discover & Plan session after import completed. | S18 Trip plan | **Minor** | See Recommendation #9 |
| Tip attribution reads "Local resident" while task framing refers to "another traveler," momentarily unclear whether it satisfies the ask. | *"For a second I second-guess if this counts."* | S10 Discovery feed | **Cosmetic** | See Recommendation #10 |
| Trip card shows an aggregate save count immediately after a single save, with no confirmation of which trip plan the item was actually added to — a risk once a user has more than one trip in progress. | *"I can't immediately tell which of the three is mine."* | S16 Trip list | **Cosmetic** | See Recommendation #11 |
| The destination picker's "Thailand" option appeared pre-highlighted before any choice was made, with no visible indication of why. Also a testing-validity caveat (see Section 6), since it may have inflated first-click accuracy for a task about Chiang Mai. | Observed directly during the Discover & Plan session; not raised spontaneously. | S9 Destination picker | **Cosmetic** | See Recommendation #12 |

---

## 5. Recommendations

Ordered by severity. These are proposed changes to prototype against in the next design pass, not yet-implemented fixes — no redesign has been made at this stage.

A feasibility note before the list: every person referenced across this test (Niran, and the three fixed Journal contacts) already exists in the prototype as a fully modeled entity — a profile page, a verified/local-resident status, and, for Niran, authored content already linked to it. What both Critical issues lack is a UI-layer search or filter over data the product already stores, not a new content type or backend concept. That lowers the realistic engineering cost of Recommendations #1–#2 considerably, and is a strong candidate for a feasibility/desirability/viability scorecard (Dippner, 2022, citing IDEO, 2015) to justify fixing both before the real moderated round rather than deferring them as future work.

**1. Person search, Connect → Browse — Critical**
- *Before:* Browse shows a fixed grid of profiles with no search bar or filter. The only way to reach a specific known local (e.g., Niran) is to navigate back to a tip they authored and tap their name from there.
- *After:* Add a search field at the top of Browse, matching the existing search pattern already used on the Explore feed ("Search destination, tip, place…"), filtering by name. Additionally, surface a "Message [Name]" quick action directly on any Explore tip card authored by a verified local, so the user need not leave the feed they're already in. Keep the verification badge and match-score visible in the redesigned card — the findability fix shouldn't bury this trust signal behind an extra tap.

**2. Person search/invite, Journal share sheet — Critical**
- *Before:* Tapping "Share" opens a sheet with exactly three hardcoded contacts (Marco D., Ines R., Priya K.) and a "copy view-only link" fallback. No one outside that list can be selected.
- *After:* Add a search/invite field above the contact list ("Search contacts or invite by name/email"). This can reuse the same search component proposed in Recommendation #1, resolving both Critical findings with one build.

**3. Location filtering, Connect → Browse — Major**
- *Before:* Browse shows locals from Chiang Mai, Hanoi, and Lisbon together with no filter, so most visible cards are irrelevant to the trip currently being planned.
- *After:* Default Browse to the active trip's destination (the product already knows this — it's shown at the top of Explore as "Near Chiang Mai"), with an explicit toggle to browse other destinations. A small addition on top of Recommendation #1's search field, using data the app already has.

**4. AI-import day-label parsing — Major**
- *Before:* Pasting "Day 3: Chiang Mai Old City walking tour" creates a single place literally titled "Day 3: Chiang Mai Old City walking tour," placed in a separate "Imported from AI" block beneath the existing day-by-day itinerary.
- *After:* Parse a leading "Day N:" pattern as a day-assignment instruction rather than place content — strip it from the title and route the item directly into the corresponding "Day N" section, matching how manually-saved tips already behave.

**5. Local profile empty states — Minor**
- *Before:* Niran's profile shows literal unbound template text ("% interest match") and empty "Interests" / "Recently shared tips" sections, despite having authored a tip.
- *After:* Bind the match-percentage field to a real value (or hide the badge entirely when no score exists), and populate "Recently shared tips" from the local's own authored content.

**6. Match-score transparency — Minor**
- *Before:* Every Browse card shows a "X% match" badge with no indication of what it measures.
- *After:* Add a one-line explainer on tap or a small info icon (e.g., "based on shared interests and travel style") so the badge reinforces trust rather than reading as an arbitrary number.

**7. CTA consistency between Browse and tip-detail messaging — Minor**
- *Before:* Browse cards say "Say hello" (generic); the tip-detail page says "Connect" and sends a message referencing the specific tip. It's unclear whether both paths produce equivalent message quality.
- *After:* Align both entry points on the same contextual-message pattern — if Browse has no specific tip to reference, default to a lighter contextual hook (e.g., shared interest tags) rather than a fully generic greeting, and use one consistent CTA label across both surfaces.

**8. Surface the share-link workaround — Minor**
- *Before:* "Copy view-only link" exists in the Journal share sheet but isn't positioned as the answer to "share with someone not in this list," so it didn't stop the participant from feeling fully blocked.
- *After:* Until search/invite (Recommendation #2) ships, add a one-line prompt above the fixed contact list — "Don't see who you're looking for? Copy a link to share with anyone" — so the existing workaround is actually discoverable.

**9. Imported item visual completeness — Minor**
- *Before:* Items brought in via AI import show a blank grey placeholder image and "Imported · —" instead of a duration estimate, unlike manually-saved tips.
- *After:* Either fetch a representative image and estimated duration for recognized place names at import time, or clearly label imported items as "details pending" rather than showing an empty dash, so they don't read as broken.

**10. Tip-source label wording — Cosmetic**
- *Before:* Task copy asks for a tip "from another traveler," but the top matching card is attributed to a "Local resident," creating a moment of doubt about whether it qualifies.
- *After:* Broaden the UI's source label (e.g., "Local resident · Contributor," or a shared "Community tip" framing) so traveler- and local-authored tips read as equally valid, independent of how future task copy is worded.

**11. Save confirmation clarity — Cosmetic**
- *Before:* After saving one tip, the trip card immediately shows an aggregate "3 saved" with no indicator of which trip plan the item actually landed in — a gap that only shows up once a user is managing more than one trip at a time.
- *After:* Retain the existing "Saved to your Chiang Mai plan" toast (it already names the trip), and add a short-lived highlight or checkmark on the specific card just saved so the destination trip and the specific item both feel confirmed, not just aggregated.

**12. Destination-picker default clarity — Cosmetic**
- *Before:* "Thailand" appears pre-highlighted on the destination picker with no explanation of why, before the participant has made any choice.
- *After:* Either make the default state neutral (no pre-selection) or label it explicitly (e.g., "Suggested based on your last search") so it reads as an intentional recommendation rather than an arbitrary default — and so the real moderated round's first-click data isn't confounded by it.

**13. Extend proactive reassurance copy to the sign-up gate — Strategic**
- *Before:* A guest tapping Save hits an account-creation prompt with no explanation of why, unlike the Connect flow's "Free exchange" reassurance, which answers the user's likely objection before they have to ask.
- *After:* Add a one-line explanation at the point of the gate (e.g., "Create a free account to save this and build your trip — takes 10 seconds"), reusing the same pre-emptive-reassurance pattern that worked well in Connect (`11_Explore_Requirements.md` EA4-03).

**14. Test the sign-up gate at production fidelity before the real round — Methodological**
- *Before:* This round's sign-up required no email, password, or verification step, so participant ease here doesn't indicate whether a real sign-up form would feel acceptable.
- *After:* Build or simulate a realistic multi-field sign-up step, then re-test RQ4 with real participants — treat this round's result as inconclusive on that question, not as evidence the gate is fine.

---

## 6. Limitations

This round substituted an AI-simulated single-rater proxy for three independent human participants due to time constraints ahead of a submission deadline. This has five consequences for how these findings should be used:

1. **No inter-participant variance.** A real moderated round with three different people would likely surface additional, participant-specific confusion points this single-rater method cannot generate.
2. **Simulated think-aloud is not human think-aloud.** While the procedure captured reasoning and hesitation in the spirit of Dippner's (2022, Ch. 9.1) definition of moderated testing, it cannot replicate genuine human uncertainty, emotional reaction, or the unpredictable phrasing a live participant would use.
3. **Findings are hypotheses, not conclusions.** Each issue in Section 4 should be treated as a candidate problem to confirm — not disprove — with real participants, particularly the two Critical findings, which would otherwise be expected to drive task-success rates in a real test below the 60% redesign-priority threshold used in `12_Unmoderated_Usability_Test_Plan.md` §8.
4. **The sign-up gate specifically could not be validly tested here.** The Explorer participant tapped "Sign up free" on the guest save-gate and was instantly authenticated with no email, password, or verification step: *"That was fast... no email/password screen, which feels too easy for a real app."* Because a production sign-up will necessarily introduce friction this prototype does not simulate, the participant's lack of hesitation likely overstates how acceptable the gate (`11_Explore_Requirements.md`, EA4-03) will feel once real account creation is involved. RQ4 ("does the sign-up gate feel like a blocker or an acceptable trade-off?") should be treated as still unanswered (see Recommendation #14).
5. **First-click accuracy on T1 may be inflated by a pre-highlighted default.** The destination picker showed "Thailand" already visually selected before the Explorer participant made any choice (Section 4), which may have made the "correct" first click easier to land on than it would be for a real participant facing five neutral options. Re-run T1's first-click measurement with the default state removed (see Recommendation #12), or treat this round's first-click accuracy figure as an upper bound rather than a reliable estimate.

---

## References

Brooke, J. (1996). SUS: A quick and dirty usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), *Usability Evaluation in Industry*. Taylor & Francis.

Dippner, D. (2022). *User Experience Design – Principles & Methods.* SRH Fernhochschule.

Nielsen, J. (2000). *Why You Only Need to Test with 5 Users.* Nielsen Norman Group.

`Submission_Outline_TravelBuddy.md` — assignment structure and §7.1–7.2 method/reporting requirements this document follows.

`12_Unmoderated_Usability_Test_Plan.md` — task set, SEQ/SUS instruments, and severity framework reused in this report.

`06_User_Personas.md` — persona definitions used for participant role assignment.

`10_Prototype_Plan.md` — screen inventory (S-numbers referenced above).

`01_Research_Hypotheses.md` — hypotheses (H4, H5) referenced in Sections 3–4.

`11_Explore_Requirements.md` — open questions (EA4-03) referenced in Sections 3, 5, and 6.
