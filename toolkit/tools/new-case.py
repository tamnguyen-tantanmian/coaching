#!/usr/bin/env python3
"""Create a clean case folder for a new project from the my-case template.

    python3 toolkit/tools/new-case.py onboarding-redesign
    python3 toolkit/tools/new-case.py onboarding-redesign --title "Onboarding redesign"

The new folder is a copy of my-case with the [EXAMPLE] items removed, the example
rows cleared from the hub pages, the case name filled in, and index.html rebuilt.
my-case itself is not changed, so it stays a clean template for the next project.
Standard library only.
"""
import argparse
import os
import re
import shutil
import subprocess
import unicodedata
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # the workspace: toolkit/tools/ is two levels down
TEMPLATE = os.path.join(ROOT, "my-case")
RESERVED = {"my-case", "demo-case", "toolkit", "guides", "templates", "tools", "skills", "index"}
IGNORE = shutil.ignore_patterns(".DS_Store", "__pycache__", "_export", "index.html")
ITEM_RE = re.compile(r"^[OHMDEF]\d+\.md$")
ITEM_LINK_RE = re.compile(r"\]\((?:\.\./)?(?:[a-z]+/)?[OHMDEF]\d+\.md\)")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def clean_hub_page(text, is_readme):
    out = []
    for line in text.split("\n"):
        if line.startswith("|"):
            first = line.split("|")[1].strip() if line.count("|") > 1 else ""
            if "[EXAMPLE]" in line or ITEM_LINK_RE.search(line):
                continue  # a row that describes an example item
            if re.match(r"^D\d+\b", first):
                continue  # example rows in the alignment audit and verdict tables
            if re.fullmatch(r"M\d+", first):
                line = line.replace("| %s |" % first, "| [metric] |", 1)
        out.append(line)
    text = "\n".join(out)
    text = re.sub(r"\[O1\]\([^)]*O1\.md\)", "[opportunity ID]", text)
    if is_readme:
        empty = {
            "alignment": "_No decisions yet. This table is built when you add items._",
            "warnings": "- No items yet, so no warnings yet.",
        }

        def block(m):
            kind = m.group(1)
            if kind in empty:
                return "%s\n%s\n<!-- /generated -->" % (m.group(0).split("\n")[0], empty[kind])
            return m.group(0)

        text = re.sub(r"<!-- generated:(\w+)[^\n]*-->\n.*?<!-- /generated -->", block, text, flags=re.S)
        for sample_note in (" Dữ liệu `[EXAMPLE]` ở đây để bạn thấy hub chạy ra sao. Xoá và thay bằng dữ liệu của bạn.",
                        " The `[EXAMPLE]` data here shows how the hub works. Delete it and replace it with your own data."):
            text = text.replace(sample_note, "")
    return text


def main():
    ap = argparse.ArgumentParser(description="Create a clean case folder from the my-case template.")
    ap.add_argument("name", help="project name or folder name, e.g. onboarding-redesign or \"Onboarding redesign\" "
                                 "(accents and spaces are turned into a folder name)")
    ap.add_argument("--title", help="project name shown in the hub (default: derived from the folder name)")
    ap.add_argument("--dest", default=ROOT, help="parent folder for the new case (default: the workspace root)")
    a = ap.parse_args()

    given = a.name.strip()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", given):
        # a human name such as "Trip Planner" or "Lập kế hoạch chuyến đi" (accents allowed): make the folder name from it
        slug = unicodedata.normalize("NFKD", given.replace("đ", "d").replace("Đ", "D"))
        slug = "".join(ch for ch in slug if not unicodedata.combining(ch)).lower()
        slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
        if not slug:
            sys.exit("Cannot make a folder name from \"%s\". Use a name with letters or digits, for example: onboarding-redesign" % given)
        if not a.title:
            a.title = given
        a.name = slug
    if a.name in RESERVED:
        sys.exit("The name \"%s\" is already used by a workspace folder. Choose another name." % a.name)
    if not os.path.isdir(TEMPLATE):
        sys.exit("Template folder not found: %s" % TEMPLATE)
    dest = os.path.join(os.path.abspath(a.dest), a.name)
    if os.path.exists(dest):
        sys.exit("Folder already exists: %s\nChoose another name, or delete that folder if you want to start over." % dest)
    title = a.title or a.name.replace("-", " ").capitalize()

    shutil.copytree(TEMPLATE, dest, ignore=IGNORE)
    insights = os.path.join(dest, "insights")

    removed = 0
    for dirpath, dirnames, filenames in os.walk(insights):
        dirnames[:] = [d for d in dirnames if not d.startswith("_")]
        for name in sorted(filenames):
            p = os.path.join(dirpath, name)
            if ITEM_RE.match(name) and "[EXAMPLE]" in read(p):
                os.remove(p)
                removed += 1
    # example rows in the stage pages and reference pages
    for folder in (os.path.join(dest, "stages"), os.path.join(dest, "standards")):
        for name in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
            p = os.path.join(folder, name)
            if os.path.isfile(p) and name.endswith(".md"):
                write(p, clean_hub_page(read(p), False))
    p = os.path.join(dest, "insights", "case-log.md")
    if os.path.isfile(p):
        write(p, clean_hub_page(read(p), False))

    for folder in ("opportunities", "hypotheses", "metrics", "decisions", "evidence", "findings"):
        d = os.path.join(insights, folder)
        os.makedirs(d, exist_ok=True)
        if not os.listdir(d):
            write(os.path.join(d, ".gitkeep"), "")  # keeps the empty folder in Git
    p = os.path.join(dest, "README.md")
    t = read(p).replace("# Project: [tên dự án]", "# Project: %s" % title).replace("# Project: [project name]", "# Project: %s" % title)
    t = re.sub(r"^\| (Tên dự án|Project name) \| \|$", lambda m_: "| %s | %s |" % (m_.group(1), title), t, flags=re.M)
    t = re.sub(r"<!-- template-only -->.*?<!-- /template-only -->\n\n?", "", t, flags=re.S)  # note that only makes sense in my-case
    t = t.replace("# my-case", "# %s" % a.name).replace("my-case/\n", "%s/\n" % a.name)
    write(p, t)

    print("Created: %s" % dest)
    print("  - Removed %d [EXAMPLE] items and cleaned the sample rows in standards/" % removed)
    tool = os.path.join(ROOT, "toolkit", "skills", "export-hub.py")
    if os.path.isfile(tool):
        r = subprocess.run([sys.executable, tool, "--case", dest], cwd=dest, capture_output=True, text=True)
        print("  - index.html: %s" % ("built" if r.returncode == 0 else "error, run it again in the project folder: python3 ../toolkit/skills/export-hub.py"))
        if r.returncode != 0:
            print(r.stderr.strip()[-400:])
    home = os.path.join(ROOT, "toolkit", "skills", "export-home.py")
    if os.path.isfile(home):
        subprocess.run([sys.executable, home, "--workspace", ROOT], capture_output=True, text=True)
        print("  - Workspace home page (index.html at the root): a card was added for this project")
    print("\nFirst steps:")
    print("  1. Open the folder %s with a tool you know (an AI coding tool, VS Code or Obsidian)." % a.name)
    print("  2. Open README.md in the folder, fill in the Project card, then fill in context/product-and-users.md and context/data-rules.md.")
    print("  3. When you have the first item, copy a file from insights/_templates/ into the folder of its type, for example insights/decisions/.")


if __name__ == "__main__":
    main()
