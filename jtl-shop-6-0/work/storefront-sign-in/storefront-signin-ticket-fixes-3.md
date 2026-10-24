# Storefront Sign-in ticket — rewrite FE section by flow (for Rovo)

## Prompt for Rovo

> In the ticket "Storefront Sign-in page (Sign in, Create account, Forgot password, Set new password)", inside **For FE Implementation**, replace everything from the heading **"Overview"** down to and including the **"States"** table with the text under "New text" below. Keep "Entry points" above it and "Out of scope (MVP)", "Components" and everything after it unchanged. Do not change any other section. Write in English, keep the headings and bullets as given.

---

## New text

### Overview

The Sign-in page covers three flows: **Sign in**, **Forgot password** and **Create account**. Each view is a centered column (440px on Desktop, full width on Mobile). Social login (Google / Microsoft) is available on Sign in and Create account. Every state below has a Desktop (1440) and Mobile (390) frame in Figma; the account flyout is Desktop only.

### 1. Sign in

- The shopper signs in with email and password, or continues with Google / Microsoft.
- Links to Create account and Forgot password.
- **States:** default · loading ("Signing in…", form disabled) · wrong email or password (one general message, does not reveal if the email has an account) · field validation.
- **After sign-in:** the shopper returns to the page they started from (cart / checkout → cart).

### 2. Forgot password

- Reset your password → enter email → Check your inbox (neutral message, same whether or not the email has an account, with Resend email) → open the link in the email → Set a new password → back to Sign in with a "Password updated" message and the email prefilled.
- No "Back to sign in" link on Set a new password.
- **States:** reset link sent · password too short · passwords don't match · password updated.

### 3. Create account

- First name, last name, email, password, terms checkbox; link to Sign in.
- **States:** default · email already registered (with links "Sign in instead" and "reset your password", both prefill the email).
- **After the account is created:** no email verification in MVP; the shopper is signed in automatically and returns to the page they started from (cart / checkout → cart). Shoppers coming from the Sign in page: pending FE confirmation (see Open Points).

### Social login (Sign in and Create account)

- Runs through Zitadel; no account yet → account is created, account exists → shopper is signed in.
- Shopper cancels the provider popup → no error.
- Provider or network error → error banner at the top of the form ("Couldn't continue with {Google / Microsoft}. Please try again.").
- Social email matches an existing password account → pending BE (see Open Points).

### Shared rules

- All fields use the same input component (label above); password fields have a Show/Hide toggle.
- Field errors are inline; banners only for errors not tied to a single field.
- Inputs and buttons are 40px high; links are underlined; focus states are on the components page.
- Loading on Create account, Send reset link and Save new password reuses the Sign in loading pattern.

---

## Check after Rovo updates

- [ ] FE section reads: Entry points → Overview → 1. Sign in → 2. Forgot password → 3. Create account → Social login → Shared rules → Out of scope
- [ ] The four section tables and the big States table are gone
- [ ] Out of scope, Components, Acceptance Criteria unchanged
