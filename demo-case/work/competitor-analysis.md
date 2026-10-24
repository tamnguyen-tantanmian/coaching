---
type: "competitor-analysis"
title: "Competitor analysis and SWOT"
stage: "Discover"
status: "verified"
summary: "Five competitors plus AI chat tools, compared on ten criteria: nobody covers all three pillars of discovery, connection and journal, for free."
takeaways:
  - "No competitor covers all three pillars at once and for free."
  - "TripAdvisor and Google Maps own discovery but have no connection or journal; Polarsteps does the journal well but has no discovery."
  - "AI chat tools are both a competitor and an opportunity: the itineraries they produce have nowhere to go."
supports:
  - "[[O1]]"
  - "[[O2]]"
  - "[[O4]]"
  - "[[D3]]"
  - "[[D5]]"
media:
  - "sources/anonymised/03_Competitor_Research_SWOT.md"
---
# Competitor analysis

*Working file for the competitor flow. The sources you saved are in `sources/anonymised/`.*

## Scope
- The decision this analysis serves: where Travel Buddy should stand against the existing platforms, and where it should not compete head-on
- The criteria that matter (at most 6): coverage of the three pillars (discovery, connection, planning and journal); free; private; whether the content is trustworthy; works offline; structured, saved output
- What I already believe: no platform covers all three pillars (RH1, RH3)

## Competitors
Five competitors, by role in the traveller's journey:

| Competitor | Role | Pillar touched |
|---|---|---|
| TripAdvisor | Discovery through reviews from strangers | Discover |
| Google Maps | Discovery and navigation | Discover |
| Foursquare | Contextual tips | Discover |
| Polarsteps | Trip journal, sharing | Journal, Share |
| Airbnb Experiences | Connecting with locals (paid) | Connect |
| *AI chat tools* (added after interview P1) | Drafting itineraries; the output is not stored in a structured way | Plan |

## Evidence (AI draft)
*None.* The original project was made before this AI-assisted way of working existed, so there is no AI draft to compare with the checked version, and an error rate cannot be calculated.

## Evidence (verified)
Source: `sources/anonymised/03_Competitor_Research_SWOT.md`, section 3.4. Key: yes = well covered, partial, no.

| Criterion | TripAdvisor | Google Maps | Foursquare | Polarsteps | Airbnb Exp. | AI chat tools |
|---|---|---|---|---|---|---|
| Local discovery | yes | yes | yes | no | partial | partial |
| Curated, personal tips | no | no | yes | no | partial | no |
| Connecting with locals | no | no | partial | no | yes | no |
| Trip planning | partial | partial | no | no | no | partial |
| Trip journal | no | no | partial | yes | no | no |
| Sharing | no | no | partial | yes | no | no |
| Works offline | no | yes | no | yes | no | no |
| Free | yes | yes | yes | yes | no | yes |
| Privacy-first design | no | no | no | yes | partial | no |
| Structured, saved output | partial | partial | no | yes | no | no |

## Patterns
- No competitor covers all three pillars (discovery, connection, journal) at once, and for free.
- TripAdvisor and Google Maps own discovery but have no connection or journal. Polarsteps does the journal well but has no discovery. Airbnb Experiences has connection but behind a paywall. Foursquare proved that contextual tips beat star ratings, then left the end-user market.
- The gap: a platform that serves travellers in real time, across all three pillars, for free.
- Counter-argument: Google has the infrastructure to copy any feature at scale.

## Insights + decision
1. **Discovery through real people, not star ratings.** Support: TripAdvisor lost trust because of fake reviews; Foursquare showed contextual tips work better.
2. **Connection must be non-transactional.** Support: authenticity is the main driver of a good experience on Airbnb Experiences, but it sits behind a paywall.
3. **The journal must be automatic and private by default.** Support: Polarsteps grew thanks to a low-effort journal and a privacy-first design.
4. **AI chat tools are both a competitor and an opportunity.** They produce text itineraries that have nowhere to go; importing an AI itinerary into Travel Buddy makes it an entry point (SP-P6).

**Decision for the question in Scope:** Travel Buddy should not compete head-on on map data or review volume; it should stand where nobody covers: tips from real people with an identity, non-transactional connection, and planning plus journal in one place, for free.

**Limits of this analysis:** it rests on public sources and has not been checked with real users; it only shows what competitors **do**, not why users choose them.
