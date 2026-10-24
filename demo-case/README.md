# Demo project: Travel Buddy

| | |
|---|---|
| Project name | Travel Buddy |
| Agreement status | not available |

This is a real project that went through the stages from Discover to Test: **Travel Buddy**, a travel companion app. It is used as the sample project so you can see what a full workspace looks like, and see **where the gaps are**.

The original project was made before this workspace's AI-assisted way of working existed. That is why some files say "not applicable", and some gates are `open` or `failed`. That is on purpose: an honest sample project is more useful than one that has been tidied up to look good.

## Start here

1. Double-click `index.html` to see the hub in the browser. Start at the **Overview** section, then open **Insights** (Tree mode) to walk from a decision back to the user's need.
2. Read `context/product-and-users.md` to learn what the project is.
3. Open `standards/gates.md` to see which gates pass, which do not, and why.

## What is in here

| Part | What it holds | Used in stage |
|---|---|---|
| `context/*.md` | Project overview, users, design system, open questions | Setup |
| `work/scope.md`, `user-voice-synthesis.md`, `competitor-analysis.md` | Scope, user voice synthesis, competitor analysis | Discover |
| `work/sources/anonymised/` | The original research documents: hypotheses, survey, interview guide, synthesis, competitors | Discover |
| `work/problem-brief.md` | Problem brief | Define |
| `work/options.md`, `alignment.md`, `work/process-map.md`, `work/wireframes/` | Directions, alignment, the E2E process map, wireframes | Develop |
| `work/test-plan.md`, `findings.md`, `handoff.md`, `measurement-plan.md` | Test plan, findings, handoff, measurement plan | Deliver |
| `insights/` | 5 needs, 6 hypotheses, 7 decisions, 2 evidence, 7 findings, 5 metrics | All stages |
| `stages/README.md` | The table of seven stage pages (scope, evidence, problem brief, develop, alignment, findings, handoff); each page is built from `work/` and `insights/` | All stages |
| `standards/` | Gates, principle checks, severity levels, case log | All stages |
| `../toolkit/skills/`, `../toolkit/templates/` | (outside this folder, in `toolkit/`) The steps for working with the AI and the document templates, shared | All stages |
| `work/original-docs/` | The original documents of the Define to Test stages (personas, solution pool, flow, IA, PRD, test plan, findings) | Reference |

## What this project teaches (including by example of what is missing)

- **Full traceability.** Every decision links back to a hypothesis and to a need with evidence.
- **Weak evidence.** The research so far has 13 survey responses and one interview; the only usability test round is **simulated** (an AI played the users). The hub marks this on every hypothesis, and gate 4a is `failed`.
- **Missing design principles.** There are no principle checks yet, so every decision lacks the "Follows principle" column.
- **No one signed off.** The stakeholders were simulated, so the agreement status is `not available`.

## Conventions in this demo

- `RH1`..`RH10`: the research hypotheses of the original project (`H1`..`H10` in `01_Research_Hypotheses.md`).
- `SP-D1`, `SP-P3`...: IDs in the original Solution Pool (`work/original-docs/07_Solution_Pool.md`).
- `O`, `H`, `D`, `E`, `M` in `insights/`: workspace items (Opportunity, Hypothesis, Decision, Evidence, Metric).
- The original documents are kept as they are; the working files, items and standards are written in English too.
- AI tool names, the owner's name, the interviewees' cities and private prototype links were removed from the copies in `work/original-docs/` and `sources/`.

## Rules

1. **Do not copy the sample project's content into your real project.**
2. **Treat the survey figures as directional only:** a small sample (13), skewed toward Asia and young people.
3. **Do not treat the simulated test results as evidence.** See `work/findings.md`.
