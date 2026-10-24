# Unmoderated Usability Test Plan — Travel Buddy
**Project:** Travel Buddy | **Phase:** Discovery → Test
**Linked to:** `10_Prototype_Plan.md` · `11_Explore_Requirements.md` · `06_User_Personas.md` · `01_Research_Hypotheses.md` · `09_Card_Sorting_IA.md`
**Prototype under test:** [Travel Buddy — Interactive Prototype]([link to the interactive prototype: removed from this demo]) · High-fidelity, 32 screens, 4 flows (see `10_Prototype_Plan.md` §3–4)
**Status:** 🟡 Ready to configure | **Method:** Unmoderated remote usability testing | **Target:** 8–12 participants

---

## 1. Theoretical Grounding

Unmoderated usability testing is a remote method in which participants complete assigned tasks on their own, without a facilitator present, typically via a screen-recording or task-based testing platform (Dippner, 2022, Ch. 9.2). It is distinguished from moderated testing (Ch. 9.1) primarily by the absence of a live observer able to probe, clarify, or redirect in real time. This trade-off has two consequences that shape every decision in this plan:

1. **Task instructions must be fully self-contained.** Since no moderator can clarify ambiguity, every task must be understandable without follow-up questions, and must avoid vocabulary that leaks the answer (e.g. a task should not use the exact label of the button the participant needs to find) (Nielsen, 2000).
2. **A larger sample is required to compensate for lost context.** Because the method captures *what* happened but less reliably *why*, more participants are needed than in a moderated session to distinguish genuine usability problems from noise, participant confusion about the platform, or one-off misunderstandings. This plan targets 8–12 participants, above the 5-user threshold Nielsen (2000) recommends for moderated testing (as cited in `04_User_Survey.md` references), because unmoderated data has a lower signal-to-noise ratio per session.

Unmoderated testing is used here to complement — not replace — the moderated session described in `Submission_Outline_TravelBuddy.md` §7.1. The moderated round (3+ participants, think-aloud) is best suited to uncovering *why* users struggle; this unmoderated round is best suited to confirming *how often* and *for whom* those struggles occur, at a scale the moderated round cannot reach, and to specifically resolve open product questions that need broader statistical signal (see Section 2.2).

---

## 2. Purpose & Research Questions

### 2.1 Primary Objective

> Determine whether unmoderated participants, without guidance, can complete the four core Travel Buddy journeys (Discover, Plan, Connect, Journal) using the high-fidelity prototype — and identify where the interface, labelling, or flow breaks down when no one is available to help.

### 2.2 Specific Questions This Test Must Answer

This round is deliberately scoped to resolve outstanding open questions flagged elsewhere in the project, rather than duplicate the moderated test's broader diagnostic goal:

| # | Open question | Source | How this test addresses it |
|---|----------------|--------|----------------------------|
| 1 | Can users complete the save → plan → import flow without assistance? | `11_Explore_Requirements.md` §8 acceptance criteria | T2 (AI itinerary import) |
| 2 | Should Map mode default to current location or saved trip destination? | `11_Explore_Requirements.md` §10, Q4 (owner: Project owner, due: usability test) | T1 variant + post-task question |
| 3 | Do the Explore/Discover navigation labels (post-card-sort) map to user expectation without explanation? | `09_Card_Sorting_IA.md` | First-click accuracy on T1, T3, T5 |
| 4 | Does the sign-up gate (triggered on Save, A4/EA4-03) feel like a blocker or an acceptable trade-off for guests? | `01_Research_Hypotheses.md` H10, `11_Explore_Requirements.md` EA4-03 | T1 completion + SEQ rating + open comment |
| 5 | Is the reciprocal-exchange framing (C3) clear enough on first contact with a local profile that users don't hesitate before messaging? | `07_Solution_Pool.md` C3, H5 | T3 + post-task comment |
| 6 | Do users discover the auto-generated journal (J1–J2) without being told it exists? | `01_Research_Hypotheses.md` H7 | T4 |

### 2.3 What This Test Will Not Answer

Consistent with the survey's own stated limitations (`04_User_Survey.md` §"What This Survey Will Not Tell Us"), unmoderated testing cannot capture *emotional reaction in the moment*, hesitation reasoning, or edge-case verbal reasoning the way a think-aloud moderated session can. Where a participant fails a task, this plan captures *what* they clicked instead, not *why* — deeper "why" questions remain the province of the moderated round and follow-up interviews.

---

## 3. Participants

### 3.1 Sample Size & Rationale

**Target: 8–12 completed sessions.** This range balances two constraints: enough responses per persona segment to see a repeatable pattern (not one outlier), and a realistic recruitment volume for a self-directed student project. Recruit slightly above target (12–15 invitations) to absorb the higher drop-off/incompletion rate typical of unmoderated studies.

### 3.2 Recruitment Criteria

Reuses the primary screener from `01_Research_Hypotheses.md` §Screener Criteria, with one addition specific to remote unmoderated testing (comfort completing a task alone on a laptop or phone without help).

**Include:**
- Traveled at least once for leisure in the past 12 months
- Uses a smartphone; used at least one digital tool before or during that trip
- Comfortable completing a short online task independently, without live assistance
- Age 18–45 priority range (per `01_Research_Hypotheses.md`), 45–55 not excluded

**Exclude:**
- Work-only travelers with no leisure component
- People who deliberately avoid all digital tools when traveling
- Anyone who has already seen the Travel Buddy prototype, participated in the P1 interview, the survey, or the card sort (avoid contamination across research rounds)
- UX/product/design professionals (same exclusion as the card sort, `09_Card_Sorting_IA.md` §4 — familiarity with prototypes and testing conventions would mask real first-time friction)

### 3.3 Persona Distribution Target

Mirrors the card sort's persona-quota approach (`09_Card_Sorting_IA.md` §4) so findings can be segmented by primary persona rather than treated as one undifferentiated pool.

| Persona | Target n | Primary flow to weight toward |
|---------|----------|-------------------------------|
| Aisha — Explorer / Pragmatic Planner | 4–5 | Flow B: Discover & Plan (T1, T2) |
| Marco — Connector | 2–3 | Flow C: Connect (T3) |
| Ji-yeon — Documenter | 2–3 | Flow D: Journal (T4, T5) |

Screener signals to identify each persona at recruitment are reused verbatim from `05_User_Interview_Guide.md` §Participant Profiles (e.g., "I plan carefully but adapt a lot once I'm there" for Aisha's type).

---

## 4. Method & Tooling

### 4.1 Test Format

Unmoderated, task-based, remote — participants complete tasks on their own device on their own time within a 1-week response window, using screen-recording so behaviour (not just outcome) is captured for later review.

### 4.2 Tool

| Tool | Why | Free tier |
|------|-----|-----------|
| **Maze** *(recommended)* | Purpose-built for unmoderated prototype testing; imports interactive prototypes directly, auto-generates click-paths, misclick rate, time-on-task, and drop-off funnels per task | Limited free tier sufficient for 8–12 responses |
| **Lyssna (formerly UsabilityHub)** | Simple task-based testing with built-in first-click and preference tests; good fallback if Maze import fails | Free tier available |
| **Loom + manual task sheet** | Fallback if no prototype-testing platform can ingest the interactive prototype: send the prototype link directly, ask participants to record their own screen via Loom while completing the printed task sheet (Section 6) | Free |

**Setup note:** the interactive prototype linked at the top of this document is hosted as a shareable AI-generated design file. Before distributing to participants, confirm the link renders correctly in a fresh, logged-out browser session (participants will not have access to the project's AI tool account) — a private/incognito-window check is the minimum verification step. If the link cannot be viewed without authentication, export the prototype to a platform-agnostic host (e.g. re-upload the flow into Maze directly, or use `Travel_Buddy_HiFi.html` from the project folder as the source file) before the pilot test.

### 4.3 Session Structure

| Stage | Est. time | Content |
|-------|-----------|---------|
| Screener | 2 min | Confirms eligibility (Section 3.2) before granting access to the test |
| Introduction screen | 1 min | Written context-setting (Section 5) — replaces a moderator's spoken introduction |
| Warm-up questions | 1 min | 3 short self-report questions (Section 5.1) — eases the participant in and cross-checks persona fit before tasks begin |
| Tasks | 10–12 min | 5 tasks, each followed by a post-task rating (Section 6) |
| Post-test questionnaire | 3 min | SUS + open-ended questions (Section 7) |
| **Total** | **~19 min** | Kept under 20 minutes to limit unmoderated drop-off |

---

## 5. Written Introduction (shown to participant before Task 1)

Because there is no moderator to set expectations verbally, this text must do that work in writing.

> **Welcome, and thank you for helping test Travel Buddy.**
>
> Travel Buddy is a prototype for a travel app that combines discovering places, planning trips, connecting with locals, and remembering trips afterward — all in one app.
>
> You'll be asked to complete **5 short tasks** using an interactive prototype. It looks and behaves like a real app, but nothing you tap is permanently saved and no real messages are sent.
>
> There are no right or wrong answers — we're testing the design, not you. If something is confusing or you get stuck, that's exactly the kind of thing we want to know. Please try to complete each task as you naturally would, then move to the next one even if you're not sure you finished correctly.
>
> After each task, we'll ask one quick question about how it felt. At the end, there's a short final survey.
>
> This should take about 15–20 minutes. Your responses are anonymous and used only for this research project.

### 5.1 Warm-Up Questions (shown after the introduction, before Task 1)

With no moderator present to build rapport before the "real" tasks, these questions do that work: they give the participant something easy and low-stakes to answer first, and they double as a lightweight self-report check against the persona they were recruited for (Section 3.3) — since screener answers and lived behavior don't always match. They are not scored as usability metrics and are not shown as timed tasks.

1. "How often do you travel for leisure (vacations, weekend trips, etc.)?" *(single choice: Monthly / A few times a year / About once a year / Less than once a year)*
2. "When you travel, what do you usually rely on to figure out what to do or see?" *(open text — baseline for D1–D3, compare against what the app offers)*
3. "Thinking about your most recent trip, which best describes you — mostly planning ahead, mostly connecting with locals along the way, or mostly documenting/journaling afterward?" *(single choice, maps to Aisha/Marco/Ji-yeon; used post-hoc to sanity-check the persona split in Section 9's segmentation cut)*

---

## 6. Tasks

Adapted from the 5 tasks defined in `10_Prototype_Plan.md` §8, rewritten for unmoderated delivery: each instruction is phrased functionally (what the participant is trying to accomplish) rather than by UI label, so it does not pre-empt navigation decisions the test is trying to observe.

| # | Task instruction (as shown to participant) | Prototype entry screen | Success signal | Solutions/Hypotheses tested |
|---|----------------------------------------------|------------------------|-----------------|------------------------------|
| T1 | "You're planning a trip to Chiang Mai. Find a food-related tip from another traveler and save it to a trip." | S10 (Discovery Feed) | Reaches S16/S18 with the tip saved to a shortlist | D1–D3, P3, EA4-03, RQ 2 & 3 |
| T2 | "You already have a rough itinerary written by an AI chatbot. Get it into your trip plan." | S18 (Trip Shortlist) | Completes the S17 import flow and returns to S18 with imported places visible | P6, RQ 1 |
| T3 | "You'd like a genuine restaurant recommendation from someone who actually lives in the city. Find a local named Niran and reach out." | S22 (Local Browse) | Reaches S25 with a message sent to Niran | C1–C4, H4, H5, RQ 5 |
| T4 | "Your trip to Chiang Mai has ended. Find the record of what you did." | S31 (Memory Layer) or app home | Opens S29 (auto-generated journal) without being told it exists | J1–J2, H7, RQ 6 |
| T5 | "Share your trip journal with your friend Ji-yeon, but only with her — not publicly." | S29 (Journal Private View) | Reaches S30 with Ji-yeon selected as recipient | J3–J4, H8 |

**Task order:** fixed in the sequence above (not randomised). The tasks intentionally follow the persona journey chronology (discover → plan → connect → remember), and randomising them would place participants in later-stage screens (e.g. a completed journal) without the preceding context, which is not representative of real use.

**Instructions to test administrator (not shown to participant):**
- Do not reveal navigation labels in task text (e.g. do not say "tap Explore" — say what the user is trying to accomplish).
- If a platform allows a "give up / skip" option, keep it enabled — forcing completion produces false success data.
- Log the exact click path and time-on-task for every participant, even on tasks they abandon; abandonment location is itself a finding.

---

## 7. Post-Task and Post-Test Questions

### 7.1 Post-task (after each of the 5 tasks)

**Single Ease Question (SEQ)**, asked immediately after each task while the experience is fresh:

> "Overall, how easy or difficult was that task?"
> 1 (Very difficult) – 7 (Very easy)

Plus one open-text prompt, shown only if the participant rated 4 or below:

> "What made this harder than expected?" *(open text)*

### 7.2 Post-test questionnaire (after Task 5)

**System Usability Scale (SUS)** — standard 10-item, 5-point agreement scale, administered in full and unmodified so scores remain comparable to published SUS benchmarks:

1. I think that I would like to use this app frequently.
2. I found the app unnecessarily complex.
3. I thought the app was easy to use.
4. I think that I would need the support of a technical person to be able to use this app.
5. I found the various functions in this app were well integrated.
6. I thought there was too much inconsistency in this app.
7. I would imagine that most people would learn to use this app very quickly.
8. I found the app very cumbersome/awkward to use.
9. I felt very confident using the app.
10. I needed to learn a lot of things before I could get going with this app.

**Open-ended wrap-up questions:**

1. "Was there any point where you weren't sure what to do next? Where?"
2. "Did anything surprise you — positively or negatively?"
3. "The app framed connecting with locals as free and reciprocal, not a paid service. How did that feel — reassuring, confusing, or something else?" *(directly targets RQ 5 / H4–H5)*
4. "Is there anything you expected the app to do that it didn't?"

---

## 8. Metrics & Success Criteria

| Metric | Definition | Target / benchmark |
|--------|-----------|---------------------|
| Task success rate | % of participants who reach the defined success signal per task, unassisted | ≥ 80% per task flagged healthy; below 60% flagged for redesign priority |
| Time on task | Median seconds from task start to success/abandon | No fixed target; used to compare tasks relatively, and flag outliers > 2x median |
| Misclick / error rate | Number of taps on non-target elements before success | Directly maps to Maze's built-in "misclick rate" per screen |
| SEQ score (per task) | Mean of 1–7 ease rating | ≥ 5.5 healthy; < 4.5 flagged |
| SUS score (overall) | Standard SUS 0–100 composite | ≥ 68 is "above average" per SUS norms; used as an overall prototype health check, not a pass/fail gate |
| First-click accuracy | % of participants whose very first tap on the entry screen was on the correct path | Directly tests RQ 3 (navigation labelling) |

---

## 9. Analysis Plan

Findings feed directly into `Submission_Outline_TravelBuddy.md` §7 (Testing & Refinement) alongside the moderated round's findings. To keep the two rounds comparable in the final report, findings from this round should be logged using the same severity framework as the moderated test:

| Severity | Definition | Action |
|----------|-----------|--------|
| Critical | Blocks task completion for most participants | Must fix before next iteration |
| Major | Causes visible hesitation/error for a majority, but recoverable | Should fix before next iteration |
| Minor | Isolated confusion, one or two participants | Note for future iteration |
| Cosmetic | No functional impact | Backlog |

**Segmentation cut:** in addition to overall metrics, re-cut Section 8's metrics by persona group (Section 3.3) — the sample is intentionally recruited to support this, since Explorer, Connector, and Documenter participants weight toward different tasks and may reveal persona-specific breakdowns rather than universal ones (consistent with how `06_User_Personas.md` treats each persona as validating different hypotheses).

**Findings table template (fill in after sessions):**

| Issue | Screen | Task | Severity | # participants affected | Related solution/hypothesis |
|-------|--------|------|----------|--------------------------|------------------------------|
| TBD | TBD | TBD | TBD | TBD | TBD |

---

## 10. Timeline

| Step | Duration |
|------|----------|
| Finalize task list & tool setup (Maze/Lyssna configuration) | 1 day |
| Pilot test with 1 participant, adjust wording if any task is misunderstood | 1 day |
| Recruit 12–15 participants against Section 3 criteria | 3–4 days |
| Test window open (participants complete independently) | 5–7 days |
| Export data, compile findings table, calculate SUS | 1–2 days |
| Write up into `Submission_Outline_TravelBuddy.md` §7 | 1 day |

---

## 11. Logistics Checklist

- [ ] Confirm the interactive prototype link renders in a logged-out/incognito browser before distributing (see Section 4.2 setup note)
- [ ] Import or rebuild the prototype flow in Maze (or chosen tool) covering S10, S16–S18, S22, S25, S29–S31
- [ ] Enter all 5 tasks and post-task SEQ prompts (Section 6–7.1)
- [ ] Add full 10-item SUS + 4 open questions as the closing survey (Section 7.2)
- [ ] Pilot test with 1 person; confirm total time stays under 20 minutes and no task instruction leaks the UI label
- [ ] Recruit 12–15 participants matching Section 3 screener and persona quotas
- [ ] Set 1-week response deadline
- [ ] Export session recordings, click-paths, and metrics after close
- [ ] Complete findings table (Section 9) with severity ratings
- [ ] Cross-reference findings against moderated test results before writing `Submission_Outline_TravelBuddy.md` §7.2–7.3

---

## References

- Dippner, D. (2022). *User Experience Design – Principles & Methods.* SRH Fernhochschule.
- Nielsen, J. (2000). *Why You Only Need to Test with 5 Users.* Nielsen Norman Group.
- Brooke, J. (1996). SUS: A quick and dirty usability scale. In P. W. Jordan, B. Thomas, B. A. Weerdmeester, & A. L. McClelland (Eds.), *Usability Evaluation in Industry*. Taylor & Francis.
- Sauro, J. (2011). *A Practical Guide to the System Usability Scale.* Measuring Usability LLC.
- `10_Prototype_Plan.md` — screen inventory, flows, and original 5-task usability hook (§8)
- `11_Explore_Requirements.md` — open questions this test is scoped to resolve (§10)
- `09_Card_Sorting_IA.md` — recruitment/exclusion approach reused for this round
- `06_User_Personas.md` — persona quotas and screener signals
- `01_Research_Hypotheses.md` — hypotheses (H1–H10) and screener criteria this round revisits at prototype stage
- `07_Solution_Pool.md` — solution IDs referenced in the task-to-solution mapping (Section 6)
