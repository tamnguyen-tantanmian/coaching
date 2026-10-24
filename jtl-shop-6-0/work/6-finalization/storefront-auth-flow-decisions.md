# Storefront Auth Flow — Design Decisions (MVP)

Scope: Sign in, Forgot password, Create account — storefront, desktop 1440 + mobile 390.
Status: design review closed, one open item to reconfirm with FE (see "Open").

---

## 1. Sign in — DONE

**Entry points**
- Desktop: account icon in header → flyout "My account" → Sign in / Create account.
- Mobile: hamburger menu → "Account" → Sign in page (no flyout on mobile).

**States designed**
- Default
- Loading — "Signing in…" on button; fields and social buttons disabled
- Wrong email or password — inline error under password: "Email or password is incorrect. Please try again."
- Field validation — invalid email, empty password

**Out of scope (MVP)**
- Post-login screens (account page, signed-in flyout)
- Lockout / captcha after repeated failed attempts

---

## 2. Forgot password — DONE (MVP)

**Flow**
1. Sign in → "Forgot password?" → Reset your password (enter email) → "Send reset link"
2. Check your inbox — neutral message: "If an account exists for {email}, we've sent a link…" + "Resend email" + "Back to sign in"
3. Shopper opens link in email → Set a new password (no "Back to sign in" on this screen)
4. "Save new password" → redirect to Sign in with success banner "Password updated" and email prefilled

**Error states (Set a new password)**
- New password too short — "Use at least 8 characters."
- Passwords don't match — "Passwords don't match."

**FE notes**
- Loading on "Send reset link" / "Save new password": reuse the Sign in loading pattern.
- "Resend email": reuse the Check your inbox (Reset link sent) state.

**Out of scope (MVP)**
- Expired / already-used reset link
- Email validation on the Reset screen
- Resend cooldown

---

## 3. Create account — DONE pending FE reconfirm

**States designed**
- Default — first name, last name, email, password (helper "At least 8 characters."), T&C checkbox
- Email already registered — error "An account with this email already exists." + links **Sign in instead** or **reset your password** (desktop + mobile)

**After account is created — NO email verification (MVP), auto login:**

| Where the shopper came from | Result |
|---|---|
| Cart / checkout | Auto login → back to cart |
| Sign in page | Auto login, **or** back to Sign in with email prefilled (shopper re-enters password) |
| Any other page | Auto login → back to previous page |

**FE notes**
- "Sign in instead" → Sign in page with email prefilled.
- "reset your password" → Reset your password page with email prefilled.

**Out of scope (MVP)**
- Field validation error states for Create account (follow Sign in validation pattern)

---

## 4. Social login (Google / Microsoft) — shared by Sign in and Create account

Same flow on both screens: no account → create; account exists → sign in.

- User cancels the provider popup → no error, stay on the current screen.
- Provider or network error → red banner at top of form: "Couldn't continue with Google. Please try again." (1 frame to design)
- Social email matches an existing password account → **pending BE**: auto-link (preferred) or banner "An account with this email already exists. Sign in with your password."

---

## Open — reconfirm before ticket is final

- [ ] **FE: confirm MVP ships WITHOUT email verification** (auto login after Create account, per the table above).
- [ ] **BE: confirm whether social login can auto-link to an existing password account.**
- [ ] Design: add social error banner frame.
- [ ] Design: add focus states for inputs and buttons.
