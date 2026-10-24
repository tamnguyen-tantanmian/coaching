# Get the Folder

This guide helps you get the workspace onto your machine. There are two ways, and you only need to pick one.

**Never used GitHub? Pick option A.** You can use this workspace without an account.

| | Way | GitHub account needed | Backed up | Good when |
|---|---|---|---|---|
| A | Download ZIP | No | No, you back it up yourself | You want to start right away |
| B | Use this template, then GitHub Desktop | Yes (free) | Yes, with change history | You want an automatic backup |

## Where to keep it

Put the folder somewhere ordinary on your machine, for example `Documents`.

**Do not put it in Google Drive, iCloud, OneDrive or Dropbox.** An AI coding tool writes many files at once, and a folder that syncs to the cloud can break halfway. If you want a backup, use option B.

## Option A: Download ZIP

1. Open the GitHub page of the repo (the link comes from whoever shared the template).
2. Click the green **Code** button, then choose **Download ZIP**.
3. Unzip the file you just downloaded:
   - Mac: double-click the file.
   - Windows: right-click, choose **Extract All**.
4. Drag the unzipped folder into `Documents`.
5. Open the folder. You will see `README.md`, `toolkit`, `my-case` and `demo-case`.

**Backup:** from time to time, compress `my-case` into a ZIP file and put it away, or copy it to another drive. The end of each work session is a good moment.

## Option B: Use this template, then GitHub Desktop

This creates your own **repo** (a repo is a folder stored on GitHub). You keep it **Private**, so only you can see it.

### Part 1: Create your repo

1. Go to [github.com](https://github.com) and sign in. No account yet? Click **Sign up** (free).
2. Open the GitHub page of the repo that the template's sharer sent.
3. Click the green **Use this template** button, then choose **Create a new repository**.
4. In the **Repository name** box, enter a name, for example `my-design-workflow`.
5. Choose **Private**.
6. Click **Create repository**.

Cannot see the **Use this template** button? Use option A, or message the person who shared the template.

> **Do not download the original repo directly to save your work.** You have no write access to it, so your changes cannot be saved there. Create your own repo with **Use this template** first.

### Part 2: Bring the repo to your machine

1. Install **GitHub Desktop** from [desktop.github.com](https://desktop.github.com) and sign in with your GitHub account.
2. Choose **File**, then **Clone repository**. (Clone means download a repo to your machine.)
3. On the **GitHub.com** tab, choose the repo you just created.
4. In the **Local path** box, choose `Documents`.
5. Click **Clone**.
6. Choose **Repository**, then **Show in Finder** (Mac) or **Show in Explorer** (Windows) to open the folder.

### Part 3: Save your work

Do this after each time you finish a piece of work:

1. Open GitHub Desktop. The left column lists the files you changed.
2. At the bottom left, type a one-line summary, for example `Discover: scope and user-voice synthesis`.
3. Click **Commit to main**. (A commit saves a point of change, with a message. `main` is the main branch, just leave it as it is.)
4. Click **Push origin** in the top bar. (Push sends those points to GitHub.)

These four actions are everything you need to know about Git. The words you just met are explained further in [`03-github-basics.md`](03-github-basics.md).

## Check before you start

- [ ] The folder is in `Documents`, not in a folder that syncs to the cloud.
- [ ] You can see `my-case` and `demo-case` in the folder.
- [ ] You can open `my-case/README.md` and read it.

Opens, but tables and links look raw? That is normal: Markdown files need a viewer. See "View markdown files" in [`02-set-up-your-case.md`](02-set-up-your-case.md).
