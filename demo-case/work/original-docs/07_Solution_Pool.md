# Solution Pool — Travel Buddy
**Project:** Travel Buddy | **Phase:** Define → Ideate  
**Linked to:** `05_Research_Synthesis.md` · `06_User_Personas.md`  
**Status:** 🟢 Draft — ready for prioritization

> **Purpose:** This document translates research-confirmed problems into a candidate set of solutions before any prioritization occurs. Each pillar is capped at 5 solutions, selected by survey signal strength. Solutions are not ranked here — that happens in the Feature Strategy (Section 4).

---

## How to Read This Document

Each problem is drawn directly from survey data or hypothesis validation. Each solution is a design response to that problem. The **User Impact** column maps which persona(s) each solution primarily serves. Solutions that serve all three types are flagged with ★.

---

## Problem Space Summary

*Updated to n=13 valid responses. Problems reordered to reflect feature importance rankings from the expanded dataset.*

| Problem Area | Source | Confidence |
|---|---|---|
| Planning tools are too rigid or too fragmented | Survey (H9) — Trip Planning now #1 feature (4.38/5); 5/13 cite multi-app fragmentation | ✅ High |
| Authentic local experiences are hard to find | Survey — #1 frustration (9/13); Discovery ranked #2 feature (3.85/5) | ✅ High |
| Review disappointment is widespread | Survey — 10/13 have been let down by highly-rated places | ✅ High |
| App fragmentation causes friction, especially offline | Survey (H3) — 5/13 cite multi-app frustration; 3/13 cite apps don't work offline · P1 interview: named as #1 pain, 8–10 apps used per trip, all information manually transferred | ✅ High (qualitatively confirmed) |
| Local connection is wanted but lacks a safe mechanism | Survey (H4, H5) — 12/13 open; verified identity (11/13), no cost (9/13), shared interests (8/13) all required | ✅ High |
| Auto-capture and polished layout both strongly desired | Survey (H7) — both tied at 8/13; journaling ranked #3 in importance (3.62/5) | ✅ High |
| Price is the #1 adoption barrier | Survey (H10) — 7/13 cite cost; privacy rising to joint second (4/13) | ✅ High |

---

## Solution Pool

### Pillar 1 — Discover

**Core problem:** Travelers cannot find recommendations they trust. Commercial platforms surface popular and paid content; genuine local knowledge lives nowhere accessible.

| ID | Solution | Description | User Type |
|----|----------|-------------|-----------|
| D1 | Peer-sourced tip feed | A content feed of tips contributed by travelers and locals — no ads, no paid placement, no affiliate links. Each tip is tied to a verified contributor profile. | ★ All |
| D2 | Traveler-style matching | Filter tips by travel style (relaxer, explorer, adventurer) so users see recommendations from people who travel like them. Based on self-declared style in onboarding. | Explorer |
| D3 | Crowd/popularity signal | Show an indicator when a spot has become over-visited or commercialized — the opposite of a popularity badge. Helps users avoid disappointing, crowded places. | Explorer |
| D4 | Video tip snippets | Short video clips attached to tips showing what a place actually looks and feels like. Closes the gap between how a place looks in photos and how it feels in person. | Explorer |
| D5 | Safety context on places | Recent traveler notes about safety conditions, accessibility, or common issues per destination. Relevant to all traveler types regardless of trip style. | ★ All |

---

### Pillar 2 — Connect

**Core problem:** Most travelers want to connect with locals, but no current tool makes it feel safe, free, and non-transactional at the same time.

| ID | Solution | Description | User Type |
|----|----------|-------------|-----------|
| C1 | Verified identity system | ID or social account verification displayed on profiles. Non-negotiable for the Connect feature — without it, willingness to reach out drops significantly. | Connector |
| C2 | Interest and style matching | Profiles include declared travel interests, languages spoken, and travel style. Enables matching before outreach so context exists from the first message. | Connector |
| C3 | Reciprocal exchange model | The platform frames local connection as a two-way exchange — not a service transaction. No money changes hands. Someone guides visitors in their city; others do the same for them elsewhere. | Connector |
| C4 | In-app messaging | Low-friction direct messaging between matched users. Opens only after both sides signal interest to reduce unsolicited contact. | Connector |
| C5 | Report and block controls | Standard safety controls available on every profile and after every interaction. Required as a trust floor for the Connect feature to feel safe. | Connector |

---

### Pillar 3 — Plan

**Core problem:** Travelers plan loosely and adapt constantly. Existing tools are either too rigid for flexible travel or too fragmented across multiple apps.

| ID | Solution | Description | User Type |
|----|----------|-------------|-----------|
| P1 | Living shortlist | A reorderable, swappable shortlist of places rather than a locked day-by-day schedule. Supports both pre-trip planning and in-destination flexibility without changing tools. | Explorer |
| P2 | Map view of saved places | Visual map showing all saved spots in a destination. Supports on-the-fly decisions based on proximity — especially useful once in-destination. | Explorer |
| P3 | One-tap save from Discovery | Any tip or place in the Discovery feed can be saved to the Trip Planner with one tap. Closes the gap between browsing and planning. | Explorer |
| P4 | Offline access | Core planning content (shortlist, map, notes) available without internet. Critical for in-destination use when data is unavailable or expensive. | ★ All |
| P5 | Collaborative trip planning | Allow two or more users to build and edit the same shortlist. Designed for group travelers who plan together before and during a trip. P1 confirms: the Google Sheets planner is shared with companions as a coordination artifact. | Explorer · Documenter |
| P6 | AI itinerary import | Allow users to paste or import AI-generated itinerary text (from ChatGPT, Gemini, etc.) directly into the Trip Planner. Converts an AI output into a structured, editable shortlist without manual re-entry. Sourced from P1: AI tools are embedded in the planning workflow but currently produce outputs with nowhere to go. | Explorer |

---

### Pillar 4 — Journal & Memory

**Core problem:** Most travelers either do not document trips at all or want documentation to happen automatically. The desire to remember is real, but the effort threshold is too high. The journal must support both real-time capture and post-trip reconstruction.

| ID | Solution | Description | User Type |
|----|----------|-------------|-----------|
| J1 | Auto-capture (location + time) | Background logging of visited locations and timestamps throughout the trip. Requires no action from the user — the journal builds itself. | Documenter |
| J2 | Auto-generated layout | The journal compiles entries into a visually polished format without the user designing it. Captures and presents — both without effort. | Documenter |
| J3 | Private-first sharing | Journal is private by default. Sharing requires an active choice. Removes the pressure of social media performance from the documentation experience. | Documenter |
| J4 | Selective sharing (specific people) | Share a journal — or a single trip — with named contacts only. No public post required. For travelers who want to share memories without broadcasting them. | Documenter |
| J5 | Contextual memory layer | Connect photos to place names, tip contributors, and visited spots automatically. The camera roll has the images — this adds the "who, where, why" that fades fastest. | Documenter |

---

### Pillar 5 — Adoption & Trust

**Core problem:** Price, complexity, and location privacy are the top barriers to trying the app at all. These solutions must work before users reach any feature.

| ID | Solution | Description | User Type |
|----|----------|-------------|-----------|
| A1 | Free-first model | Core features (Discovery, Planning, basic Journal) available at no cost. Premium features gated behind an optional subscription. Required to get past the primary adoption barrier. | ★ All |
| A2 | Value-first onboarding | Show a personalized discovery result or an auto-captured moment within the first 60 seconds. Users should experience value before being asked to set up a full profile. | ★ All |
| A3 | Granular location controls | Users choose exactly what location data is captured and when. Clear off/on toggle visible at all times. Addresses location privacy as an adoption concern without disabling core features. | ★ All |
| A4 | No-account browsing | Allow users to browse the Discovery feed without creating an account. Registration required only when saving or connecting. Lowers the first barrier to entry. | Explorer |
| A5 | Lightweight onboarding | Travel style, interests, and home city only — three questions maximum before the user reaches value. No form-heavy setup. | ★ All |

---

## Cross-User Coverage Map

| Solution | Explorer | Connector | Documenter |
|---|:---:|:---:|:---:|
| D1 Peer-sourced tip feed | ✅ | ✅ | ✅ |
| D2 Traveler-style matching | ✅ | | |
| D3 Crowd/popularity signal | ✅ | | |
| D4 Video tip snippets | ✅ | | |
| D5 Safety context | ✅ | ✅ | ✅ |
| C1 Verified identity | | ✅ | |
| C2 Interest & style matching | | ✅ | |
| C3 Reciprocal exchange model | | ✅ | |
| C4 In-app messaging | | ✅ | |
| C5 Report and block | | ✅ | |
| P1 Living shortlist | ✅ | | |
| P2 Map view | ✅ | | |
| P3 One-tap save | ✅ | | |
| P4 Offline access | ✅ | ✅ | ✅ |
| P5 Collaborative planning | ✅ | | ✅ |
| P6 AI itinerary import | ✅ | | |
| J1 Auto-capture | | | ✅ |
| J2 Auto-generated layout | | | ✅ |
| J3 Private-first sharing | | | ✅ |
| J4 Selective sharing | | | ✅ |
| J5 Contextual memory layer | | | ✅ |
| A1 Free-first model | ✅ | ✅ | ✅ |
| A2 Value-first onboarding | ✅ | ✅ | ✅ |
| A3 Location controls | ✅ | ✅ | ✅ |
| A4 No-account browsing | ✅ | | |
| A5 Lightweight onboarding | ✅ | ✅ | ✅ |

---

## Solutions with Highest Cross-User Reach

Top candidates for Must Have in the next prioritization pass (updated to n=13):

- **Serve all user types:** D1, D5, P4, A1, A2, A3, A5
- **Strongest single-type signals:** P1 (flexible planning — #1 rated feature overall), C1 (verified identity — non-negotiable for Connector), J1+J2 (auto-capture + layout — co-equal for Documenter), D1 (peer tips — top frustration driver for Explorer)
- **P4 (offline access)** is reinforced from two directions — cited as a frustration by some and as a desired journal feature by others. Treat as a cross-pillar infrastructure requirement, not a bonus feature.
- **P6 (AI itinerary import)** is a new addition from P1 interview. Not yet quantitatively validated but represents a real workflow gap: AI tools generate planning content that currently has nowhere to go. Low-effort implementation (paste/import) with high perceived value for the Explorer/Planner type.

---

## Tensions and Open Questions

1. **Auto-capture vs. privacy.** J1 (background location logging) and A3 (granular location controls) are in tension. Auto-capture only works well with always-on location access; privacy concerns have risen to 4/13 as an adoption barrier. The design must make opt-out feel safe without gutting the product's strongest feature.

2. **Trip Planning as the lead — Aisha reframed.** ✅ Resolved after P1 interview (Jun 2026). Aisha has been updated in `06_User_Personas.md` to absorb the Pragmatic Planner archetype. Her primary pain is now fragmentation across planning tools, and her quote, bio, and frustrations reflect this shift.

3. **Discovery quality over time.** Peer-sourced content (D1) is the most trusted format, but quality degrades as volume grows. A curation or flagging mechanism will be needed but is not yet defined.

4. **Free model vs. sustainable product.** A1 is required for adoption, but the pool does not yet specify what sits behind a paywall. J2 (premium layouts) and physical output are natural candidates. This needs resolution in the Feature Strategy.

6. **AI tools as workflow participants.** P1 uses ChatGPT and Gemini actively in the planning workflow. P6 (AI itinerary import) is a first-response solution, but the broader question — whether Travel Buddy should integrate with AI APIs or position as an alternative — remains open. This has implications for the competitive SWOT and Feature Strategy.

5. **Journaling demand: aspirational vs. actual.** Auto-capture and layout are both wanted by 8/13 including non-documenters. It is not yet known whether this is behavioral intent or aspirational. Qualitative interviews should probe this before either is built as a core feature.

---

## Next Step

→ `08_Feature_Strategy.md` — Apply MoSCoW prioritization to this pool. Define Must Have, Should Have, Could Have, and Won't Have for v1. Map to the three personas and the four travel journey phases (Pre-trip, In-destination, Post-trip, Between trips).

---

## References

- `05_Research_Synthesis.md` — source data for all problem statements
- `06_User_Personas.md` — persona definitions and feature–hypothesis links
- Dippner, D. (2022). *User Experience Design: Principles & Methods* (1st ed.). SRH Fernhochschule.
- Martin, B., & Hanington, B. (2012). *Universal Methods of Design.* Rockport Publishers.
