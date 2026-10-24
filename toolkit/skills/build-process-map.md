# Build a process map or user flow (diagram-design)

Use this when a project needs an end-to-end process map, a swimlane, a user flow or any other diagram (journey, sequence, state machine…). The diagram is one self-contained HTML file with inline SVG, drawn with the `diagram-design` skill that lives in this workspace: [`../diagram-design/SKILL.md`](../diagram-design/SKILL.md).

The demo project shows the result: `demo-case/work/original-docs/08_E2E_Process_Map.html` (opened by `demo-case/work/process-map.md`).

## Before you start

- Open the whole workspace folder in the AI tool, so it can read `toolkit/diagram-design/`.
- Collect the **actors** (people or systems, at most 5), the **steps** each actor does, the **decisions** (yes/no) and the **handovers** between actors. A written flow, a Mermaid chart or your notes are enough.
- Use generic labels in the diagram text (for example "the AI chat tool", not a product name), and anonymise names of real people.

## Steps

| # | Who | What |
|---|---|---|
| 1 | You | Tell the AI tool: *"Read `toolkit/diagram-design/SKILL.md`, then build the process map for this project. Source: `<file or notes>`."* |
| 2 | AI | Picks the diagram type (swimlane for who-does-what and handovers; flowchart for one actor's decisions; journey for feelings) and **states the plan before drawing**: type, size, what it will cut. |
| 3 | You | Answer the style question once: keep the default skin, or give a website, colours or a design system. Check the plan, then say go. |
| 4 | AI | Draws the diagram as `work/<name>/process-map.html` (or into `work/original-docs/`) and runs `python3 toolkit/diagram-design/scripts/self_check.py <file>`. |
| 5 | You | Open the HTML in a browser. Check: every step in its actor's column, no line crossing a box, each decision has Yes and No, the key moment is the only orange box. |
| 6 | AI | Copies `toolkit/templates/process-map.md` to `work/process-map.md`, fills `summary`, `takeaways`, `supports`, and sets `source:` and `media:` to the HTML file with `embed: true`. |
| 7 | AI | Runs `python3 toolkit/skills/export-hub.py` **from inside the project folder** (no `--out`), so the media path stays correct. Open `index.html` → Work → the new card. |

## Rules that make the diagram readable

- **One diagram, one story.** About 9 nodes per diagram. A long journey becomes an overview plus one view per stage. Above 9 nodes, zone them (one labelled band per stage, 2 to 4 bands) and stop at 24.
- **One owner per step.** A step sits in exactly one actor's column.
- **Lines turn at right angles only**, never diagonal, never through a box that is not their start or end.
- **Orange is for 1 or 2 things per diagram**: the key moment or the one handover the story is about. Nothing else.
- **Branches are labelled** YES / NO; the alternative branch is dashed.
- **Do not invent steps.** Every box comes from your source. If a step is missing, ask.

## Changing the skin or the size

Edit `toolkit/diagram-design/references/style-guide.md` (colours and fonts) or ask the AI tool to run the onboarding in `references/onboarding.md` with your brand URL. For a slide or a printout, ask for a size: `slide-16x9`, `print-a4-landscape` and so on (`references/output-spec.md`). To get a PNG or SVG file out of the HTML, ask: *"Export this diagram to PNG"* (`references/export.md`; needs Python and a headless browser).

## Updating the skill

`toolkit/diagram-design/` is a trimmed copy of the `diagram-design` skill (templates and a few examples; the full gallery is not included). It is kept up to date by `sync-workspace.py` of the `product-workspace` skill: `--check` reports files that differ from the `diagram-design` skill, and running it without `--check` copies them over. Do not edit it per project: put project choices in the diagram, not in the skill.
