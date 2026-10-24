# AGENTS.md: workspace

This is the **workspace root**: the place that holds several projects (each project is a case folder) and the shared `toolkit/`. The rules for working *inside* a project are in that project's `AGENTS.md` (for example `my-case/AGENTS.md`). When you are working inside a project, read that file, not this one.

## What each folder is

| Folder | What it is | What you do |
|---|---|---|
| `my-case/` | The blank template | **Do not fill it in.** It is only there for `new-case.py` to copy |
| `demo-case/` | The sample project (Travel Buddy) | Read for reference, do not edit unless asked |
| `<project-name>/` | The workspace owner's project | Work following that project's `AGENTS.md` |
| `toolkit/` | Guides, document templates, step cards, scripts | Read, do not edit unless asked |
| `index.html` | The home page: one card per project | Do not edit by hand. Build it with `toolkit/skills/export-home.py` |

## When asked to create a new project

For example: "Create a new project called …", "Tạo một dự án mới tên …", "Start the project …".

1. **Ask for the project name** if it is not given. One question is enough.
2. **Run the command, do not copy `my-case` yourself:**

   ```
   python3 toolkit/tools/new-case.py "<Project name>"
   ```

   The command turns a name with accents or spaces into a folder name, removes the `[EXAMPLE]` items, fills in the project name, builds the project's `index.html` and adds a card to the home page. Add `--title "…"` if the display name should differ from the folder name.
3. **Tell the workspace owner:** the path of the new folder, that the home page now has a card for the project, and the first thing to do: fill in the Project card in the project's `README.md`, then `context/product-and-users.md` and `context/data-rules.md`.
4. **Do not fill it in for them.** Do not invent the product name, the users or any figures. Leave what you do not know empty for the project owner to fill in.

If a folder with the same name already exists, the command stops. Do not delete or overwrite it: ask the workspace owner to choose another name.

## Other requests at the workspace level

| Request | What to do |
|---|---|
| See or update the home page | `python3 toolkit/skills/export-home.py` |
| See the report of a project | Open `<project>/index.html`. To rebuild it: run `python3 ../toolkit/skills/export-hub.py` **inside** the project folder |
| Add a new document to a project | Open a template in `toolkit/templates/`, copy it into that project's `work/`, and follow that project's `AGENTS.md` |
| Draw a process map, swimlane or user flow | Follow `toolkit/skills/build-process-map.md` (uses `toolkit/diagram-design/`); template: `toolkit/templates/process-map.md` |
| Unclear which project it belongs to | Ask one question. Do not guess |

## Hard rules

1. **Do not read** `_personal/` and `work/sources/_raw-private/` of any project.
2. **Do not edit `my-case/`** when creating or working on a project. It must stay as it is to serve as the template.
3. **Propose first** for anything that creates or changes many files. Wait for the workspace owner to approve.
4. **Anonymise before using real data.** Names of people, company names and real figures do not go to an AI tool before they are anonymised.
5. **Answer in the language the workspace owner writes in.**
