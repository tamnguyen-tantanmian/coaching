#!/usr/bin/env python3
"""
export-home.py - build the workspace home page (index.html at the workspace root).

One card per case folder (a folder with AGENTS.md next to insights/ or work/). Each card opens that
case's report. The page is a pure function of the files: no timestamp, so a rebuild with nothing
changed produces no diff.

    python3 export-home.py                        # the workspace you are in
    python3 export-home.py --workspace PATH
    python3 export-home.py --title "My workspace"
"""
import argparse
import html
import os
import re
import sys

STAGES = ["Setup", "Discover", "Define", "Develop", "Deliver", "Learn"]
EXAMPLES = ("demo-case", "my-case")  # listed after the real projects


def is_case(p):
    return os.path.isfile(os.path.join(p, "AGENTS.md")) and (
        os.path.isdir(os.path.join(p, "insights")) or os.path.isdir(os.path.join(p, "work")))


def find_workspace(start):
    p = os.path.abspath(start)
    while True:
        try:
            if any(is_case(os.path.join(p, d)) for d in os.listdir(p) if os.path.isdir(os.path.join(p, d))):
                return p
        except OSError:
            pass
        if is_case(p):
            return os.path.dirname(p)
        q = os.path.dirname(p)
        if q == p:
            return None
        p = q


def read(path):
    try:
        with open(path, encoding="utf-8") as f:
            return f.read()
    except OSError:
        return ""


def card_value(md, *keys):
    for k in keys:
        m = re.search(r"^\|\s*%s[^|]*\|\s*([^|]*?)\s*\|\s*$" % re.escape(k), md, flags=re.M | re.I)
        if m:
            v = re.sub(r"[*`]", "", m.group(1)).strip()
            v = re.sub(r"\s*\*[^*]*\*\s*$", "", v).strip()
            if v and not v.startswith("[") and " / " not in v:
                return v
    return ""


def description(md):
    """First prose paragraph after the project card; markdown stripped, cut at a sentence."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    parts = re.split(r"\n\s*\n", md)
    seen_table = False
    for part in parts:
        t = part.strip()
        if not t:
            continue
        if t.startswith("|"):
            seen_table = True
            continue
        if t.startswith("#") or not seen_table:
            continue
        t = re.sub(r"^>\s?", "", t, flags=re.M)
        t = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", t)
        t = re.sub(r"[*`_]", "", t)
        t = " ".join(t.split())
        if len(t) > 190:
            cut = t[:190]
            end = max(cut.rfind(". "), cut.rfind("; "))
            t = (cut[:end + 1] if end > 80 else cut.rsplit(" ", 1)[0] + "...")
        return t
    return ""


def front_status(path):
    m = re.match(r"---\n(.*?)\n---", read(path), flags=re.S)
    if m:
        s = re.search(r"^status:\s*\"?([\w-]+)", m.group(1), flags=re.M)
        if s:
            return s.group(1).lower()
    return ""


def count_items(case):
    n = 0
    base = os.path.join(case, "insights")
    for folder in ("opportunities", "hypotheses", "metrics", "decisions", "evidence", "findings"):
        d = os.path.join(base, folder)
        if os.path.isdir(d):
            n += sum(1 for f in os.listdir(d) if f.endswith(".md") and not f.startswith(("_", "README")))
    return n


def count_documents(case):
    active = planned = 0
    base = os.path.join(case, "work")
    if not os.path.isdir(base):
        return 0, 0
    for name in sorted(os.listdir(base)):
        if name in ("README.md", "sources") or name.startswith(("_", ".")):
            continue
        p = os.path.join(base, name)
        if os.path.isdir(p):
            st = front_status(os.path.join(p, "index.md"))
            if not os.path.isfile(os.path.join(p, "index.md")):
                continue
        elif name.endswith(".md"):
            st = front_status(p)
        else:
            continue
        if st == "planned":
            planned += 1
        else:
            active += 1
    return active, planned


def case_card(ws, d):
    case = os.path.join(ws, d)
    md = read(os.path.join(case, "README.md"))
    name = card_value(md, "Tên dự án", "Project name", "Project")
    template = d == "my-case" and not name
    if not name:
        name = "Product Name" if d == "my-case" else d
    stage = card_value(md, "Giai đoạn hiện tại", "Stage", "Current stage")
    owner = card_value(md, "Chủ dự án", "Owner")
    question = card_value(md, "Câu hỏi của business", "Business question")
    desc = description(md)
    items = count_items(case)
    docs, planned = count_documents(case)
    kind = "Template" if template else ("Example" if d == "demo-case" else "Project")
    return {
        "dir": d, "name": name, "stage": stage if stage in STAGES else "", "owner": owner, "question": question,
        "desc": desc, "items": items, "docs": docs, "planned": planned, "kind": kind,
        "report": os.path.isfile(os.path.join(case, "index.html")),
    }


CSS = """
/* Minimal theme, same as the reports (tokens are read from export-hub.py at build time) */
:root{--ink:#1c252e;--bg:#fff;--surface:#f4f6f8;--muted:#637381;--line:rgba(145,158,171,.28);--purple:#00a76f;--link:#007867;--tint:rgba(0,167,111,.08);--tint2:rgba(0,167,111,.16);--on-purple:#fff;--r:8px;color-scheme:light}
*{box-sizing:border-box}
html{overflow-y:scroll}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 "Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
header.top{position:sticky;top:0;z-index:20;background:rgba(255,255,255,.86);backdrop-filter:blur(6px);border-bottom:1px dashed var(--line)}
.wrap{max-width:1040px;margin:0 auto;padding:0 20px}
.brand{display:flex;align-items:center;gap:10px;padding:14px 0;font-weight:800;letter-spacing:-.01em}
.logo{width:34px;height:auto;color:var(--ink)}
h1{font-size:1.9rem;line-height:1.2;margin:40px 0 8px;font-weight:800;letter-spacing:-.01em}
.lede{color:var(--muted);margin:0 0 28px;max-width:60ch}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:24px;margin:0 0 56px}
a.card,div.card{display:flex;flex-direction:column;gap:10px;padding:24px;border:0;border-radius:16px;background:#fff;color:inherit;text-decoration:none;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12);transition:box-shadow .2s,transform .2s}
a.card:hover,a.card:focus-visible{box-shadow:0 0 2px 0 rgba(145,158,171,.24),0 20px 40px -4px rgba(145,158,171,.24);transform:translateY(-2px);outline:0}
a.card:focus-visible{box-shadow:0 0 0 2px var(--purple)}
.card.off{opacity:.7}
.kind{align-self:flex-start;font-size:.75rem;font-weight:700;line-height:24px;padding:0 8px;border-radius:6px;background:var(--tint2);color:var(--link)}
.kind.Example{background:rgba(0,184,217,.16);color:#006c9c}
.kind.Template{background:rgba(145,158,171,.16);color:#637381}
.card h2{margin:0;font-size:1.15rem;line-height:1.35;font-weight:700;color:var(--ink)}
.card p{margin:0;color:var(--muted);font-size:.93rem}
.q{color:var(--ink)!important}
.meta{display:flex;flex-wrap:wrap;gap:6px 14px;margin-top:auto;padding-top:14px;border-top:1px dashed var(--line);font-size:.84rem;color:var(--muted)}
.meta b{color:var(--ink);font-weight:800}
.stage{font-weight:700;color:var(--link)}
.open{margin-left:auto;font-weight:700;color:var(--link)}
section h3{font-size:.8rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);font-weight:700;margin:0 0 16px}
code{font:.88em ui-monospace,SFMono-Regular,Menlo,monospace;background:var(--surface);padding:2px 6px;border-radius:6px}
footer{padding:24px 0 48px;border-top:1px dashed var(--line);color:var(--muted);font-size:.88rem}
"""


def minimal_tokens():
    """The colour tokens of the report's Minimal theme, as a :root rule (None if not found)."""
    here = os.path.dirname(os.path.abspath(__file__))
    m = re.search(r"\[data-theme=minimal\]\{(--ink:[^}]*)\}", read(os.path.join(here, "export-hub.py")))
    return ":root{%s;color-scheme:light}" % m.group(1) if m else None


def render(cards, title, logo):
    def card(c):
        tag = "a" if c["report"] else "div"
        href = ' href="%s/index.html"' % html.escape(c["dir"], quote=True) if c["report"] else ""
        cls = "card" if c["report"] else "card off"
        parts = ['<%s class="%s"%s>' % (tag, cls, href), '<span class="kind %s">%s</span>' % (c["kind"], c["kind"]),
                 "<h2>%s</h2>" % html.escape(c["name"])]
        if c["question"]:
            parts.append('<p class="q">%s</p>' % html.escape(c["question"]))
        if c["desc"]:
            parts.append("<p>%s</p>" % html.escape(c["desc"]))
        meta = []
        if c["stage"]:
            meta.append('<span class="stage">%s</span>' % html.escape(c["stage"]))
        if c["owner"]:
            meta.append("<span>Owner: %s</span>" % html.escape(c["owner"]))
        meta.append("<span><b>%d</b> items</span>" % c["items"])
        docs = "<span><b>%d</b> documents" % c["docs"]
        docs += " <small>(+%d planned)</small></span>" % c["planned"] if c["planned"] else "</span>"
        meta.append(docs)
        meta.append('<span class="open">%s</span>' % ("Open report &rarr;" if c["report"] else "No report yet"))
        parts.append('<div class="meta">%s</div>' % "".join(meta))
        parts.append("</%s>" % tag)
        return "".join(parts)

    real = [c for c in cards if c["kind"] == "Project"]
    other = [c for c in cards if c["kind"] != "Project"]
    body = []
    if real:
        body.append('<section><h3>Your projects</h3><div class="grid">%s</div></section>' % "".join(card(c) for c in real))
    else:
        body.append('<section><h3>Your projects</h3><p class="lede">No project yet. Create one with '
                    '<code>python3 toolkit/tools/new-case.py project-name</code>, or ask your AI tool: '
                    '&ldquo;Create a new project called &hellip;&rdquo;.</p></section>')
    if other:
        body.append('<section><h3>Examples and template</h3><div class="grid">%s</div></section>' % "".join(card(c) for c in other))
    return """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>%(css)s</style>
</head>
<body>
<header class="top"><div class="wrap"><div class="brand">%(logo)s<span>%(title)s</span></div></div></header>
<main class="wrap">
<h1>All projects</h1>
<p class="lede">Every project in this workspace, in one place. Open a card to see that project&rsquo;s report.</p>
%(body)s
</main>
<footer><div class="wrap">This page is generated from the project folders. To refresh it, rebuild any report or run <code>export-home.py</code>.</div></footer>
</body>
</html>
""" % {"title": html.escape(title), "css": CSS + (minimal_tokens() or ""), "logo": logo, "body": "\n".join(body)}


def load_logo():
    here = os.path.dirname(os.path.abspath(__file__))
    src = read(os.path.join(here, "export-hub.py"))
    m = re.search(r'<svg class="logo".*?</svg>', src, flags=re.S)
    return m.group(0) if m else ""


def main():
    ap = argparse.ArgumentParser(description="Build the workspace home page (index.html at the workspace root).")
    ap.add_argument("--workspace", help="workspace folder (default: the one you are in)")
    ap.add_argument("--title", default="Product Workspace")
    ap.add_argument("--out", help="output file (default: <workspace>/index.html)")
    a = ap.parse_args()
    ws = os.path.abspath(a.workspace) if a.workspace else find_workspace(os.getcwd())
    if not ws or not os.path.isdir(ws):
        sys.exit("Workspace not found. Run inside the workspace, or pass --workspace <path>.")
    dirs = sorted(d for d in os.listdir(ws) if not d.startswith((".", "_")) and is_case(os.path.join(ws, d)))
    dirs = [d for d in dirs if d not in EXAMPLES] + [d for d in EXAMPLES if d in dirs]
    cards = [case_card(ws, d) for d in dirs]
    out = a.out or os.path.join(ws, "index.html")
    page = render(cards, a.title, load_logo())
    if read(out) != page:
        with open(out, "w", encoding="utf-8") as f:
            f.write(page)
    print("Home: %d project card(s) -> %s" % (len(cards), out))


if __name__ == "__main__":
    main()
