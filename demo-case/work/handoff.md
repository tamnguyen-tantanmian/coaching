---
type: "handoff"
title: "Handoff"
stage: "Deliver"
status: "draft"
summary: ""
supports: []
---
*Deliver stage, at handoff. What a developer needs to build it without coming back with questions.*

> **Status:** not ready for handoff. There is a PRD for only one tab (Explore); the Plan, Connect and Journal tabs have no PRD yet. Gate 4c is still `open`.

## The prototype
A link or a folder. This is a reference, not production code.

- Wireframe: `work/wireframes/Travel_Buddy_Wireframe.html`
- The final prototype: `work/final-prototype/travel-buddy-final-prototype.html`
- The build plan, the list of 32 screens, 4 flows: `work/original-docs/10_Prototype_Plan.md`
- E2E process map: `work/process-map.md` (source: `work/original-docs/08_E2E_Process_Map.html`)

## Decisions and reasons
(Point to the decision log in `insights/case-log.md`)

The seven decisions and their reasons are in `insights/decisions/`; the timeline log is in `insights/case-log.md`.

## Acceptance notes
*What must be true when the product has been built. From the PRD of the Explore tab (section 8).*
- All three modes (Near Me, Country, Map) can be navigated through the mode toggle
- The filter panel opens from all three modes and applies correctly
- The crowd signal badge shows on every tip card in every mode
- Pressing Save as a visitor opens the sign-up bottom sheet
- The video player and the safety panel open from a tip card and from the Tip Detail screen
- Visitors can browse every mode without being forced to sign up
- The prototype is tested with at least two participants using the tasks of the plan

## Open questions
- Is the crowd signal user-reported data, an algorithmic score, or both?
- Is video uploaded by travellers, curated by Travel Buddy, or both at v1?
- Should Map mode default to the current location or to the destination of a saved trip?
- What is the minimum number of tips for a destination to show in Country mode?
