# Principle checks

*Written when the Define stage starts. This is the set of principles used in **Heuristic Evaluation**: checking a design against Nielsen's 10 usability heuristics. Turn each principle into a yes/no question for your product. Add your organisation's own principles below, numbered from P11.*

## How to use

1. **Write a yes/no question for your product** in the last column of the table below. Each principle in the "Details" part has suggested questions: pick, adapt them to your product, then write them into the table.
2. **Evaluate the design:** for each decision or screen, go through every question. An answer of "no" is a violation.
3. **Record each violation with its severity** (0 to 4), using [Severity levels](severity-levels.md).
4. **Evaluate independently, then merge:** one person usually finds only part of the problems. If you can, ask 3 to 5 people to evaluate separately, then merge the results.
5. **Link back to the hub:** a decision that passes gets `follows` pointing at the principle; a decision that violates it and that you accept gets `pulls_against` and the reason (see `../toolkit/skills/how-the-hub-works.md`).

## Principle table

| ID | Principle | Yes/no check for my product |
|---|---|---|
| P1 | Visibility of system status | |
| P2 | Match between system and the real world | |
| P3 | User control and freedom | |
| P4 | Consistency and standards | |
| P5 | Error prevention | |
| P6 | Recognition rather than recall | |
| P7 | Flexibility and efficiency of use | |
| P8 | Aesthetic and minimalist design | |
| P9 | Help users recognise, diagnose and recover from errors | |
| P10 | Help and documentation | |
| P11 | (your organisation's own principle, if any) | |

---

# Details of the 10 heuristics

Each entry has four parts: **It means** (an explanation in plain words), **Ask when evaluating** (yes/no questions to copy into the table above), **Signs of a violation**, and **Example**.

## P1 · Visibility of system status

**It means:** the system always tells users what is happening, through timely and visible feedback. Users do not have to guess whether their action took effect.

**Ask when evaluating:**
- After each action, does the user see feedback right away (saved, sent, loading)?
- For anything that takes more than a few seconds, is progress or a "working" state shown?
- Does the user know where they are in a multi-step process (which step out of how many)?
- Is the current state of an item (selected, off, confirmed) visible without opening it?

**Signs of a violation:** pressing a button and nothing happens; a blank page while loading; users pressing again and again because they are not sure the first press worked.

**Example:** a progress bar while uploading a file; a "Saved" label after pressing Save; a "Step 2 of 4" indicator at the top of a form.

## P2 · Match between system and the real world

**It means:** the system speaks the users' language: words, concepts and an order that are familiar to them, not the system's internal jargon.

**Ask when evaluating:**
- Do labels, buttons and messages use words that real users use (no internal terms, error codes, technical names)?
- Does the order of the steps follow the natural order of what the user is doing in real life?
- Do icons and metaphors resemble things the user already knows?
- Does information appear in the user's logic (for example by trip) rather than by the system's data structure?

**Signs of a violation:** users ask "what does this word mean?"; labels taken from database table names; unexplained abbreviations.

**Example:** "Shopping cart" instead of "Selected items list"; saved credit cards laid out like physical cards.

## P3 · User control and freedom

**It means:** users often press the wrong thing. They need a clearly marked "emergency exit" to leave an unwanted state without going through a long process.

**Ask when evaluating:**
- Can the user cancel or go back at every step of a process?
- Is there undo for actions that are easy to get wrong?
- Can the user leave an open window or mode without losing the work in progress?
- Can a delete or an overwrite be reversed, or is there a confirmation first?

**Signs of a violation:** no Cancel button; the only way out is to close the whole app; one wrong delete is gone for good.

**Example:** a "Deleted. Undo" message that shows for a few seconds; a Back button that keeps the data already entered.

## P4 · Consistency and standards

**It means:** the same thing looks and works the same everywhere. Users should not have to wonder whether two different words or actions mean the same thing. Follow the conventions of the platform and the industry.

**Ask when evaluating:**
- Does the same action have the same name and the same position on every screen?
- Does the same component (button, input, card) have the same shape and behaviour?
- Does the product follow the platform's conventions (iOS, Android, web) for familiar things?
- Does a word always refer to the same concept?

**Signs of a violation:** "Save" on one screen but "Confirm" on another for the same job; two different kinds of primary button; an icon that means one thing but is used for two jobs.

**Example:** the primary button is always at the bottom right and the same colour; the logo at the top left leads to the home page.

## P5 · Error prevention

**It means:** even better than a clear error message is a design that keeps the error from happening. Remove the situations that invite errors, or check and ask for confirmation before the user commits.

**Ask when evaluating:**
- For a high-stakes action (delete, pay, send), is there a confirmation step or a way to undo?
- Does the input help the user enter the right thing (a format hint, sensible defaults, limits)?
- Does the system block invalid choices instead of letting the user choose and then reporting an error?
- Are two easily confused actions placed far apart, or clearly different in form?

**Signs of a violation:** letting the user enter a date in the past and only then saying "invalid date"; a Delete button right next to Save, in the same style.

**Example:** a date picker that disables the dates that cannot be chosen; a Delete button in a warning colour that asks for confirmation.

## P6 · Recognition rather than recall

**It means:** reduce the load on memory. Put options, information and actions right in front of the user so they can recognise them, instead of forcing them to remember from the previous screen.

**Ask when evaluating:**
- Is the information needed for a step shown at that step (the user is not made to remember it from an earlier one)?
- Can the user pick from a list instead of retyping something from memory?
- Are actions and options visible instead of hidden behind invisible gestures?
- If there is history or suggestions (recently used items, autofill), can the user use them?

**Signs of a violation:** being made to retype a code seen on the previous screen; a function reachable only through a hidden gesture with no hint.

**Example:** showing recent searches; an order summary next to the payment step.

## P7 · Flexibility and efficiency of use

**It means:** the system serves both newcomers and experienced users. There are shortcuts, customisation and fast ways for frequent users, without confusing newcomers.

**Ask when evaluating:**
- Do experienced users have shortcuts (keyboard shortcuts, quick actions, bulk actions)?
- Does the system remember repeated choices, settings or data so they do not have to be redone?
- Can newcomers follow the full, clear path?
- Can users customise the parts they use often?

**Signs of a violation:** long-time users go through the same five steps every time; no way to act on many items at once.

**Example:** keyboard shortcuts for common actions; "buy again" from a previous order; multi-select.

## P8 · Aesthetic and minimalist design

**It means:** the interface does not carry extra or barely relevant information. Every additional piece of information competes for attention with the important information and makes it harder to see.

**Ask when evaluating:**
- Does each screen have one clear main job, and does it stand out from the rest?
- Does every element on the screen serve what the user is doing?
- Is the text short, and is rarely used information tucked away (expandable when needed)?
- Does decoration slow the user down or make reading harder?

**Signs of a violation:** a screen full of text and buttons of equal weight; banners, popups and icons competing with each other; long explanatory text nobody reads.

**Example:** a checkout screen that keeps only the necessary fields; advanced features behind "More options".

## P9 · Help users recognise, diagnose and recover from errors

**It means:** error messages use plain language (no error codes), say precisely what the problem is, and constructively suggest a solution.

**Ask when evaluating:**
- Is the error message written in plain words, without error codes or technical terms?
- Does it say what is wrong and where (pointing to the exact field or step)?
- Does it say what the user needs to do next, and is there a button to do it?
- Is the work the user already entered kept so they can fix it without starting over?

**Signs of a violation:** "An error occurred. Code 500."; an error shown in red at the top of the page without saying which field is wrong; clearing the whole form after an error.

**Example:** "This email is already in use. Sign in or use another email." with a Sign in button.

## P10 · Help and documentation

**It means:** it is best when the system can be used without explanation. But when help is needed, it must be easy to find, tied to the task at hand, give concrete steps and not be too long.

**Ask when evaluating:**
- Can the user find help at the right time and in the right place (in context)?
- Is the help content searchable and organised by what the user wants to do, not by feature structure?
- Does it have short, concrete, easy-to-follow steps?
- For things the user meets for the first time, is there a short hint (onboarding, tip)?

**Signs of a violation:** help is one long PDF; you have to leave the screen you are on to find it; there is no way to search.

**Example:** a "?" icon next to a confusing field that opens a one-line explanation; a help-centre search by task.

---

# Sources

- Nielsen, J. (1994). *10 Usability Heuristics for User Interface Design.* Nielsen Norman Group. Nielsen refined this set of 10 heuristics in 1994 from an analysis of 249 usability problems; Nielsen Norman Group has updated the explanations since.
- Nielsen, J. (1994). *How to Conduct a Heuristic Evaluation.* Nielsen Norman Group.
- Nielsen, J., & Molich, R. (1990). *Heuristic evaluation of user interfaces.* Proceedings of ACM CHI'90.

The explanations and questions above are rewritten in plain words so you can use them in a project right away. When you need an exact citation, read the original at Nielsen Norman Group.
