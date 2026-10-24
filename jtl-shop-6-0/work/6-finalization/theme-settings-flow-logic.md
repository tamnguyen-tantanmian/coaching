# Theme Settings — Configuration, Save & Apply

How a merchant opens a theme, edits it, saves it, and makes it live. Covers the page anatomy, the version model, and every state the Save / Apply buttons can be in.

**Source of truth:** Figma board *Theme Settings | Configurations and Save/Apply flow*.

---

## Page anatomy

Three fixed regions. Only the right panel scrolls its own content; the centre is read-only.

| Region | Width | Contents | Behaviour |
| --- | --- | --- | --- |
| **Theme rail** (left) | 100 px | `THEMES` list — one row per installed theme with its active preset (*Tangerine · Default*, *Indigo · Default*) | Selecting a row loads that theme into the preview and the config panel |
| **Preview** (centre) | fluid | Rendered storefront page + page selector | **Read-only.** Not an editor — no click-to-select, no inline editing |
| **Config panel** (right) | 240 px | `Theme Setting > Config-panel`, full config tree | Every control writes to the working copy, never straight to live |

### Page selector

A dropdown above the preview. It changes *what the preview renders*, not what is being edited — the config is theme-wide.

Home page · Default page · Product page · Cart · Check out · Login / Register · Account settings

The preview fetches the **latest saved version of the selected page**, so content edits made elsewhere in the admin show up here without republishing the theme.

---

## Theme identity

| Field | Rule |
| --- | --- |
| **Theme Name** | Editable text field |
| **Default badge** | Shown on a theme that ships with the shop. Renaming a default theme keeps the badge — the badge marks origin, not the name |

---

## Version model

A theme carries a **draft** plus up to **five saved versions**.

| Slot | Count | Notes |
| --- | --- | --- |
| Draft | 1 | Overwritten on every *Save as Draft*. There is only ever one |
| Versions | max 5 | `Version 1 … Version 5`, newest last |

**The default theme, as shipped, counts as Version 1.** A merchant who has never saved anything already has one version on the stack.

### Version dropdown

Lists `Draft`, then the saved versions newest first. Each row offers:

| Action | Available on | Result |
| --- | --- | --- |
| **Reset** | any version | Loads that version into the default of the selected theme. **Does not make it applicable** |
| **Delete** | any version with no badge | Removes it from the stack, freeing a slot |
| **Apply** | latest version only | Confirmed. An older version cannot be applied directly — it must be reset, then saved as a new latest version, and that new version is what goes live |

### Badges

Two versions in the list are doing a job right now, and each is marked on its row.

| Badge | Marks | There is |
| --- | --- | --- |
| **Live** | The version currently published to the storefront | Exactly one, always |
| **Active** | The version applied in the current Theme Builder session | At most one |

A version can carry **both badges at once** — the usual case, where the merchant is working on the same version shoppers are seeing. It shows `Live` and `Active` together rather than either one alone.

**Neither can be deleted.** `Delete` is disabled on those rows, not merely warned about: removing the live version would leave the storefront rendering something with no entry in the list, and removing the active one would cut the working session out from under the merchant.

---

## Save & Apply flow

```
Start
 └─ default theme = Version 1
      │
      ├─▶ Apply this theme
      │      └─ toast "Theme applied successfully"
      │         [Open in editor]
      │
      └─▶ Make changes
             │
             ├─▶ Save as Draft
             │      └─ overwrites the existing draft
             │
             └─▶ Save as Version
                    ├─ "Saved as Version X"
                    │
                    └─ at 5 of 5
                         └─▶ "Exceed 5 versions limitation"
                                ├─ [Cancel] ......... no write
                                └─ [Save anyway] .... drops the
                                     oldest unbadged version,
                                     saves as the next number
```

### Buttons

| Control | Type | Behaviour |
| --- | --- | --- |
| **Save as Draft** | split button with caret | Primary action writes the draft. The caret opens *Save as Version* |
| **Apply this theme** | primary | Publishes the currently loaded version to the storefront |

### Draft states

`Remove` → `Unsaved` → `Assign`. The draft is a scratch slot: it is never live, and saving a new draft discards the previous one without a confirm.

### The 5-version ceiling

Saving a sixth version does not silently succeed. The merchant gets the *Exceed 5 versions limitation* modal:

- **Cancel** — nothing is written, the working copy stays dirty.
- **Save anyway** — the oldest version is dropped and the new one is saved.

The overwrite is **destructive and not undoable**, so the modal is required — the cap must never be enforced silently.

**A version still doing a job is never dropped.** The version live on the storefront is marked `Live`; the version applied in the Theme Builder is marked `Active`. Neither is ever removed — if the oldest version carries either badge it stays where it is, and the oldest version with no badge goes in its place.

### Numbering

**Version numbers are monotonic and never reused.** The counter keeps climbing regardless of what is dropped; the surviving versions keep the labels they were born with.

| Save | Stack after | Dropped |
| --- | --- | --- |
| Version 5 | 1 · 2 · 3 · 4 · 5 | — |
| Version 6 | 2 · 3 · 4 · 5 · 6 | Version 1 |
| Version 7 | 3 · 4 · 5 · 6 · 7 | Version 2 |

The table assumes none of the dropped versions is badged. A `Live` or `Active` version is skipped and the next-oldest unbadged one goes instead.

So a full stack is *not* `Version 1 … Version 5` — after a while it reads `Version 12 … Version 16`. The dropdown always shows five rows, but the numbers on them are history, not positions. A merchant who sees the list start at Version 12 has simply saved eleven times.

The version number is a **stable identifier**: FE may key on it, and a number, once used, never points at different content.

---

## Rules the front end must hold

- The preview is read-only. No affordance in it may look interactive.
- Only the latest version is applicable. `Apply` is disabled on every other row.
- Applying does not create a version. Apply publishes; Save records.
- The draft is singular. One draft per theme, overwritten on save.
- A version marked `Live` or `Active` cannot be deleted, and is never the one dropped at the ceiling.
- Version numbers are stable IDs, not positions. They only ever increase and are never recycled — dropping Version 1 does not free the number 1.

---

## Open items

- [ ] Does `Reset` overwrite the draft, or load alongside it?
- [ ] What happens to the applied theme if the merchant **deletes the version that is currently live**?
- [ ] Is the draft carried across a theme switch, or discarded when another theme is selected in the rail?
- [ ] Does `Apply` warn when the working copy has unsaved changes that are not in the version being applied?
- [ ] Are versions per-theme or per-shop? Five versions of *Tangerine* and five of *Indigo*, or five total?
