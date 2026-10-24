---
type: "measurement-plan"
title: "Measurement plan"
stage: "Deliver"
status: "draft"
summary: ""
takeaways:
  - ""
supports: []
# source: "../../work/measurement-plan.md"
# media: []
# links: []
# embed: false
---
*Answers the question: after release, how do we know whether it worked. Each metric is a file in `insights/metrics/` (M#) and that file is the single source for `target`, `result` and `verdict`. The table here records **how to measure**, it does not copy those numbers.*

## Goal
The desired outcome (from the Problem brief) and the question to answer after release.

## Metrics
| Metric (M#) | Exact definition | Formula | Target | Type (outcome / leading / guardrail) |
|---|---|---|---|---|
| M? | | | | |

*Each plan should have one main outcome metric, one or two leading metrics, and one "guardrail" metric to know we did not break something else.*

## Data and tracking
| Metric | Data source | Events / queries needed | Already available? | Who builds it |
|---|---|---|---|---|
| M? | | | yes / not yet | |

## Segments and baseline
Which groups to split by (new / returning users, device...), where the current baseline comes from, or write `assumed` if there is none yet.

## Cadence and owners
| Metric | Who is responsible | When to look | Threshold to act |
|---|---|---|---|
| M? | | | |

## Decision rules
Decide before the numbers are in: what result means **continue**, **adjust**, **stop**. Write it first so it is not interpreted to taste.

| If | Then |
|---|---|
| Meets or beats the target | |
| Close to the target | |
| Misses the target | |

## Qualitative signals
The qualitative signals to follow too (feedback, support tickets, sessions with users), to explain *why* the numbers moved.

## Limits
What makes the numbers less reliable (small sample, seasonality, another change at the same time). Fill in `result` and `verdict` in each M# file once measured; only the project owner sets `verdict`.

*Images, videos and PDFs of this document: drop them into the same folder as this file and the report shows them by itself. See the case's `work/README.md`.*
