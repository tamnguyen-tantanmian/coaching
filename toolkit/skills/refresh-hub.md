# Workflow: Review the Hub

Ask the AI to read the item files and list what is not linked, does not match or is missing, then you decide how to handle each one. **This workflow writes to no file**: the tables and warnings in the report are computed by `python3 ../toolkit/skills/export-hub.py`.

*Status: draft.*

| | |
|---|---|
| When | After you add or edit many items, or before handoff |
| Before | Run `python3 ../toolkit/skills/export-hub.py` so the report is up to date |
| Working file | None. The result is answered right in the chat |

## Step 1: Review (AI)

**Who:** AI
**Input:** `insights/opportunities/*.md`, `insights/hypotheses/*.md`, `insights/metrics/*.md`, `insights/decisions/*.md`, `insights/evidence/*.md`, `insights/findings/*.md`, `standards/gates.md`, `standards/principle-checks.md`
**Output:** The list of problems found, answered in the chat. Nothing is written to a file.

**Instruction:**
> Read the input files and list the problems, one group per kind, in plain words with the item codes. Relationships are in the properties at the top of each item file (wikilinks) and are declared in one direction only: H has `serves` (O) and `metric` (M); D has `tests` (H), `follows` and `pulls_against` (P); E has `tests` (H) and `measures` (M); F has `found_in` (E), `affects` (D), `principle` (P), `severity` (0 to 4) and `resolution`. The reverse direction you work out yourself.
>
> - A decision that cannot be traced back to any user need (empty `tests`); a decision that goes against a principle (`pulls_against`); a need with no decision serving it; a hypothesis with no evidence or no metric; evidence with `status: planned` or `participants_type: simulated`; a hypothesis whose tests are all planned or simulated.
> - A metric with no `target`, or with a `verdict` but no `result`; an `accepted` decision with no `owner`; an opportunity with no `rank_reason`.
> - A finding missing `severity` or `found_in`; a level 3 or 4 finding that is not handled.
> - A principle in `principle-checks.md` with no yes/no question.
>
> Do not edit any file. Do not guess: if a link points at a file that does not exist, or an ID does not match the file name, or an ID is duplicated, list it at the end of the answer.

**Check:** Open any 3 entries in the list and compare them with the matching item files.
**Failure sign:** The AI reports a problem that is not in the item file; the AI edited a file; the list misses a problem the report already warned about.

## Step 2: Decide (YOU)

**Who:** YOU
**Input:** The warnings just built, and the AI's answer from step 1
**Output:** `work/alignment.md` (a verdict for each warning), `insights/case-log.md`

For each warning pick one: fix the item file, accept it as a trade-off with a reason, or cut it. For a cut item, delete the file and run this workflow again.

**Check:** Can you defend each decision by pointing to the opportunity and the hypothesis behind it?
**Failure sign:** A warning ignored because "the AI is wrong" without opening the file to check.
