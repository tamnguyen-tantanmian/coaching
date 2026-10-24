# User Personas: Travel Buddy
**Project:** Travel Buddy | **Phase:** Discovery  
**Linked to:** `05_Research_Synthesis.md` · `01_Research_Hypotheses.md`  
**Status:** Updated to n=13 survey data · P1 interview complete — Aisha reframed to include Pragmatic Planner traits · ⚠️ flags on Ji-yeon partially resolved

> **Note on confidence:** Based on survey data (n=13) and one user interview (P1). Sections marked with ⚠️ that P1 partially resolved are noted inline. Remaining ⚠️ flags require additional interview participants.

---

## 1. Literature Review

A persona is "the creation of a representative user based on available data and user interviews. Though the personal details of the persona may be fictional, the information used to create the user type is not" (Gladkiy, 2016, as cited in Dippner, 2022, p. 140). Personas exist because, as Garrett (2011, p. 42) reminds us, "we are not designing for ourselves; we are designing for other people" (as cited in Dippner, 2022, p. 107). Without them, teams risk building products shaped by internal assumptions rather than real user needs. Marsh (2018) describes personas as one of the core methods for presenting research insights, alongside affinity diagrams and journey maps, because they translate patterns from raw data into something the whole team can reason with (as cited in Dippner, 2022, p. 206). For Travel Buddy, three personas were developed rather than one or four because the product is built around three distinct pillars: Discover, Connect, and Plan and Share. Each pillar addresses a fundamentally different need, and the survey data confirmed that these differences are real. The Explorer is a curious, practical traveler who creates detailed pre-trip plans but adapts constantly on arrival — her core frustration is not just poor discovery but the fragmentation of planning across too many tools. P1 interview data prompted a reframe of this persona to absorb the Pragmatic Planner archetype, which surveys confirmed is the primary Trip Planning user type. The Connector is someone who wants to meet locals in an authentic, non-transactional way but has never had a safe tool to do it. The Documenter captures everything on a trip but has no system for organizing or sharing those memories without it feeling like extra work.

---

## 2. Problem Definition

Travelers are surrounded by more information than ever, and trust almost none of it. Survey data (n=13) shows local recommendations score **4.46 / 5** in trust while TripAdvisor star ratings score **3.38** and stranger reviews **3.31**. Yet the apps travelers rely on are built almost entirely around those lower-trust sources. **10 of 13 respondents have been disappointed by a highly-reviewed place.**

The problem spans three stages of travel, now reordered to reflect feature importance rankings from the expanded dataset:

1. **Planning is fragmented and inflexible.** 9 of 13 travelers plan loosely and adapt constantly, yet planning is the feature they rate most important (4.38 / 5). "I have to use many different apps" rose to 5/13 as a top frustration. P1 interview confirmed this qualitatively: travelers use 8–10 tools per trip and manually move information between each one — TikTok → Google Maps → Google Sheets → AI tools — with no automation at any step. Existing tools force a choice between rigid itineraries or scattered saves across multiple apps.
2. **Discovery is broken.** Platforms surface what is commercially popular, not what is genuinely worth visiting. "Hard to find authentic local experiences" was the #1 frustration (9/13), and local discovery ranked second in feature importance (3.85 / 5).
3. **Connection is untapped.** 12 of 13 travelers are open to meeting locals, but no current tool makes it feel safe, free, and non-transactional at the same time. Verified identity (11/13), no monetary exchange (9/13), and shared interests on profile (8/13) are all required.
4. **Memory fades by default.** 7 of 13 either do not document at all or want it fully automatic. Auto-capture and a beautiful auto-generated layout are now co-equal top journal features (both 8/13). Journaling ranks third in feature importance (3.62 / 5) — strong, but no longer the lead hook.

Travel tools optimize for volume and reach, not for trust, ease, and human connection. Travel Buddy's opportunity is to close that gap across the full travel journey, with flexible trip planning as the primary acquisition hook.

---

## 3. Personas

### Persona 1: The Explorer / Pragmatic Planner

> *"I look things up before I go, build a whole planner, and still end up winging 30% of it once I'm there. The problem isn't finding information — it's that I have to collect it from everywhere myself."*

*Note: Reframed after P1 interview (Jun 2026) to absorb Pragmatic Planner archetype. Aisha now represents the traveler who plans seriously but flexibly, and whose primary pain is fragmentation — not just poor discovery.*

| | |
|---|---|
| **Name** | Aisha |
| **Age** | 26 |
| **Occupation** | Content coordinator (remote) |
| **Location** | Kuala Lumpur, Malaysia |
| **Travel frequency** | 1–3 trips per year, mix of regional and international |
| **Travel style** | Mix — comfortable travel focused on food, culture, and sightseeing |

### Bio
Aisha does her research. Before any trip she has a Google Sheets planner with a budget, shortlist of restaurants, must-see spots, and rough itinerary. She uses Google, TikTok, ChatGPT, YouTube, Facebook travel groups, and Google Maps — sometimes all on the same trip. The problem is that every discovery in one app has to be manually moved to the next. She finds the restaurant on TikTok, saves the location on Maps, confirms it in a Facebook group, then types it into her spreadsheet. By the time she arrives, she has a solid plan — but she built it through sheer effort, not good tools. Once on the ground, she stays flexible: 30–40% of her best moments come from spontaneous detours or recommendations she picks up along the way. She represents the most common user in the survey: a Mix traveler who plans seriously but hates being locked in.

### Goals
- Find places that feel worth going to, not just highly reviewed
- Build a trip plan without manually stitching information across six apps
- Come home with memories she can actually find and share

### Frustrations
- Moving information between apps is the most time-consuming part of planning — and no tool fixes it
- AI tools like ChatGPT generate good itinerary ideas, but the outputs have nowhere to go
- Highly-reviewed places consistently disappoint with crowds, inaccurate photos, and a commercial vibe
- She cannot always tell which recommendation is from a local and which is from a tourist who visited once

### Motivation
- A trip that feels genuinely local, not a tourist loop of the same five places
- The efficiency of having everything in one place so she can focus on the trip, not the prep
- Returning home with clear memories of where she went and why it mattered

### Expectation
- Recommendations she can trust across discovery, confirmation, and saving — without switching apps
- A planning tool that stays flexible and does not lock her into a set itinerary
- AI-assisted organization that knows what she has saved and helps her turn it into a plan

### Personality
- Practical and methodical at the planning stage; spontaneous once she arrives
- Trusts recommendations more when they are consistent across multiple sources
- Budget-conscious: checks financial feasibility before committing to a destination
- Would switch apps if the utility gain is clear and immediate

### Hobbies
- Food, local culture, sightseeing, shows, and theme parks
- TikTok and Facebook travel groups for inspiration; ChatGPT for itinerary drafting

**Primary feature:** Trip Planner · **Hypothesis links:** H1, H2, H3, H9  
**Key data:** Local tips avg trust 4.46 vs. platform 3.38 (n=13) · 9/13 cite "hard to find authentic experiences" · Trip Planning rated #1 feature (4.38/5) · P1 confirmed 8–10 apps/trip and named fragmentation as the single most important thing to fix

---

### Persona 2: The Connector

> *"I've had conversations with locals that changed how I thought about a place. But I've never found a reliable way to make that happen. It has always been luck."*

| | |
|---|---|
| **Name** | Marco |
| **Age** | 29 |
| **Occupation** | Freelance UX designer |
| **Location** | Barcelona, Spain |
| **Travel frequency** | 1 to 3 trips per year, mix of Europe and Southeast Asia |
| **Travel style** | Solo or with partner |

### Bio
Marco has had meaningful local interactions that reshaped how he experienced a destination, but they only happened by chance. He would not pay for a local experience because it changes the dynamic: the moment money is involved, the authenticity drains out. He represents the 7 of 8 travelers who are open to connection but have never had a tool that made it feel both safe and genuine at the same time.

### Goals
- Have at least one meaningful conversation with a local per trip
- Find things to do that were not part of any plan
- Feel like a real person in a place, not a tourist moving between checkboxes

### Frustrations
- Platforms like Airbnb Experiences make human connection feel like a product
- There is no safe, low-friction way to meet locals organically
- Group tours feel staged, and solo outreach feels awkward without any shared context

### Motivation
- The feeling of being welcomed into a place, not just passing through it
- Reciprocity: he is happy to show travelers around Barcelona in return
- Human stories that no guidebook ever captures

### Expectation
- A verified, free way to connect with locals before or during a trip
- Confidence that the other person is who they say they are
- No pressure, just a genuine exchange rather than a paid service

### Personality
- Warm and people-oriented, distrustful of anything that feels commercial or algorithmic
- Prefers depth over breadth: one real conversation over five tourist stops
- Comfortable with ambiguity and does not need a structured plan to feel at ease

### Hobbies
- Language learning, local markets, neighborhood exploration
- Community travel platforms like Couchsurfing, local meetups when abroad

**Primary feature:** Local Match · **Hypothesis links:** H4, H5  
**Key data:** 12/13 open to local connection (n=13) · Verified identity (11/13) + no money involved (9/13) + shared interests on profile (8/13), all three near-required · ⚠️ *Qualitative confirmation needed: whether "no cost" is a dealbreaker or a preference*

---

### Persona 3: The Documenter

> *"I always think I'll organize my photos when I get home. I never do. Then two years later I'm looking at 800 pictures and I can't remember half of what I was doing."*

| | |
|---|---|
| **Name** | Ji-yeon |
| **Age** | 27 |
| **Occupation** | Product manager |
| **Location** | Seoul, South Korea |
| **Travel frequency** | 2 to 4 trips per year |
| **Travel style** | Usually with friends or partner |

### Bio
Ji-yeon takes hundreds of photos every trip and genuinely intends to organize them later. She never does. It is not laziness: every journaling tool she has tried demands more attention than the trip itself is worth giving up. She is not a creator or a public poster. She wants memories for herself and the people who were there. She represents the strongest product signal in the survey: auto-capture was the most wanted feature (7/8), including from people like her who currently do not document anything.

### Goals
- Keep a record of trips without it feeling like a second job
- Share memories with the people she traveled with, not the whole internet
- Look back on a trip in two years and remember the context, not just the photo

### Frustrations
- Her camera roll has no context, just images with no notes on where, who, or why
- Journaling apps require effort she does not sustain past day two
- Instagram feels performative and WhatsApp threads get buried immediately

### Motivation
- The fear of forgetting: she knows how fast trip memories fade
- Wanting something to show people when they ask how the trip was
- Private, meaningful sharing with the people who were actually there

### Expectation
- Documentation that happens automatically in the background
- A beautiful, shareable output she did not have to build herself
- Sharing that is private by default with an easy option to open up later

### Personality
- Organized at work and spontaneous in travel
- Values aesthetics and wants outputs to look good with minimal effort
- Prefers private sharing and is neither a broadcaster nor a dedicated journaler

### Hobbies
- Cafe-hopping, photography, watching travel vlogs as a viewer not a creator
- Pinterest boards and Notion trip notes that never get finished

**Primary feature:** Travel Journal · **Hypothesis links:** H7, H8  
**Key data:** Auto-capture and beautiful layout tied as top journal features (8/13 each, n=13) · Journaling ranked #3 in feature importance (3.62/5, down from #1 at 4.38/5 in n=8) · Private-by-default strengthened (6/13) · *P1 partially resolves ⚠️: aspiration-execution gap confirmed as real — P1 loses restaurant names/details from past trips and responded positively to auto-capture concept. Whether non-documenters will actually engage once built still requires diary study or follow-up.*

---

## 4. Persona Summary Matrix

| Persona | Primary Feature | Key Signal | Hypotheses |
|---------|----------------|------------|------------|
| Aisha, The Explorer / Pragmatic Planner | Trip Planner | 9/13 cite "hard to find authentic experiences" · Trip Planning #1 feature (4.38/5) · P1: 8–10 apps/trip, fragmentation named as #1 pain | H1, H2, H3, H9 |
| Marco, The Connector | Local Match | 12/13 open to local connection · verified identity (11/13) + no cost (9/13) + shared interests (8/13) all required | H4, H5 |
| Ji-yeon, The Documenter | Travel Journal | Auto-capture + beautiful layout both 8/13 · Journaling #3 feature (3.62/5) · P1 confirms aspiration-execution gap is real | H7, H8 |

---

## 5. What the Research Changed from Initial Assumptions

| Initial assumption | What the data shows |
|-------------------|---------------------|
| The Explorer is the primary user | Mix and Relaxer travelers dominate the sample (8/13). Design must work for casual, comfort-oriented travelers, not just enthusiasts. Aisha reframed accordingly after P1 interview. |
| App fragmentation (H3) is a key pain point | Survey: 5/13 cite it (3rd). P1 interview: named as the single most important thing to change. The gap between survey rank and qualitative intensity suggests fragmentation is a compound, systemic pain that multiple-choice formats underweight. Treat as co-equal to content quality. |
| Network effects are the main adoption barrier (H10) | Price still dominates (7/13). P1 frames switching in terms of utility gain, not social network — would switch if consolidation value is clear. Network effects (2/13) remain a signal to monitor. |
| Journaling is a supporting feature | Journaling rose to #1 in n=8, then dropped to #3 in n=13 (3.62/5) as Trip Planning surged to #1 (4.38/5). P1 confirms journaling is desired but not the primary hook. |
| Trip Planning is a secondary feature | Now ranked #1 in feature importance (4.38/5), up from last place (3.00/5) in n=8. P1 confirms: planning is the most painful workflow and the highest-value consolidation opportunity. |
| AI tools are outside the product's competitive scope | P1 actively uses ChatGPT and Gemini in the planning workflow. These tools contribute to fragmentation and represent a workflow Travel Buddy could partially absorb. Treat as both a competitive signal and a design opportunity. |

---

## 6. References

- Dippner, D. (2022). *User Experience Design: Principles & Methods* (1st ed.). SRH Fernhochschule. [Cited as: Dippner, 2022]
- Garrett, J. J. (2011). *The Elements of User Experience* (2nd ed.). New Riders. (as cited in Dippner, 2022, p. 107)
- Gladkiy, A. (2016). Persona definition. (as cited in Dippner, 2022, p. 140)
- Marsh, J. (2018). *UX for Beginners: A Crash Course in 100 Short Lessons.* O'Reilly Media. (as cited in Dippner, 2022, pp. 138, 205, 206)
- Whitenton, K. (2021). Triangulation definition. (as cited in Dippner, 2022, p. 112)
- `05_Research_Synthesis.md` — full survey data and hypothesis tracker
- `01_Research_Hypotheses.md` — original archetype definitions and screener criteria
