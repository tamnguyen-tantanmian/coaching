---
type: "usability-test-script"
title: "Usability test script"
stage: "Deliver"
status: "draft"
summary: ""
takeaways:
  - ""
supports: []
# source: "../../work/usability-test-script.md"
# media: []
# links: []
# embed: false
---
*Use it after you have a test plan (`work/test-plan.md`) and before you write the test report (`test-report`). Anyone who reads this script can run the session.*

## Goal
The hypothesis (H#) being tested, and what would make you **change your mind**. If you cannot say it, do not test yet.

## Setup
| Item | Content |
|---|---|
| What is tested | The prototype or product, the version, the link |
| Format | In person / remote, whether the screen is recorded |
| Length | Usually 30 to 45 minutes |
| Participant | Code P#, criteria. Do not write real names |
| Roles | The moderator, the note taker |
| Preparation | Device, test account, sample data, consent obtained |

## Introduction (read verbatim)
> Thank you for taking part. Today we are testing the **product**, not you. There are no right or wrong answers. Please say out loud whatever you are thinking. You can stop at any time. We will record the session to review it; the data is anonymised. Do you agree?

## Warm-up
One or two easy questions about their background (not about the product):
- 

## Tasks
Each task is a **situation**, without saying beforehand how to do it, without using the exact name of a button or menu.

| # | The situation read to the participant | Success is when | Hypothesis | Time limit |
|---|---|---|---|---|
| T1 | "You are about to travel... Try to..." | Completes without a hint | H? | 3 minutes |

**When the participant is stuck:**
1. Stay silent for a few seconds.
2. Ask: "What are you thinking?"
3. Give a light hint only if they are stuck for more than 1 minute; record it as *with help*.

## After each task
- Difficulty (1 to 5, Single Ease Question): "How easy or hard was this for you?"
- "What surprised you?"

## Closing
- "What did you like most? What was most annoying?"
- The SUS scale (if used).
- Thank them, and say clearly how the data is used.

## Observation sheet
Record behaviour, not interpretation. Rate severity with Severity levels (the case's `standards/severity-levels.md`), 0 to 4.

| P# | Task | Completed? (yes / with help / no) | Time | Error / notable behaviour | Verbatim quote | Severity (0-4) |
|---|---|---|---|---|---|---|
| | | | | | | |

## Pilot checklist
- [ ] Run it with one person from outside the team, fix the tasks that were misunderstood.
- [ ] Measure the real time, adjust the number of tasks to fit the session.
- [ ] The prototype has no blocking bug other than the intended ones.
- [ ] Decided how to take notes and where to save the files (`work/sources/_raw-private/`).

*Images, videos and PDFs of this document: drop them into the same folder as this file and the report shows them by itself. See the case's `work/README.md`.*
