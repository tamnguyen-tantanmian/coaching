# Product and users

*AI draft (24 Oct 2026), from `work/1-discovery/` and `work/2-define/`. Not checked yet.*

## The product
JTL-Shop 6.0 is a cloud-based multi-shop SaaS shop system with headless storefronts and an API-first architecture, built on top of JTL-WaWi (the ERP that stays the central data source). A merchant runs one or more shops from an **Admin Dashboard**; the public **Storefront** is produced entirely from configuration held there, through the **Theme Editor**.

## The users
- **Shop owner** (primary): owner-operator or e-commerce manager, 1–50 employees, DACH, migrating from JTL-Shop 5.0. Described in the Pflichtenheft (§3.1) as having no technical background and depending heavily on service partners. Has just bought 6.0, products already live in WaWi, and wants a storefront that looks like the brand and can take real orders without calling a partner.
- **Shop staff** (secondary): a colleague invited into a shop someone else set up, who needs to know what is theirs to touch.
- **Shopper**: the end customer on the storefront (cart, checkout, sign-in).
- Agency / partner / developer who authors new themes: named as a separate, later persona, not in MVP scope.

## Where it stands now
- The MVP (Pflichtenheft, 31.03.2026) covers a working storefront, WaWi integration for products, stock, customers and orders, a basic customer account, checkout with shipping and payment, multiple shops with market-specific settings, and first AI-assisted features for shop design. Planned build time: six to nine months.
- Design work so far: admin and shop setup prototypes, a heuristic audit of the setup screens, journey map, problem statements and opportunity map, token specs for colour and type, the Theme Editor save/apply logic, storefront sign-in, and (newest) the AI Theme Assistant.
- No merchant has been contacted yet: every problem and opportunity is derived from the build, the Pflichtenheft and the audit.

## What success might look like
- Merchants publish only what they have been shown is ready (outcome of O1). **assumed**
- A merchant can go live without a service partner. **assumed**

## What I do not know
- Which of the two owner profiles is right: the non-technical, ROI-driven owner (§3.1) or the UX-minded target customer (§3.2). This is assumption A2.
- Any real merchant behaviour or figures: there is no research with merchants yet.
