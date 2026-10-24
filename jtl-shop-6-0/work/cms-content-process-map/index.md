---
type: "process-map"
title: "CMS content process map"
stage: "Develop"
status: "draft"
summary: "To-be lifecycle of a storefront content page under Shop settings › Storefront pages: create as Draft, edit in a page content editor, preview, publish, change a live page through a new Draft version, and unpublish."
takeaways:
  - "A page is never public until someone publishes it; publishing is the one moment it reaches shoppers."
  - "Editing a live page makes a new Draft version, so the live page never changes by accident."
  - "Delete works on drafts only; Unpublish takes a page offline (404) but keeps its last version."
  - "The prototype only covers create and list; Edit has no action and Delete removes live pages without a confirmation."
supports: ["O1"]
source: "process-map.html"
media:
  - "process-map.html"
embed: true
# links: []
---
# CMS content process map

The to-be lifecycle of a CMS content page in one shop, from Shop settings › Storefront pages: who creates, edits, publishes, changes and takes a page offline, and what shoppers see at each point. For the design and build of the page content editor and page states.

Built from the Shop Setup Platform prototype (Storefront pages section) and the owner's answers on 24 Oct 2026. To rebuild it, ask the AI tool: *"Follow `toolkit/skills/build-process-map.md`."*

## What it shows

| View | What it covers |
|---|---|
| 1. Create a page | Staff open Storefront pages, enter a title and pick a template; the page is saved as a Draft with a slug from the title |
| 2. Edit and publish | Edit content in the page content editor (CMS blocks), preview, decide, publish; the page goes live at its slug |
| 3. Change a live page | The owner edits a live page; a new Draft version is saved while the live version stays; publish it or delete the draft |
| 4. Take a page offline | Unpublish: the storefront returns 404, the last version is kept until it is published again |

## How to read it

- Each column is one actor: Shop owner, Shop staff, Admin dashboard, Public storefront. A line that crosses into another column is a handover.
- Owner and staff have the same rights; the map splits them only to show a typical case.
- Hexagons are decisions; shaded boxes are where a path starts.
- Dashed lines are alternative branches. Orange marks the key moment: Publish.

## How it relates to the decisions

| Moment on the map | Decision |
|---|---|
| Publish (both roles, no approval step) | Owner's answer, 24 Oct 2026; no decision item yet |
| Delete only on drafts; live version stays until a new version is published | Owner's answer, 24 Oct 2026; no decision item yet |
| Unpublish keeps the last version | Owner's answer, 24 Oct 2026; no decision item yet |

## What it does not show

- Templates management (page templates, CMS block library, design variants, inheritance) in the Theme Editor.
- What the page content editor looks like inside, SEO fields, scheduling, and multi-language pages.
- Error states and edge cases.
- Scope: the Pflichtenheft (§9.1) lists "Management of CMS Elements and Templates" outside the MVP. This map is a to-be proposal, not a committed MVP flow.

## Open questions

- Can an unpublished page be deleted, or must it stay because it still holds a version?
- Should Delete on a page with no live version ask for confirmation?
