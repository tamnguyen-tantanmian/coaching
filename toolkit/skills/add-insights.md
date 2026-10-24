# Workflow: Add insights from new research

Turn a new piece of research (interview, survey, test results) into items in `insights/`, so the new insight shows on the Insights page and links to the need, hypothesis and decision behind it.

*Status: draft. Try it on a real document and adjust it to how you work before you rely on it.*

| | |
|---|---|
| When | After you add a research file to `work/` (or `work/<name>/index.md`) and want to bring what was learned into the hub |
| Before | Anonymise the data, save a checkpoint (commit or copy the folder) |
| Working file | None. The result is written into `insights/` and the document's `supports` property |
| Related | `../toolkit/skills/new-item.py` (creates items), `../toolkit/skills/refresh-hub.md` (checks the warnings afterwards) |

The hub does **not extract insights by itself** from files in `work/`. This workflow is the step that does that, and you approve before any file is created.

## Step 1: Propose (AI)

**Who:** AI
**Input:** The new document (a single file), the list of existing items in `insights/` (codes and titles), `standards/principle-checks.md`
**Output:** A proposal table right in the chat. **No file is created yet.**

**Instruction:**
> Read the new document. Propose the insights that are in that document itself, one table row per insight with: (1) a short excerpt or quote code as the source, (2) the proposed item type (evidence, opportunity, finding, hypothesis), (3) a one-sentence title, (4) its relationships to existing items (`tests`, `serves`, `found_in`...) using codes that really exist, (5) whether it **reinforces**, **contradicts** or is **new** compared with the existing items, (6) how sure it is: one source or several.
>
> Rules: use only what is in the document, do not infer more. An interview or a test is always one evidence; propose a new opportunity only when the need is not in the list yet. If an insight contradicts an existing item, say so clearly and do not merge them. Do not set any decision to `accepted`, and do not pick a rank or an impact yourself: leave it empty for me to decide.

**Check:** Open the document and cross-check any three rows: is the source really there?
**Failure sign:** An insight with no source in the document; an item code in the relationship column that does not exist; the AI merged a contradicting insight into an old item without saying so.

## Step 2: Decide (YOU)

**Who:** YOU
**Input:** The proposal table from step 1
**Output:** The list of approved rows, with your edits

For each row pick one: keep it, edit the title or the relationships, or cut it. For a new opportunity, say the `impact`, the `confidence` and the reason for the rank yourself (or leave it empty and fill it in later).

**Check:** Can you defend each kept row by pointing to a passage in the document?
**Failure sign:** Keeping a row only because the AI wrote it in a way that sounds reasonable.

## Step 3: Create the items (AI)

**Who:** AI
**Input:** The rows approved in step 2
**Output:** New files in `insights/<type>/`

**Instruction:**
> For each approved row, run `python3 ../toolkit/skills/new-item.py <type> --title "..." <relationships> --no-build`. For the evidence of an interview or a test that has taken place: `--status run --participants <number of people>`. Do not overwrite files. After creating them, fill in the content of each file with what is in the document, with its source. If the command says a code does not exist, stop and ask me, do not guess.

**Check:** Open two of the new files: do the title, the relationships and the source match the row you approved?
**Failure sign:** More files were created than rows approved; an item has `status: run` but the test never ran.

## Step 4: Link the document (AI)

**Who:** AI
**Input:** The new document and the codes of the items just created or affected
**Output:** The `supports` property in the head of the document

**Instruction:**
> Fill the document's `supports` with the codes of the items just created and of the existing items that the document reinforces or contradicts. Edit only this property; do not edit the content of the document.

**Check:** Open the document in the report: does the "Supports" line list exactly the right items?
**Failure sign:** `supports` points at an unrelated item.

## Step 5: Rebuild and read the warnings (YOU)

**Who:** YOU
**Input:** The whole hub
**Output:** A new `index.html`

Run `python3 ../toolkit/skills/export-hub.py`, open the **Insights** page to see the new items, then read the warnings on the Overview: a new opportunity with no decision, a hypothesis with no test, a metric with no target are the things to do next. If you want this piece of research to show on the Evidence page in Stages, add the file name to the **From work** column of the `evidence` row in `stages/README.md`.

**Check:** Can each insight you approved be found in Insights, and traced back to the document?
**Failure sign:** A new item is linked to nothing (it sits in the group "Not linked to any opportunity").
