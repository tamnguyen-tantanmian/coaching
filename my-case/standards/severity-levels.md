# Severity levels

*The scale for how serious a usability problem is, used when you evaluate a design (Heuristic Evaluation) or record findings from a test with users. Based on Nielsen's 0 to 4 scale. Use the same scale for every finding so the levels can be compared with each other.*

## The 0 to 4 scale

| Level | Name | Meaning | Example | What to do |
|---|---|---|---|---|
| **0** | Not a problem | You do not agree this is a usability problem | One evaluator finds a label slightly odd, but real users understand it right away | Record it and drop it, with the reason |
| **1** | Cosmetic | A matter of appearance only, it does not get in the way of the user's work | Two icons are a few pixels out of line; capitalisation of labels is inconsistent | Fix only if there is time |
| **2** | Minor | A small problem: annoying or a little slow, the user still completes the task | A button is a bit far away so the user has to scroll; an error message does not say clearly how to fix it | Low priority; put it in the backlog |
| **3** | Major | A big problem: many users get blocked, lose a lot of time or have to take a detour | Cannot find where to share; has to re-enter data after an error | Important, high priority; fix before launch, or record clearly why it is accepted |
| **4** | Catastrophe | So serious that the user cannot complete the main task, or it causes lost data or lost money | The pay button does not work; an accidental delete that cannot be undone | **Must be fixed before release** |

## How to decide a level

A problem is rated on three factors, looked at together, not added up:

| Factor | Question | Leans toward a higher level when |
|---|---|---|
| **Frequency** | How often does this problem happen? How many people meet it? | Most users meet it, or meet it in the main task |
| **Impact** | When they meet it, is it easy or hard to get past? | They are blocked, lose data, or do not know how to continue |
| **Persistence** | Is it met once, or again and again? | Users cannot learn to avoid it and meet it every time |

For example: a rare error that wipes out all the data can be level 4. An annoyance that happens on every visit but costs one second can be level 2.

## How to rate

1. **Rate after you have seen the whole design,** not halfway through. You need the overall picture to compare problems with each other.
2. **Each person rates separately,** then compare. A single rater is often off; the average of 3 or more people is more reliable.
3. **Rate the problem, not the solution.** Severity is about the impact on users, not about how easy it is to fix.
4. **Write a short reason** for levels 3 and 4, so others understand why.

## Using this scale in the hub

- Each finding is a file in `insights/findings/` with the properties `severity` (0 to 4) and `principle` (see [Principle checks](principle-checks.md)). The report ranks findings by level by itself, and the Findings page in Stages shows the list.
- At the Deliver gate, check 4b requires findings to be ranked by importance: use this scale.
- Level **4** blocks handoff: the report warns while a level 4 finding still has `resolution: open`, and flags the decision that is affected.
- Level **3** needs a clear decision: fix it, or accept it as a trade-off and record it in `insights/case-log.md`.
- Levels **0 to 2** can go into the backlog after launch.

## How to record a finding

| Finding | Principle violated | Severity (0 to 4) | Evidence | What to do |
|---|---|---|---|---|
| One sentence describing the problem, from the user's point of view | The principle code, for example P1 | 0 to 4, with a short reason if it is 3 or 4 | An evidence code or a recording | Fix / accept / defer |

## Sources

- Nielsen, J. (1994). *Severity Ratings for Usability Problems.* Nielsen Norman Group.
- Nielsen, J. (1994). *How to Conduct a Heuristic Evaluation.* Nielsen Norman Group.
