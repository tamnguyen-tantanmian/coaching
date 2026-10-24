# Product Requirements Document — Explore Experience
## Travel Buddy

| Field | Value |
|-------|-------|
| **Feature** | Explore Tab — Full Discovery Experience |
| **Version** | v1.0 |
| **Status** | 🟡 Ready for design |
| **Phase** | Prototype |
| **Author** | Project owner |
| **Last updated** | Jul 2026 |
| **Linked docs** | `07_Solution_Pool.md` · `08_E2E_User_Flow.md` · `06_User_Personas.md` · `05_Research_Synthesis.md` · `10_Prototype_Plan.md` |
| **Solutions in scope** | D1, D2, D3, D4, D5, A4 |

---

## 1. Overview

The Explore tab is the primary entry point of Travel Buddy. It is the first surface a user encounters — including unauthenticated guests — and the main reason they return between trips. Its purpose is to help travelers discover authentic, peer-sourced places and experiences, without relying on commercial listings or opaque ratings.

The Explore experience offers three discovery modes: **Near Me** (location-aware default feed), **by Country** (destination-first inspiration), and **by Map** (spatial/proximity-based discovery). All three modes share a unified filter system, crowd signal layer, and one-tap save action connecting discovery directly to trip planning.

---

## 2. Problem Statement

Travelers currently use 8–10 separate apps per trip because no single platform combines discovery, trustworthy peer context, and planning in one place (P1 interview, Jun 2026; H3 confirmed). Existing platforms like TripAdvisor and Google Maps are perceived as commercially biased — users distrust aggregate ratings and cannot tell whether a recommendation came from someone who travels like them (H1 confirmed, n=13 survey).

Travel Buddy's Explore experience must solve two problems simultaneously:

1. **Trust gap** — Surface tips with visible traveler identity and travel style so users can apply their own trust logic, not just a star average.
2. **Fragmentation gap** — Connect discovery directly to planning (save to shortlist in one tap) so users never need to switch apps to act on what they find.

---

## 3. Goals

### 3.1 User Goals
- Find authentic, non-commercial travel tips that match their travel style
- Understand a place's crowd level and safety context before visiting
- Save anything interesting to a trip plan without leaving the discovery flow
- Browse freely without being forced to create an account

### 3.2 Product Goals
- Demonstrate core value to a new user within the first session (before sign-up)
- Drive conversion from guest to registered user via save and connect actions
- Establish Travel Buddy as the single place where discovery and planning coexist

### 3.3 Success Metrics

| Metric | Target |
|--------|--------|
| Time to first tip interaction (tap or save) | < 30 seconds from app open |
| Guest-to-registered conversion rate via Explore | ≥ 25% of guests who tap Save |
| Tips saved per session (registered users) | ≥ 2 per session |
| Filter usage rate | ≥ 40% of active users apply at least one filter per week |
| Mode switch rate (Country → Map → List) | Tracked; no target for v1, used for IA validation post-launch |

---

## 4. Users & Personas

| Persona | Primary need in Explore | Primary mode |
|---------|------------------------|--------------|
| **Aisha — Explorer / Pragmatic Planner** | Research a destination thoroughly before committing; avoid tourist traps; build a structured shortlist from peer tips | Near Me (filtered by Explorer style) + Country drill-down |
| **Ji-yeon — Social Connector** | Find where other travelers and locals hang out; discover human connection opportunities alongside places | Near Me (filtered by Local life) + Map |
| **Documenter** | Browse for inspiration; save things that feel worth revisiting; low-intent browsing | Country (inspiration-first) |
| **Guest (unauthenticated)** | Explore without commitment; see what the app offers before signing up | All modes, read-only |

---

## 5. Scope

### In Scope — v1
- Explore tab with three discovery modes: **Near Me** (default, location-aware), **Country** (browse beyond current location), **Map** (spatial). Near Me is the intelligent default; Country and Map are how users expand outward. Within Country mode, search or manual country selection is a secondary action — contextual destination suggestions are shown first
- Shared filter system (travel style, category, timing)
- Crowd signal badge on all tips (D3)
- Video snippet badge and player (D4)
- Safety context panel (D5)
- One-tap save to shortlist (P3) with guest sign-up gate
- Guest browsing access to all three modes (A4)
- Tip detail screen with Details / Video / Safety tabs

### Out of Scope — v1
- User-generated tip submission (post-launch)
- Offline map caching in Explore (offline access is scoped to Plan tab, P4)
- Paid or promoted tips
- Social following (follow a traveler, see their feed) — post-launch
- Collaborative real-time exploration with companions (post-launch)
- Search by tip text / full-text search (post-launch; v1 has destination search only)

---

## 6. Functional Requirements

Priority levels: **P0** = must have for v1 · **P1** = should have · **P2** = nice to have

---

### 6.1 Mode Switcher

| ID | Requirement | Priority |
|----|-------------|----------|
| EX-01 | The Explore tab shall display a mode toggle (Near Me / Country / Map) permanently below the top bar, with Near Me as the leftmost and default-active tab | P0 |
| EX-02 | On first open, the app shall default to **Near Me** mode. If the user has granted location permission, the feed shall be filtered to tips relevant to their detected location or nearest destination | P0 |
| EX-03 | If location permission has not been granted, Near Me mode shall fall back to the personalised feed based on onboarding travel style (A5), with a soft prompt to enable location | P0 |
| EX-04 | Country and Map modes shall be framed visually as "explore further" — i.e. they expand beyond the user's current context, not replace it | P1 |
| EX-05 | Switching modes shall preserve any active filters | P0 |
| EX-06 | The last active mode shall be restored when the user returns to the Explore tab within the same session | P1 |
| EX-07 | Mode switch shall animate with a crossfade or horizontal slide transition | P1 |

---

### 6.2 Explore by Country

Country mode is for users who want to explore beyond their current location. The entry experience is **contextual and curated** — the user sees suggested destinations relevant to them without needing to type anything. Search and manual country selection are available but secondary.

| ID | Requirement | Priority |
|----|-------------|----------|
| EC-01 | The Country mode shall open with contextually curated destination suggestions — no search prompt, no blank state. Suggestions are based on: user's travel style (A5), trending destinations this month, and destinations popular among similar traveler profiles | P0 |
| EC-02 | Destinations shall be presented as full-bleed photo cards with country name, flag, and crowd signal (D3) — browseable without any search input | P0 |
| EC-03 | Destinations shall be groupable by region via a horizontal pill tab row (Asia, Europe, South America, Africa, etc.) shown below the curated section | P0 |
| EC-04 | A search / country selector shall be accessible via the search icon in the top bar — it is a secondary action, not the primary entry point of Country mode | P0 |
| EC-05 | Tapping a destination card shall navigate to a Country Detail screen | P0 |
| EC-06 | The Country Detail screen shall show: hero photo, destination stats (best season, region, tip count), and a scrollable tip list | P0 |
| EC-07 | The Country Detail screen shall include a "Map" sub-tab that shows embedded map view of tips in that destination | P1 |
| EC-08 | A stacked card fan UI shall be used for the "Popular Destinations" section to support browsing multiple destinations visually | P1 |
| EC-09 | The Country mode shall surface a "Trending this month" featured destination card at full width above the curated grid | P1 |

---

### 6.3 Explore by Map

| ID | Requirement | Priority |
|----|-------------|----------|
| EM-01 | The Map mode shall render an interactive map occupying the full screen below the mode toggle | P0 |
| EM-02 | Tips shall be displayed as colour-coded map pins: green (local favourite), amber (popular), red (very touristy), based on crowd signal data (D3) | P0 |
| EM-03 | Pins in close proximity shall cluster into a numbered cluster pin; tapping expands or zooms in | P0 |
| EM-04 | Tapping any pin shall surface a peek card from the bottom (partial bottom sheet, ~180px) showing: tip thumbnail, name, city, crowd badge, traveler credit, Save and "See full tip" actions | P0 |
| EM-05 | Tapping the peek card or "See full tip" shall navigate to the Tip Detail screen | P0 |
| EM-06 | A "My location" button shall centre the map on the user's current GPS location | P0 |
| EM-07 | A horizontal category pill row shall appear above the peek card area to filter which pin types are visible (Food, Nature, Art, Culture, Local) | P1 |
| EM-08 | The map shall use a topographic contour line style (light grey contour lines on white) — not satellite, not standard street map | P1 |
| EM-09 | The user's own saved/visited places shall appear as photo thumbnail pins on the map (distinct style from tip pins) | P1 |
| EM-10 | Long-pressing on any map location shall trigger an "Explore tips near here" action | P2 |

---

### 6.4 Explore — Near Me

| ID | Requirement | Priority |
|----|-------------|----------|
| EL-01 | The Near Me mode shall display a vertical scrolling feed of peer-sourced tip cards (D1) relevant to the user's current or nearest location, full width | P0 |
| EL-02 | When location is detected, the feed shall prioritise tips near the user's current location or nearest travel destination, labelled "Tips near [City]". When location is unavailable, the feed shall fall back to personalisation based on travel style (A5 answers), labelled "Tips for you" | P0 |
| EL-03 | A location context label shall appear above the feed showing the detected city (e.g. "📍 Near Chiang Mai") with a "Change" link to manually set a location | P0 |
| EL-04 | For guest users (A4), the feed shall show 6 tips followed by an inline "Sign up to see more" nudge card | P0 |
| EL-05 | Each tip card in Near Me mode shall display: full-bleed photo (200px tall), place name, city/country, category tag, crowd signal badge (D3), video badge if applicable (D4), safety indicator if applicable (D5), traveler avatar + name + travel style tag + recency, one-line tip preview text, save icon | P0 |
| EL-06 | Tapping any tip card shall navigate to the Tip Detail screen | P0 |
| EL-07 | Active filters shall be shown as a horizontally scrollable chip row at the top of the feed; each chip has an ✕ to remove it | P0 |
| EL-08 | The feed shall support pull-to-refresh to load new tips | P1 |
| EL-09 | Tips with video content shall display a 🎬 badge on the card; tapping the badge opens the Video Snippet Player in full screen (D4) | P1 |
| EL-10 | The feed shall display a tip count (e.g. "124 tips near Chiang Mai") beside the section header | P1 |
| EL-11 | Infinite scroll or "Load more" pagination shall prevent long load times on initial render | P1 |

---

### 6.5 Shared Filter System (D2)

| ID | Requirement | Priority |
|----|-------------|----------|
| EF-01 | A filter panel shall be accessible from the filter icon in the top bar across all three modes | P0 |
| EF-02 | The filter panel shall be presented as a bottom sheet | P0 |
| EF-03 | The filter panel shall include the following filter groups: Travel style (multi-select chips: Explorer, Cultural, Relaxed, Adventure, Solo, Family), Category (multi-select chips: Food, Nature, Art, Hidden gems, Local life, Nightlife), Timing (single-select: Planning soon, Already there, Just browsing), Verified travelers only (toggle) | P0 |
| EF-04 | Applying filters shall update all three modes simultaneously | P0 |
| EF-05 | The filter panel shall include an "Apply" CTA and a "Clear all" text action | P0 |
| EF-06 | Filters shall persist across mode switches within the same session | P0 |
| EF-07 | The number of active filters shall be shown as a badge on the filter icon (e.g. "Filters · 2") | P1 |

---

### 6.6 Crowd Signal (D3)

| ID | Requirement | Priority |
|----|-------------|----------|
| ED3-01 | Every tip card and map pin shall display a crowd signal badge at all times — not hidden behind a tap | P0 |
| ED3-02 | Crowd signal shall use a 3-level scale: 🟢 Local favourite / 🟡 Popular / 🔴 Very touristy | P0 |
| ED3-03 | Tapping the crowd signal badge shall display an inline tooltip: "Based on recent traveler reports" | P1 |
| ED3-04 | The Tip Detail screen shall show an expanded crowd signal section with a brief trend note (e.g. "Busiest on weekends") | P1 |

---

### 6.7 Video Snippets (D4)

| ID | Requirement | Priority |
|----|-------------|----------|
| ED4-01 | Tips with video content shall display a 🎬 badge on their card in Near Me and Country Detail modes | P0 |
| ED4-02 | The Tip Detail screen shall include a "Video" segment tab that opens the video player | P0 |
| ED4-03 | The video player shall play vertically full-screen | P0 |
| ED4-04 | Video shall be muted by default; tapping the video unmutes | P0 |
| ED4-05 | In list mode, swiping up while the video player is open shall advance to the next video tip | P1 |
| ED4-06 | Swiping down shall close the video player and return to the list | P1 |

---

### 6.8 Safety Context (D5)

| ID | Requirement | Priority |
|----|-------------|----------|
| ED5-01 | Tips with safety data shall display a ⚠️ safety indicator on their list card | P0 |
| ED5-02 | The safety context panel shall be accessible as a bottom sheet from both the tip card and the Tip Detail screen | P0 |
| ED5-03 | The safety panel shall display: overall safety level (colour-coded), last updated date, and a list of recent traveler-submitted safety notes | P0 |
| ED5-04 | Each safety note shall show: note text, traveler type, and recency (days ago) | P0 |
| ED5-05 | The safety panel shall include a "Contribute a note" action (requires account) | P1 |
| ED5-06 | The safety panel shall include a "Report inaccurate info" action | P1 |

---

### 6.9 Guest Access (A4)

| ID | Requirement | Priority |
|----|-------------|----------|
| EA4-01 | All three Explore modes shall be fully browseable without an account | P0 |
| EA4-02 | Tip detail screens shall be fully accessible without an account | P0 |
| EA4-03 | The save (♡) action shall be gated: tapping while unauthenticated shall trigger a bottom sheet with "Sign up free" and "Log in" options | P0 |
| EA4-04 | Accessing a local profile from Explore shall be gated with the same sign-up bottom sheet | P0 |
| EA4-05 | A dismissable nudge banner shall appear once at the top of the Near Me feed for guest users | P1 |
| EA4-06 | The guest feed shall show 6 tips before displaying an inline "Sign up to see more" card | P1 |

---

### 6.10 Tip Detail Screen (S11 — shared)

| ID | Requirement | Priority |
|----|-------------|----------|
| ES11-01 | The Tip Detail screen shall display: full-bleed hero photo (≥55% screen height), floating back and save buttons, place name, location, duration estimate, crowd signal, safety indicator | P0 |
| ES11-02 | The screen shall include a segment tab control: Details / Video / Safety | P0 |
| ES11-03 | The Details tab shall show: traveler avatar, name, travel style, tip rating, and full tip text in the traveler's own voice | P0 |
| ES11-04 | The screen shall show a "Similar tips" horizontal scroll section | P1 |
| ES11-05 | A persistent bottom bar shall show "Save to trip" and "Share" actions | P0 |

---

## 7. Non-Functional Requirements

| ID | Requirement | Priority |
|----|-------------|----------|
| NF-01 | The Near Me feed shall render the first 6 tip cards within 2 seconds on a standard mobile connection | P0 |
| NF-02 | The Map mode shall render visible pins within 1.5 seconds of mode switch | P0 |
| NF-03 | Video snippets shall begin playback within 1 second of the player opening | P1 |
| NF-04 | All interactive elements (cards, buttons, pins) shall have a minimum tap target of 44×44px (iOS HIG standard) | P0 |
| NF-05 | The experience shall be fully functional on iOS 16+ and Android 12+ | P0 |
| NF-06 | Guest browsing shall not require network permissions or location access (location is opt-in, prompted only when Map mode is used) | P0 |
| NF-07 | Text on photo overlays shall meet WCAG AA contrast ratio (4.5:1 minimum) | P1 |

---

## 8. Acceptance Criteria

The Explore feature is considered complete for prototype sign-off when:

- [ ] All three modes (Country, Map, List) are navigable via the mode toggle
- [ ] Filter panel opens from all three modes and applies correctly
- [ ] Crowd signal badge (D3) appears on every tip card across all modes
- [ ] Save action (P3) triggers sign-up bottom sheet for guest users
- [ ] Video player (D4) opens from list tip card and Tip Detail screen
- [ ] Safety panel (D5) opens from list tip card and Tip Detail screen
- [ ] Tip Detail screen is reachable from all three modes
- [ ] Guest can browse all modes without being forced to sign up
- [ ] Prototype is tested with at least 2 participants using tasks from `10_Prototype_Plan.md` §8

---

## 9. Dependencies

| Dependency | Required for | Status |
|------------|-------------|--------|
| `10_Prototype_Plan.md` design system | All screens | ✅ Ready |
| `07_Solution_Pool.md` D1–D5 definitions | Feature requirements | ✅ Ready |
| Crowd signal data model | ED3 requirements | 🔲 To be defined |
| Safety notes data model | ED5 requirements | 🔲 To be defined |
| Card sort results (`09_Card_Sorting_IA.md`) | Tab label finalisation (Explore vs. Discover) | 🔲 Pending |
| Real Unsplash photo URLs | Prototype visual fidelity | 🔲 To be sourced |

---

## 10. Open Questions

| # | Question | Owner | Due |
|---|----------|-------|-----|
| 1 | Should "Explore" be the final tab label, or will card sort results suggest a different word (e.g. "Discover", "Find")? | Project owner | After card sort |
| 2 | Is the crowd signal a user-reported metric, an algorithmic score, or both? Data model needs to be defined before backend spec | TBD | Pre-wireframe |
| 3 | What is the minimum number of tips needed for a destination to appear in Country mode? Avoid showing destinations with 1–2 tips | TBD | Pre-launch |
| 4 | Should the Map mode default to the user's current location or their saved trip destination? | Project owner | Usability test |
| 5 | Video content — is this traveler-uploaded, curated by Travel Buddy, or both in v1? Affects content strategy significantly | TBD | Product strategy |

---

## References

- Dippner, D. (2022). *User Experience Design – Principles & Methods.* SRH Fernhochschule.
- `05_Research_Synthesis.md` — P1 interview: trust, fragmentation, cross-source convergence
- `06_User_Personas.md` — Aisha (primary), Ji-yeon, Documenter
- `07_Solution_Pool.md` — D1–D5 solution definitions, H1–H3 hypothesis confidence
- `08_E2E_User_Flow.md` — Phase 1 Pre-Trip Discover, Phase 3 In-Destination Navigate
- `10_Prototype_Plan.md` — Design system, screen inventory S10–S15, build instructions
