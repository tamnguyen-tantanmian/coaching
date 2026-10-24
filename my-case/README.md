# Project: [project name]

The front page of the project. Fill in the **Project card** first, then pick your next move from the table below.

## Project card

| | |
|---|---|
| Project name | |
| Business question (one sentence) | |
| Current stage | Setup / Discover / Define / Develop / Deliver |
| Owner | |
| Stakeholders (product, business, engineering) | |
| Started | |
| Last updated | |
| AI tools allowed for this project | |
| Agreement status | pending *(agreed / pending / not available)* |
| Data rules | See `context/data-rules.md` |

<!-- template-only -->
> **This is `my-case`, the blank workspace.** Do not fill it in directly: open the workspace folder with an AI tool and say "Create a new project called *project-name*". To see a finished project, open `demo-case`.
<!-- /template-only -->

## What do you want to do?

Open this folder with an AI tool and say it in plain words.

| I want to | Say to the AI |
|---|---|
| Record the product and the users | "Help me fill in the background about the product and users. Ask me one question at a time." |
| Pull what I learned from an interview or survey | "Extract insights from the file *file-name*. Propose first, do not create." |
| Record a decision | "Record a decision: *one sentence*. Reason: *…*. Not accepted yet." |
| Add images, wireframes, a prototype | "Add the files in the folder *folder-name* to the report." |
| See progress | Double-click `index.html` and open the **Overview** tab |
| Send the report to someone | "Pack the report into a zip file to send." |

The full list is in the **Guide** tab of `index.html`.

## Four rules

1. **Anonymise before you give anything to the AI.** Keep the original data in `work/sources/_raw-private/`.
2. **Let the AI propose first;** you approve, then it creates.
3. **AI drafts and what you have checked live in two separate places.**
4. **A number nobody has confirmed is marked `assumed`.**

## What each folder is

| Folder | What is in it |
|---|---|
| `context/` | What the product is, who the users are |
| `work/` | Everything you make: analysis, wireframes, prototype |
| `insights/` | What you learned and the decisions you made |
| `stages/` | The story of each stage (built automatically, you do not write here) |
| `standards/` | Yardsticks to check the work |
| `AGENTS.md` | Rules for the AI tool, rarely needs opening by hand |
| `_personal/` | Your private notes, never given to the AI |

*The steps for the AI (`toolkit/skills/`) and the document templates (`toolkit/templates/`) sit **outside** this folder, in `toolkit/` at the workspace root, shared by every project.*
