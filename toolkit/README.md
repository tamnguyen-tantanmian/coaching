# Toolkit

Everything shared by the projects in this workspace. The home page that lists every project is the `index.html` at the workspace root. **You do not fill anything in here.** Each project (`my-case`, `demo-case`, your own) sits outside this folder.

| Folder | What it holds | When to open it |
|---|---|---|
| `guides/` | Step-by-step guides: get the folder onto your machine, set up a project, GitHub, share the report, Obsidian | The first time, or when you are stuck |
| `templates/` | Empty templates for working documents (research plan, interview guide, PESTEL, journey map...) | When you start a new document |
| `skills/` | The steps for the AI tool (step cards) and the script that builds the `index.html` report | Rarely: the AI tool reads them itself |
| `diagram-design/` | The `diagram-design` skill (templates, rules, check script) the AI tool uses to draw process maps, user flows and other diagrams | Read `skills/build-process-map.md` first |
| `tools/` | `new-case.py`: create a new project with one command | When you want a new project |

Create a new project (from the workspace root):

```
python3 toolkit/tools/new-case.py project-name
```

Details: [`guides/02-set-up-your-case.md`](guides/02-set-up-your-case.md).
