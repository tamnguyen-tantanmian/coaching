# Work

This folder is **where everything made in the project sits in one place**: the working files of each stage (`scope.md`, `problem-brief.md`, `findings.md`...), and the documents (competitor analysis, persona, wireframes, prototype, user flow...).

Every file or folder with an `index.md` here becomes a card in the **Work** section of the `index.html` report, linked to the items it is evidence for (opportunity, hypothesis, decision, evidence, metric). From a decision, a reader clicks through to the document behind it, and back. Sections with "(AI draft)" in the heading are hidden from the report.

Two subfolders do not become cards: `sources/` (research data, with `_raw-private/`, which is never given to the AI) and `original-docs/` if there is one. A subfolder only becomes a card when it has an `index.md`.

## Add a file or a document

Pick your situation:

| You have | What to do |
|---|---|
| A text file (`.md`) | Put it in the `work/` folder, for example `competitor-analysis.md` |
| Several files: images, PDFs, HTML, video | Create a subfolder in `work/` (for example `user-flow/`), add an `index.md` that describes it, then **drop the files into that folder** |
| Content that already lives elsewhere in the project (for example `work/sources/`) | Create an `.md` file here and use `source:` to point at it, so the content is not copied twice |
| A Figma, Miro or Notion link | Write the link in the document (see "External links" below) |

The easiest way: **start from a template in the `toolkit/templates/` folder** at the workspace root, next to the cases (copy it into `work/`, rename it). Or ask the AI tool: *"Create a persona document from the template `toolkit/templates/persona.md`."*

The document type is **free**: you can use a type like `journey-map` or `brand-guidelines` and the report still shows it normally.

## Add images, video, PDFs

The report recognises the format from the file extension, **you do not configure anything**. There are two ways, depending on whether you want the media to be a document of its own or sit inside a page.

### Way 1: Drop it into a document's folder (recommended)

1. Create the folder `work/<short-name>/`, for example `work/wireframes/`.
2. Drop the images, videos, PDFs into it.
3. Add an `index.md` file (copy it from a template in `toolkit/templates/` at the workspace root) with a `title` and a `type`.

Done. The report builds a document page with a **card in the Work section**, the first image as the cover, and every file in the folder shown on the page. You can ask the AI tool to do all three steps: *"Add these images to the project as a wireframe document."*

| You drop in | The report shows |
|---|---|
| `.png` `.jpg` `.jpeg` `.gif` `.webp` `.svg` `.avif` `.bmp` | An image grid, click for full size. **The file name becomes the caption** |
| `.mp4` `.webm` | A video player right on the page |
| `.pdf` | A card with an open button; add `embed: true` to view it right on the page |
| `.html` (prototype, flow) | An "Open in new tab" card; add `embed: true` to run it right on the page |
| `.csv` | A table (the first 40 rows) |
| `.xlsx` `.docx` `.pptx` and other files | An attachment card with an open button |

**Naming tip:** the file name becomes the caption (`2-discover.png` shows "2 discover") and images are ordered by name, so put a number at the start of the name (`1-`, `2-`, `3-`) to control the order.

### Way 2: Insert an image in the middle of a page

In any page or item (a stage page, a decision, evidence, a finding), write:

```
![Image description](path/image.png)
```

The path is counted **from the file you are writing in**. For example in `insights/decisions/D4.md`, if the image is at `work/wireframes/3-plan.png`, write `![Plan screen](../../work/wireframes/3-plan.png)`. Videos are inserted with the same syntax (`![demo](../../work/flow/demo.mp4)`). For PDFs and HTML, use a normal link or way 1.

### Files the report does not pick up

- Files in `_personal/` or `work/sources/_raw-private/` (the private zone): ignored.
- Files outside the project folder: not packed. Copy them into the project folder.

### The report warns you when something is wrong

On the document page (and in the output when you build the report) a warning shows if: a file is not found, an image is heavier than 2.5 MB (compress it below 2 MB), a format the browser cannot display (`.heic`, `.tiff`, `.psd`, `.fig`: export to PNG or JPG), or a `.mov` video (export to `.mp4`).

## AI drafts

A working file has two parts: **(AI draft)** is the AI's original draft, **(verified)** is the version you checked. By default the report **hides** every section with "AI draft" in its heading, so viewers see only checked content. There is a mode for the working team that shows draft sections folded and marked "not checked". Do not send that version to outsiders.

## Send the report to someone

Ask the AI tool: *"Export the report package to send to stakeholders, with a zip file."* The AI creates a compact folder with only `index.html` and exactly the files the documents use. This package **does not contain** raw working files, original data that is not anonymised, or your private notes.

---

# Technical details (optional)

This part is for people who want to write the information block at the top of a file themselves, or run the commands themselves.

## The information block at the top of a file

Every `.md` document has a block between two `---` lines at the top of the file:

```
---
type: "competitor-analysis"      # the document type, free
title: "Competitor analysis"
stage: "Discover"                # Setup, Discover, Define, Develop or Deliver
status: "verified"               # verified, draft, simulated or planned
summary: "One summary sentence."
takeaways:                       # 2 to 4 key points
  - "First key point"
supports:                        # items this document is evidence for
  - "[[O1]]"
  - "[[D3]]"
source: "competitor-analysis.md"   # optional: take the content from a working file
media:                           # optional: files that live elsewhere in the project
  - "prototype/index.html"
links:                           # optional: external links, as "Label | URL"
  - "Prototype in Figma | https://www.figma.com/..."
embed: true                      # optional: embed an HTML or PDF file right on the page
embed_url: ""                    # optional: embed a web address on the page
---
```

Only `title` and `type` are required. The other lines make the page fuller.

## The export command

```
python3 ../toolkit/skills/export-hub.py --bundle send-to-stakeholders --zip
```

This creates the compact folder and the zip file described above. Run with `--team` and the AI draft sections show up (folded).
