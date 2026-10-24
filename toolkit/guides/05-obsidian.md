# Obsidian

This guide is **optional**. The hub works in any tool that can open a folder (see [`02-set-up-your-case.md`](02-set-up-your-case.md)). Obsidian is an extra choice for when you want to see the relationships between decisions, hypotheses and tests as a picture, and to have tables by type without running a script.

## Setup

1. Install Obsidian from [obsidian.md](https://obsidian.md) (free for personal use). You need version **1.9 or later** to use Bases.
2. Open Obsidian and choose **Open folder as vault**. (A vault is what Obsidian calls a folder that it manages.)
3. Choose **your case folder** (for example `onboarding-redesign`). Do not choose the workspace root folder.
4. Obsidian will create an extra `.obsidian/` folder in the case folder to store settings. You do not need to touch it.
5. Open **Settings**, choose **Core plugins**, and turn on **Bases** if it is not already on.

Obsidian may ask whether you want to turn on "community plugins". You do not need them.

## What you get

| Feature | Use it to | How |
|---|---|---|
| **Tables by type** | See every decision, hypothesis, test at once | Open `insights/traceability.base`, then switch between the tabs: Opportunities, Hypotheses, Decisions, Tests, Metrics |
| **Properties** | Link one item to another without typing a code | Open an item file, click the `tests` line, type `[[`, then choose a file from the list |
| **Backlinks** | See which items link to this one | Open the Backlinks pane in the right sidebar while an item is open |
| **Graph view** | See the whole network of relationships in one picture | `Cmd+G` (Mac) or `Ctrl+G` (Windows) |
| **Search** | Find by code or keyword | `Cmd+Shift+F` or `Ctrl+Shift+F`, for example `file:/^D\d+/ P8` (decision files only) |

## Make the graph readable

By default Graph view shows the working files too. To see only the hub:

1. In Graph view, open the **Filters** pane and type `path:insights` into the search box.
2. Open **Groups** and add one group per type, each in its own colour:
   - `file:/^O\d+/`
   - `file:/^H\d+/`
   - `file:/^D\d+/`
   - `file:/^T\d+/`
   - `file:/^M\d+/`
3. An item that stands alone, with no line connecting it, is an item that is not linked to any need. That is exactly a "warning" of the hub.

## Rules that keep it working

- **A value that links items is a code in double square brackets and quotes**, for example `"[[H1]]"`. If you enter it with Obsidian's Properties pane, the quotes are added automatically.
- **Declare in one direction only.** A decision says which hypothesis it tests; Obsidian shows the reverse direction in Backlinks by itself.
- **Keep the item file names as they are.** The file name is the item's code.
- **Anonymise before you put data in this folder.** Obsidian opens the `_raw-private/` and `_personal/` folders too.

## Limits

- **Links in Properties are only clickable in Obsidian.** On GitHub they show as plain text. To share with others, build the HTML report (see [`04-share-your-hub.md`](04-share-your-hub.md)).
- **AI plugins in Obsidian can read the whole folder**, including `_raw-private/`. If you install a plugin like that, apply the same data rules as for an AI coding tool.
- **Bases is still new**, so the display may differ between Obsidian versions. If `traceability.base` shows an error, delete that file. The hub still works normally because the data lives in the item files.
