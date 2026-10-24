# _skills: step cards and scripts for the AI

> **Shared.** This folder sits in `toolkit/` at the workspace root and is shared by every case. It is a copy of the `product-workspace` skill (the master). Do not edit it here: edit the skill, then run `sync-workspace.py`.

This folder holds two things. **Step cards** (`.md` files): they define AI-assisted procedures as files, so the AI tool can read them and the procedure is stored with the case. Each file is one workflow made of ordered steps, and each step says who does it (the AI or you), which files to read and where to write.

## Cards

| Workflow | Stage | When to use | Status |
|---|---|---|---|
| [`competitor-analysis.md`](competitor-analysis.md) | Discover | When you need to know what competitors are doing | Draft, not tried much |
| [`user-voice-synthesis.md`](user-voice-synthesis.md) | Discover | When you have quotes or user interviews to synthesise | Draft, not tried much |
| [`add-insights.md`](add-insights.md) | Discover, Test | When there is new research (interview, survey, test results) to turn into items | Draft |
| [`refresh-hub.md`](refresh-hub.md) | All stages | When you want the AI to review where items are not linked or are missing | Draft |
| [`add-media.md`](add-media.md) | All stages | When there are images, video, PDFs or documents to put into the report | Draft |
| [`export-hub.md`](export-hub.md) | All stages | When you need to see the hub in a browser or send it to someone | Draft |
| [`build-process-map.md`](build-process-map.md) | Develop | When you need a process map, swimlane or user flow drawn as a diagram (uses `../diagram-design/`) | Draft |

**Scripts** (`.py` files): `export-hub.py` builds the `index.html` report, `serve-hub.py` shows the report as you save files. You usually ask the AI to run them rather than opening them by hand.

The cards for Frame, Explore, Prototype and Test will be added. You can add your own cards following the guide below.

## How to run a step

1. Open the whole case folder in the AI tool. The tool reads `AGENTS.md` at the root by itself.
2. Commit first (if you use Git), so you can go back.
3. Tell the tool: *"Run step 5 of `../toolkit/skills/user-voice-synthesis.md`."*
4. Read the result, then check it yourself in the next step. A step labelled **(YOU)** is the part you still do yourself.

## Card format

Each step has fixed lines:

| Line | Meaning |
|---|---|
| **Who** | `YOU` or `AI` |
| **Input** | The files this step may read, and only those files |
| **Instruction** | The prompt given to the AI (only on AI steps) |
| **Output** | The section or file that is written |
| **Check** | What you check before moving to the next step |
| **Failure sign** | The signal that this step has gone wrong |

## Add your own workflow

Copy a card, rename it, keep the fixed lines above. Each workflow should have at most 8 steps, one working file, and two rules: the AI returns only its own section, and the AI draft is always kept apart from the version you checked.
