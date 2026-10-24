---
type: "problem-brief"
title: "Problem brief"
stage: "Define"
status: "draft"
summary: ""
supports: []
---
*Define stage. A shared requirement. Sign it off with product and business, or record the agreement status.*

## Outcome and success metrics
*Goal, signal, metric. Write **assumed** for anything the PO has not confirmed. Each metric is a file in `insights/metrics/` (M1, M2 ...) and that file is the single source.*

| Goal | Signal | Metric (and baseline) | Status |
|---|---|---|---|
| New users see value right in the first session | They tap or save a tip early | M4: time to first interaction under 30 seconds (baseline: none yet) | assumed |
| Turn visitors into registered users | They accept the sign-up gate when they press Save | M5: 25% or more of visitors who press Save sign up (baseline: none yet) | assumed |
| Every core journey can be done without help | They complete the task without asking | M1: task completion rate of 80% or more (below 60% is a redesign priority) | assumed |
| It feels easy to use | The ease score per task and from the standard questionnaire | M2: SEQ of 5.5/7 or more; M3: SUS of 68 or more | assumed |

## Opportunities (ranked)
*A user need backed by evidence, not a feature. Each opportunity is a file in `insights/opportunities/` (O1, O2 ...) and that file is the single source: write it there directly, do not keep a duplicate table here. The summary table shows on the Problem brief page in Stages, built from those files.*

The ranking follows the importance score users gave to the features in the survey (n=13): planning 4.38; discovery 3.85; journal 3.62; free connection 3.38.

## Hypotheses
*We believe that [decision] for [users] will [change what], and we will know by [test and metric]. Each hypothesis is a file in `insights/hypotheses/` (H1, H2 ...), with a `Serves` line pointing to the opportunity and a `Metric` line.*

The six design hypotheses (`H1`..`H6`) were drawn from the six open questions of the test plan (`work/original-docs/12_Unmoderated_Usability_Test_Plan.md`, section 2.2). They differ from `RH1`..`RH10` in `scope.md`, which are hypotheses about users.

## Principle checks to apply
(Point to `standards/principle-checks.md`)
*The original project did not write the principle checks, so that file is still a template. This is a real gap of the project, recorded at gates 2d and 3c.*

## Agreement
Status: **not available**. The project is an academic practice, with no real person to sign off.
