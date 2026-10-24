# UI Brief — Storefront Purchase Flow (Cart → Checkout → Order Tracking)

**Product:** JTL-Shop 6.0 storefront · **Brand used in mockups:** L'alouette · **Scope:** B2C, MVP only
**Version:** 2.1 · 16 Sep 2026 · supersedes v1.0 · **all copy in English** (see §7.10)
**Source of truth:** the two existing storefront designs (Home, Category/PLP), `1 discovery/JTL_Shop_6.0_Pflichtenheft_EN.md`, `2 define/breakpoint grid spacing/storefront-layout-system.md`, `2 define/breakpoint grid spacing/typography-spec-handoff.md` (v2), `2 define/ARC-17 Theme & Preset System.md`

---

## 0. What changed in v2, and why

v1 was written before the existing storefront screens were available, so it invented a placeholder visual system. The Home and Category pages settle almost all of it. **The purchase flow is no longer a design from scratch — it is an extension of a storefront that already exists.** Nine things change:

| | v1 assumed | The screens show | Effect on the flow |
|---|---|---|---|
| Brand | "Lili", unnamed look | **L'alouette** — orange header, navy footer, white page | Header/footer are fixed chrome, not a choice |
| Ground | Grey canvas `#F6F8F9` | **White** page, grey only for image blocks | Cart/checkout panels sit on white |
| Surfaces | Everything a bordered, shadowed card | **Flat** — product cards have no border, no shadow, no radius on the image block | Cards must earn a border; line items use dividers |
| Primary button | Brand blue | **Navy/near-black fill** (`Apply`); orange is chrome, not an action colour | CTA is dark, not orange |
| Prices | `€89.90` | **`€ 129,00`** on the live screens — German format | Drawn here as **`€129.00`**: this brief is English throughout, number format included (§7.10) |
| Unit price | My addition | **Already shipping** (`€ 5,16 / 100ml`), and `Grundpreise` is a footer link | Not a new requirement — match the existing line |
| Compare-at | Not designed | **`€ 149,00` struck through** + red `SALE` badge | Cart must carry both |
| Wishlist | "Out of scope, not MVP" | **Heart on every product card** | Contradiction to resolve (G7 below) |
| Copy language | English throughout | **English UI labels, German chrome and legal** (`SUCHE · KONTO · WARENKORB`, `Widerrufsrecht`, `Grundpreise`) | Flow is **English throughout** — the German chrome needs an English translation set (§7.10) |

Everything in §1 (artboards), §4 (screens), §4b (states) and §6–§8 stands. §2, §3 and §5 are rewritten.

---

## 0.1 How to use this file

Feed this whole file to Claude Design. It is self-contained — every token value, every string of UI copy, and every piece of sample data needed to draw the screens is written out below. Do not invent products, prices, or labels; use §5.

**Produce:** one pan/zoom canvas, artboards laid out left → right in flow order, desktop row on top, mobile row beneath, state variants on their own page.

**Fidelity:** high-fidelity UI matching the two existing screens, not wireframe. **Anything the Home or Category page already solves — header, footer, product card, button, badge, breadcrumb, sort control, pagination, filter controls — is copied, not redesigned.** New UI extends that vocabulary.

**Do not design:** admin/merchant screens, PLP, PDP, B2B surfaces, gift vouchers. Those are out of scope (§8).

---

## 1. Artboard list

| # | Artboard name | Viewport | Canvas size |
|---|---|---|---|
| A1 | Cart — Desktop | Desktop 1440 | 1440 × 1240 |
| A2 | Checkout · Identify — Desktop | Desktop 1440 | 1440 × 940 |
| A3 | Checkout · Address & Delivery — Desktop | Desktop 1440 | 1440 × 1300 |
| A4 | Checkout · Payment — Desktop | Desktop 1440 | 1440 × 1200 |
| A5 | Checkout · Review & Place Order — Desktop | Desktop 1440 | 1440 × 1400 |
| A6 | Order Confirmation — Desktop | Desktop 1440 | 1440 × 1200 |
| A7 | Account · Order Detail & Tracking — Desktop | Desktop 1440 | 1440 × 1350 |
| B1–B7 | Same seven screens — Mobile | Mobile 390 | 390 × (content) |
| S1 | Empty cart | Desktop 1440 | 1440 × 820 |
| S2 | Order submission blocked (ERP unreachable) | Desktop 1440 | 1440 × 980 |
| S3 | Payment declined | Desktop 1440 | 1440 × 980 |
| S4 | Price / stock changed since you added it | Desktop 1440 | 1440 × 1120 |
| S5 | Guest order lookup | Desktop 1440 | 1440 × 820 |

Mobile artboards use the Compact type mode (§2.2). Desktop artboards use Default.

---

## 2. Design system — taken from the live screens

### 2.1 Grid, spacing, containers

| Tier | Viewport | Columns | Gutter | Margin |
|---|---|---|---|---|
| Mobile | 360–767 | 4 | 16 | 16 |
| Tablet | 768–1023 | 8 | 16 | 24 |
| Desktop | 1024–1439 | 12 | 24 | 32 |
| Wide | 1440+ | 12 | 24 | 48 |

- **Desktop artboards (1440):** 12 columns, 24px gutter, content max-width **1200px**, centered → 8-col column = 792px, 4-col = 384px.
- **Mobile artboards (390):** 4 columns, 16px gutter, 16px side margin.
- **Spacing scale (only these values):** XS 4 · S 8 · M 16 · L 24 · XL 32 · XXL 48 · XXXL 64.
- Section padding 24 mobile / 32 desktop / 48 wide. Inline gap 8.
- **Sidebar + content** is an established pattern on the Category page (filter rail ≈ 3 columns, content ≈ 9). Reuse it verbatim for the account area on A7.

### 2.2 Typography — v2, 12 tokens, face Inter

| Token | Default (≥1024) | Compact (<1024) | Line height | Weight | Tracking |
|---|---|---|---|---|---|
| `display` | 56 | 40 | 1.10 | 700 | −0.02em |
| `h1` | 40 | 32 | 1.15 | 700 | −0.02em |
| `h2` | 32 | 24 | 1.20 | 700 | −0.02em |
| `h3` | 24 | 18 | 1.30 | 600 | 0 |
| `h4` | 18 | 16 | 1.40 | 600 | 0 |
| `body` | 16 | 16 | 1.60 | 400 | 0 |
| `body-sm` | 14 | 14 | 1.50 | 400 | 0 |
| `caption` | 12 | 12 | 1.40 | 400 | 0 |
| `label` | 14 | 14 | 1.40 | 600 | 0 |
| `cta` | 16 | 16 | 1.20 | 600 | 0 |
| `price-m` | 24 | 24 | 1.20 | 700 | 0 |
| `price-s` | 16 | 16 | 1.30 | 600 | 0 |

Hard rules, all of them visible in the two screens:
- Product title is `h3` semibold; price is a **bold** `price-s` on cards, `price-m` for the cart total.
- Every price, quantity, order number and date uses `tabular-nums`.
- Input text and placeholders 16px minimum.
- Nothing below 12px. `SALE`, facet counts and the `Slot` chip are `caption`.
- Badges/overlines: `caption` + uppercase + +0.08em tracking + 600.
- Compare-at price: `price-s` + strikethrough + muted.

### 2.3 Colour — read off the live screens

Approximate values sampled visually. **Confirm the exact hex against the Figma file before build; the names are what matters, because ARC-17 makes them theme-owned tokens.**

| Token | Value | Where it appears |
|---|---|---|
| `--color-brand` | `#E85C24` (orange) | Header bar only. **Chrome, not an action colour** |
| `--color-ink` | `#111827` | Primary text, footer ground, primary button fill |
| `--color-ink-muted` | `#6B7280` | Secondary text, facet counts, delivery line |
| `--color-surface` | `#FFFFFF` | Page ground, inputs, cards |
| `--color-subtle` | `#F3F4F6` | Product image block, active sidebar row, newsletter band |
| `--color-line` | `#E5E7EB` | Dividers, input borders, facet separators |
| `--color-line-strong` | `#D1D5DB` | Secondary button border, range-slider track |
| `--color-sale` | `#E1352B` | `SALE` badge, compare-at price |
| `--color-success` | `#1F7A4D` | In stock, paid, delivered |
| `--color-warning` | `#B4541C` | Low stock, changed price, action needed |
| `--color-danger` | `#B3261E` | Errors, declined payment, blocked submission |

**Two rules the screens establish and the flow must not break:**

1. **Orange is the header and nothing else.** No orange buttons, links or highlights. The primary button is `--color-ink` filled with white text (as `Apply` on the Category page). Secondary is white with a `--color-line-strong` border (`Clear all`).
2. **Flat by default.** Product cards have no border, no shadow, and no radius on the image block. Reserve a border for panels that genuinely enclose a decision — the order summary, the selected delivery/payment option. Radii: button 6 · input 6 · badge 3 · pill 999. One elevation level, used only on the mobile sticky bar.

### 2.4 Components — reuse before you draw

Already solved on the two screens. Copy them:

Announcement bar · orange header (desktop nav + `SUCHE · KONTO · WARENKORB`, cart badge) · navy footer (4 link columns + legal row) · breadcrumb · page title + description block · product card (1:1 image block, `SALE` badge, wishlist heart, `Slot` chip, title, price + compare-at, unit price, delivery line) · sort select · view toggle (grid/list) · checkbox + count · colour swatch · range slider · pagination (`Previous 1 2 3 … Next`, `Showing 1–8 of 28`) · primary/secondary buttons · sidebar tree with expand chevrons and an active row.

New for this flow, drawn in the same vocabulary: quantity stepper · cart line item · order summary panel · step indicator (4 steps) · text input with label/helper/error · radio card (delivery + payment) · address card · alert banner (info / warning / error) · order timeline (5 nodes) · empty state.

Touch targets ≥44px. Visible focus ring on every control: 2px `--color-ink`, 2px offset.

### 2.5 The `Slot` chip

The dashed `Slot` chips on the product cards are the theme's slot-based composition model (Pflichtenheft §8.10) surfacing in the design. Decide before build whether cart, checkout and confirmation carry slots too — and if so, where. Draw them only where a merchant is genuinely allowed to insert content: a trust/USP slot under the cart summary and one under the confirmation total are the safe candidates. **Checkout steps 2–5 should carry no slots** — merchant content inside a payment flow is exactly the kind of override the spec forbids (§6.6).

---

## 3. Global chrome

**Announcement bar** (A1, A6, A7, S1, S4, S5): full-width, `--color-ink`, white `caption`, centred: "Free shipping on orders over €75.00 · Shop now". This is a promise the flow must honour — see the shipping figures in §5.

**Storefront header**: `--color-brand` orange, 64px desktop / 56px mobile. Logo "L'alouette" white, left. Nav centred: `All products · Backpacks · Bags · Accessories · Collections · Sale`. Right: search, account, cart icons in white, cart with a count badge, plus the `SEARCH · ACCOUNT · CART` label row at wide width.

**Checkout header** (A2–A6): same orange bar, but **nav, search and cart removed** — logo left, "Need help?" and a lock icon + "Secure checkout" right. The reduction is deliberate: nothing competes with the flow. Keep the orange so the buyer never feels they left the shop.

**Step indicator** (A2–A5), directly under the header on white: `1 Identify · 2 Delivery · 3 Payment · 4 Review`. Completed steps clickable with a check, current in `--color-ink` bold, later steps muted. Mobile: `Step 2 of 4 · Delivery` plus a progress bar.

**Footer** (A1, A6, A7, S1, S5 — never inside checkout): `--color-ink` navy, four columns matching the live screens, translated — **Shop** (All products, Backpacks, Bags, Accessories, Sale) · **Service** (Contact, Shipping, Returns, Size guide, FAQ) · **Company** (About us, Careers, Sustainability, Press) · **Contact** (info@lalouette.de, +49 30 1234 5678, Berlin, DE). Legal row below a hairline: `Legal notice · Terms & Conditions · Right of withdrawal · Privacy policy · Cookie policy · Unit pricing`, then `© 2026 L'alouette. All rights reserved.`

---

## 4. Screens

Each screen lists **purpose → layout → sections → copy → annotations**. Annotations sit beside the artboard in `caption`, prefixed `NOTE:`.

---

### A1 · Cart

**Purpose:** let the buyer verify what they are about to buy and the real cost, and move to checkout without hesitation.

**Layout (desktop):** breadcrumb `Home / Shopping cart`; `h1` "Shopping cart" with a one-line description beneath it (the pattern the Category page uses for "Backpacks"); then 8 columns of line items + a 4-column order summary, sticky.
**Layout (mobile):** single column; summary collapses into a sticky bottom bar with the total and the CTA.

**Sections**

1. **Line items** — one row per item, separated by `--color-line` dividers, **not boxed individually**. Each row: 1:1 image block 96×96 on `--color-subtle` · title (`h3`) · variant line (`body-sm`, muted) · availability badge · delivery line reusing the card wording, "Delivered in 2–3 working days" · quantity stepper · `Remove` link · price right-aligned, with the struck compare-at beneath it where the item is on sale, and the unit price beneath that where the item is sold by weight.
2. **`SALE` badge** carries over from the product card onto any discounted line — same red, same size.
3. **Order summary card** (one of the few bordered panels): Subtotal · Shipping · VAT (included) · divider · **Total** in `price-m`. Shipping reads **"Free"** with a `caption` beneath: "Free over €75.00" — the announcement bar's promise, kept.
4. **Primary CTA** "Proceed to checkout", `--color-ink` fill, full width, 52px.
5. **Discount code** — collapsed row above the CTA *(pending: see G5)*.
6. **Under the CTA** — the payment marks row and "Free returns within 30 days".
7. **Continue shopping** link under the items.

**Annotations**
- `NOTE: Session-bound page. Not indexed, no CDN HTML cache (§8.9 Table 16).`
- `NOTE: Price and stock here come from an ERP projection and may lag. Binding figures are confirmed at A5 (§8.16).`
- `NOTE: MVP has no cart-preview overlay, so this page carries all add-to-cart feedback alone.`
- `NOTE: Reuses the product card's own price block — price, struck compare-at, unit price, delivery line — so the figures read identically to the PLP the buyer just came from.`

---

### A2 · Checkout · Identify

**Purpose:** get past the account question in one screen without making guest feel punished.

**Layout:** centred single column, max 560px.

1. `h2` "How would you like to continue?"
2. **Guest card first**, equal visual weight: `h3` "Continue as guest" · email input with helper "We'll send your order confirmation and delivery updates here." · primary "Continue as guest".
3. Divider with `caption` "or".
4. **Sign in card**: email, password with a `Show` toggle, "Forgot password?", primary "Sign in", then "Continue with Google" / "Continue with Apple" as secondary buttons.
5. "New here? Create an account".

**Annotations**
- `NOTE: Guest checkout is a per-shop merchant setting — draw the variant with the guest card removed.`
- `NOTE: Social login and MFA are MVP scope (§9.1).`

---

### A3 · Checkout · Address & Delivery

**Layout:** 8 columns form + 4 columns sticky summary.

1. `h2` "Delivery address" — fields in DE postal order: First name · Last name · Company (optional) · Street and house number · Address line 2 (optional) · Postcode · City · Country (default Germany) · Phone (optional, "Only for delivery questions").
2. Checkbox "Billing address is the same as delivery address", checked by default; unchecking reveals a second group.
3. `h2` "Delivery method" — radio cards: name (`label`), arrival in bold, price right:
   - "Standard · DHL" — "Arrives Fri, 18 Sep – Tue, 22 Sep" — **Free**
   - "Express · DHL" — "Arrives Thu, 17 Sep" — **€9.95**
   - "Pickup station" — "Arrives Fri, 18 Sep – Tue, 22 Sep" — **Free**, with "Choose station"
4. **Delivery-time update banner** above the methods once the address is entered: "Delivery estimate updated for 10999 Berlin." The spec requires address-based delivery calculation; this is where the buyer sees it happen.
5. Primary "Continue to payment"; tertiary "Back to cart".

**Annotations**
- `NOTE: Delivery options, costs and dates come from the ERP/logistics layer (§6.1). The storefront displays them.`
- `NOTE: Free standard shipping is the announcement bar's promise. If the threshold is merchant-configurable, this row must render a price too — draw both.`
- `NOTE: Draw the "no delivery method available for this address" error.`

---

### A4 · Checkout · Payment

**Layout:** 8 + 4.

Radio cards, each with the consequence stated before selection:
- **PayPal** — "You'll be redirected to PayPal to confirm."
- **Credit or debit card** — "Visa, Mastercard, Amex." Selecting expands card number, expiry, CVC, name on card.
- **Purchase on account** — "Pay within 14 days of dispatch."
- **Prepayment** — "We'll ship once your bank transfer arrives."

Selected card takes a 2px `--color-ink` border. Under the group: "Your payment details are handled by our payment provider. L'alouette never sees your card number."

**Annotations**
- `NOTE: Payment runs entirely inside the storefront from the buyer's perspective, through a PSP underneath (§6.1).`
- `NOTE: The method list is merchant-configured per shop and market — data, not a fixed set.`

---

### A5 · Checkout · Review & Place Order

**Layout:** 8 + 4, summary fully expanded (no collapse on mobile).

1. `h2` "Review your order"
2. Three summary cards with `Edit` links: **Contact** · **Delivery** · **Payment**.
3. Condensed items, 48×48 image blocks, no stepper.
4. Cost breakdown ending in `price-m` total.
5. **Legal block** — checkbox "I have read and accept the Terms and Conditions and the Cancellation Policy." plus `caption` "Right of withdrawal: you may cancel within 14 days of receiving the goods." Both links go to the footer's `Terms & Conditions` and `Right of withdrawal`.
6. **Primary CTA naming the obligation:** **"Buy now — pay €366.00"**, full width, 52px.
7. `caption` beneath: "Your order is only confirmed once you see the confirmation page."
8. **Submitting state** drawn beside it: disabled, spinner, "Placing your order…".

**Annotations**
- `NOTE: HIGH RISK. The order only exists once the ERP confirms it, and in MVP the shop stores no order of its own (§8.7, §8.16, §8.19). See S2.`
- `NOTE: Button names the payment obligation, as required for DE distance selling (zahlungspflichtig bestellen).`

---

### A6 · Order Confirmation

**Layout:** centred 792px column, XXL rhythm, footer beneath.

1. Success check in `--color-success`, 48px. No illustration.
2. `h1` "Thank you, Anna." · "Your order is confirmed. We've sent the details to anna.brandt@example.de."
3. **Order reference card**: `label` "Order number", `h3` tabular "LA-2026-018472", `Copy` action.
4. **What happens next** — three numbered steps (a real sequence): prepare · tracking link by email · delivery window.
5. Read-only order summary: items, address, delivery method, payment, total.
6. **Guest block** — warning-tinted: "Save your order details … you'll need your order number together with your email to look up this order", with "Create an account to track it".
7. "Continue shopping".

**Annotations**
- `NOTE: This page already exists as a stub in the merchant admin: slug /checkout/thank-you, template "Confirmation".`
- `NOTE: The guest block is a PROPOSAL — the Pflichtenheft names no guest order-tracking surface at all.`

---

### A7 · Account · Order Detail & Tracking

**Purpose:** answer "where is my parcel" in the first screenful.

**Layout:** the Category page's sidebar + content split, reused. Sidebar (3 cols): Orders (active, `--color-subtle` row) · Addresses · Payment methods · Profile · Newsletter. Content 9 cols.

1. **Header row** — `h2` "Order LA-2026-018472" · `caption` "Placed 16 Sep 2026" · status badge "Shipped" · secondary "Download invoice (PDF)".
2. **Tracking block, first and largest** — `h3` "Arriving Fri, 18 Sep", "DHL · 00340434161094042557", "Track parcel", then a **vertical timeline**: Order placed ✓ · Payment received ✓ · Being prepared ✓ · **Shipped ● (current)** · Delivered ○ expected.
3. **Items** with a "Buy again" secondary button each.
4. Delivery / payment / totals cards.
5. "Return an item" · "Contact support".

**Annotations**
- `NOTE: Every status originates in the ERP. The storefront displays, it never owns order state (§6.1).`
- `NOTE: Spec says tracking IDs "can be made available" — not guaranteed. Draw the no-tracking-yet variant: "Tracking number will appear here once your parcel is scanned."`
- `NOTE: The orders LIST view should reuse the Category page's pagination and "Showing 1–8 of 28" pattern.`

---

## 4b. State artboards

### S1 · Empty cart
Centred: line icon, `h2` "Your cart is empty", "Items you add will appear here.", primary "Start shopping", then a **"Recently viewed" row of four real product cards** — the same card component as the PLP, which is also the honest way to fill the space.

### S2 · Order submission blocked — ERP unreachable
**The most important state in the set, and nothing in the project designs it today.** From A5, plus:
- `danger` banner: `h4` "We can't place your order right now" · "Our order system isn't responding. Nothing has been charged and your cart is saved. Please try again in a few minutes."
- CTA disabled, "Try again"; secondary "Save cart and email me when it's back".
- `caption` "No payment has been taken."
- A side panel stating what still works: Browse the shop ✓ · Your cart ✓ saved · Placing an order ✗ paused.
- `NOTE: Order placement needs ERP confirmation; if unavailable, checkout enters a controlled emergency mode and blocks submission. In MVP the shop cannot store a pending order, so there is no "awaiting confirmation" fallback (§8.7, §8.16 Table 18).`

### S3 · Payment declined
From A4. `danger` alert: "Your payment was declined — your bank declined the payment. Try another method, or contact your bank and try again." The failed method takes a `--color-danger` border and an inline reason line. Other methods stay selectable. `caption` "Your delivery details are saved."

### S4 · Price or stock changed since you added it
From A1. `warning` alert "Two items changed — prices and availability update from our warehouse. Please review before continuing." Affected rows take a warning left border plus a change line: "Price changed: €149.00 → €129.00" and "Only 1 left — quantity reduced from 2 to 1". CTA becomes "Accept changes and continue", with the previous total struck through beside the new one.

### S5 · Guest order lookup
Proposal. Centred 480px: `h2` "Track your order", order number + email inputs, primary "Find my order", "Ordered with an account? Sign in instead."

---

## 5. Sample data — use these exact values everywhere

Drawn from the live screens' own assortment (outdoor/backpacks) and their number format.

**Shop:** L'alouette · Berlin, DE · info@lalouette.de · +49 30 1234 5678
**Customer:** Anna Brandt · anna.brandt@example.de
**Address:** Anna Brandt, Oranienstrasse 12, 10999 Berlin, Germany · +49 30 1234567
**Order:** LA-2026-018472 · placed 16 Sep 2026 · DHL 00340434161094042557

**Cart contents (4 units, 3 lines)**

| # | Product | Variant | Qty | Unit price | Line total | Extras |
|---|---|---|---|---|---|---|
| 1 | Ridge 28 Daypack, ripstop shell | Colour: Black | 1 | €129.00 | €129.00 | `SALE` · compare-at €149.00 · In stock · Delivered in 2–3 working days |
| 2 | Kestrel 45 Travel Backpack | Colour: Green | 1 | €189.00 | €189.00 | In stock · Delivered in 2–3 working days |
| 3 | Trail Fuel Bars, 12 × 50 g | — | 2 | €24.00 | €48.00 | **Unit price €40.00 / kg** · Only 3 left |

**Totals:** Subtotal €366.00 · Shipping **Free** (over €75.00) · VAT 19% included €58.44 · **Total €366.00**
**Payment shown A5–A7:** Credit card · Visa •••• 4242

**Number format, everywhere:** `€129.00` — euro sign, no space, point decimal, two decimals. Dates `Fri, 18 Sep`. Order numbers and tracking numbers tabular. *(The live screens use the German `€ 129,00`; see §7.10.)*

**Imagery:** the live cards use a `--color-subtle` block with a centred image glyph and a `1:1` label. Use exactly that as the placeholder in the flow too — it is the product's own house placeholder, not a stand-in I invented.

---

## 6. Non-negotiables

1. **Do not redesign what already exists.** Header, footer, product card, buttons, badges, breadcrumb, sidebar, pagination come from the live screens unchanged. If something in the flow seems to need a new component, check the two screens first.
2. **Legal elements are part of the layout.** Unit price on weight-sold items, VAT statement, withdrawal policy, T&C acceptance, and the payment-obligation button label at full readable size. The project's own audit already found compliance elements missing from the merchant setup flow — do not repeat it on the buying flow. The footer's `Unit pricing` link is a promise the cart has to keep.
3. **Tabular figures** on every price, quantity, order number and date.
4. **Accessibility floor:** 12px minimum, inputs ≥16px, targets ≥44px, visible focus, contrast surviving 200% zoom. BFSG / EN 301 549 apply. *Check the orange header's white text and icons at AA — it is borderline and the flow inherits it.*
5. **The storefront never claims to own order state.** No screen implies the shop decides status, stock or shipping.
6. **No cart-preview overlay** in any artboard — Must-have but not MVP.

---

## 7. Open questions to surface on the canvas

1. **Voucher field in MVP?** Discount codes and gift vouchers are Must-have but unflagged for MVP. Drawn as a collapsed row, pending.
2. **Guest order tracking** — no specified surface (S5 is a proposal).
3. **Price/stock reconciliation point** — where does S4 fire?
4. **ERP-unreachable copy** — how much is the buyer told (S2)?
5. **Stock reservation during checkout** — visible hold, or silent? Drawn silent.
6. **Type mode boundary** — 1024 assumed, pending confirmation against the layout system.
7. **Wishlist is on every product card but marked non-MVP in the Pflichtenheft.** Either it ships (and the heart needs a signed-in state, an account page, and a slot in the cart's empty state) or the card drops it. Cannot stay ambiguous — the heart is on screen today.
8. **The live card shows `€ 5,16 / 100ml` on a backpack.** Grundpreis applies to goods sold by weight or volume, not to a daypack. The cart must render the unit-price line **conditionally**, and the PLP card probably should too.
9. **Do checkout pages carry theme slots?** (§2.5) Recommendation: cart and confirmation yes, checkout steps no.
10. **Copy language and locale.** The live Home page is German, the Category page's UI labels are English. **This brief and the canvas are English throughout — nav, footer, legal links and number format included.** Two things follow: the German chrome on the live screens needs an English translation set (or these artboards a German one), and the DE market legally needs German legal texts and the `€ 129,00` price format at runtime. So locale is a theme-level switch, not a copy decision — decide where it lives before build.

---

## 8. Out of scope for this canvas

PLP · PDP · search · product comparison · gift vouchers · pre-order · B2B (quick order, order lists, packaging units) · subscriptions · returns workflow beyond the "Return an item" entry point · merchant admin · theme editor · end-customer AI assistant (explicitly Phase 2).
