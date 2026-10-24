# Set Up Your Case

This guide helps you name your project, understand what each folder is for, and know how to work with an AI tool in this folder.

## Step 1: Name your case

1. Open Terminal at the workspace root folder and run:

   ```
   python3 toolkit/tools/new-case.py onboarding-redesign
   ```

   Add `--title "Onboarding redesign"` if you want a display name that differs from the folder name.
2. A folder name uses lowercase letters joined with hyphens, no spaces. For example: `onboarding-redesign`, `checkout-flow`. Pick a name that tells you what the case is about, because you will see it at the start of every path. A plain name such as "Trip Planner" also works: the command turns it into a folder name.
3. The command creates a new folder next to `my-case`, clean and ready to fill in. `my-case` is kept as the template.

If you have two cases, run the command twice with two different names.

**Cannot use Terminal?** Rename the `my-case` folder to your case and fill it in. This loses the original template, so keep a clean ZIP to get it back when you need it.

## Step 2: Understand the folders

Folders are named after **what you do** there:

| Folder | Use it for | When |
|---|---|---|
| `context/` | **Background:** product, users, data rules, design system. You give it to the AI to read first in every step | When you start the project, add to it over time |
| `work/` | **The working files of each stage:** `scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` (Discover), `problem-brief.md` (Define), `options.md`, `alignment.md` (Develop), `test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` (Deliver). The stage pages in `stages/` are built from these files | Throughout the project |
| `work/sources/` | `anonymised/` holds anonymised data, `_raw-private/` holds original data | Discover |
| `work/prototype/` | Prototype code | The Develop stage |
| `stages/` | **One page per stage**, built from `work/` and `insights/` by the Pages table in `stages/README.md`; you do not write here | Edit the table only to change the order or add a stage |
| `insights/` | **The linked items:** needs, hypotheses, decisions, evidence, findings, metrics; one file per item, in the folder of its type | Update when something changes |
| `standards/` | **Reference:** gates, principle checks, severity levels, case log. Drop a new `.md` file here and it shows in the report by itself | When you need to look something up |
| `../toolkit/skills/` and `../toolkit/templates/` | (in `toolkit/`, outside the case) Step cards, the script that builds the `index.html` report, and document templates. Shared by every case | When you run a step; rarely opened by hand |
| `_personal/` | Private notes, not given to the AI | Whenever you want |

The `README.md` at the root of the project folder has a "What do you want to do?" table with sample sentences for each job, so when you do not know where to start, read it.

## Step 3: Fill in the first files

When you start the project, fill in the files in `context/` and one separate file:

1. `context/product-and-users.md`: what the product is, who the users are, what you know and what you do not.
2. `context/accessibility-rules.md`: the accessibility requirements the design must meet.
3. `context/data-rules.md`: three lines in your own words: what you may give the AI, what you will not, which tool you use for what.
4. `context/open-questions.md`: the questions the AI says it needs answered.
5. `_personal/my-direction.md`: two or three lines about the career direction you lean toward. This is a private note, so it sits outside the working folders and is not given to the AI.

Each file comes with hint lines. Replace the hints with your own content, and keep the headings as they are.

## Step 4: Work with an AI tool

This folder is built so an AI tool knows what to do by itself, thanks to four things:

| Thing | What it is |
|---|---|
| `AGENTS.md` | A file with the "rules of the game" already written. The AI tool reads it by itself when you open the folder, so you do not have to repeat the rules every time. If your tool reads its rules file under another name, copy the content to that name |
| `../toolkit/skills/*.md` | The **step cards**: each step says who does it (the AI or you), which files to read, where to write |
| `work/sources/` | The AI may read `anonymised/`. `_raw-private/` is never given to the AI and never goes to GitHub |
| `insights/` | Each decision, hypothesis and evidence is one file. The summary tables are rebuilt by the AI |

A session with the AI looks like this:

1. **Open exactly one case folder** as the project in the AI tool. Do not open the root folder, and do not open `my-case` and `demo-case` at the same time, or the data of the two cases will mix.
2. **Save a checkpoint before the AI writes files.** If you use GitHub Desktop, click Commit (see [`03-github-basics.md`](03-github-basics.md)). If not, copy the case folder into a `...-backup` copy. That way, if the AI breaks something, you can go back.
3. **Say one sentence to the tool**, for example: *"Run step 5 of `../toolkit/skills/user-voice-synthesis.md`."* The tool reads only the files the step card lists.
4. **Read the result and check it yourself** in the next step. The AI draft and the version you corrected sit in two separate places.
5. **Write a line in `insights/case-log.md`:** what you decided, why, and where the AI helped.

## Step 5: Use the hub

The hub is where you answer the question: "Which user need is this decision based on?"

- **Each design decision is its own file.** For example decision `D2` lives at `insights/decisions/D2.md`.
- **You write each fact in one place only.** Decision `D2` says which hypothesis it tests; the hub works out the reverse direction.
- **After each update,** run `python3 ../toolkit/skills/export-hub.py` (or ask the AI tool to) so the report rebuilds the summary tables and warnings.

How the hub works is in `toolkit/skills/how-the-hub-works.md`.

## View markdown files

An `.md` file is plain text, so **any tool that can open a folder will do**. Pick by what you need:

| Tool | What it does |
|---|---|
| **AI coding tool** | Open the whole case folder as the project. The tool reads `AGENTS.md`, reads and edits files directly, and runs the step cards. This is how you work with the AI |
| **Obsidian** (free) | Open the whole case folder as a vault. Adds Graph view, Backlinks and tables by item type. See [`05-obsidian.md`](05-obsidian.md) |
| **VS Code** (free) | Install it from [code.visualstudio.com](https://code.visualstudio.com), open the whole case folder, click an `.md` file, then press `Cmd+Shift+V` (Mac) or `Ctrl+Shift+V` (Windows) to see the rendered version |
| **GitHub** | If you saved the folder to a Private repo, open the repo on github.com; Markdown is already rendered |
| **Browser** (nothing to install) | Double-click the `index.html` at the root of the case folder: that is the home page of the hub. After you edit the hub, ask the AI tool to run `python3 ../toolkit/skills/export-hub.py` to rebuild it. See [`04-share-your-hub.md`](04-share-your-hub.md) |

Open the **whole folder**, not single files: the links between pages only work when the whole folder is open.

**A note on links:** items link to each other with `[[ ]]` in the properties block at the top of a file. Only Obsidian turns them into clickable links. Other tools can still read and edit them because they are just text, and an AI coding tool understands them normally.

## Make it your own

| You want to | How |
|---|---|
| Add your own folder (notes, images, recordings) | Create a new folder at the same level as `work/`, for example `notes/` |
| Remove a file you do not use | Delete it. If a page in `stages/` uses that file, remove it from the From work column in the Pages table in `stages/README.md`. If it is an item, run `python3 ../toolkit/skills/export-hub.py` again |
| Add a stage page | Add a row to the Pages table in `stages/README.md`: set an Id, pick the file in the From work column and the item tables you want to show. No new file needed |
| Add an item (need, hypothesis, decision...) | Run `python3 ../toolkit/skills/new-item.py` in the project folder: the command asks one question at a time, picks the next code and links the relationships for you |
| Add a document (competitor analysis, persona, flow, prototype...) | Copy a template from `toolkit/templates/` into `work/`, or create a folder and drop images, PDFs, HTML into it. See `work/README.md` |
| Add a decision or a test | Run `python3 ../toolkit/skills/new-item.py D` (or `E`): the command picks the new code and links the relationships for you |
| Use your company's design system | Write your `context/design-system-notes.md` and use `work/prototype/` as the model |
| Write the files in Vietnamese | You can. Only keep file names and folder names in English |

## Keep it safe

- **Anonymise before giving anything to an AI tool or sharing it outside.**
- **Do not keep passwords, users' personal data or unpublished financial figures in this folder**, even when the repo is Private.
- The hub is private by default. How to let others see it is in [`04-share-your-hub.md`](04-share-your-hub.md).
