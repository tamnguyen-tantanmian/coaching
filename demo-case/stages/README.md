# Stages

Each stage of the project has a page in the report, in the **Stages** section. **You do not write stage pages.** The report assembles each page by itself from two sources:

- the working files in `work/` (the **From work** column), together with the `status` of each file (verified, draft...);
- the item tables from `insights/` (the **Item tables** column): opportunities, hypotheses, metrics, decisions, evidence, findings.

To change the content: edit the file in `work/` or the item in `insights/`, then rebuild `index.html`. To change the order or add a stage: edit the table below (the order of the rows is the order in the report).

## Pages

| Id | Page | Stage | Content | From work | Item tables |
|---|---|---|---|---|---|
| `scope` | Scope | Discover | Business question, outcome, agreement | `scope.md` | |
| `evidence` | Evidence | Discover | What was learned from the sources, one source per claim | `user-voice-synthesis.md`, `competitor-analysis.md` | |
| `problem-brief` | Problem brief | Define | Opportunity, hypothesis, metric, principle | `problem-brief.md` | opportunities, hypotheses, metrics |
| `develop` | Options, flows, prototype | Develop | The directions explored, decisions | `options.md`, `process-map.md`, `wireframes/`, `final-prototype/` | decisions |
| `alignment` | Alignment check | Develop | Principle audit, verdict | `alignment.md` | |
| `findings` | Findings | Deliver | Results of testing with users | `findings.md` | evidence, findings |
| `handoff` | Handoff and measurement | Deliver | Handoff pack, measurement plan | `handoff.md`, `measurement-plan.md` | |
| `learning` | Learning | Learn | What was learned after launch: metric against target, traced back to the opportunity | `learning.md` | outcomes |
| `decision-log` | Decision log | All stages | One line per decision, with its reason | `insights/case-log.md` | |

## How to read the table

| Column | Meaning |
|---|---|
| **Id** | A short name, lowercase, no accents. Used as the address of the page. |
| **From work** | A file in `work/` (write the file name, for example `scope.md`) or a folder with an `index.md` (for example `wireframes/`). A file in `insights/` is written with its full path (for example `insights/case-log.md`). May list several, separated by commas. |
| **Item tables** | Which tables show on this page: `opportunities`, `hypotheses`, `metrics`, `decisions`, `evidence`, `findings`, or `outcomes` (metric, measured result and the opportunity behind it). Leave empty if not needed. |

Each source file shows its status. A file that is still `draft` is shown, but labelled "Draft, not checked" so the reader knows it is not something that has been checked: change `status` to `verified` when you have checked it.
