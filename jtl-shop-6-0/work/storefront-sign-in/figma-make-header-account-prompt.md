# Figma Make prompt — Storefront Header + Account entry

Copy everything below the line into Figma Make.

---

Build a responsive storefront **Header component** for an e-commerce shop (JTL-Shop 6.0), with desktop and mobile variants, an account flyout (desktop) and a mobile menu (drawer). Use auto layout everywhere. Font: Inter. Header background: brand orange `#EE7244`, icons and nav text white. Dark UI text `#111827`, muted text `#6B7280`, borders `#D1D5DB`, surface white, page background `#F3F4F6`.

## 1. Desktop header (1440 wide, height 64)

Contents: logo placeholder, nav links (Home, Backpacks, Bags, Accessories, Collection, Deals), and on the right: Search, Account (user), Cart icons. Cart has a dark round badge with count.

Create these variants as one component set:

- `logo-ratio`: `1:1` (displayed 40×40) | `3:1` (displayed 120×40)
- `logo-align`: `left` (logo left, nav centered) | `center` (nav left, logo centered)
- `account`: `signed-out` | `signed-in` (signed-in shows a small dot or initials on the user icon)

Logo placeholder = light blue dashed box with the ratio text inside. Source assets are 144×144 (1:1) and 432×144 (3:1); display height is 40 on desktop.

States to include:
- Nav link: default, hover (underline), active/current page (white 2px underline), focus (visible focus ring)
- Icon buttons: default, hover, focus; each icon has a 44×44 tap/click area
- Cart badge: hidden when 0, `1–99`, `99+`
- Logo fallback: when no logo, show the shop name as white text

## 2. Account flyout (desktop only)

Opens on **click** of the user icon, anchored below it, right-aligned. White card, radius 12, shadow, padding 24, width ~390. Closes on click outside or Esc.

**Signed out:**
- Title "My account" (semibold 18)
- Text "Sign in to see your orders and check out faster." (muted 16)
- Primary button full width, dark `#111827`: "Sign in"
- Secondary button full width, outlined: "Create account"

**Signed in:**
- Name (semibold) + email (muted)
- Divider
- Links: "Profile", "Orders"
- Divider
- "Sign out" (text button)

## 3. Mobile header (390 wide, height 56)

**No account icon on mobile.** Account lives in the menu only. Icons: Search, Cart, Menu (hamburger). Each icon 24px inside a 44×44 tap area. Logo display height 32 (1:1 = 32×32, 3:1 = 96×32).

Variants:
- `logo-align = left`: `[logo] …… [search] [cart] [menu]`
- `logo-align = center`: `[menu] [search] …… [logo] …… [cart]`
- `menu`: `closed` (hamburger icon) | `open` (icon becomes X / close)

Search tap state: full-width search input overlay directly under the header, with a close button.

## 4. Mobile menu (drawer)

Full-height drawer sliding in from the menu side, white, with a dark scrim (40% black) over the page behind it. Tap on scrim closes it. Content scrolls if long.

Order from top:

1. **Account section** (top, so Sign in is always visible without scrolling)
   - **Signed out:** text "Sign in to see your orders and check out faster." + full-width "Sign in" (primary) + full-width "Create account" (secondary). Same copy and order as the desktop flyout.
   - **Signed in:** name + email, then links "Profile", "Orders", "Sign out".
2. Divider
3. **Categories:** Home, Backpacks, Bags, Accessories, Collection, Deals. Each row 48 high. Rows with children show a chevron and open a sub-level with a "Back" row.

On mobile, "Sign in" and "Create account" navigate to their own pages (no modal).

## 5. Frames to output

- Desktop header: all 4 logo combinations × signed-out/signed-in
- Desktop header with account flyout open: signed-out, signed-in
- Mobile header: 1:1 and 3:1 × left/center
- Mobile header with search open
- Mobile menu open: signed-out, signed-in, category sub-level
- A small states sheet: nav link states, icon button states, cart badge states, logo fallback

Label each frame clearly (e.g. "Desktop / 3:1 / left / signed-in"). Use **left** and **center** for logo alignment labels (not "right").
