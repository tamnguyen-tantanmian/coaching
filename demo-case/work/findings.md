---
type: "findings"
title: "Findings"
stage: "Deliver"
status: "draft"
summary: ""
supports: []
---
*Deliver stage, after the test. What real users did. The AI can help analyse; check every finding against the notes or the recording.*

> **Read carefully before using:** this test round is **simulated**. The researcher (through an AI tool) played each persona on the real prototype, instead of using independent participants. Under the workspace principle (the AI does not play the users), the results below are only **hypotheses to be confirmed** and do **not** meet gate 4a. The original wording of the limits: `work/original-docs/13_Simulated_Usability_Findings.md`, section 6.

## Results against the baseline
| Metric | Baseline | Result | Met? |
|---|---|---|---|
| Task success | none yet | T1, T2, T4 completed; T3 completed through a detour; T5 blocked | no (2 of 5 tasks have serious problems) |
| Mean SEQ | none yet | 4.6/7 (T1 6, T2 6, T3 3, T4 7, T5 1) | no (target 5.5 or more) |
| Mean SUS | none yet | 69.2/100 (Aisha 80; Marco 62.5; Ji-yeon 65) | yes, but pulled up by one good run and only simulated |

## Findings, weighted by importance
*Ranked by importance, not by how many times it was mentioned. Link each finding to a recording or a note.*

| Finding | Severity | Evidence | What changes |
|---|---|---|---|
| The Connect → Browse screen has no search or filter; a specific local can only be found by working backwards through their tips | **Critical** | Connect session notes, screen S22 | Add search by name and invitations (recommendation #1) |
| The journal sharing screen only has a fixed list of 3 people, with no search or invite by name; someone outside the list cannot be chosen | **Critical** | Journal session notes, screen S30 | Add recipient search and invitations (recommendation #2) |
| The Browse list mixes locals from many cities, with no filter by location or trip | **Major** | Connect session notes, S22 | Filter by the destination of the trip (recommendation #3) |
| The AI itinerary parser keeps the day label as part of the place name and does not fit into the existing day structure | **Major** | Plan session notes, S17 and S18 | Fit it into the matching day (recommendation #4) |
| The "X% match" badge does not explain what it is based on | Minor | Direct observation, S22 | Explain it or remove it (recommendation #6) |
| An entry from AI shows a grey image and a dash instead of a duration, looking lower quality than a tip saved by hand | Minor | Direct observation, S18 | Show the image and an estimated duration (recommendation #9) |
| The label "Local resident" while the task says "another traveler" | Cosmetic | Discover session, S10 | Review the wording (recommendation #10) |

*The two Critical findings share one cause: the missing interaction pattern "find a specific person and invite them". They should be fixed as one piece of work, not two.*

## What changed because of this
- Combine the two Critical findings into one piece of work: design one **find a person and invite** pattern shared by Connect and journal sharing. Not done yet (no decision is recorded in `insights/decisions/`).
- The sign-up gate was not validated in this round: the prototype authenticates instantly, with no email or password step, so acceptance is over-rated.
- The first-click result of T1 may be inflated because the destination screen has "Thailand" pre-selected; treat it as an upper bound.
- **What to do before treating it as evidence:** run it again with real participants (`insights/evidence/E2.md`).
