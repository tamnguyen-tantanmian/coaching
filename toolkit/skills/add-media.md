# Workflow: Add media to the Hub

Put images, video, PDFs or a document into the hub so it shows in the report, in the right place and linked to the items it is evidence for.

*Status: draft.*

| | |
|---|---|
| When | When you have images (wireframes, screenshots, photos of a test session), video, PDFs or an HTML prototype that the report needs |
| Before | Save a checkpoint (commit or copy the folder) |
| Working file | None. The result is written into `work/` |
| Full guide | `work/README.md`, the "Add images, video, PDFs" section |

## Step 1: Place the files (AI)

**Who:** AI
**Input:** The files you gave, and the list of folders in `work/`
**Output:** A folder `work/<short-name>/` holding the files, or single files placed in an existing folder

**Instruction:**
> Put the files you were given into `work/<short-name>/`. Name folders and files in lowercase joined with hyphens, and add a number at the start (`1-`, `2-`...) to images in the order they should show, because the file name becomes the caption. Convert `.heic`, `.tiff`, `.psd` or `.mov` to `.png`, `.jpg`, `.pdf` or `.mp4` if you can, otherwise say so clearly. Do not overwrite existing files and do not place files in `_personal/` or `work/sources/`. If a file looks like it contains real names or personal data, stop and ask.

**Check:** Open the folder and compare the file names with the list you gave.
**Failure sign:** A file was overwritten or placed outside `work/`.

## Step 2: Describe it (AI)

**Who:** AI
**Input:** The files from step 1, a template in `toolkit/templates/`, and the list of items in `insights/`
**Output:** `work/<short-name>/index.md`

**Instruction:**
> Create `index.md` from the closest template. Fill `type` (free), `title`, `stage`, `status` (`draft` if not checked yet) and a one-sentence `summary`. Fill `takeaways` only with what can be seen in the files themselves. Fill `supports` with the item codes that this document is clearly evidence for; if you are not sure, leave `[]` and list the items that may be related at the end of the answer. Do not invent content that is not in the files.

**Check:** Open `index.md`: does every code in `supports` have a matching item file?
**Failure sign:** `takeaways` says something that is not in the images; `supports` points at an item that does not exist.

## Step 3: Rebuild and look (YOU)

**Who:** YOU
**Input:** `work/<short-name>/`
**Output:** A new `index.html`

Ask the AI tool to run `python3 ../toolkit/skills/export-hub.py`, open `index.html`, go to the **Work** section and click the new card.

**Check:** The images all show in the right order, the captions are easy to understand, and there is no yellow warning (heavy file, format that cannot be displayed, file not found).
**Failure sign:** A warning is still on the document page: do what the warning says, then rebuild the report.
