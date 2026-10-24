# Design system notes

*Write this when you start building the prototype, in a form an AI coding tool can read. Short, concrete, no paragraph that needs interpreting.*

## Where the source of truth lives
`work/original-docs/10_Prototype_Plan.md`, section 2 (Design Direction & Design System). Prototype: `work/prototype/`.

## Tokens
- Colour: `--primary` #5DB85C (main CTA, verified badge); `--primary-lime` #C4E03A (selected nav, highlighted chip); `--primary-dark` #3A7A39 (pressed state); `--nav-bg` #1C1C2E (bottom navigation bar); `--surface` #FFFFFF; `--bg` #F7F7F7; `--text` #111111; `--text-secondary` #555555; `--border` #EBEBEB; `--warning` #F5A623 (high crowd signal); `--danger` #E74C3C (safety, report/block, errors)
- Type: DM Sans (fallback Inter, SF Pro Text). Display 32–38px/800; screen title 24px/700; section 18px/600; card title 16px/600; body 14px/400; caption 12px/500; button 15px/600
- Spacing and radius: base unit 4px (4, 8, 16, 24, 32, 48). Photo card 20px; card 16px; bottom sheet 24px (top two corners); CTA and chips are pills (50px); input 14px

## Components
| Component | States it has | Rules |
|---|---|---|
| Tip card (full-bleed photo) | default, saved | Has a crowd signal badge; text over the photo uses a gradient to reach contrast |
| Map pin | local favourite (green), popular (amber), very touristy (red) | Clusters when close together; tap to open the peek card |
| Bottom sheet | collapsed (peek), open | Used for the peek card, safety context, the sign-up gate |
| Filter chip | default, selected | A pill; must be kept as it is when the mode changes |

## Patterns
Mobile 390 × 844px. A dark bottom navigation bar, a light content background and a photo-led direction. Explore has three modes (Near Me, Country, Map) that share one filter system.

## Do and do not
- Do: let viewers browse tips without an account; ask for sign-up only on Save or Connect
- Do not: use a popularity badge; use the crowd signal instead

## Accessibility rules
See `accessibility-rules.md`. This project was not checked per component beyond the contrast requirement on photo overlays.
