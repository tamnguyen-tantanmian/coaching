# Starter design system: notes

*This is the `design-system-notes.md` for the starter system, in the form an AI coding tool can read. If you have your own design system, write your own version of this file instead (template in `context/design-system-notes.md`).*

## Where the source of truth lives
`tokens.css` (variables) and `components.css` (components) in this folder. `components.html` shows every component and state.

## Tokens
- Colour: `--color-primary`, `--color-primary-hover`, `--color-on-primary`, `--color-text`, `--color-muted`, `--color-bg`, `--color-surface`, `--color-border` (decorative), `--color-border-strong` (inputs), `--color-danger`, `--color-danger-bg`, `--color-focus`, `--color-badge-bg`, `--color-badge-text`
- Type: system font stack, sizes `--text-sm` to `--text-xl`, weights regular and bold
- Spacing: 4 px base, `--space-1` (4) to `--space-6` (32)
- Radius: `--radius-sm`, `--radius-md`, `--radius-lg`
- Touch target: `--target-min` (44 px)

## Components
| Component | Class | States it has |
|---|---|---|
| Button | `.btn`, `.btn--secondary`, `.btn--block` | default, hover, focus, disabled |
| Field | `.field`, `.label`, `.input`, `.help`, `.error`, `.field--error` | default, focus, error |
| Radio card | `.radio-card` (a real radio input inside a label) | default, selected, focus |
| Card | `.card` | default |
| Badge | `.badge` | default |
| Alert | `.alert`, `.alert--error` | information, error |
| Step indicator | `.steps` (an ordered list; `aria-current="step"` on the active one) | done, current, upcoming |

## Patterns
One column, readable width (`.container`), mobile first. Stack vertically with `.stack`. One main action per screen. Errors appear next to the field and are announced.

## Do and do not
- Do use only the tokens and components above.
- Do keep every screen a real `<h1>`, a landmark (`<main>`), labelled inputs and a visible focus.
- Do not add colours, fonts, sizes or libraries. If something is missing, say so instead of inventing it.

## Accessibility rules
Text 4.5:1, interface parts 3:1, keyboard operable, focus always visible, targets at least 44 px, meaning never by colour alone. (See `context/accessibility-rules.md`.)
