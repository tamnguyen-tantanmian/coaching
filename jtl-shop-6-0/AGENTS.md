# Rules for the AI tool

This file is for the AI tool. Read it before you do anything in this folder. The project owner decides; you draft and check.

## What this folder is

The case folder of one person who builds a product (designer, researcher, PM...) and works in an AI-assisted way: the AI drafts, the owner checks and decides. The folder is organised by the work you do: `context/` (background), `stages/` (a page per stage that tells the story), `work/` (everything that gets made), `insights/` (items linked to each other), `standards/` (reference pages), and `../toolkit/skills/` (step cards and scripts for the AI). Each way of working with the AI is defined by a step card in `../toolkit/skills/`.

## Map

Every folder at the root without a leading `_` is a section of the `index.html` report menu, with the same name.

| Path | What it is | What you may do |
|---|---|---|
| `AGENTS.md` | Rules for the AI tool (this file) | Read |
| `README.md` | Overview: the project card and the "What do you want to do?" table | Read. Edit only when asked |
| `guide.md` | The Guide page of the report (the "Guide" tab in the left menu): what the workspace is, starting a project, adding a task, preview, AI vocabulary. Written for non-technical readers | Read. Edit only when asked; keep the simple voice and the sample prompts that can be pasted into an AI tool |
| `context/*.md` | Context pack: background (product, users, data rules, design system) | Read first, in every step. Do not edit unless asked |
| `../toolkit/skills/*.md` | The definition of each way of working with the AI (step cards) | Read the card of the step that is running |
| `stages/README.md` | The Pages table: each row is a stage page, assembled from the files in `work/` and the item tables in `insights/` | Edit the table only when asked. Do not create other `.md` files here: a stage page has no content of its own |
| `work/*.md`, `work/<name>/index.md` | Everything that gets made: working files per stage (`scope`, `problem-brief`, `findings`...) and documents (wireframe, persona, flow). May include images, PDFs, HTML in the folder | Write only into the section you were asked for. Do not copy content into `stages/`: that page links back to the working file |
| `work/sources/anonymised/` | Anonymised data, with IDs | Read. The only source for quotes and figures |
| `work/prototype/` | Prototype code | Work here when building the prototype, following `project-rules.md` in that folder |
| `insights/opportunities/O1.md`, `hypotheses/H1.md`, `metrics/M1.md`, `decisions/D1.md`, `evidence/E1.md`, `findings/F1.md`... | The **single source** of each item (O, H, M, D, E, F). One folder per type; the file name is the item code | Read. Edit only when asked to edit that exact item. Never set `resolution: fixed` or `accepted` on a finding yourself |
| `insights/_templates/` | Empty templates for each item type | Read. Copy into the right type folder (for example `insights/decisions/`) when asked to create an item; never edit the template file |
| `standards/*.md` | Yardsticks to check the work: gates, principle checks, severity levels, and any criteria the owner adds | Read. Edit only when asked for that exact page. `insights/case-log.md`: add a line when asked |
| `../toolkit/skills/new-item.py` | The command that creates an item and links it | Run when asked to create an item (see Where things go). Do not edit |
| `../toolkit/skills/export-hub.py` | The script that exports the report to one HTML file | Run after you change files in the case, and when asked (`python3 ../toolkit/skills/export-hub.py`). Do not edit, and do not write the HTML yourself instead of the script |
| `index.html` | The report, exported from Markdown to view in a browser | Do not read, do not edit by hand. To update it run `../toolkit/skills/export-hub.py` (run it yourself after every change to the files) |
| `_personal/` | The owner's private notes | **Do not read, do not write** |
| `work/sources/_raw-private/` | Raw data that is not anonymised | **Do not read, do not write** |

## Where things go

When the owner asks you to make or add something without saying where it goes, choose the place from this table. If the owner already said where, follow them.

| The owner gives or asks for | Put it in | Notes |
|---|---|---|
| Images, PDFs, video, an HTML prototype, a flow, or a document for others to view | `work/<short-name>/` with an `index.md` (start from a template in `../toolkit/templates/`); a single file goes to `work/<name>.md`. Follow `../toolkit/skills/add-media.md` | Fill `supports` with the item codes it is evidence for, if known. If not known, leave `[]`; do not guess |
| A flow diagram from Mermaid (user flow, E2E) | `python3 ../toolkit/skills/flow-from-mermaid.py <file.md> --out work/<name> --title "..."`: one picture per subgraph; solution codes (A4, P3) get the decision code from the decision's `solutions` property | Needs the archify skill. If a decision implements a solution, put its code in `solutions` |
| Running a method (assumptions map, journey map, ideation...) | Fill the method card that already exists in `work/` (see the stage tabs of Work); do not create a new file if one exists | Change `status` from `planned` when you start |
| A draft or summary of a stage | `work/<name>.md`, the file of that stage (`scope`, `user-voice-synthesis`, `competitor-analysis`, `problem-brief`, `options`, `alignment`, `test-plan`, `findings`, `handoff`, `measurement-plan`) | Write only into the section you were asked for |
| A design decision | `python3 ../toolkit/skills/new-item.py D ...` with `--owner`, `--state`, `--reason` (also writes the case log). Never set `accepted` before the owner says so | `proposed` is the default |
| New research material (interview, survey, test) to extract insights from | Follow `../toolkit/skills/add-insights.md`: propose first, wait for the owner to approve, only then create the items with `new-item.py` | Do not create items before approval |
| The measured result of a metric after launch | Fill `result`, `measured_on`, `verdict` in `insights/metrics/M<number>.md`; write what was learned in `work/learning.md` | Record only the numbers the owner gives; do not guess a `verdict` |
| A need, hypothesis, metric, decision, evidence or finding | `python3 ../toolkit/skills/new-item.py <O/H/M/D/E/F> --title "..."` with the relationships (`--tests H1`, `--serves O1`, `--found-in E1`...). The command picks the next code, creates the file in the right folder and checks that every code you link exists | Fill the relationships from what the owner gave you; if you are unsure about a relationship, ask, do not guess. See `python3 ../toolkit/skills/new-item.py --help` |
| New background about the product (glossary, brand voice, rules...) | `context/<name>.md` | The AI reads it first; it shows up in the Context section by itself |
| A new criterion or checklist to check the work | `standards/<name>.md` | Shows up in the Standards section by itself |
| Raw research data (interviews, surveys) | **Never** put it into `work/sources/anonymised/` yourself. Ask the owner to anonymise it first; the original goes to `work/sources/_raw-private/`, which you do not read | |
| The owner's private notes | `_personal/` | You do not read or write it |
| Unclear which kind it is | Ask one question | Do not guess and do not put it at the root of the folder |

When you place a file:

1. **Next code:** list the type folder and use the largest number plus one. Never overwrite an existing file.
2. **Short, lowercase file names joined by hyphens** for documents; the item code for items.
3. **Say where you put it:** give the full path, and anything you are unsure about (for example `supports` left empty).
4. **Rebuild the report yourself** after you add or edit files in the case: run `python3 ../toolkit/skills/export-hub.py`, then say the result (the number of warnings and what needs fixing before handoff). For a deeper review use `../toolkit/skills/refresh-hub.md`.

## Hard rules

1. **Return only the section you were asked for.** Do not edit other sections or other files. The owner pastes the result in, or you write exactly into the section you were pointed to.
2. **Do not edit an "(AI draft)" section after you created it, and do not edit the owner's "(verified)" section** unless you were asked for exactly that section. Drafts and checked versions always sit in two separate sections.
3. **Use only sources in `work/sources/anonymised/`.** Never invent a quote, a figure, a product name or a source. If it is not in the sources, write `unknown`.
4. **Quote verbatim, with the ID.** Do not rewrite or shorten.
5. **Any number that is not confirmed is `assumed`.** An inference that is not in the sources is `inferred`.
6. **Stop and tell the owner** if you see data that looks not anonymised (names, emails, usernames, company names) in a folder you are allowed to read.
7. **Say what you are unsure about.** List the items you are unsure of instead of guessing a link or a relationship.
8. **Never make a copy of an item.** An item exists only in its own file (`insights/decisions/D2.md`...). Relationships live in the properties (the `---` block at the top of the file) as wikilinks in quotes, declared in one direction only. Tables elsewhere are `generated` blocks; do not fill them by hand.
9. **If the folder is a git repo with uncommitted changes,** remind the owner to commit before you write files.

## Reading order

1. `AGENTS.md`
2. `context/*.md` (all of them, unless the card says otherwise)
3. The card of the step that is running, in `../toolkit/skills/`
4. Exactly the input files the card lists, nothing more

Do not read the whole folder "to get more context": unrelated files make the result worse.

## Running a step

When the owner says "run step N of `../toolkit/skills/<name>.md`":

1. Read the card and find step N.
2. Read only the files on that step's `Input` line.
3. Follow the `Instruction` line and write the result into the section on the `Output` line.
4. Report: which files you read, where you wrote, what you are unsure about.

A step labelled **(YOU)** is the owner's job: do not do it for them, help only if asked.

## Writing

- Answer in the language the owner writes in. Write document content in the language of the source material and the owner (Vietnamese if that is what they use), and keep trade terms in English (insight, hypothesis, opportunity, handoff...).
- Keep section headings in English: the step cards and the hub refer to them by those names.
