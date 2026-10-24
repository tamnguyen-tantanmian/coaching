# Workflow: User-Voice Synthesis

Turn what real users say (reviews, forums, short interviews) into themes and opportunities, without the AI inventing quotes and with every theme traceable to the original words.

*Status: draft. Try the instructions on a real case and adjust them to how you work before you rely on them.*

| | |
|---|---|
| Working file | `work/user-voice-synthesis.md` (each step fills one section) |
| Sources | `work/sources/anonymised/` (quotes with IDs: R01..., I01-01...) |
| Original data | `work/sources/_raw-private/` (the AI does not read it) |
| Final output | `work/user-voice-synthesis.md` (the Evidence page in Stages is built from this file) and the `insights/opportunities/O*.md` files |

## What counts as user voice

| Source | Kind | Good for | Be careful of |
|---|---|---|---|
| Public reviews, forums, communities | Secondary, real words | Pain, expectations, wording, at scale | Skewed to extremes; fake reviews; you know nothing about the writer |
| Short interviews (3 to 5 current users, 15 to 20 minutes) | Primary | The reasons behind behaviour, events that happened | Small sample; friends are polite; leading questions; **personal data**: needs consent and anonymising |
| Support tickets, feedback (if you have access) | Secondary, internal | Real problems in the wild | Often personal or internal data: anonymise and use only approved tools |
| Open answers in a survey (if there is one) | Primary | Many short answers | Shallow; people choose themselves to answer |

The goal: at least 30 quotes from at least 3 sources or 3 people, so that a theme can be judged.

## Sections of the working file

| Section | Filled in step | By |
|---|---|---|
| `## Scope` (question, who, beliefs) | 1 | YOU |
| `## Sources and guide` | 2 and 3 | Step 2: the AI's suggestions, labelled. Step 3: your final list of sources and your interview guide |
| `sources/anonymised/` | 4 | YOU |
| `## Coding (AI draft)` | 5 | AI. **Do not edit** |
| `## Coding (verified)` | 6 | YOU: your corrected copy |
| `## Themes` | 7 | AI |
| `## Opportunities + limits` | 8 | YOU |

Two rules: the AI returns only its own section, and the AI draft is always kept apart from the checked version.

## If a gate is not met

| Gate | After step | If the answer is no |
|---|---|---|
| A: the right speakers? | 3 | Go back to step 2 and widen the sources |
| B: verbatim and traceable? | 6 | Run step 5 again with a tighter instruction (many errors), then check again |
| C: weighed by importance, not only counted? | 8 | Go back to step 7 and redo the synthesis |

---

## Step 1: Frame the question

**Who:** YOU
**Input:** `work/scope.md`
**Output:** `## Scope`

Fill in: the question (taken from the scope); who we need to hear from (which users, which situation); what you want to learn (a behaviour or a pain, not a feature); 3 to 5 beliefs to test in step 7.

**Check:** Does the question ask about behaviour and problems that happened, and not whether people like your idea?
**Failure sign:** "What do users think about feature X?" with no situation or behaviour.

## Step 2: Suggest

**Who:** AI
**Input:** `## Scope` (only this section)
**Output:** `## Sources and guide`, labelled "AI suggestions"

**Instruction:**
> Use only the scope below. Suggest the places where real users of this product talk about it in public (the kinds of source, do not invent specific pages), and draft eight interview questions. The questions must ask about past behaviour and real situations ("tell me about the last time you..."), not ask for opinions about ideas, and must not lead. Do not invent sources and do not quote anyone. Say what you are not sure about. Return only the two lists.

**Check:** Is there a source you cannot really find? Is there a question that suggests its answer?
**Failure sign:** Made-up forum names; questions like "do you use...".

## Step 3: Review the voices · Gate A

**Who:** YOU
**Input:** `## Sources and guide`
**Output:** `## Sources and guide` (final)

Edit it into the final list of sources and the interview guide, with reasons. Add the voices the AI missed. Agree on consent for the interviews: participants know this is a learning project, and you will remove their names.

**Gate A:** Who is missing (light users, people who left, people who never signed up)? Is the sample skewed (only angry reviews, only friends, only one group)? Is consent clear and recorded?
**Failure sign:** Everyone you picked is like you; no consent note.

## Step 4: Collect and anonymise

**Who:** YOU
**Input:** Public sources and your interviews
**Output:** Files in `work/sources/anonymised/`

Collect at least 30 quotes from public sources and run 3 to 5 short interviews (recorded when allowed). Keep the original data in `_raw-private/`. **Anonymise before the AI sees anything:** remove names, usernames, emails, company names (find and replace on your machine, do not ask the AI). Give each quote an ID (R01... for reviews, I01-01... for interview 1 quote 1) and keep it verbatim.

**Failure sign:** A quote was rewritten "to make it shorter"; no IDs; a name was left behind.

## Step 5: Code

**Who:** AI
**Input:** `## Scope` and the quotes in `sources/anonymised/`
**Output:** `## Coding (AI draft)`

**Instruction:**
> Use only the quotes below and group them into themes. For each theme, give a short name, then list the ID and the exact verbatim text of every quote in it. Never rewrite, shorten or invent a quote. A quote that fits no theme goes into "unclassified". A theme with fewer than three quotes, or quotes from fewer than two sources or two people, gets the label "weak". If you are not sure, write "unknown". Return only the table.

**Failure sign:** A quote that is not in the sources; no "unclassified"; every theme is "strong".

## Step 6: Verify · Gate B

**Who:** YOU
**Input:** `## Coding (AI draft)` and `sources/anonymised/`
**Output:** `## Coding (verified)`, with the number of wrong quotes, the number of misplaced quotes and the error rate at the top

Copy the draft into `## Coding (verified)`. (1) Check **every quote cited for the top three themes** is verbatim: find the passage in `sources/anonymised/`. (2) Spot-check 20% of the rest at random. (3) Read ten quotes from "unclassified" and ten from other themes: did the AI miss or misplace something important? (4) Fix the errors.

Better, do it once: code 20 quotes yourself first, then compare with how the AI grouped them.

**Gate B:** Is every quote verbatim and with an ID? Do the themes stand up against the sample you read yourself? Is the error rate acceptable?
**Failure sign:** Only the first few quotes were checked; no error rate recorded.

## Step 7: Synthesise and test

**Who:** AI
**Input:** `## Scope` (including what you already believed) and `## Coding (verified)`. **Do not** give it the AI's draft
**Output:** `## Themes`

**Instruction:**
> From the checked coding, list the needs and pains that matter for the question in the scope. For each one: how many quotes and from how many sources or people, one example quote with its ID, and a counter-quote if there is one. Then for each, give the strongest argument that it is wrong or misleading, and say what evidence would change your mind. Go through each belief I wrote down and say which quotes support it, contradict it or do not mention it. Do not propose actions yet. Say what this sample cannot tell us. Return only this section.

**Failure sign:** Generic needs ("users want simplicity"); no counter-quote; every belief is "supported".

## Step 8: Interpret and decide · Gate C

**Who:** YOU
**Input:** `## Themes`, `## Scope`
**Output:** `## Opportunities + limits`, the `insights/opportunities/O*.md` files, and the Evidence page in Stages (built from the working file)

Weigh each theme by **severity** (how bad when it happens), **context** (who, when) and **breadth** (how many different people), not only by how many quotes mention it. Write 3 to 5 opportunities as user needs, not features, each with its quote IDs. Each opportunity is its own file in `insights/opportunities/`. State the limits of the sample.

**Gate C:** Is each opportunity based on severity and context, not a quantity metric? Can you defend it by pointing at the quotes? Have you said what this sample cannot tell us?
**Failure sign:** The theme with the most quotes automatically becomes the top opportunity; missing quote IDs.

---

## The limit to state plainly

This analysis shows what users **say**, not what they **do**. Reviews skew to extremes, friends are polite, the sample is small. Treat the themes as hypotheses and test them with real users in the later weeks.
