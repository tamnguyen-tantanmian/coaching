# Share Your Hub

Your hub is private by default: it lives in the case folder on your machine, and nobody sees it unless you send it. This guide explains how to let others see it, from the least risky way to the most risky.

## Choose how to share

| You want | Way | The recipient needs |
|---|---|---|
| A stakeholder to read it, with nothing to install | **HTML report** (Option 1) or **PDF** (Option 2) | A browser |
| To send the whole folder to a colleague | **ZIP file** (Option 3) | Obsidian or VS Code to view it nicely |
| One person to view it directly on GitHub | **Invite to a Private repo** (Option 4) | A free GitHub account |
| Anyone with the link to view it | **Public repo** (Option 5), only when the case may be shared | Nothing |

**For real company work, use Option 1 or 2.**

## Option 1: HTML report

One self-contained HTML file with a menu, opened by double-clicking in a browser, and sendable by email.

1. **Build the report.** The easiest way: ask the AI tool that has the case folder open to run `python3 ../toolkit/skills/export-hub.py`.
   - Running it yourself on Mac: right-click the case folder, choose **New Terminal at Folder**, then type the command above.
   - Running it yourself on Windows: open the case folder, click the address bar, type `cmd`, press Enter, then type the command above.
   - The machine needs Python 3. A Mac may ask you to install a set of tools the first time; Windows needs Python installed from [python.org](https://www.python.org).
2. **Open the file** `index.html` at the root of the case folder in a browser (double-click).
3. **Check before sending.** If there is a black bar at the top saying "sample content or blanks remain", the hub still has sample content or empty places. Fill them in or delete them, then rebuild.
4. **Send the file.** Copy `index.html` out and rename it so it is easy to recognise, for example `onboarding-redesign-report.html`. The recipient only needs a browser.

If you use GitHub, `index.html` is also **rebuilt automatically** after each push (the `Update index.html` workflow). You only need to download the repo, or choose **Fetch origin** and then **Pull** in GitHub Desktop, to get the latest copy, with no command to run.

The report contains only the hub, the decision log and the principles. It has no working files or AI drafts.

To send a compact package (images and prototype included, without exposing raw working files): run `python3 ../toolkit/skills/export-hub.py --bundle folder-name --zip` and send the ZIP file. The recipient unzips it and double-clicks `index.html`.

## Option 2: PDF

1. Open the hub page you want to send: in the HTML report from Option 1, or in Obsidian or VS Code.
2. Print that page (`Cmd+P` on Mac, `Ctrl+P` on Windows) and choose **Save as PDF**.
3. Repeat for the main pages: Overview, Problem brief, Findings.
4. Send the PDF files, or attach them to the company wiki.

## Option 3: ZIP file

1. Compress the **whole case folder**, not only `insights/`, because the pages in the report link to `work/`, `standards/` and the working files.
2. Send the ZIP file. The recipient unzips it and opens the whole folder in Obsidian or VS Code.
3. Try opening it on another machine before you send it.

## Option 4: Invite one person to a Private repo

1. Open your repo on GitHub, choose **Settings**, then **Collaborators**.
2. Click **Add people** and enter that person's account name or email.
3. They get an invitation email. After they accept, they read the hub right on GitHub.

You can revoke access at any time on the same screen.

## Option 5: Public repo

GitHub shows Markdown directly, so no website needs building: the link to the repo is the hub.

Only do this when the **whole case folder** may be shared, for example the sample project, or a cleaned copy of real work. The report links to files across the case folder, so publishing only part of it would break those links.

1. Create a **new** repo on GitHub and choose **Public**. Do not switch the Private repo you are using to Public, because the old history stays in it.
2. Copy the cleaned case folder into the new repo.
3. Open the repo link in a **private window** to see exactly what others see.

## Before you share anything

- **Do not put up confidential company figures,** details of an unreleased product, users' personal data, or passwords. Check your company's policy first.
- **A public link can be forwarded** to anyone.
- **Your GitHub account name is part of the repo address.** Pick a name you are comfortable seeing there.
- **You are the one sharing and you are responsible** for the link and the content. Nobody posts for you.
- **Use anonymised or fake data** for anything public.
