# How the Hub Works

The hub is where you record **what the project decided and why**. Each design decision is linked back to the user need behind it, so anyone can ask "why did we do this?" and trace the answer.

The word "hub" here is the common name for the whole body of content of the project and the `index.html` report that displays it. This page has two parts: **Read the hub**, for everyone, and **Update the hub**, for the person who keeps the hub.

---

# Read the hub

## Where to see the hub

Double-click the `index.html` file in the project folder: it opens in the browser, nothing to install. The left menu has six sections, each matching a folder of the same name:

| Section | Folder | What you see |
|---|---|---|
| **Overview** | `README.md` | Where the project stands: the number of items of each type, the gates, what needs review (warnings), and how far decisions are linked back to needs |
| **Context** | `context/` | What the product is, who the users are, the data rules, the design system |
| **Stages** | `stages/` | The story of the project stage by stage: scope, evidence, problem brief, the directions explored, findings, handoff. Assembled from the files in `work/` and the items in `insights/`, not written separately |
| **Work** | `work/` | Everything made in the project: working files, competitor analysis, personas, surveys, wireframes, prototype |
| **Insights** | `insights/` (`opportunities/`, `hypotheses/`, `decisions/`, `evidence/`, `findings/`, `metrics/`) | All the linked items. You can filter, search, and view them as Cards, Tree or Alignment table |
| **Standards** | `standards/` | The yardsticks to check against: gates, principle checks, severity levels |

## The six types of item

| Type | What it is | Example |
|---|---|---|
| **Opportunity** | A user need or difficulty, backed by evidence. Not a feature | "Travellers want to plan in one place" |
| **Hypothesis** | Something the team believes is true, with how it will be known whether it is | "One-tap save gets information into the plan faster" |
| **Decision** | A specific design choice, with its reason | "Open the Explore tab in Near Me mode" |
| **Evidence** | A test or a study that checks a hypothesis, with its result | "Usability test with 8 people" |
| **Metric** | The number that tells you whether a hypothesis is right | "80% of users complete the task without help" |
| **Finding** | A usability problem found in an evaluation or a test, with a severity (0 to 4) | "There is no way to invite someone who is not on the list" |

The right reading chain is: **Opportunity → Hypothesis → Decision**, and **Evidence** checks the hypothesis measured by a **Metric**. From Evidence, a **Finding** says which problem showed up and which decision it affects.

## A few things to know when reading

- **The ⚠ sign** means that spot needs a second look, it is not an error. It may be a decision not yet linked to any need, a hypothesis with no test, or evidence that is only a plan.
- **assumed** is a number nobody has confirmed. Do not treat it as fact.
- **Evidence labelled Simulated or Planned** is not yet evidence from real users. The hub labels it so you do not mistake it.
- **Items whose `state` is `shipped`, `superseded` or `dropped`** are hidden by default in Insights. Turn on "Show closed items" to see them again.
- **Sharing:** send the `index.html` file (rename it so it is easy to recognise, for example `onboarding-redesign-report.html`), not the whole folder.

---

# Update the hub

This part is for the person who keeps the hub.

## Folder structure

```
(the root folder of the project)
├── README.md              Overview: the project card, and the source of the Overview page in the report
├── context/               background: product, users, rules, design system
├── stages/                stage pages built from work/ and insights/
│   └── README.md          the Pages table: each row is a page, in the order of the report
├── work/                  everything made: working files, wireframes, prototype, personas...
│   ├── README.md          how to add documents, images, video, PDFs
│   ├── sources/           research data (anonymised/ and _raw-private/)
│   └── prototype/
├── insights/
│   ├── opportunities/     O1.md, O2.md ...   one file per item, one folder per type
│   ├── hypotheses/  metrics/  decisions/  evidence/  findings/
│   ├── _templates/        empty templates for each item type (copy into the type folder)
│   └── traceability.base  tables by item type, used when opened in Obsidian
├── standards/             gates, principle checks, severity levels, and the case log
└── _personal/             private notes
```

The shared step cards and scripts live in `toolkit/skills/`, the document templates in `toolkit/templates/`, the guides in `toolkit/guides/`. All three sit **outside the case**, in `toolkit/` at the workspace root, not inside each case.

The decision log is at `insights/case-log.md`, and the principles (P1 to P10) are at `standards/principle-checks.md`.

## The principle: each fact is written in one place

**Each item is its own file, and that file is the single source.** Every summary table in the hub (alignment, warnings, the item lists, the gate status, the tables on the stage pages) is built by `export-hub.py` from the item files, `gates.md` and the files in `work/`. You do not fill them in by hand and you do not copy an item to another place. To change a decision, edit that decision's file, then ask the AI to update the tables.

| You write | The report builds (do not edit by hand) |
|---|---|
| Item files (`O*.md`, `H*.md`, `M*.md`, `D*.md`, `E*.md`, `F*.md`) | The alignment table, Warnings and the item lists |
| Working files in `work/` (scope, problem brief, options, findings, learning...) | The stage pages in the Stages section |
| The status of each check in `standards/gates.md` | The Gates table and the gate row of each stage |
| Your verdicts in `work/alignment.md` | The Outcomes table on the Learning page |

## Create an item

1. Copy a file from `insights/_templates/` into the folder of its type (for example `insights/decisions/`).
2. Name the file after the next code (for example `D4.md`). A code is unique across the whole hub; the first letter tells the type: O, H, M, D, E.
3. Fill in the information at the top of the file and a few lines of description.

The block at the top of the file (between the two `---` lines) is the only place that records **relationships between items**. A relationship is written in one direction only, from the later item back to the earlier one:

| Type | What to fill in | Points to |
|---|---|---|
| Opportunity | `title`, `rank`, `evidence` | a quote code or a source |
| Hypothesis | `title`, `serves`, `metric` | Opportunity, Metric |
| Metric | `title`, `status`, `baseline`, `measured_by` | values |
| Decision | `title`, `tests`, `follows`, `pulls_against` | Hypothesis, principle |
| Evidence | `title`, `tests`, `measures`, `participants`, `result`; optional `status` (`planned` if not run yet) and `participants_type` (`simulated` if not real people) | Hypothesis, Metric |
| Finding | `title`, `severity` (0 to 4), `principle`, `found_in`, `affects`, `resolution` (`open`, `fixed`, `accepted`, `deferred`) | Principle, Evidence, Decision |

How to record a relationship:

```
---
type: "decision"
title: "Add a progress bar to the checklist"
tests:
  - "[[H1]]"
follows:
  - "[[principle-checks|P1]]"
pulls_against:
  - "[[principle-checks|P8]]"
---
```

Rules:

1. **Write each link as `"[[H1]]"`**, with quotes and two pairs of square brackets. For a principle, write `"[[principle-checks|P8]]"`.
2. **If there is none, write `[]`.** Do not delete the line.
3. **In Obsidian you do not need to type it by hand:** click the field, type `[[`, choose the file.
4. A decision that goes against a principle gets `pulls_against`, and the reason it was accepted is written in the description.
5. If you cannot confirm it yet, write `assumed`.

The reverse direction (which hypothesis serves this opportunity, which evidence this hypothesis has) is **not written in the file**: the report works it out and shows it under "Linked from".

## Topic and state (optional)

When the hub has many items, these two help you filter. They work for every item type:

| Information | Values | What it does |
|---|---|---|
| `area` | a word of your own, for example `onboarding`, `pricing` | Filters by topic in Insights. An item with no `area` always shows, even when you filter |
| `state` | `active` (default), `proposed`, `accepted`, `shipped`, `superseded`, `dropped` | `shipped`, `superseded`, `dropped` are hidden by default in Insights and no longer create warnings. `proposed` and `accepted` are for decisions: proposed, then accepted |

## Documents (artifacts)

An item says **what was decided and why**. A document is **the thing that was made** behind the decisions: a competitor analysis, a persona, survey results, a user flow, a prototype, a test report. Each document has its own page in the Work section and links to the items it supports.

How to add a document is in `work/README.md`. A document points back at the original working file instead of copying the content, so a fact lives in one place only.

## Add images, video, PDFs

Drop images, videos or PDFs into a folder in `work/`, or insert an image in the middle of a page with `![description](path)`. The report recognises the format by itself; details and warnings are in `work/README.md`.

## Each time you update

1. Create or edit the item files of the stage you are working on.
2. Write the narrative part on the stage page, from the checked version. Do not put the AI's draft on the hub.
3. Update the status in `gates.md`.
4. Ask the AI tool to update the hub (see below) to rebuild the tables and warnings.
5. Read the warnings, decide each one, and write the verdict in `alignment.md`.
6. Add a line to `insights/case-log.md`.
7. Rebuild `index.html` so others see the new version.

## Ask the AI to review the hub

Save a checkpoint first (commit in GitHub Desktop, or copy the folder into a `-backup` copy), then tell the AI tool:

> Run `../toolkit/skills/refresh-hub.md` (review where items are not linked or are missing).

This step only returns the list of problems found; it writes to no file. After it runs, check a few lines of the table against the item files to be sure the AI did not infer a wrong relationship.

To rebuild `index.html`, ask the AI tool to run `python3 ../toolkit/skills/export-hub.py`. To see changes as soon as you save a file, run `python3 ../toolkit/skills/serve-hub.py` (details in `../toolkit/skills/export-hub.md`).

## Decisions, ranking and the outcome loop

Three groups of information help the hub answer "why" and "what was the result". All are optional, but the report reminds you when they are missing:

| Item | Property | Meaning |
|---|---|---|
| Decision | `owner`, `decided_on`, `state` | Who is responsible, the date of the decision, and whether it is `proposed` or `accepted`. An `accepted` decision with no `owner` gets a reminder |
| Opportunity | `rank`, `impact`, `confidence`, `rank_reason` | The rank with its reason: impact (`high`/`medium`/`low`), how sure the evidence is, and one or two sentences of explanation |
| Metric | `target`, `result`, `measured_on`, `verdict` | The threshold, the measured result, the date measured, and the verdict: `pending`, `met`, `missed`, `inconclusive` |

After launch, fill `result` and `verdict` in the metric file, then open the **Learning** page in Stages: the Outcomes table links each metric to the hypothesis and opportunity behind it, and a `missed` metric marks the opportunity "revisit". The text part (what was learned, which opportunities to reopen) you write in `work/learning.md`.

## What the report checks by itself

The report does not only display, it also cross-checks the parts against each other:

- **Gates:** for the checks the data can answer (1b, 2a, 2c, 2d, 3b, 3c, 4a, 4b), the "Automatic check" column on the Gates page shows whether the current data meets them. The status you set stays yours; if you set `passed` and the data does not support it, the report shows a warning.
- **Findings:** an unhandled level 4 blocks handoff, an unhandled level 3 needs a decision, and the affected decision is flagged too.
- **Case log:** the codes mentioned in the Items column must exist, and each decision should have at least one line in the log. Codes become links.

## Gates

The four gates and the checks 1a to 4d are in [`gates.md`](../standards/gates.md). For each check, set the status to `open`, `passed` or `failed`. **Do not rename a check, only change its status.** A gate is `passed` when all its checks are `passed`, `failed` when any check is `failed`, otherwise `open`.

## Common mistakes

| Mistake | How to fix it |
|---|---|
| Editing an automatic table by hand | The next update overwrites it. Edit the item file, then ask the AI to update again |
| Copying an item into a stage page or a working file | Link to the item file, do not copy the content |
| Two items share one code | Change one item to a new code, and rename its file too |
| A code in a file does not match the file name | Change it to match |
| A link points at a file that does not exist | Create the missing item file, or fix the code |
| A relationship written at both ends | Keep it at the `serves` / `tests` / `follows` end, delete the other |
| A decision with `tests: []` | Link it to a hypothesis, or cut it. Record it in the verdict in `alignment.md` |
| `[[ ]]` links cannot be clicked on GitHub | As designed: only Obsidian turns them into links. Use the `index.html` report to share |

## Notes

- The hub is private by default. How to let others see it is in `toolkit/guides/04-share-your-hub.md` at the workspace root.
- P1 to P10 are Nielsen's 10 usability heuristics. Add your organisation's own principles from P11 on in `standards/principle-checks.md`.
- The hub works with any tool that can open a whole folder: an AI coding tool, VS Code or Obsidian. Obsidian adds Graph view and Backlinks (see `toolkit/guides/05-obsidian.md`).
