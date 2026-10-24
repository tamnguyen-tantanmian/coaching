---
type: "finding"
title: ""
area: ""
severity: 2
principle:
  - "[[principle-checks|P1]]"
found_in:
  - "[[E1]]"
affects:
  - "[[D1]]"
resolution: "open"
---
*How to use: copy this file into `insights/findings/`, name it after the next code (for example `F1.md`), fill in the title (one sentence describing the problem from the user's point of view), then delete this line.*

- `severity`: a number from 0 to 4, see [Severity levels](../../standards/severity-levels.md). For levels 3 and 4, add a short reason in the description.
- `principle`: the principle that was violated (P1 to P10). Leave empty if it cannot be tied to one yet.
- `found_in`: the evidence in which the finding was discovered.
- `affects`: the decision that is affected (may be `[]`).
- `resolution`: `open` (not handled), `fixed`, `accepted` (accepted as a trade-off) or `deferred`.

## What happened
What the user did, where, and what went wrong.

## Why it matters
Frequency, impact and persistence (see Severity levels).

*Images that illustrate the problem: drop them into `work/<name>/` and insert them with `![description](../../work/<name>/<image>.png)`.*
