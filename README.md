# AI Product Workspace

Three months from now someone asks: "Why did we choose this?" You open it and can answer, with the evidence.

**Every design decision traces back to the user need behind it.**
The AI drafts, you decide. No coding or GitHub knowledge needed.

---

## Introduction

| | |
|---|---|
| **What this hub is** | A folder with a report you view in a browser. Research, user needs, decisions and test results sit in one place, linked to each other. The AI helps you draft |
| **The problem today** | Work is scattered across documents, notes, slides and design files. A few months later nobody remembers **why** something was chosen. The AI writes very fast, but you do not know what it relied on, so it is easy to believe a sentence only because it sounds reasonable |
| **The hub helps you** | Every decision has a **reason and evidence**. The AI only **proposes, with sources**, and you are the one who decides. The report shows **what is missing**, and you can send it to stakeholders |
| **Why it matters** | When asked "why did you do that?", you answer with evidence, not gut feeling. When the AI is fast, mistakes spread fast too, so traceability is how you keep control. Knowledge about the project stays in the folder, even when people leave |

---

## How it works: 6 steps

| Step | You do | You get |
|---|---|---|
| **1. Create a new project** | Tell the AI tool: *"Create a new project called …"* | A clean project folder, and a new card on the home page |
| **2. Set the context** | Write briefly: what the product is, who uses it, what data goes to the AI. Anonymise real names and figures | The AI knows the background before it helps |
| **3. Add documents by stage** | Add interviews, surveys, competitor analysis, wireframes | Everything is in the right place, no longer scattered |
| **4. Let the AI propose, you decide** | The AI proposes needs, hypotheses, decisions from the **ready-made templates**, with sources. You keep, edit or cut | Only what you approved gets recorded |
| **5. Review the whole picture** | Open the report: every decision leads back to its reason and evidence. Gaps are shown | You know what is missing before handoff or a meeting |
| **6. Measure and learn** | After release, record the result against the goal. If it is not met, go back to the need | The next decision is grounded in real results |

---

## Example: a travel companion app

| Step | What happens |
|---|---|
| **1. Create a new project** | You say: *"Create a new project called Travel Buddy."* The home page gets a new Travel Buddy card |
| **2. Set the context** | You write: the app helps travellers plan in one place, users are aged 18 to 45 |
| **3. Add documents by stage** | You add the results of a survey of 13 people and the notes of one interview |
| **4. Let the AI propose, you decide** | You say: *"Extract insights from the survey file. Propose first, do not create."* The AI returns the need **"get past the barrier to trying it"**, with its source: price is barrier number 1, 7 of 13 people. You keep it |
| **5. Review the whole picture** | The report links the decision back to the evidence, as below |
| **6. Measure and learn** | The goal is that 25% of visitors who press Save sign up. After release only 18% do *(a made-up figure)*. The report marks it as not met and the need "barrier to trying it" for review |

At step 5, clicking a decision shows the chain of reasons behind it:

```
Decision: "Visitors can browse without an account"
  ← hypothesis: enough people will sign up when they press Save
    ← need: get past the barrier to trying it
      ← evidence: survey of 13 people, price is barrier number 1 (7/13)
```

Steps 2 to 5 come from the sample project `demo-case`. Open that project to see it in full.

---

## Try it in 1 minute

Click **Code → Download ZIP**, unzip, then double-click **`index.html`** at the root. That is the home page: each project is a card, click a card to open the project's report.

| To see | Click the card |
|---|---|
| The finished sample project | **Travel Buddy** (`demo-case`) |
| The blank workspace | **Product Name** (`my-case`) |

---

## Start your own project

1. **Download and unzip.**
2. **Open the folder with an AI tool** and say: *"Create a new project called … ."*
3. **Double-click `index.html`** at the workspace root: your project shows as a new card.

No AI tool? Rename the `my-case` folder, then fill it in.

---

## Four rules

1. **Anonymise** names, company names and real figures before giving anything to the AI.
2. **The AI proposes first.** You approve, then it creates.
3. **The AI's drafts** and what you have checked live in two separate places.
4. **A number nobody has confirmed** is marked `assumed`.

---

## Need help?

The folder [`toolkit/guides/`](toolkit/guides/) has step-by-step guides: getting the folder onto your machine, working with an AI tool, sharing the report. In the report, the **Guide** tab has sample sentences for each job.

<details>
<summary>For people who want to customise</summary>

```
workspace/
├── toolkit/         guides, document templates, steps for the AI, the tool to create projects
│   ├── guides/      step-by-step guides
│   ├── templates/   document templates, shared by every project
│   ├── skills/      steps and scripts for the AI, shared by every project
│   └── tools/       create a new project with one command
├── my-case/         the blank workspace (make a copy, do not fill it in directly)
├── demo-case/       the sample project
└── <project-name>/  your project
```

In each project: `context/` (background), `work/` (everything made), `insights/` (needs, decisions, evidence), `stages/`, `standards/`, `AGENTS.md` (rules for the AI tool).

- **Keep** the folder names above and the item codes (`O1`, `H1`, `D1`...) as they are.
- **Create a project with a command:** `python3 toolkit/tools/new-case.py project-name`
- **Real projects:** read your company's AI policy, keep the original data in `work/sources/_raw-private/`, and keep the repo **Private** if it is not cleared for sharing.

</details>
