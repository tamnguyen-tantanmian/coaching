# Insights

This folder holds the **linked items**: user needs, what the team believes, design decisions, evidence, problems found, and the measured numbers. Each item is one file, each type has one folder:

| Folder | Type | Code | What it is |
|---|---|---|---|
| `opportunities/` | Opportunity | O1, O2... | A user need or difficulty, backed by evidence |
| `hypotheses/` | Hypothesis | H1... | Something the team believes, with a way to know if it is right |
| `decisions/` | Decision | D1... | A design choice, with its reason |
| `evidence/` | Evidence | E1... | A test or a study that checks a hypothesis |
| `findings/` | Finding | F1... | A usability problem, with a severity from 0 to 4 |
| `metrics/` | Metric | M1... | The number that tells you whether a hypothesis is right |

## Add an item

1. Copy a file from `_templates/` into the folder of its type.
2. Name the file after the next code (for example `D4.md`). A code is unique across the whole project.
3. Fill in the information at the top of the file, especially the lines that link to other items (`tests`, `serves`, `found_in`...).

The report shows these items in the **Insights** section, links them into a tree from need to decision, and warns by itself about missing links. How linking works in detail is in `../toolkit/skills/how-the-hub-works.md`.

This `README.md` does not show in the report.
