# Storefront Sign-in ticket — fixes round 2 (for Rovo)

## Prompt for Rovo

> Update the description of the ticket "Storefront Sign-in page (Sign in, Create account, Forgot password, Set new password)" with the 5 edits below. Apply only these edits. Keep all other text, tables, statuses and formatting exactly as they are. Write in English. Where an edit says "replace", replace the quoted text word for word.

---

## Edit 1 — "do not reveal" conflicts with "Email already registered"

**Section:** Acceptance Criteria

**Replace:**
> Error and reset messages do not reveal whether an email has an account

**with:**
> Sign-in and reset messages do not reveal whether an email has an account (Create account intentionally shows "An account with this email already exists.")

---

## Edit 2 — only "Signing in…" is designed; the other loading states reuse it

**Section:** Acceptance Criteria

**Replace:**
> Loading states are defined for Sign in ("Signing in…"), Create account ("Creating account…"), Send reset link and Save new password

**with:**
> The Sign in loading state ("Signing in…") is designed; Create account ("Creating account…"), Send reset link and Save new password reuse the same pattern

---

## Edit 3 — confirm-field placeholder must match Figma

**Section:** For FE Implementation → Form rules → Placeholders

**Replace:**
> the confirm field on Set new password shows "Re-enter your password".

**with:**
> the confirm field on Set new password shows "Re-enter your password" (Figma to be updated to match).

> Note for Tam: if you prefer to keep "Enter your password" in Figma, change this edit to replace "Re-enter your password" with "Enter your password" instead.

---

## Edit 4 — Figma flow list in Background is outdated

**Section:** Background

**Replace:**
> The Figma section is organised as user flows (sign in, wrong email / password, forgot password, field validation, create account, set new password errors, social sign-in error), each with Desktop and Mobile frames.

**with:**
> The Figma section is organised as user flows (sign in, wrong email / password, field validation, social sign-in error, forgot password incl. set new password errors, create account, email already registered), each with Desktop and Mobile frames.

---

## Edit 5 — Testing points to the wrong section

**Section:** Testing → Testing procedure

**Replace:**
> Follow Acceptance Criteria in the For FE Implementation section.

**with:**
> Follow the Acceptance Criteria section.

---

## Check after Rovo updates

- [ ] AC "do not reveal" line now says Sign-in and reset only
- [ ] AC loading line says only Sign in is designed
- [ ] Confirm placeholder matches Figma
- [ ] Background flow list has no separate "set new password errors" and includes "email already registered"
- [ ] Testing says "Follow the Acceptance Criteria section."
