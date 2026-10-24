# Guide

## 1. What this workspace is, and who it is for

**What it is.** One folder for one product, where you and your AI tool work together. Documents, research, decisions and measured results sit in the right place and are linked to each other, so the AI always has enough context.

**Who it is for.** PMs, designers, researchers, or anyone building a product on their own. You do not need to know how to code.

| You work in | To do what |
|---|---|
| `work/` | The work you have done: analysis, wireframes, prototype |
| `insights/` | What you learned and what you decided, linked back to user needs |
| `context/` | Background for the AI to read first |
| The left menu | For **viewing** only: built automatically from the three folders above |

## 2. I have a new product or project

| Step | What to do | Say to the AI |
|---|---|---|
| 1 | Create the project (open the workspace folder with an AI tool) | `Create a new project called <project-name>` |
| 2 | Tell the AI about the product and the users | `Help me fill in the background about the product and users. Ask me one question at a time.` |
| 3 | Write the scope of the project | `Help me write the scope: the business question, the desired outcome, the main users.` |
| 4 | Add the research data (anonymised) | `Extract insights from the file <file-name>. Propose first, do not create.` |
| 5 | Look at the hub | Double-click `index.html` in the project folder |

Then you go through the stages:

| Stage | What you are doing |
|---|---|
| **Discover** | Understand the problem and the users |
| **Define** | Decide which problem is worth solving |
| **Develop** | Explore solutions, draw wireframes, build a prototype |
| **Deliver** | Test with users and hand off |
| **Learn** | Read the results after release |

## 3. I have a new task or piece of work

| I have | What to do | Say to the AI |
|---|---|---|
| A new interview or survey | Save the file (anonymised) in `work/` | `Extract insights from the file <file-name>. Propose first, do not create.` |
| Images, wireframes, a prototype | Drop them into a new folder in `work/` | `Add the files in the folder <folder-name> to the report.` |
| A design decision | No file needed first | `Record a decision: <one sentence>. It tests hypothesis H1. Reason: <...>. Not accepted yet.` |
| A new need or hypothesis | No file needed first | `Record a user need: <one sentence>. Impact <high/medium/low>, because <reason>.` |
| A measured result after launch | No file needed first | `Metric M1 measured <number> on <date>, the target was <...>. Verdict: <met / missed>.` |

**Where things go:** work you have done lives in `work/`; what you learned and decided lives in `insights/`. Each piece of information is written in one place only.

## 4. I want to preview the hub

| Way | When | What to do |
|---|---|---|
| **Quick look** | You only need to look | Double-click `index.html` in the project folder: it opens in the browser, nothing to install |
| **Look and auto-refresh** | You are editing files all the time | Tell the AI: *"Open a preview of the hub that refreshes when I save a file"*, then open the address it gives you |
| **Send to someone** | Sharing | Tell the AI: *"Pack the report into a zip file to send"* |

The report changes only when it is rebuilt. Just added a file and do not see it? Tell the AI: *"Rebuild the report"*, then reload the page.

## 5. Words for working with the AI

**Things in the workspace**

| Word | Meaning |
|---|---|
| **Hub** | The whole project folder and the `index.html` report that shows it |
| **Item** | A need, hypothesis, metric, decision, evidence or finding. Each item is one file in `insights/` |
| **Working file** | A file in `work/` (for example `scope.md`) |
| **Step card** | A ready-made procedure for the AI to run (it lives in `toolkit/skills/`, outside the case and shared). You do not need to name it: say what you want done and the AI picks the right procedure |
| **Context** | The files in `context/` that the AI reads first in every step |

**Words you say to the AI**

| You say | The AI understands |
|---|---|
| "Propose first, do not create" | List it for me to approve, do not write any file yet |
| "Anonymise" | Replace real names, company names and figures with made-up ones before giving them to the AI |
| "assumed" | Nobody has confirmed this number |
| "Draft" / "verified" | Not checked yet / I have checked it |
| "Proposed" / "accepted" | A decision just suggested / a decision that has been accepted |
| "Link to H1" | Record the relationship to item H1 (for example the decision tests hypothesis H1) |
| "Rebuild the report" | Refresh the report from the current files so the menu and the tables match the latest changes |

To understand more deeply how the workspace works, tell the AI: *"Explain to me how this workspace works."*
