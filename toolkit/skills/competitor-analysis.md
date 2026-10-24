# Workflow: Competitor Analysis

Shows **what competitors do**, not why users choose them. Treat the result as hypotheses to test with real users.

*Status: draft. Try the instructions on a real case and adjust them to how you work before you rely on them.*

| | |
|---|---|
| Working file | `work/competitor-analysis.md` (each step fills one section) |
| Sources | `work/sources/anonymised/` |
| Final output | `work/competitor-analysis.md` (the Evidence page in Stages is built from this file) |

## Sections of the working file

| Section | Filled in step | By |
|---|---|---|
| `## Scope` | 1 | YOU |
| `## Competitors` | 2 and 3 | Step 2: the AI's suggestions, labelled. Step 3: your final list |
| `## Evidence (AI draft)` | 5 | AI. **Do not edit** |
| `## Evidence (verified)` | 6 | YOU: your corrected copy |
| `## Patterns` | 7 | AI |
| `## Insights + decision` | 8 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the checked version.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: the right competitors? | 3 | Go back to step 2 and fix the list |
| B: traceable? | 6 | Run step 5 again with a tighter instruction, then check again |
| C: evidence, not the AI's opinion? | 8 | Go back to step 7 and redo the comparison |

---

## Step 1: Frame the question

**Who:** YOU
**Input:** `work/scope.md`
**Output:** `## Scope`

Fill in: the decision this analysis serves (for example "Should we add a self-service onboarding flow?"), the criteria that matter (at most 6, set by you), and 3 to 5 things you already believe, for step 7 to test.

**Check:** Would a stranger reading it know what a good answer looks like?
**Failure sign:** Criteria like "features", "UI" that are not tied to the decision; no beliefs written down.

## Step 2: Suggest

**Who:** AI
**Input:** The `## Scope` of the working file (only this section)
**Output:** `## Competitors`, labelled "AI suggestions"

**Instruction:**
> Use only the scope below. Suggest competitors in three groups: direct, indirect and alternatives (including "doing nothing" and doing it by hand). One line per competitor saying why it competes for the same job of the user. Say how sure you are and what you are not sure about. Do not invent products; if you are not sure a product exists, say so. Then suggest only the criteria that are **missing** from my list and why each one matters for the decision. Do not replace my criteria.

**Check:** Is there a name that sounds plausible but you cannot find on the web? Mark it to drop.
**Failure sign:** Only famous brands; names that sound made up; your criteria were silently changed.

## Step 3: Review the list · Gate A

**Who:** YOU
**Input:** `## Competitors` (the AI's suggestions)
**Output:** `## Competitors` (the final list)

Edit the suggestions into a final list, with a reason for each competitor chosen and each one dropped. Add the people who are missing. Ask someone in sales, support or the customer team.

**Gate A:** Are these real alternatives of **our own users**, or just famous names? Who is missing? Why were those others cut?
**Failure sign:** Everything in the AI's list was kept.

## Step 4: Collect sources

**Who:** YOU
**Input:** The final list in `## Competitors`
**Output:** Files in `work/sources/anonymised/`

Save the pricing page, the features page, the onboarding screens, the app store reviews and the help pages of the competitors you kept, and only those competitors. Name them clearly (for example `competitor-a-pricing-2026-10.png`) and write the date. You open and save every source yourself. Do not let the AI supply information from its memory.

**Failure sign:** A competitor's source was cut off; no date; only a link saved instead of a copy.

## Step 5: Extract

**Who:** AI
**Input:** `## Scope`, `## Competitors`, and the files in `sources/anonymised/` (one competitor at a time)
**Output:** `## Evidence (AI draft)`

**Instruction:**
> Fill the table using only the sources provided. For each cell, write the source file name and the exact phrase or screen it rests on. If the source does not say, write "unknown"; do not guess and do not use background knowledge. Anything that is an inference is marked "inferred". Return only the markdown table, nothing else, so I can paste it as a section of its own.

Columns: Competitor, Criterion, Finding, Source file, Quote or screen, Status (stated / inferred / unknown).

**Failure sign:** No "unknown" cell at all; citations to sources that are not in the folder.

## Step 6: Spot-check · Gate B

**Who:** YOU
**Input:** `## Evidence (AI draft)` and the source files
**Output:** `## Evidence (verified)`, with the error rate at the top of the section

Copy the draft table into `## Evidence (verified)`. Check **every cell of the top 2 to 3 criteria**, plus about 20% at random of the rest, plus every "inferred" row and everything surprising. Open the source and compare. Fix the errors.

**Gate B:** Does every cell trace back to a source you opened? Is "unknown" still unknown? Is the error rate acceptable? If many cells are wrong, go back to step 5.
**Failure sign:** Only the easy cells were checked; no error rate recorded.

## Step 7: Compare + challenge

**Who:** AI
**Input:** `## Scope` (including what you already believed) and `## Evidence (verified)`. **Do not** give it the AI's draft
**Output:** `## Patterns`

**Instruction:**
> From the checked table, list the patterns, the gaps and the differences that matter for the decision in the scope. Cite the rows each rests on. Then go through each belief I wrote down and say whether the evidence supports it, contradicts it or does not mention it. Then for each pattern, write the strongest argument that it is wrong or misleading, and say what evidence would change your mind. Do not propose actions yet. Say what this table cannot tell us. Return only this section.

**Check:** Does every pattern cite rows? Is the counter-argument real or one sentence to fill the space? Is any belief of yours contradicted (that is the most valuable part)?
**Failure sign:** Generic findings ("competitors focus on simplicity"); the counter-argument agrees with the finding; every belief is "supported".

## Step 8: Interpret + decide · Gate C

**Who:** YOU
**Input:** `## Patterns`, `## Scope`, `standards/principle-checks.md`
**Output:** `## Insights + decision`, then the Evidence page in Stages (built from the working file)

Weigh each pattern against your own users and the principles. A pattern that appears across many competitors is not necessarily important. Write 3 to 5 insights with links to the evidence, **the answer to the decision in step 1** in one sentence ("Should / should not do X, because Y", or "not enough evidence" with what is missing), and the open questions to ask real users. Put the checked version on the hub's Evidence page.

**Gate C:** Is each insight tied to our problem and our principles? Is it evidence, or an AI opinion you have not checked? Can you defend it by opening the source?
**Failure sign:** An insight copied straight from `## Patterns`; no decision; no open questions.

---

## The limit to state plainly

This analysis shows what competitors **do**, not **why** users choose them or whether it works. Use the findings as hypotheses for the interviews in the later weeks.
