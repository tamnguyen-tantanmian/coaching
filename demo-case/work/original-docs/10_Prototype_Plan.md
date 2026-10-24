# Prototype Plan — Travel Buddy
**Project:** Travel Buddy | **Phase:** Prototype  
**Linked to:** `07_Solution_Pool.md` · `08_E2E_User_Flow.md` · `06_User_Personas.md` · `09_Card_Sorting_IA.md`  
**Fidelity:** 🎨 High-fidelity | **Platform:** Mobile (iOS-style, 390 × 844px)  
**Status:** 🟡 Ready to build | **Scope:** All 26 solutions · 4 flows · 32 screens

---

## 1. Theoretical Grounding

A prototype is "a simulation of the final product used to test design decisions before the cost of implementation is incurred" (Dippner, 2022, p. 192). High-fidelity prototypes closely approximate the final visual design and are appropriate when the goal is to test usability with real users, present a concept to stakeholders, or validate emotional response to the product's look and feel.

At this stage, Travel Buddy has completed discovery (hypotheses, survey, interviews), definition (personas, competitor research, solution pool), and ideation (E2E user flow, card sorting IA). The prototype translates those outputs into interactive screens that can be tested. Each screen in this prototype directly traces back to at least one solution from `07_Solution_Pool.md`.

The four flows prototyped here follow the happy path convention (Patton, 2014, as cited in Dippner, 2022, p. 171): they assume a motivated user with no errors. Edge cases and empty states are noted but not prototyped in this first iteration.

---

## 2. Design Direction & Design System

> **Visual reference:** Photography-forward travel app with clean white content screens, bold editorial typography, lime-green accent, dark bottom navigation bar, and topographic map motifs. Inspired by modern travel app aesthetics (Airbnb 2024, Wanderlog, Polarsteps).

---

### 2.1 Colour Tokens

| Token | Hex | Usage |
|-------|-----|-------|
| `--primary` | `#5DB85C` | Primary CTAs, active icon fill, verified badges |
| `--primary-lime` | `#C4E03A` | Active nav indicator pill, highlighted chips |
| `--primary-dark` | `#3A7A39` | Pressed CTA state, dark overlays |
| `--nav-bg` | `#1C1C2E` | Dark bottom navigation bar background |
| `--surface` | `#FFFFFF` | Cards, bottom sheets, modals, content screens |
| `--bg` | `#F7F7F7` | Screen background (very light warm grey) |
| `--input-bg` | `#F0F0F0` | Search bars, text inputs, inactive filter chips |
| `--text` | `#111111` | Primary headlines and body text |
| `--text-secondary` | `#555555` | Subtitles, captions, secondary info |
| `--text-light` | `#999999` | Placeholder text, disabled states |
| `--text-on-dark` | `#FFFFFF` | Text on photo overlays, dark nav icons |
| `--border` | `#EBEBEB` | Card outlines, dividers (very light) |
| `--overlay` | `linear-gradient(to top, rgba(0,0,0,0.65) 0%, transparent 60%)` | Photo card gradient for text legibility |
| `--success` | `#5DB85C` | Verified badge, confirmed states (same as primary) |
| `--warning` | `#F5A623` | Crowd signal high, caution |
| `--danger` | `#E74C3C` | Safety flags, report/block, errors |
| `--star` | `#F5C518` | Ratings, star icons |

---

### 2.2 Typography

**Font:** DM Sans (primary) — geometric, friendly, readable at small sizes. Fallback: Inter, SF Pro Text.

| Role | Size | Weight | Line height | Usage |
|------|------|--------|-------------|-------|
| Display hero | 32–38px | 800 | 1.1 | Splash headlines ("Unveil The Travel Wonders") |
| Screen title | 24px | 700 | 1.2 | Top bar titles, section openers |
| Section header | 18px | 600 | 1.3 | "Find your favorite place", "Popular Destinations" |
| Card title | 16px | 600 | 1.3 | Tip card names, place names on photo overlays |
| Body | 14px | 400 | 1.5 | Description text, detail paragraphs |
| Caption | 12px | 500 | 1.4 | Stats labels, traveler metadata, timestamps |
| Button | 15px | 600 | 1 | All CTA and button text |
| Tab label | 10px | 500 | 1 | Bottom nav labels |
| Chip / tag | 13px | 500 | 1 | Filter chips, category pills |

---

### 2.3 Spacing System

Base unit: **4px**

| Token | Value | Common use |
|-------|-------|------------|
| `--space-xs` | 4px | Icon gaps, tight chip padding |
| `--space-sm` | 8px | Between related elements |
| `--space-md` | 16px | Card padding, section gaps |
| `--space-lg` | 24px | Screen horizontal padding |
| `--space-xl` | 32px | Between major sections |
| `--space-2xl` | 48px | Hero areas, large vertical gaps |

---

### 2.4 Border Radius

| Element | Radius |
|---------|--------|
| Photo cards (large) | 20px |
| Standard cards | 16px |
| Bottom sheets | 24px top corners only |
| CTA buttons | 50px (fully pill-shaped) |
| Filter chips / tags | 50px (pill) |
| Input fields | 14px |
| Floating action buttons | 50% (circle) |
| Stats badges | 8px |
| Avatar thumbnails | 50% |
| Map memory pins | 12px |

---

### 2.5 Shadow System

| Level | Value | Usage |
|-------|-------|-------|
| Card | `0 2px 12px rgba(0,0,0,0.08)` | Standard cards, trip cards |
| Sheet | `0 -4px 28px rgba(0,0,0,0.14)` | Bottom sheets sliding up |
| Float | `0 4px 16px rgba(0,0,0,0.18)` | FABs, floating action buttons |
| Nav | `0 -1px 0 rgba(0,0,0,0.06)` | Bottom nav separator |
| None | — | Full-bleed photo screens (no card shadow needed) |

---

### 2.6 Key UI Patterns (from visual reference)

**1. Full-bleed photo splash**
Full-screen travel photography · Dark gradient overlay at bottom 40% · White display text · Pill CTA button in `--primary` green · Location tag in small caps above title.

**2. Photography card with overlay**
Rounded card (20px) · Full-bleed photo · Gradient overlay · Place name in white bold · Rating badge (star + score) bottom-left · Heart/save icon top-right.

**3. Horizontal scrolling card row**
Section label "View All" link right-aligned · Cards at ~48% screen width · Horizontal scroll · Cards slightly cut off to signal scrollability.

**4. Filter chip row**
Horizontal scrollable · Active chip: `--primary` green fill + white text + optional icon · Inactive: `--input-bg` grey fill + dark text · Pill-shaped (50px radius).

**5. Dark bottom navigation bar**
Background `--nav-bg` `#1C1C2E` · Icon-only OR icon + label · Active tab: lime pill `--primary-lime` behind icon · Inactive icons: white at 50% opacity · Height 72px + safe area.

**6. Topographic map aesthetic**
Used on splash / memory screens · Contour lines in very light grey `#E8E8E8` on white · Photo thumbnail pins floating on map · Creates depth without competing with content.

**7. Stats strip**
Row of 3 stats: icon · value (bold) · label (muted) · Separated by light dividers · Used on place detail screens (Duration · Distance · Reviews).

**8. Segment tab control**
3 options (Details / Route / Reviews) · Pill-shaped container · Active tab: white filled pill on grey background · Sits below stats strip.

**9. Floating circular buttons**
Back arrow: white circle `40px` with shadow · Favourite/heart: white circle overlaid on photo top-right · `--float` shadow level.

**10. Stacked card fan**
2–3 cards stacked with slight rotation and scale offset · Tap to expand into horizontal/list view · Used for trip planning or destination browse.

---

### 2.7 Bottom Navigation Structure

*(Based on hypothesised IA — update labels after card sort results from `09_Card_Sorting_IA.md`)*

| Tab | Icon | Label | Active indicator | Primary screens |
|-----|------|-------|-----------------|-----------------|
| 1 | 🏠 Explore | Explore | Lime pill | S10–S15 |
| 2 | 🧭 Compass | Plan | Lime pill | S16–S21 |
| 3 | ➕ Plus | — (centre FAB) | — | Quick save / add trip |
| 4 | 🤍 Favourite | Connect | Lime pill | S22–S26 |
| 5 | 💬 Message | Journal | Lime pill | S27–S31 |

> **Note:** Centre tab (➕) is a floating action shortcut for quick-adding a place — consistent with the reference app pattern. Profile lives in the top bar (avatar icon) rather than a 6th tab.

---

### 2.8 Imagery & Photography Direction

- **Hero images:** Aerial / drone shots of destinations — coastlines, city grids, forests
- **Card thumbnails:** Eye-level authentic travel photography — markets, streets, nature, food
- **Mood:** Lush, saturated but natural — no heavy filters, no stock clichés
- **Overlay:** Always use `--overlay` gradient token on photos that carry text
- **Memory pins:** Circular thumbnail crops of actual trip photos, pinned to topo map
- **Avatars:** Real-looking traveler portraits, circular crop

---

## 3. Screen Inventory

32 screens across 4 flows. Each screen maps to at least one solution ID.

### Flow A — Onboarding (9 screens)

| Screen | ID | Name | Solutions covered | Key UI elements |
|--------|----|------|-------------------|-----------------|
| 1 | S01 | Splash / Welcome | A4 | Full-bleed travel photo, "Explore without signing up" ghost button + "Get started" primary CTA |
| 2 | S02 | Guest Discovery Feed | A4 | Tip feed in read-only state · Soft sign-up nudge banner at top · No save/connect actions |
| 3 | S03 | Sign-up Gate | A1, A4 | Bottom sheet triggered when guest tries to save · "It's free — always" message · Sign up / Continue browsing |
| 4 | S04 | Onboarding Q1 — Travel style | A5 | Q1/3 progress · "How do you like to travel?" · 4 style chips (Relaxed / Exploratory / Cultural / Adventure) |
| 5 | S05 | Onboarding Q2 — Interests | A5 | Q2/3 progress · "What matters most on a trip?" · Multi-select interest chips (Food / Art / Nature / Local life / etc.) |
| 6 | S06 | Onboarding Q3 — Home city | A5 | Q3/3 progress · "Where are you based?" · City search input + skip option |
| 7 | S07 | Free Access Confirmation | A1, A2 | "You're in" celebration screen · Highlight 3 core value props · "Start exploring" CTA |
| 8 | S08 | Personalised First Moment | A2 | Personalised tip card based on Q1–Q3 answers · "We picked this for you" label · Visual wow moment |
| 9 | S09 | Location Controls | A3 | "What can Travel Buddy see?" · Toggle list: Location while using / Background / Never · Plain-language explanation of each |

---

### Flow B — Discovery & Planning (12 screens)

| Screen | ID | Name | Solutions covered | Key UI elements |
|--------|----|------|-------------------|-----------------|
| 10 | S10 | Discovery Feed | D1, D2 | Full-width tip cards · Traveler avatar + name + style tag · "Why this tip" context line · Save icon |
| 11 | S11 | Tip Detail | D1, D3, D4, D5 | Full-screen tip · Video snippet autoplay (D4) · Crowd signal badge (D3) · Safety note (D5) · Save + Share CTAs |
| 12 | S12 | Filter Panel | D2 | Bottom sheet · "Travel style" chips · "Trip type" chips · "When" selector · Apply button |
| 13 | S13 | Crowd Signal View | D3 | Tip card with crowd meter (1–5 bars) · "Mostly tourists" / "Local favourite" label · Historical trend note |
| 14 | S14 | Video Snippet Player | D4 | Full-screen vertical video · Swipe up for tip detail · Mute toggle · Creator credit overlay |
| 15 | S15 | Safety Context Panel | D5 | Bottom sheet on tip · "Safety notes from recent travelers" · Colour-coded recency · Contribute note option |
| 16 | S16 | Save to Shortlist | P3 | Bottom sheet · "Save to…" with existing trips + "New trip" · Confirmation tick animation |
| 17 | S17 | AI Itinerary Import | P6 | Paste text area · "Paste your ChatGPT / Gemini itinerary" · Parse preview showing detected places · "Import" CTA |
| 18 | S18 | Trip Shortlist — List View | P1, P3 | Trip header · Draggable shortlist cards · Status chips (To visit / Saved / Done) · Add manually button |
| 19 | S19 | Trip Shortlist — Map View | P2 | Full-screen map · Pins for saved places · Tap pin = mini card · List toggle button |
| 20 | S20 | Companion Invite | P5 | "Plan together" screen · Invite via link / contact · Permissions (View / Edit) · Active collaborators list |
| 21 | S21 | Offline Mode | P4 | Offline banner · "Your shortlist and map are available offline" · Cached content visible · Sync indicator |

---

### Flow C — Connect (5 screens)

| Screen | ID | Name | Solutions covered | Key UI elements |
|--------|----|------|-------------------|-----------------|
| 22 | S22 | Local Browse | C2 | Grid of local profiles · Interest-match % badge · Location tag · "Say hello" button |
| 23 | S23 | Local Profile Detail | C1, C2, C3 | Avatar + verified badge (C1) · Interest tags (C2) · "Free exchange" label (C3) · Recent tips they've shared · Message CTA |
| 24 | S24 | Reciprocal Exchange Intro | C3 | Contextual explainer shown before first message · "This is free — no fees, no tours" · Community guidelines link |
| 25 | S25 | Message Thread | C4, C5 | In-app chat UI · Message bubbles · "Share a tip" shortcut · Report / block ⋯ menu (C5) |
| 26 | S26 | Report / Block Modal | C5 | "Report [name]" sheet · Reason selection · "Block & remove" option · Confirmation state |

---

### Flow D — Journal & Memory (6 screens)

| Screen | ID | Name | Solutions covered | Key UI elements |
|--------|----|------|-------------------|-----------------|
| 27 | S27 | Auto-Capture Indicator | J1 | Subtle status bar pill "📍 Capturing your trip" · Tap = control sheet · Pause / Stop options |
| 28 | S28 | Journal Auto-Generated | J2 | "Your trip to [City] is ready" push notification state · Full journal layout with map header · Photo grid · Timeline |
| 29 | S29 | Journal Private View | J3 | Journal screen with 🔒 "Only you can see this" badge · Edit button · Share CTA at bottom |
| 30 | S30 | Share Options | J4 | Bottom sheet · "Share with specific people" · Contact picker · "Copy link" (view-only) · NOT public posting |
| 31 | S31 | Memory Layer — Past Trips | J5 | "Your travels" screen · Trip cards sorted by date · Search bar · Filter by city / year |
| 32 | S32 | Past Trip Detail | J5 | Individual archived trip · Map trace · Day-by-day breakdown · "Places I loved" shortlist |

---

## 4. Prototype Flows (Screen Connections)

### Flow A — Onboarding
```
S01 → [Explore without account] → S02 → [Try to save] → S03 → [Sign up] → S04 → S05 → S06 → S07 → S08 → S09 → S10
S01 → [Get started] → S04 → S05 → S06 → S07 → S08 → S09 → S10
```

### Flow B — Discovery & Planning
```
S10 → [Tap tip card] → S11 → [Save] → S16 → S18
S10 → [Filter] → S12 → [Apply] → S10
S11 → [Video] → S14 → [Back] → S11
S11 → [Safety] → S15 → [Back] → S11
S11 → [Crowd signal] → S13 → [Back] → S11
S18 → [Map view] → S19 → [List view] → S18
S18 → [Invite] → S20
S18 → [Import AI] → S17 → [Import] → S18
S18 → [Offline] → S21
```

### Flow C — Connect
```
S22 → [Tap profile] → S23 → [Message] → S24 → [Continue] → S25
S25 → [⋯ menu] → S26
```

### Flow D — Journal & Memory
```
[Active trip] → S27 → [Trip ends] → S28 → S29
S29 → [Share] → S30
S31 → [Tap trip] → S32
```

---

## 5. Component Inventory

Components needed across all 32 screens. Build once, reuse everywhere.

### Navigation
- `BottomNavBar` — 5 tabs, active/inactive states
- `TopBar` — title + optional back arrow + optional action icon
- `StatusBarSafe` — status bar + safe area padding

### Cards & Tiles
- `TipCard` — traveler avatar · tip title · style tag · crowd signal · save icon
- `TripCard` — trip name · destination · date · status pill
- `LocalProfileCard` — avatar · verified badge · name · interest tags · match %
- `JournalCard` — trip thumbnail · city · date range · lock/share state

### Inputs & Controls
- `SearchBar` — with clear button and cancel
- `ChipSelector` — single and multi-select variants
- `ToggleRow` — label + description + toggle
- `TextAreaInput` — for AI import paste
- `CitySearchInput` — with autocomplete suggestions

### Overlays & Sheets
- `BottomSheet` — drag handle · title · content slot · CTA button
- `Modal` — overlay + centred card (report/block)
- `Toast` — success · error · info variants (bottom of screen)
- `NudgeBanner` — soft sign-up prompt (dismissable)

### Indicators & Badges
- `VerifiedBadge` — ✓ icon + "Verified" label
- `CrowdMeter` — 1–5 bar visual + label
- `SafetyBadge` — colour-coded recency dot
- `MatchBadge` — "87% match" chip
- `CapturePill` — "📍 Capturing" status bar element
- `OfflineBanner` — "You're offline · Saved content available"

### Media
- `VideoPlayer` — full-screen · mute toggle · swipe hint
- `MapView` — pin clusters · mini-card on tap
- `PhotoGrid` — 1 hero + 2×2 grid layout for journal

---

## 6. Content Placeholders

Use these placeholder values for high-fidelity screens so they feel real without needing live data.

| Placeholder | Value to use |
|-------------|--------------|
| User name | Aisha M. |
| Destination | Chiang Mai, Thailand |
| Local name | Niran K. · Bangkok |
| Tip title | "The night market locals actually go to" |
| Tip author | "Solo traveler · Cultural style · 4 trips/yr" |
| AI import paste | Pre-filled ChatGPT itinerary sample (3 days, 6 places) |
| Journal title | "Chiang Mai — March 2026" |
| Companion | Ji-yeon + 1 other |
| Match % | 87% |

---

## 7. Build Instructions for the AI coding tool

When ready to build, use this prompt structure for each screen group:

> "Build a high-fidelity mobile HTML prototype screen for Travel Buddy. Design system: font DM Sans (Google Fonts); primary green `#5DB85C`; lime accent `#C4E03A`; dark nav bar `#1C1C2E`; background `#F7F7F7`; surface white `#FFFFFF`; input bg `#F0F0F0`; text `#111111`; secondary text `#555555`; border `#EBEBEB`. Mobile viewport 390×844px. Cards 20px radius, buttons fully pill-shaped (50px radius), inputs 14px radius, floating buttons circular. Photo cards use full-bleed imagery with dark gradient overlay for text. Bottom nav is dark (`#1C1C2E`) with active lime pill indicator. Use real travel photography placeholder URLs (Unsplash). Build: **[Screen name]** — [description from screen inventory]. Include: [specific UI elements from screen row]. No Lorem Ipsum — use the Chiang Mai / Aisha M. placeholder content from Section 6."

**Build order (dependency-first):**
1. Shared components (BottomNavBar dark, TopBar, TipCard, FloatingBtn) — establishes the visual language
2. Flow A: S01 Splash → S04–S06 Onboarding questions → S07 Confirmation → S09 Location controls
3. Flow B: S10 Discovery feed → S11 Tip detail → S18 Shortlist → S19 Map view → S17 AI import
4. Flow C: S22 Local browse → S23 Profile detail → S25 Message thread
5. Flow D: S28 Journal generated → S29 Private view → S31 Memory layer

---

## 8. Usability Testing Hook

Once screens are built, this prototype will be used for usability testing. Prepare these 5 tasks to test with participants:

| Task | Screen entry | Success signal |
|------|-------------|----------------|
| 1. Find a local food tip in Chiang Mai and save it to a trip | S10 | Reaches S18 with saved item |
| 2. Import a ChatGPT itinerary into your trip plan | S18 | Completes S17 import flow |
| 3. Message a local named Niran for a restaurant recommendation | S22 | Reaches S25 with message sent |
| 4. Find where your auto-generated journal for Chiang Mai is | S31 | Opens S29 |
| 5. Share your journal privately with Ji-yeon | S29 | Reaches S30 with contact selected |

---

## 9. Checklist

- [ ] Design tokens confirmed (update after card sort if IA changes nav labels)
- [ ] Components built (Section 5)
- [ ] Flow A screens S01–S09 built and linked
- [ ] Flow B screens S10–S21 built and linked
- [ ] Flow C screens S22–S26 built and linked
- [ ] Flow D screens S27–S32 built and linked
- [ ] All prototype flows connected (Section 4)
- [ ] Usability test tasks written and tested (Section 8)
- [ ] Prototype exported / hosted for participant access

---

## References

- Dippner, D. (2022). *User Experience Design – Principles & Methods.* SRH Fernhochschule.
- Patton, J. (2014). *User Story Mapping.* O'Reilly Media. (as cited in Dippner, 2022, p. 171)
- `07_Solution_Pool.md` — all 26 solutions mapped to screens
- `08_E2E_User_Flow.md` — flow connections and happy path reference
- `06_User_Personas.md` — placeholder content and persona context
- `09_Card_Sorting_IA.md` — IA structure (update bottom nav labels post-sort)
