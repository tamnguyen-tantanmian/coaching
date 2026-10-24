# Storefront Sign-in ticket — fixes for Rovo

## Prompt for Rovo

> Update the description of the ticket "Storefront Sign-in page (Sign in, Create account, Forgot password, Set new password)" with the 5 edits below. Apply only these edits. Keep all other text, tables, statuses and formatting exactly as they are. Write in English. Where an edit says "replace", replace the quoted text word for word. Where it says "add", insert the new text at the location given.

---

## Edit 1 — "Sign in page" row is undecided → move it to Open Points

**Section:** For FE Implementation → Behaviour → Create account — after the account is created (table)

**Replace** the Result cell of the row "Sign in page":
> Auto login, or back to Sign in with the email prefilled (shopper re-enters the password)

**with:**
> Auto login → back to the previous page (pending FE confirmation, see Open Points)

**Section:** Open Points — **add** a new row:

| Issue | Output | Status |
|---|---|---|
| FE: confirm the result after Create account when the shopper came from the Sign in page — auto login, or back to Sign in with the email prefilled (shopper re-enters the password). | | Open |

---

## Edit 2 — "only banner" conflicts with the BE fallback banner

**Section:** For FE Implementation → Form rules → Errors

**Replace:**
> The only banner is the social sign-in error at the top of the form.

**with:**
> Error banners appear only at the top of the form, and only for errors that are not tied to a single field (e.g. the social sign-in error).

**Section:** Acceptance Criteria

**Replace:**
> Field errors are shown inline (red border + message under the field); the social sign-in error is the only banner

**with:**
> Field errors are shown inline (red border + message under the field); errors not tied to a single field are shown as a banner at the top of the form

---

## Edit 3 — add loading for "Create account"

**Section:** For FE Implementation → FE notes

**Replace:**
> Loading on "Send reset link" and "Save new password": reuse the Sign in loading pattern.

**with:**
> Loading on "Create account" ("Creating account…"), "Send reset link" and "Save new password": reuse the Sign in loading pattern.

---

## Edit 4 — social error copy covers both providers

**Replace every occurrence** (Social login behaviour, States table, To-do list if present):
> "Couldn't continue with Google. Please try again."

**with:**
> "Couldn't continue with {Google / Microsoft}. Please try again." — {provider} matches the button the shopper used.

---

## Edit 5 — where the shopper lands after signing in

**Section:** For FE Implementation → Behaviour → Sign in — **add** at the end:
> After a successful sign-in, the shopper returns to the page they started from (cart / checkout → cart; any other page → that page). Same logic as "Create account — after the account is created".

**Section:** For FE Implementation → Behaviour → Social login

**Replace:**
> returns them to the shop they started from.

**with:**
> returns them to the page they started from.

---

## Check after Rovo updates

- [ ] Open Points has 4 open rows (FE verification, FE Sign-in-page result, BE auto-link, BE password rule) + 2 resolved
- [ ] No sentence still says the social error is "the only banner"
- [ ] "Creating account…" appears in FE notes
- [ ] No social error copy mentions Google only
- [ ] Sign in behaviour ends with the redirect sentence
