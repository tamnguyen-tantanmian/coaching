---
type: "process-map"
title: "E2E process map: how a trip moves through Travel Buddy"
stage: "Develop"
status: "draft"
summary: "A swimlane map of the Travel Buddy journey with four actors (traveler, Travel Buddy, a local, a companion or contact): how the parts of the app hand over to each other, before the trip, on the trip and after it."
takeaways:
  - "Each column is one actor, and every line that crosses into another column is a handover; the lines between traveler and local are highlighted."
  - "A visitor can browse without an account, and the chat with a local only opens when both sides have shown interest."
  - "The journal stays private unless the traveler chooses contacts to share it with; after the trip the next trip starts in Discover again."
supports:
  - "[[D2]]"
  - "[[D3]]"
  - "[[D4]]"
  - "[[D5]]"
  - "[[D6]]"
  - "[[D7]]"
source: "original-docs/08_E2E_Process_Map.html"
media:
  - "original-docs/08_E2E_Process_Map.html"
embed: true
---
# E2E process map

The end-to-end journey of Travel Buddy as a swimlane map. It is the **main flow document** of this project. It shows **who does what and where the work is handed over**, so a reader can see every handover between the traveler, the app, a local and a companion.

The original written flow, with the 26 solutions placed in four stages of the trip, is kept as a source document: `work/original-docs/08_E2E_User_Flow.md`.

## What it shows

| View | What it covers |
|---|---|
| 1. How the parts hand over | Getting started, Discover, Plan, Connect and Journal, and the five handovers between them |
| 2. Before the trip | Opening the app, browsing without an account, the three onboarding questions, saving a tip with one tap, importing an AI-made itinerary, planning together with a companion |
| 3. On the trip | Arrival, opening a local's profile, the two-way chat, the safety check, report or block |
| 4. After the trip | Building the journal, choosing who may see it, and the next trip starting in Discover |

## How to read it

- Each column is one actor: the traveler, Travel Buddy itself, a local, and a companion or contact.
- A line that crosses into another column is a handover. The pink lines are the ones between traveler and local.
- Diamonds are decisions; rounded boxes are the start or the end of a path.

## How it relates to the decisions

| Moment on the map | Decision |
|---|---|
| Shows tips right away, no account needed | D2 |
| Tips come with a crowd signal and safety notes | D3 |
| Saves a tip with one tap | D4 |
| Turns a pasted AI itinerary into shortlist items | D5 |
| Opens the chat only when both sides show interest | D6 |
| The journal is private unless contacts are chosen | D7 |

## What it does not show

- The map shows the **main path**. Error states and edge cases are not drawn.
- It is a design artifact, not a test result. Whether users follow these paths is not confirmed: the only usability round so far is simulated (see E1).
