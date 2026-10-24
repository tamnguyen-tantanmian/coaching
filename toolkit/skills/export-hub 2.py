#!/usr/bin/env python3
"""Export the markdown hub of a case folder to ONE self-contained HTML file.

    python3 export-hub.py                 # case = the case folder you are in -> <case>/index.html
    python3 export-hub.py --case PATH     # another case folder
    python3 export-hub.py --out FILE.html # custom output path (e.g. a copy to send)

Why a script and not an AI tool: turning markdown into HTML and tracing links between items is
deterministic. A script gives the same output every time, invents nothing and sends no data anywhere.
Python 3.8+ standard library only.

The report is an OUTPUT. Never edit it by hand: change the markdown and export again.

Included : README.md, stages/, work/, insights/, standards/ and context/
Excluded : AI drafts, _personal/, work/sources/, AGENTS.md

Layout: Overview, Context, Stages, Work, Insights, Standards (one menu item per top-level folder). Items (O, H, M, D, E) are not in the menu:
they live in the Trace tab as a tree  Opportunity > Hypothesis > Decision / Evidence / Metric, with search
and filters, so the report still works with hundreds of items.
"""
import argparse
import base64
import datetime
import html
import mimetypes
import os
import re
import sys

def find_case(start=None):
    """The case folder: the nearest folder, from `start` (default: the current folder) upwards,
    that has AGENTS.md next to insights/ or work/. Falls back to the folder above this script
    (a copy of this script in the workspace's toolkit/skills/ folder)."""
    p = os.path.abspath(start or os.getcwd())
    while True:
        if os.path.isfile(os.path.join(p, "AGENTS.md")) and (
                os.path.isdir(os.path.join(p, "insights")) or os.path.isdir(os.path.join(p, "work"))):
            return p
        parent = os.path.dirname(p)
        if parent == p:
            break
        p = parent
    legacy = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isdir(os.path.join(legacy, "insights")):
        return legacy
    return None

import csv
import shutil
import urllib.parse

TYPES = [
    # letter, folder, singular, plural
    ("O", "opportunities", "Opportunity", "Opportunities"),
    ("H", "hypotheses", "Hypothesis", "Hypotheses"),
    ("M", "metrics", "Metric", "Metrics"),
    ("D", "decisions", "Design decision", "Decisions"),
    ("E", "evidence", "Evidence", "Evidence"),
    ("F", "findings", "Finding", "Findings"),
]
LETTER_NAME = {t[0]: t[2] for t in TYPES}
EXCLUDE_HUB_FILES = {"how-the-hub-works.md"}
VI_NAME = {"O": ("Opportunity", "Opportunity"), "H": ("Hypothesis", "Hypothesis"), "M": ("Metric", "Metric"),
           "D": ("Decision", "Design decision"), "E": ("Evidence", "Evidence"), "F": ("Finding", "Finding")}
CLOSED_STATES = {"shipped", "superseded", "dropped"}
SEVERITY_LABEL = {"0": "0 · Not a problem", "1": "1 · Cosmetic", "2": "2 · Minor", "3": "3 · Major", "4": "4 · Catastrophe"}
RESOLUTION_LABEL = {"open": "Open", "fixed": "Fixed", "accepted": "Accepted", "deferred": "Deferred"}
RESOLVED = {"fixed", "accepted", "deferred"}
STATE_LABEL = {"proposed": "Proposed", "accepted": "Accepted", "active": "Active", "shipped": "Shipped", "superseded": "Superseded", "dropped": "Dropped"}
VERDICT_LABEL = {"pending": "Not measured", "met": "Target met", "missed": "Target missed", "inconclusive": "Inconclusive"}
LEVEL_LABEL = {"high": "High", "medium": "Medium", "low": "Low"}
VI_SHORT = {"O": "Opportunity", "H": "Hypothesis", "M": "Metric", "D": "Decision", "E": "Evidence", "F": "Finding"}
PROP_LABEL = {"type": "Type", "rank": "Rank", "evidence": "Evidence source", "serves": "Serves need", "metric": "Metric",
              "tests": "Tests hypothesis", "follows": "Follows principle", "pulls_against": "Pulls against principle",
              "measures": "Measures metric", "status": "Status", "baseline": "Baseline", "measured_by": "Measured by",
              "participants": "Participants", "result": "Result", "participants_type": "Participant type",
              "area": "Area", "state": "State", "owner": "Owner", "decided_on": "Decided on",
              "impact": "Impact", "confidence": "Confidence", "rank_reason": "Rank reason",
              "target": "Target", "measured_on": "Measured on", "verdict": "Verdict", "solutions": "Solution codes",
              "severity": "Severity", "found_in": "Found in", "affects": "Affects decision",
              "principle": "Principle violated", "resolution": "Resolution"}
VALUE_LABEL = {"status": {"assumed": "Assumed", "planned": "Planned", "run": "Run"},
               "participants_type": {"simulated": "Simulated", "real": "Real users"},
               "state": STATE_LABEL,
               "verdict": VERDICT_LABEL, "impact": LEVEL_LABEL, "confidence": LEVEL_LABEL,
               "severity": SEVERITY_LABEL,
               "resolution": RESOLUTION_LABEL}
BACK_LABEL = {"serves": "Served by", "metric": "Metric of", "tests": "Tested by",
              "measures": "Measured by", "follows": "Followed by", "pulls_against": "Pulled against by",
              "found_in": "Has finding", "affects": "Affected by finding"}
STATUS_VI = {"open": "Open", "passed": "Passed", "failed": "Failed"}
AGREE_VI = {"agreed": "Agreed", "pending": "Pending", "not available": "Not available"}


# --------------------------------------------------------------------------- markdown (subset)
def _split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, cur, in_code = [], "", False
    i = 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur += "|"
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append(cur.strip())
            cur = ""
        else:
            cur += ch
        i += 1
    cells.append(cur.strip())
    return cells


def _is_sep(line):
    s = line.strip()
    return s.startswith("|") and re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)*\|?", s) is not None


class Renderer(object):
    def __init__(self, src_path, resolver, problems):
        self.src = src_path
        self.resolve = resolver
        self.problems = problems

    def inline(self, text):
        text = html.escape(text, quote=False)
        codes, links = [], []

        def stash_code(m):
            codes.append("<code>%s</code>" % m.group(1))
            return "\x00C%d\x00" % (len(codes) - 1)

        text = re.sub(r"`([^`]+)`", stash_code, text)

        def stash_link(m):
            label, url = m.group(1), html.unescape(m.group(2)).strip()
            is_img = m.group(0).startswith("!")
            kind, val = self.resolve(self.src, url, is_img)
            inner = self._emph(label)
            if is_img:
                if kind == "file" and os.path.splitext(url.split("#")[0])[1].lower() in VIDEO_EXT:
                    out = '<video controls preload="metadata" src="%s"></video>' % val
                elif kind == "file":
                    out = '<a href="%s" target="_blank" rel="noopener"><img loading="lazy" src="%s" alt="%s"></a>' % (val, val, html.escape(label, quote=True))
                elif kind == "data":
                    out = '<img src="%s" alt="%s">' % (val, html.escape(label, quote=True))
                else:
                    out = '<span class="ext">[image: %s]</span>' % (label or url)
            elif kind == "file":
                out = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (val, inner)
            elif kind == "page":
                out = '<a href="#/%s">%s</a>' % (val, inner)
            elif kind == "web":
                out = '<a href="%s" target="_blank" rel="noopener">%s</a>' % (html.escape(val, quote=True), inner)
            elif kind == "anchor":
                out = '<span class="ext">%s</span>' % inner
            elif kind == "outside":
                out = '<span class="ext" title="Outside the report: %s">%s</span>' % (html.escape(val, quote=True), inner)
            else:
                self.problems.append("Broken link in %s: %s" % (os.path.basename(self.src), url))
                out = '<span class="broken" title="Broken link: %s">%s</span>' % (html.escape(url, quote=True), inner)
            links.append(out)
            return "\x00L%d\x00" % (len(links) - 1)

        text = re.sub(r"!?\[([^\]]*)\]\(([^)\s]+)\)", stash_link, text)
        text = self._emph(text)
        text = re.sub(r"\x00L(\d+)\x00", lambda m: links[int(m.group(1))], text)
        text = re.sub(r"\x00C(\d+)\x00", lambda m: codes[int(m.group(1))], text)
        return text

    @staticmethod
    def _emph(text):
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        return re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", text)

    def render(self, md):
        lines = md.replace("\r\n", "\n").split("\n")
        out, i, n = [], 0, len(lines)
        while i < n:
            s = lines[i].strip()
            if not s:
                i += 1
                continue
            if s.startswith("<!--") and s.endswith("-->"):
                i += 1
                continue
            if s.startswith("```"):
                buf = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    buf.append(lines[i])
                    i += 1
                i += 1
                out.append("<pre><code>%s</code></pre>" % html.escape("\n".join(buf), quote=False))
                continue
            m = re.match(r"(#{1,6})\s+(.*)", s)
            if m:
                lvl = len(m.group(1))
                out.append("<h%d>%s</h%d>" % (lvl, self.inline(m.group(2)), lvl))
                i += 1
                continue
            if re.fullmatch(r"-{3,}|\*{3,}", s):
                out.append("<hr>")
                i += 1
                continue
            if s.startswith(">"):
                buf = []
                while i < n and lines[i].strip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                if re.match(r"\s*\*\*(?:Cách điền|How to fill)", "\n".join(buf)):
                    continue  # authoring hint for the writer, not for the reader of the report
                out.append("<blockquote>%s</blockquote>" % self.render("\n".join(buf)))
                continue
            if s.startswith("|") and i + 1 < n and _is_sep(lines[i + 1]):
                head = _split_row(lines[i])
                i += 2
                rows = []
                while i < n and lines[i].strip().startswith("|"):
                    rows.append(_split_row(lines[i]))
                    i += 1
                thead = ""
                if any(c.strip() for c in head):
                    thead = "<thead><tr>%s</tr></thead>" % "".join('<th scope="col">%s</th>' % self.inline(c) for c in head)
                body = ""
                for r in rows:
                    r = (r + [""] * len(head))[: len(head)]
                    body += "<tr>%s</tr>" % "".join("<td>%s</td>" % self.inline(c) for c in r)
                cols, cls = "", ""
                if len(head) >= 3:
                    # balance the columns: width follows the typical text length, softened and clamped
                    ws = []
                    for k in range(len(head)):
                        cells = [re.sub(r"[`*_\[\]()]", "", (r[k] if k < len(r) else "")) for r in rows]
                        lens = [len(c.strip()) for c in cells if c.strip()]
                        avg = sum(lens) / len(lens) if lens else 0
                        ws.append(max(avg, len(head[k].strip()), 6) ** 0.6)
                    tot = sum(ws) or 1
                    # floor per column: the longest word of the header (and of the cells) must not be cut mid-word
                    floors_px = []
                    for k in range(len(head)):
                        words = re.sub(r"[`*_\[\]()]", "", head[k]).split()
                        for r in rows[:30]:
                            words += re.sub(r"[`*_\[\]()]", "", (r[k] if k < len(r) else "")).split()
                        longest = max([len(w_) for w_ in words if len(w_) <= 14] or [4])
                        floors_px.append(min(112, max(70, longest * 8 + 26)))
                    fl = [fp / 8.0 for fp in floors_px]  # px to percent of an ~800px content column
                    spare = max(0.0, 100.0 - sum(fl))
                    pct = [f_ + spare * w / tot for f_, w in zip(fl, ws)]
                    tp = sum(pct)
                    cols = "<colgroup>%s</colgroup>" % "".join('<col style="width:%.1f%%">' % (100.0 * x / tp) for x in pct)
                    minw = sum(floors_px)
                    cls = ' class="bal" style="min-width:%dpx"' % minw
                out.append('<div class="table-wrap"><table%s>%s%s<tbody>%s</tbody></table></div>' % (cls, cols, thead, body))
                continue
            if re.match(r"([-*]|\d+\.)\s+", s):
                block, i = self._list(lines, i)
                out.append(block)
                continue
            buf = []
            while i < n and lines[i].strip() and not re.match(r"(#{1,6}\s|```|>|\||([-*]|\d+\.)\s+|-{3,}$)", lines[i].strip()):
                buf.append(lines[i].strip())
                i += 1
            if not buf:
                buf.append(lines[i].strip())
                i += 1
            out.append("<p>%s</p>" % self.inline(" ".join(buf)))
        return "\n".join(out)

    def _list(self, lines, i):
        n = len(lines)
        items = []
        while i < n:
            line = lines[i]
            m = re.match(r"^(\s*)([-*]|\d+\.)\s+(.*)", line)
            if m:
                items.append([len(m.group(1).replace("\t", "    ")), m.group(2)[0].isdigit(), m.group(3)])
                i += 1
            elif line.strip() and items and re.match(r"^\s{2,}\S", line):
                items[-1][2] += " " + line.strip()
                i += 1
            else:
                break

        def build(pos, indent):
            parts, ordered = [], items[pos][1]
            while pos < len(items) and items[pos][0] >= indent:
                ind, _, text = items[pos]
                if ind > indent:
                    sub, pos = build(pos, ind)
                    if parts:
                        parts[-1] = parts[-1][:-5] + sub + "</li>"
                    continue
                cb = re.match(r"\[( |x|X)\]\s+(.*)", text)
                li = self.inline(cb.group(2)) if cb else self.inline(text)
                if cb:
                    li = '<span class="box" aria-hidden="true">%s</span> %s' % ("☑" if cb.group(1) != " " else "☐", li)
                parts.append("<li>%s</li>" % li)
                pos += 1
            tag = "ol" if ordered else "ul"
            return "<%s>%s</%s>" % (tag, "".join(parts), tag), pos

        block, _ = build(0, items[0][0])
        return block, i


# --------------------------------------------------------------------------- model
class Page(object):
    def __init__(self, pid, path, kind, label=None):
        self.id, self.path, self.kind = pid, path, kind
        self.md = open(path, encoding="utf-8").read()
        m = re.search(r"^#\s+(.+)$", self.md, flags=re.M)
        self.heading = m.group(1).strip() if m else pid
        self.label = label or self.heading
        self.letter = None
        self.title = self.heading
        self.meta = {}
        self.rank = 999


class StagePage(object):
    """A stage of the project, assembled from work files and item tables (see stage_specs)."""
    kind = "week"
    letter = None

    def __init__(self, spec, case):
        self.spec = spec
        self.id = self.slug = spec["id"]
        self.path = os.path.join(case, "stages", "README.md")
        self.heading = self.label = self.title = spec["label"]
        self.meta, self.rank = {}, 999
        self.parts, self.missing = [], []
        work = os.path.join(case, "work")
        for ref in spec["work"]:
            cand = os.path.join(case, ref) if ref.split("/")[0] in ("insights", "standards", "context") else os.path.join(work, ref)
            if os.path.isdir(cand):
                cand = os.path.join(cand, "index.md")
            if os.path.isfile(cand):
                meta, body = _front(open(cand, encoding="utf-8").read())
                body = re.sub(r"^\s*#\s+.*\n", "", body, count=1)
                self.parts.append((cand, meta, body))
            else:
                self.missing.append(ref)
        self.md = "\n\n".join(b for _, _, b in self.parts)


def _unq(s):
    s = s.strip()
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "\"'":
        s = s[1:-1]
    return s


def _csv(s):
    out, cur, q = [], "", None
    for ch in s:
        if q:
            cur += ch
            if ch == q:
                q = None
        elif ch in "\"'":
            q = ch
            cur += ch
        elif ch == ",":
            out.append(cur)
            cur = ""
        else:
            cur += ch
    if cur.strip():
        out.append(cur)
    return out


def _front(md):
    """YAML front matter (small subset: scalars, inline lists, '- item' lists) -> (dict, body)"""
    m = re.match(r"---[ \t]*\n(.*?)\n---[ \t]*\n?", md, flags=re.S)
    if not m:
        return {}, md
    data, key = {}, None
    for line in m.group(1).split("\n"):
        if not line.strip() or line.strip().startswith("#"):
            continue
        li = re.match(r"^\s+-\s+(.*)$", line)
        if li and key is not None:
            if not isinstance(data.get(key), list):
                data[key] = []
            data[key].append(_unq(li.group(1)))
            continue
        kv = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if kv:
            key, val = kv.group(1).lower(), kv.group(2).strip()
            if val == "":
                data[key] = []
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                data[key] = [_unq(x) for x in _csv(inner)] if inner else []
            else:
                data[key] = _unq(val)
    return data, md[m.end():]


REL_KEYS = ("serves", "metric", "tests", "measures", "follows", "pulls_against", "found_in", "affects", "principle")
TYPE_WORD = {"O": "opportunity", "H": "hypothesis", "M": "metric", "D": "decision", "E": "evidence", "F": "finding"}


def _ids(value):
    if isinstance(value, list):
        value = " ".join(value)
    v = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", value or "")
    v = re.sub(r"\[\[([^\]]+)\]\]", r"\1", v)
    v = re.sub(r"\]\([^)]*\)", "]", v)
    return re.findall(r"\b([OHMDEFP]\d+)\b", v)


def _natkey(s):
    return [int(t) if t.isdigit() else t for t in re.split(r"(\d+)", s)]


def collect(case):
    """Everything the report shows. A folder at the top of the case is a menu item of the report:
    stages/, work/ (see collect_artifacts), insights/, standards/ and context/; README.md is the Overview."""
    ov = os.path.join(case, "README.md")
    if not os.path.isfile(ov):
        sys.exit("README.md not found in %s" % case)
    overview = Page("overview", ov, "overview")
    weekly, items, ref, ctx = [], [], [], []
    # Stage pages: one per row of the Pages table in stages/README.md, in that order. Nothing to write per stage:
    # each page is built from the work files named in the row and the item tables chosen there.
    idx_ = os.path.join(case, "stages", "README.md")
    for spec in stage_specs(open(idx_, encoding="utf-8").read() if os.path.isfile(idx_) else ""):
        weekly.append(StagePage(spec, case))
    # Reference pages: every .md file in reference/ (README.md excluded). Drop a new file there and it appears.
    # Known pages keep their ids and come first; the rest follow alphabetically, and the case log goes last.
    ref_dir = os.path.join(case, "standards")
    if not os.path.isdir(ref_dir) and os.path.isdir(os.path.join(case, "reference")):  # cases made before the rename
        ref_dir = os.path.join(case, "reference")
    known = {"gates": ("gates", "Gates"), "principle-checks": ("principles", "Principle checks"),
             "severity-levels": ("severity", "Severity levels")}
    first = ["gates", "principle-checks", "severity-levels"]
    stems = sorted(f[:-3] for f in os.listdir(ref_dir) if f.endswith(".md") and f.lower() != "readme.md") if os.path.isdir(ref_dir) else []
    for st in [x for x in first if x in stems] + [x for x in stems if x not in first and x not in ("case-log", "how-the-hub-works")]:
        pid, lab = known.get(st, (st, None))
        ref.append(Page(pid, os.path.join(ref_dir, st + ".md"), "ref", lab))
    # Context pages: every .md in context/ (README.md excluded), the usual ones first.
    ctx_dir = os.path.join(case, "context")
    cfirst = ["product-and-users", "accessibility-rules", "data-rules", "design-system-notes", "glossary", "open-questions"]
    cstems = sorted(f[:-3] for f in os.listdir(ctx_dir) if f.endswith(".md") and f.lower() != "readme.md") if os.path.isdir(ctx_dir) else []
    for st in [x for x in cfirst if x in cstems] + [x for x in cstems if x not in cfirst]:
        ctx.append(Page(st, os.path.join(ctx_dir, st + ".md"), "ref", None))
    letters = {t[0] for t in TYPES}
    # Items live in insights/<type>/ (folders starting with _ hold templates and are skipped).
    found = []
    for dirpath, dirnames, filenames in os.walk(os.path.join(case, "insights")):
        dirnames[:] = sorted(d for d in dirnames if not d.startswith((".", "_")))
        for name in filenames:
            found.append((name, os.path.join(dirpath, name)))
    for name, path in sorted(found, key=lambda x: _natkey(x[0])):
        m = re.match(r"([A-Z])\d+\.md$", name)
        if m and m.group(1) in letters:
            p = Page(name[:-3], path, "item")
            p.letter = m.group(1)
            p.meta, p.body = _front(p.md)
            hm = re.search(r"^#\s+(?:[A-Z]\d+:\s*)?(.+)$", p.body, flags=re.M)
            p.title = str(p.meta.get("title") or (hm.group(1) if hm else name[:-3])).strip()
            r = re.search(r"\d+", str(p.meta.get("rank", "")))
            p.rank = int(r.group(0)) if r else 999
            items.append(p)
    return overview, weekly, items, ref, ctx


def case_info(overview_md, case):
    name = os.path.basename(os.path.abspath(case))
    if name == "my-case":  # the blank template has no project yet
        name = "Product Name"
    m = re.search(r"^\|\s*(?:Tên (?:dự án|case)|Project name|Project)\s*\|\s*([^|\s][^|]*?)\s*\|\s*$", overview_md, flags=re.M)
    if m and not m.group(1).startswith("["):
        name = re.sub(r"[*`]", "", m.group(1))
    status = ""
    m = re.search(r"^\|\s*Agreement status\s*\|\s*([^|\s][^|]*?)\s*\|\s*$", overview_md, flags=re.M)
    if m:
        status = re.sub(r"\*.*?\*|[*`]", "", m.group(1)).strip()
    return name, status


def stage_specs(md):
    """Rows of the Pages table in stages/README.md: Id | Page | Stage | Content | From work | Item tables.
    A stage page is built from these rows alone: there is no file to write per stage."""
    out = []
    for line in md.split("\n"):
        if not line.strip().startswith("|"):
            continue
        c = _split_row(line)
        if len(c) < 6:
            continue
        sid = c[0].strip("` ")
        if not re.fullmatch(r"[a-z][a-z0-9-]*", sid) or sid == "id":
            continue
        out.append({
            "id": sid, "label": re.sub(r"[*`]", "", c[1]).strip() or sid, "stage": c[2].strip(), "desc": c[3].strip(),
            "work": [re.sub(r"^work/", "", t.strip()) for t in re.findall(r"`([^`]+)`", c[4]) if t.strip()],
            "tables": [t.strip().lower() for t in re.split(r"[,\s]+", c[5].replace("`", "")) if t.strip()],
        })
    return out


def stage_table_issues(md):
    """Rows of the Pages table that stage_specs skips, so a mistake or an old-format table is never silent."""
    out = []
    in_pages = False
    for line in md.split("\n"):
        if line.startswith("## "):
            in_pages = line.strip().lower() == "## pages"
            continue
        if not in_pages or not line.strip().startswith("|") or _is_sep(line):
            continue
        c = _split_row(line)
        sid = c[0].strip("` ") if c else ""
        if sid.lower() in ("id", "page", "") and not re.fullmatch(r"[a-z][a-z0-9-]*", sid or "-"):
            continue
        if sid.lower() == "id":
            continue
        if len(c) < 6:
            out.append("Stages: row \"%s\" in the Pages table has %d columns, needs 6 (Id, Page, Stage, Content, From work, Item tables)" % (sid[:40], len(c)))
        elif not re.fullmatch(r"[a-z][a-z0-9-]*", sid):
            out.append("Stages: Id \"%s\" is not valid (lowercase, no accents, joined by hyphens)" % sid[:40])
    return out


def week_info(overview_md):
    """slug -> (stage, description, label) from the Pages table in stages/README.md"""
    return {sp["id"]: (sp["stage"], sp["desc"], sp["label"]) for sp in stage_specs(overview_md)}


def parse_gates(md):
    out, cur = [], None
    for line in md.split("\n"):
        h = re.match(r"##\s+Gate\s+\d+:\s*(.+)", line)
        if h:
            cur = {"name": h.group(1).strip(), "checks": []}
            out.append(cur)
            continue
        if cur and line.strip().startswith("|"):
            c = _split_row(line)
            if len(c) >= 3 and re.fullmatch(r"\d[a-z]", c[0]):
                cur["checks"].append((c[0], c[1], c[2].strip().lower()))
    for g in out:
        st = [c[2] for c in g["checks"]]
        g["passed"] = sum(1 for s in st if s == "passed")
        g["total"] = len(st)
        g["status"] = "failed" if "failed" in st else ("passed" if st and all(s == "passed" for s in st) else "open")
    return out


def parse_principles(md):
    out = {}
    for line in md.split("\n"):
        if line.strip().startswith("|"):
            c = _split_row(line)
            if len(c) >= 3 and re.fullmatch(r"P\d+", c[0]):
                out[c[0]] = (c[1], c[2].strip())
    return out


def parse_case_log(md):
    """rows of the case log table: (date, decision, reason, [ids])"""
    rows = []
    for line in md.split("\n"):
        if not line.strip().startswith("|"):
            continue
        c = _split_row(line)
        if len(c) < 4 or set(c[0]) <= set("-: ") or c[0].lower() in ("date", "ngày", "ngay"):
            continue
        if not any(x.strip() for x in c):
            continue
        rows.append((c[0], c[1], c[2], _ids(c[3])))
    return rows


def auto_checks(G, principles):
    """Checks of the gates that the data can answer by itself: check id -> (ok or None, detail).
    They are shown next to the status a person set; they never change it."""
    out = {}
    PLACEHOLDERS = ("quote ID hoặc nguồn", "quote ID or source")  # the template text, in either language
    NO_SOURCE = ("chưa có", "none yet")

    def has_src(o):
        v = str(G.items[o].meta.get("evidence", "")).strip()
        return bool(v) and v.lower() not in NO_SOURCE and not any(ph in v for ph in PLACEHOLDERS)

    O = [o for o in G.O if o not in G.closed]
    H = [h for h in G.H if h not in G.closed]
    D = [d for d in G.D if d not in G.closed]
    if O:
        n = sum(1 for o in O if has_src(o))
        for cid in ("1b", "2a"):
            out[cid] = (n == len(O), "%d of %d opportunities have an evidence source" % (n, len(O)))
    if H:
        n = sum(1 for h in H if G.tests_of(h) and G.metric.get(h))
        out["2c"] = (n == len(H), "%d of %d hypotheses have evidence and a metric" % (n, len(H)))
    real = [(k, nm, chk) for k, (nm, chk) in principles.items() if not nm.startswith("(")]
    if real:
        n = sum(1 for _, _, chk in real if chk.strip())
        out["2d"] = (n == len(real), "%d of %d principles have a yes/no question" % (n, len(real)))
    if D:
        unlinked = sum(1 for d in D if not any(G.serves.get(h) for h in G.tests.get(d, [])))
        unserved = sum(1 for o in O if not any(G.decisions_of(h) for h in G.hyps_of(o)))
        out["3b"] = (unlinked == 0 and unserved == 0, "%d decisions not traced to a need, %d opportunities without a decision" % (unlinked, unserved))
        n = sum(1 for d in D if G.follows.get(d) or G.strains.get(d))
        out["3c"] = (n == len(D), "%d of %d decisions checked against principles" % (n, len(D)))
    if H:
        def kind(t):
            m = G.items[t].meta
            return not (str(m.get("status", "")).lower() == "planned" or str(m.get("participants_type", "")).lower() == "simulated")
        n = sum(1 for h in H if any(kind(t) for t in G.tests_of(h)))
        out["4a"] = (n == len(H), "%d of %d hypotheses have evidence from real users" % (n, len(H)))
    if G.F:
        bad = [f for f in G.F if G.severity[f] is None or not G.found_in[f]]
        out["4b"] = (not bad, "%d findings, %d missing severity or source" % (len(G.F), len(bad)))
    return out


# --------------------------------------------------------------------------- graph
def _gen_tables(G, page_dir):
    """The six tables of the stage pages, built from the item files (the single source of truth)."""
    def link(i):
        p = G.items[i]
        folder = {"O": "opportunities", "H": "hypotheses", "M": "metrics", "D": "decisions", "E": "evidence", "F": "findings"}[p.letter]
        rel = os.path.relpath(p.path, page_dir).replace(os.sep, "/")
        return "[%s](%s)" % (i, rel)

    def ids(xs):
        return ", ".join(xs) if xs else "—"

    def row(cells):
        return "| " + " | ".join(str(c).replace("|", "\\|").replace("\n", " ") for c in cells) + " |"

    def table(head, rows):
        return "\n".join([row(head), "|" + "---|" * len(head)] + rows)

    T = {}
    def lvl(o, k):
        v = str(G.items[o].meta.get(k) or "").strip().lower()
        return LEVEL_LABEL.get(v, v) or "\u2014"

    def met(m, k, dash="\u2014"):
        return str(G.items[m].meta.get(k) or "").strip() or dash

    T["opportunities"] = table(["Rank", "ID", "Opportunity", "Impact", "Confidence", "Rank reason"], [
        row([n + 1, link(o), G.items[o].title, lvl(o, "impact"), lvl(o, "confidence"), met(o, "rank_reason")]) for n, o in enumerate(G.O)])
    T["hypotheses"] = table(["ID", "Hypothesis", "Serves", "Evidence"], [
        row([link(h), G.items[h].title, ids(G.serves.get(h, [])), ", ".join(G.tests_of(h)) or "none yet"]) for h in G.H])
    T["metrics"] = table(["ID", "Metric", "Baseline", "Target", "Result", "Verdict"], [
        row([link(m), G.items[m].title, met(m, "baseline", "unknown"), met(m, "target"), met(m, "result"),
             VERDICT_LABEL.get(met(m, "verdict", "pending").lower(), met(m, "verdict", "pending"))]) for m in G.M])
    T["decisions"] = table(["ID", "Decision", "Tests", "Follows principle", "Pulls against principle", "Owner", "Date", "State"], [
        row([link(d), G.items[d].title, ids(G.tests.get(d, [])), ids(G.follows.get(d, [])), ids(G.strains.get(d, [])),
             met(d, "owner"), met(d, "decided_on"), STATE_LABEL.get(G.state.get(d, ""), G.state.get(d) or "\u2014")]) for d in G.D])
    T["evidence"] = table(["ID", "Evidence", "Tests", "Measures"], [
        row([link(e), G.items[e].title, ids(G.tests.get(e, [])), ids(G.measures.get(e, []))]) for e in G.E])

    def opps_of_metric(m):
        hs = [h for h in G.H if m in G.metric.get(h, [])]
        return hs, sorted({o for h in hs for o in G.serves.get(h, [])}, key=_natkey)

    def outcome_row(m):
        hs, os_ = opps_of_metric(m)
        vd = met(m, "verdict", "pending").lower()
        back = ids(os_) + (" (revisit)" if vd == "missed" and os_ else "")
        return row([link(m), G.items[m].title, met(m, "target"), met(m, "result"), met(m, "measured_on"),
                    VERDICT_LABEL.get(vd, vd), ids(hs), back])
    T["outcomes"] = table(["ID", "Metric", "Target", "Result", "Measured on", "Verdict", "Hypothesis", "Opportunity behind it"],
                          [outcome_row(m) for m in G.M])
    fo = sorted(G.F, key=lambda f: (-(G.severity[f] if G.severity[f] is not None else -1), _natkey(f)))
    T["findings"] = table(["ID", "Finding", "Severity", "Principle", "Found in", "Affects", "Resolution"], [
        row([link(f), G.items[f].title,
             SEVERITY_LABEL.get(str(G.severity[f]), "not rated").replace(" · ", " ") if G.severity[f] is not None else "not rated",
             ids(G.principle_of.get(f, [])), ids(G.found_in.get(f, [])), ids(G.affects.get(f, [])),
             G.resolution.get(f, "open").capitalize()]) for f in fo])
    return T


# How much a warning matters. "block": the case's conclusions are not safe to hand off yet.
# "review": worth a look, the owner decides. "info": housekeeping; listed, never counted, no badge on items.
WARN_TIER = {
    "no-need": "block", "d-no-owner": "review", "o-no-reason": "review", "m-no-target": "review", "m-no-result": "review", "m-missed": "review", "f-sev4": "block", "d-open-finding": "block", "gate-mismatch": "block", "log-unknown-id": "block",
    "strain": "review", "unserved": "review", "untested": "review", "nometric": "review", "no-real-evidence": "review",
    "f-sev3": "review", "f-noevidence": "review", "f-nosev": "review", "simulated": "review", "no-log": "review",
    "planned": "info", "art-orphan": "info", "principles": "info",
}
TIER_LABEL = {"block": "Fix before handoff", "review": "Worth a look", "info": "Housekeeping"}


def warn_tier(kind):
    return WARN_TIER.get(kind, "review")


class Graph(object):
    def __init__(self, items, principles):
        self.items = {p.id: p for p in items}
        self.principles = principles
        # Optional properties on any item: `area` (a topic, free text) and `state`.
        # A closed item (shipped, superseded, dropped) is hidden by default and raises no warnings.
        self.area = {i: str(p.meta.get("area") or "").strip() for i, p in self.items.items()}
        self.state = {i: str(p.meta.get("state") or "").strip().lower() for i, p in self.items.items()}
        self.closed = {i for i, st in self.state.items() if st in CLOSED_STATES}
        g = lambda i, k: _ids(self.items[i].meta.get(k, ""))
        self.serves = {i: [x for x in g(i, "serves") if x in self.items] for i, p in self.items.items() if p.letter == "H"}
        self.metric = {i: [x for x in g(i, "metric") if x in self.items] for i, p in self.items.items() if p.letter == "H"}
        self.tests = {i: [x for x in g(i, "tests") if x in self.items] for i, p in self.items.items() if p.letter in "DE"}
        self.measures = {i: [x for x in g(i, "measures") if x in self.items] for i, p in self.items.items() if p.letter == "E"}
        self.follows = {i: g(i, "follows") for i, p in self.items.items() if p.letter == "D"}
        self.strains = {i: g(i, "pulls_against") for i, p in self.items.items() if p.letter == "D"}
        # Findings: where a usability problem was seen, which decision it touches, how bad it is, and what was done.
        self.found_in = {i: [x for x in g(i, "found_in") if x in self.items] for i, p in self.items.items() if p.letter == "F"}
        self.affects = {i: [x for x in g(i, "affects") if x in self.items] for i, p in self.items.items() if p.letter == "F"}
        self.principle_of = {i: [x for x in g(i, "principle") if x in principles] for i, p in self.items.items() if p.letter == "F"}
        def _sev(i):
            m = re.match(r"\s*([0-4])\b", str(self.items[i].meta.get("severity", "")))
            return int(m.group(1)) if m else None
        self.severity = {i: _sev(i) for i, p in self.items.items() if p.letter == "F"}
        self.resolution = {i: (str(p.meta.get("resolution") or "open").strip().lower()) for i, p in self.items.items() if p.letter == "F"}
        letters = lambda L: sorted([i for i, p in self.items.items() if p.letter == L], key=_natkey)
        self.O, self.H, self.M, self.D, self.E, self.F = [letters(L) for L in "OHMDEF"]
        self.O.sort(key=lambda i: (self.items[i].rank, _natkey(i)))
        self.back = {}
        for src, p in self.items.items():
            for label, val in p.meta.items():
                if label not in REL_KEYS:
                    continue
                for t in _ids(val):
                    if t in self.items and t != src:
                        e = (src, label)
                        if e not in self.back.setdefault(t, []):
                            self.back[t].append(e)
        self.warn = {}
        self.warnings = []  # (kind, [ids], text)

        def flag(kind, ids, text):
            ids = [i for i in ids if i not in self.closed]
            if not ids:
                return
            self.warnings.append((kind, ids, text))
            if warn_tier(kind) == "info":
                return
            for i in ids:
                self.warn.setdefault(i, []).append(text)
        self.flag = flag

        for d in self.D:
            hs = self.tests.get(d, [])
            if not hs or all(not self.serves.get(h) for h in hs):
                flag("no-need", [d], "This decision is not traced to any opportunity")
        for d in self.D:
            for p in self.strains.get(d, []):
                flag("strain", [d], "This decision pulls against principle %s: consider changing it, or record why you accept it" % p)
        for o in self.O:
            hs = [h for h in self.H if o in self.serves.get(h, [])]
            if not hs or not any(self.decisions_of(h) for h in hs):
                flag("unserved", [o], "No decision serves this opportunity yet")
        for h in self.H:
            if not self.tests_of(h):
                flag("untested", [h], "This hypothesis has no test yet")
            if not self.metric.get(h):
                flag("nometric", [h], "This hypothesis has no metric to tell if it is right")
        # Evidence quality: a test can be planned (not run) or run with simulated participants. Neither counts as evidence.
        def kind(t):
            m = self.items[t].meta
            if str(m.get("status", "")).lower() == "planned":
                return "planned"
            if str(m.get("participants_type", "")).lower() == "simulated":
                return "simulated"
            return "real"
        for t in self.E:
            k = kind(t)
            if k == "planned":
                flag("planned", [t], "This evidence is only planned, not run yet")
            elif k == "simulated":
                flag("simulated", [t], "This evidence uses simulated people, not real users: it does not count as real evidence")
        for h in self.H:
            ts = self.tests_of(h)
            if ts and not any(kind(t) == "real" for t in ts):
                flag("no-real-evidence", [h], "This hypothesis has no evidence from real users yet")
        # Decisions: an accepted decision has an owner. Opportunities: a rank has a reason. Metrics: a target, then a verdict.
        for d in self.D:
            m_ = self.items[d].meta
            if self.state.get(d) == "accepted" and not str(m_.get("owner") or "").strip():
                flag("d-no-owner", [d], "This decision is accepted but has no owner")
        if len(self.O) > 1:
            for o in self.O:
                m_ = self.items[o].meta
                if not str(m_.get("rank_reason") or "").strip():
                    flag("o-no-reason", [o], "This opportunity has a rank but no reason (impact, confidence)")
        for m in self.M:
            m_ = self.items[m].meta
            vd = str(m_.get("verdict") or "pending").strip().lower()
            if not str(m_.get("target") or "").strip():
                flag("m-no-target", [m], "This metric has no target: success is not defined")
            if vd in ("met", "missed") and not str(m_.get("result") or "").strip():
                flag("m-no-result", [m], "This metric has a verdict but no measured result")
            if vd == "missed":
                flag("m-missed", [m], "This metric missed its target: revisit the hypothesis and opportunity behind it")
        # Findings
        for f in self.F:
            if self.severity[f] is None:
                flag("f-nosev", [f], "This finding has no valid severity (a number from 0 to 4)")
            if not self.found_in[f]:
                flag("f-noevidence", [f], "This finding is not linked to any evidence (found_in is empty)")
            if self.is_open_finding(f) and self.severity[f] == 4:
                flag("f-sev4", [f], "Severity 4 finding is unresolved: blocks handoff")
            elif self.is_open_finding(f) and self.severity[f] == 3:
                flag("f-sev3", [f], "Severity 3 finding is unresolved: fix it, or accept it and record why")
        for d in self.D:
            bad = [f for f in self.F if d in self.affects.get(f, []) and self.is_open_finding(f) and (self.severity[f] or 0) >= 3]
            if bad:
                flag("d-open-finding", [d], "This decision still has serious unresolved findings: %s" % ", ".join(bad))
        empty = [p for p, (nm, chk) in principles.items() if not chk.strip() and not nm.startswith("(")]
        if empty:
            self.warnings.append(("principles", empty, "Principle has no yes/no question to check against"))

    def is_open_finding(self, f):
        return f not in self.closed and self.resolution.get(f, "open") not in RESOLVED

    def findings_of(self, e):
        return sorted([f for f in self.F if e in self.found_in.get(f, [])], key=lambda f: (-(self.severity[f] if self.severity[f] is not None else -1), _natkey(f)))

    def hyps_of(self, o):
        return [h for h in self.H if o in self.serves.get(h, [])]

    def decisions_of(self, h):
        return [d for d in self.D if h in self.tests.get(d, [])]

    def tests_of(self, h):
        return [t for t in self.E if h in self.tests.get(t, [])]

    def paths(self, i, depth=0):
        """chains from an Opportunity down to item i (list of id lists)"""
        p = self.items[i]
        if p.letter == "O":
            return [[i]]
        parents = []
        if p.letter == "H":
            parents = self.serves.get(i, [])
        elif p.letter in "DE":
            parents = self.tests.get(i, [])
        elif p.letter == "F":
            parents = self.found_in.get(i, [])
        elif p.letter == "M":
            parents = [h for h in self.H if i in self.metric.get(h, [])]
        res = []
        for par in parents:
            for chain in self.paths(par, depth + 1):
                res.append(chain + [i])
        return res


# --------------------------------------------------------------------------- html
CSS = r"""
:root{--ink:#14121c;--bg:#fff;--surface:#faf9ff;--muted:rgba(20,18,28,.66);--line:rgba(20,18,28,.13);--purple:#6B3FEE;--link:#5530d4;--tint:rgba(107,63,238,.10);--tint2:rgba(107,63,238,.18);--on-purple:#fff;--r:12px;color-scheme:light}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.65 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}
a{color:var(--link)}
a:focus-visible,button:focus-visible,input:focus-visible,summary:focus-visible{outline:3px solid var(--purple);outline-offset:2px;border-radius:6px}
.skip{position:absolute;left:-999px;top:0;background:var(--purple);color:var(--on-purple);padding:8px 14px;z-index:30}
.skip:focus{left:8px;top:8px}
header.top{position:sticky;top:0;z-index:20;background:var(--bg);border-bottom:1px solid var(--line)}
.top-in{max-width:1280px;margin:0 auto;padding:10px 24px;display:flex;gap:18px;align-items:center;flex-wrap:wrap}
.brand{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:-.01em;margin-right:auto}
.brand .logo{height:22px;width:auto;flex:none;color:var(--ink)}
.brand small{display:block;font-weight:500;color:var(--muted);font-size:.74rem;letter-spacing:0}
.tabs{display:flex;gap:4px;overflow-x:auto}
.tabs a{padding:8px 14px;border-radius:999px;text-decoration:none;color:var(--ink);font-weight:600;font-size:.92rem;white-space:nowrap}
.tabs a:hover{background:var(--tint)}
.tabs a[aria-current=page]{background:var(--purple);color:var(--on-purple)}
.themepick{font-size:.8rem;color:var(--muted);display:flex;gap:6px;align-items:center}
.themepick select{font:inherit;padding:6px 8px;border:1px solid var(--line);border-radius:8px;background:var(--surface);color:var(--ink)}
.view{display:none}
.view.on{display:block}
.wrap{max-width:1280px;margin:0 auto;padding:28px 24px 80px}
h1{font-size:1.8rem;line-height:1.25;margin:0 0 8px;letter-spacing:-.015em}
h2{font-size:1.1rem;margin:34px 0 12px;letter-spacing:-.005em}
h3{font-size:1rem;margin:22px 0 6px}
.lede{color:var(--muted);margin:0 0 22px}
.banner{background:var(--ink);color:var(--bg);border-radius:var(--r);padding:12px 16px;margin:0 0 22px;font-size:.92rem}
.cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:8px 0 8px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:14px 16px}
.card .num{font-size:1.9rem;font-weight:800;line-height:1.1;letter-spacing:-.02em}
.card .lbl{color:var(--muted);font-size:.85rem}
.card.warnc .num::after{content:" ⚠";font-size:1rem}
.gatecards{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px}
.gate{border-radius:var(--r);padding:14px 16px;background:var(--ink);color:var(--bg)}
.gate small{display:block;opacity:.8}
.gate .st{margin-top:8px;font-weight:700}
.gate .bar{height:6px;border-radius:99px;background:rgba(255,255,255,.25);margin-top:8px;overflow:hidden}
.gate .bar i{display:block;height:100%;background:#fff}
.table-wrap{overflow-x:auto;margin:12px 0}
table{border-collapse:collapse;width:100%;font-size:.92rem}
table.bal{table-layout:fixed}
table.bal th,table.bal td{overflow-wrap:break-word;word-break:normal}
th,td{text-align:left;padding:9px 12px;border-bottom:1px solid var(--line);vertical-align:top}
th{background:var(--tint);font-weight:700}
table.props th{background:none;color:var(--muted);font-weight:600;width:11em}
.missing{font-weight:700;color:var(--muted);font-style:italic}
.card .lbl small{display:block;font-size:.74rem;opacity:.85}
details.help{background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:12px 18px;margin:0 0 22px}
details.help summary{cursor:pointer;font-weight:700}
details.help ul,details.help dl{margin:10px 0 4px}
details.help dt{font-weight:700;margin-top:10px}
details.help dd{margin:2px 0 0;color:var(--muted)}
.chip,.idc,.idtag{display:inline-block;font-weight:800;font-size:.8rem;line-height:1;padding:4px 8px;border-radius:7px;text-decoration:none;letter-spacing:.03em;vertical-align:middle;border:2px solid transparent;white-space:nowrap}
.t-O{background:var(--purple);color:var(--on-purple)}
.t-H{border-color:var(--purple);color:var(--link)}
.t-D{background:var(--ink);color:var(--bg)}
.t-E{border-color:var(--ink);color:var(--ink)}
.t-F{background:var(--tint2);color:var(--ink)}
.t-M{background:var(--tint2);color:var(--ink)}
.t-P{border:2px dashed var(--muted);color:var(--ink)}
a.chip:hover{filter:brightness(1.1)}
.chips{display:flex;flex-wrap:wrap;gap:6px}
.warnlist{list-style:none;margin:0;padding:0}
.warnlist li{padding:10px 14px;margin:8px 0;border-radius:var(--r);background:var(--tint);border-left:4px solid var(--purple)}
.ok{padding:10px 14px;border-radius:var(--r);background:var(--tint)}
.wgroup{border:1px solid var(--line);border-radius:var(--r);margin:0 0 10px;background:var(--surface)}
.wgroup>summary{display:flex;align-items:center;gap:10px;padding:10px 14px;cursor:pointer;list-style:none;font-weight:600}
.wgroup>summary::-webkit-details-marker{display:none}
.wgroup>summary::before{content:"▸";color:var(--muted);font-size:.8rem}
.wgroup[open]>summary::before{content:"▾"}
.wcount{margin-left:auto;font-size:.8rem;font-weight:700;padding:2px 9px;border-radius:99px;background:var(--tint)}
.whint{margin:0;padding:0 14px 8px;font-size:.88rem;color:var(--muted)}
.wgrid{list-style:none;margin:0;padding:0 14px 12px;display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:6px 14px}
.wgrid li{display:flex;align-items:center;gap:8px;min-width:0;font-size:.9rem}
.wt{overflow:hidden;text-overflow:ellipsis;white-space:nowrap;min-width:0}
.wn{margin-left:auto;font-size:.8rem;color:var(--muted);white-space:nowrap}
/* journey */
.jcards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px}
.jcard{display:block;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:16px 18px;text-decoration:none;color:var(--ink)}
.jcard:hover{border-color:var(--purple);box-shadow:0 2px 0 var(--purple)}
.jcard .wk{font-size:.75rem;font-weight:800;letter-spacing:.1em;text-transform:uppercase;color:var(--link)}
.jcard h3{margin:4px 0 6px;font-size:1.05rem}
.jcard p{margin:0;color:var(--muted);font-size:.9rem}
.has-doc .jlist{display:none}
.journey .doc,.reference .doc{display:none}
.journey .doc.on,.reference .doc.on{display:block}
.reading{max-width:76ch}
.pn{display:flex;justify-content:space-between;gap:16px;margin-top:40px;padding-top:16px;border-top:1px solid var(--line);flex-wrap:wrap}
.back{display:inline-block;margin:0 0 16px;font-size:.9rem}
.subtabs{display:flex;gap:6px;margin:0 0 18px;flex-wrap:wrap}
.subtabs a{padding:6px 12px;border-radius:999px;border:1px solid var(--line);text-decoration:none;color:var(--ink);font-size:.9rem;font-weight:600}
.subtabs a[aria-current=page]{background:var(--ink);color:var(--bg);border-color:var(--ink)}
/* trace */
.trace{display:grid;grid-template-columns:minmax(300px,380px) minmax(0,1fr);gap:28px;align-items:start}
.pane-tree{position:sticky;top:76px;max-height:calc(100vh - 96px);overflow:auto;border:1px solid var(--line);border-radius:var(--r);background:var(--surface);padding:12px}
.filters{display:flex;flex-wrap:wrap;gap:6px;margin:0 0 10px}
.filters button{border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:999px;padding:5px 11px;font:inherit;font-size:.8rem;font-weight:700;cursor:pointer}
.filters button[aria-pressed=true]{background:var(--purple);border-color:var(--purple);color:var(--on-purple)}
.tsearch{width:100%;border:1px solid var(--line);background:var(--bg);color:var(--ink);border-radius:10px;padding:8px 12px;font:inherit;font-size:.9rem;margin:0 0 10px}
.tcount{font-size:.8rem;color:var(--muted);margin:0 0 8px}
.tree,.tree ul{list-style:none;margin:0;padding:0}
.tree ul{margin-left:14px;padding-left:10px;border-left:1px solid var(--line)}
.tree li[hidden]{display:none}
.tree summary{cursor:pointer;display:flex;align-items:flex-start;gap:6px;padding:3px 0;list-style:none}
.tree summary::-webkit-details-marker{display:none}
.tree summary::before{content:"▸";color:var(--muted);width:1em;flex:none;font-size:.8rem;margin-top:5px}
.tree details[open]>summary::before{content:"▾"}
.tree li.leaf{padding-left:1.35em}
.tree a.node{display:flex;gap:8px;align-items:flex-start;text-decoration:none;color:var(--ink);padding:4px 6px;border-radius:8px;flex:1;min-width:0;font-size:.9rem}
.tree a.node:hover{background:var(--tint)}
.tree a.node.sel{background:var(--tint2);font-weight:700}
.tree .idc{font-size:.72rem;padding:3px 6px;flex:none;margin-top:2px}
.tree .nt{overflow-wrap:anywhere}
.tree .wb{margin-left:auto;flex:none}
.tree .cnt{display:block;color:var(--muted);font-size:.75rem;font-weight:500}
.tree .gh{font-size:.8rem;font-weight:800;color:var(--muted);padding:8px 0 2px}
.pane-detail .doc{display:none}
.pane-detail .doc.on{display:block}
.empty{color:var(--muted);border:1px dashed var(--line);border-radius:var(--r);padding:28px;text-align:center}
.pane-detail .doc.on~.empty{display:none}
.ihead{display:flex;gap:14px;align-items:flex-start;margin:0 0 14px}
.ihead .idtag{font-size:1rem;padding:7px 12px;flex:none;margin-top:2px}
.ihead .kind{margin:0;color:var(--muted);font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.ihead h1{margin:2px 0 0;font-size:1.5rem}
.warnbox{margin:0 0 14px;padding:10px 14px;border-radius:var(--r);background:var(--tint);border-left:4px solid var(--purple);font-size:.92rem}
.path{font-size:.88rem;color:var(--muted);margin:0 0 14px}
.path .chain{margin:6px 0 0;align-items:center}
.path .more{display:block;margin-top:6px}
.backlinks{margin-top:30px;padding:14px 18px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r)}
.backlinks h2{margin:0 0 8px;font-size:.95rem}
.backlinks .row{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin:6px 0}
.backlinks .lbl{font-size:.8rem;color:var(--muted);min-width:7em}
.dlist{display:flex;flex-direction:column}
.dlink{display:flex;align-items:center;gap:12px;padding:9px 4px;border-top:1px solid var(--line);color:var(--ink);text-decoration:none;font-size:.92rem}
.dlink:first-child{border-top:0}
.dlink:hover{background:var(--tint)}
.dlink:hover .darr{color:var(--purple);transform:translateX(2px)}
.dtype{flex:0 0 14em;font-size:.72rem;font-weight:600;letter-spacing:.03em;text-transform:uppercase;color:var(--muted);overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.dtitle{flex:1;min-width:0}
.darr{color:var(--muted);transition:transform .15s}
@media (max-width:600px){.dtype{flex-basis:6.5em}}
.back-tree{display:none}
.acards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:14px;margin-top:6px}
.acard{display:flex;flex-direction:column;gap:6px;background:var(--surface);border:1px solid var(--line);border-radius:var(--r);padding:0 0 14px;text-decoration:none;color:var(--ink);overflow:hidden}
.acard[hidden]{display:none}
.acard:hover{border-color:var(--purple);box-shadow:0 2px 0 var(--purple)}
.acard .thumb{width:100%;height:150px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);background:var(--tint)}
.acard>*:not(.thumb){margin-left:16px;margin-right:16px}
.acard:not(:has(.thumb))>.atype{margin-top:14px}
.atype{font-size:.72rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:var(--link)}
.acard h3{margin:0;font-size:1.02rem}
.acard p{margin:0;color:var(--muted);font-size:.88rem}
.ameta{font-size:.78rem;color:var(--muted)}
.st{display:inline-block;padding:1px 8px;border-radius:999px;font-weight:700;font-size:.72rem;background:var(--tint2);color:var(--ink)}
.st-simulated,.st-planned,.st-draft{background:var(--ink);color:var(--bg)}
.ahead .sum{font-size:1.05rem;color:var(--muted);margin:6px 0 10px}
.ahead .kind{margin:0;color:var(--muted);font-size:.8rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
.supports{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin:6px 0 14px}
.backlinks .row{align-items:baseline}
.supports .lbl{font-size:.8rem;color:var(--muted)}
.figs{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:14px;margin:8px 0}
.fig{margin:0;border:1px solid var(--line);border-radius:var(--r);overflow:hidden;background:#fff}
.fig img{display:block;width:100%;height:auto}
.fig figcaption,.mcard .cap{font-size:.8rem;color:var(--muted);padding:6px 12px}
.mcard{border:1px solid var(--line);border-radius:var(--r);margin:12px 0;overflow:hidden;background:var(--surface)}
.mhead{display:flex;gap:10px;align-items:center;flex-wrap:wrap;padding:10px 14px}
.mtag{font-size:.72rem;font-weight:700;color:var(--muted);text-transform:uppercase;letter-spacing:.06em}
.btn{margin-left:auto;padding:5px 12px;border-radius:999px;background:var(--purple);color:var(--on-purple);text-decoration:none;font-size:.82rem;font-weight:700}
.mcard iframe{display:block;width:100%;height:560px;border:0;border-top:1px solid var(--line);background:#fff}
.mcard video{display:block;width:100%}
.achip{display:inline-flex;gap:8px;align-items:baseline;padding:6px 12px;border:1px solid var(--line);border-radius:10px;text-decoration:none;color:var(--ink);background:var(--surface);font-size:.9rem}
.achip:hover{border-color:var(--purple)}
.achip .atype{font-size:.66rem}
.sgroup{margin:10px 0}
.sgroup h3{margin:0 0 6px;font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--muted)}
.t-A{background:var(--tint2);color:var(--ink);border-color:transparent}
details.draft{margin:14px 0;border:1px dashed var(--muted);border-radius:var(--r);padding:10px 14px;background:var(--surface)}
details.draft>summary{cursor:pointer;font-weight:700;color:var(--muted)}
.srcnote{margin-top:24px;font-size:.82rem;color:var(--muted)}
.docs .doc{display:none}
.docs .doc.on{display:block}
.has-doc .jlist{display:none}
blockquote{margin:16px 0;padding:10px 16px;background:var(--tint);border-left:4px solid var(--purple);border-radius:0 10px 10px 0}
blockquote p{margin:6px 0}
code{font:.88em ui-monospace,Menlo,Consolas,monospace;background:var(--tint);padding:1px 5px;border-radius:5px}
pre{background:var(--tint);padding:12px 14px;border-radius:10px;overflow-x:auto}
pre code{background:none;padding:0}
hr{border:0;border-top:1px solid var(--line);margin:28px 0}
ul,ol{padding-left:1.4em}
li{margin:4px 0}
.box{font-family:ui-monospace,Menlo,Consolas,monospace}
.ext{color:var(--muted);border-bottom:1px dotted var(--muted);cursor:help}
.broken{color:#9b1c1c;text-decoration:underline wavy}
img{max-width:100%}
footer.foot{margin-top:56px;color:var(--muted);font-size:.85rem;border-top:1px solid var(--line);padding-top:14px}
@media (max-width:900px){
  .trace{grid-template-columns:1fr}
  .pane-tree{position:static;max-height:none}
  .has-item .pane-tree{display:none}
  .has-item .back-tree{display:inline-block}
  .wrap{padding:20px 16px 60px}
}
@media print{
  header.top,.skip,.pane-tree,.back,.pn,.subtabs,.back-tree,.themepick,.filters,.tsearch{display:none!important}
  .view,.journey .doc,.reference .doc,.docs .doc,.pane-detail .doc{display:block!important}
  .jlist{display:none}
  .doc{break-before:page}
  .wrap{padding:0;max-width:none}
  .trace{display:block}
  a{color:inherit;text-decoration:none}
  table{font-size:.8rem}
  .banner{border:1px solid #000;background:none;color:#000}
}
"""

NAV_CSS = r"""
/* sidebar layout (mirrors the website structure: one page per document, nested menu on the left) */
.shell{display:grid;grid-template-columns:300px minmax(0,1fr);max-width:1480px;margin:0 auto;align-items:start}
.side{position:sticky;top:51px;height:calc(100vh - 51px);overflow:auto;border-right:1px solid var(--line);padding:16px 12px 48px;font-size:.9rem;background:var(--bg)}
.side nav{display:block}
.side a{display:block;text-decoration:none;color:var(--ink);padding:5px 10px;border-radius:8px;overflow-wrap:anywhere}
.side a:hover{background:var(--tint)}
.side a[aria-current=page]{background:var(--purple);color:var(--on-purple);font-weight:700}
.side .s-top{font-weight:700}
.side details{margin:0}
.side summary{cursor:pointer;list-style:none;font-weight:800;padding:7px 10px;border-radius:8px;display:flex;gap:6px;align-items:baseline}
.side summary::-webkit-details-marker{display:none}
.side summary::before{content:"▸";color:var(--muted);font-size:.75rem;width:.9em;flex:none}
.side details[open]>summary::before{content:"▾"}
.side summary:hover{background:var(--tint)}
.side .grp{margin-top:6px}
.side .grp>.sub{margin-left:12px;border-left:1px solid var(--line);padding-left:6px}
.side .sub summary{font-weight:700;color:var(--ink);font-size:.88rem}
.side .sub .cnt{margin-left:auto;font-weight:500;color:var(--muted);font-size:.78rem}
.side .sub a{font-size:.85rem;color:var(--ink)}
.side .sub a .idc{font-size:.66rem;padding:2px 5px;margin-right:6px}
.side .sub a[aria-current=page] .idc{border-color:var(--on-purple);background:transparent;color:var(--on-purple)}
.side .menu>summary{display:none}
.shell .wrap{max-width:1000px;padding:28px 40px 80px}
/* one page at a time: the trace tree is its own page, items are pages of their own */
.trace{display:block}
.pane-tree{position:static;max-height:none;overflow:visible;border:0;background:none;padding:0}
#v-trace.has-item .pane-tree{display:none}
#v-trace:not(.has-item) .pane-detail{display:none}
#v-trace .back-tree{display:inline-block}
#v-reference .wrap>h1,#v-reference .wrap>.lede,#v-reference .subtabs{display:none}
@media (max-width:900px){
  .shell{display:block}
  .side{position:static;height:auto;border-right:0;border-bottom:1px solid var(--line);padding:8px 12px;max-height:none}
  .side .menu>summary{display:block;cursor:pointer;font-weight:800;padding:8px 10px;list-style:none}
  .side .menu[open]>summary{border-bottom:1px solid var(--line);margin-bottom:6px}
  .shell .wrap{padding:20px 16px 60px}
}
@media print{.side{display:none!important}.shell{display:block}.shell .wrap{max-width:none;padding:0}}
"""
CSS += NAV_CSS

MIN_CSS = r"""
/* minimalist layer: fewer boxes, more air, one accent */
body{font-size:15.5px;line-height:1.7}
header.top{border-bottom:1px solid var(--line)}
.top-in{padding:12px 24px}
.brand{font-weight:700}
.brand small{display:none}
h1{font-size:1.75rem;font-weight:700}
h2{font-size:.8rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:44px 0 12px}
.lede{margin:0 0 26px}
.stats{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));row-gap:18px;margin:14px 0 6px;padding:0}
.stats span{display:flex;flex-direction:column;gap:2px;padding:2px 18px;border-left:1px solid var(--line);color:var(--muted);font-size:.8rem;text-transform:capitalize}
.stats span:nth-child(4n+1){border-left:0;padding-left:0}
.stats span:last-child:nth-child(4n+1){grid-column:span 4}
.stats .w{text-transform:none}
.stats b{display:block;margin:0;font-size:1.7rem;line-height:1.15;font-weight:700;color:var(--ink);letter-spacing:-.02em}
.stats .w b{color:#b76e00}
.stats .w b::after{content:" ⚠";font-size:.9rem}
.stats .w.bad b{color:#b71d18}
.stats .w.ok b{color:#118d57}
.stats .w.ok b::after{content:" ✓"}
.wtier{margin:18px 0 8px;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted)}
.wtier-block{color:#b71d18}
.winfo{margin:18px 0 0}
.winfo>summary{cursor:pointer;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);padding:6px 0}
@media(max-width:560px){.stats{grid-template-columns:repeat(2,minmax(0,1fr))}.stats span:nth-child(4n+1){border-left:1px solid var(--line);padding-left:18px}.stats span:nth-child(2n+1){border-left:0;padding-left:0}.stats span:last-child:nth-child(4n+1){grid-column:auto}}
.glist{margin:0;border-top:1px solid var(--line)}
.grow{display:grid;grid-template-columns:minmax(0,1.4fr) 110px minmax(80px,1fr) 70px;gap:16px;align-items:center;padding:11px 0;border-bottom:1px solid var(--line)}
.grow .gn small{display:block;color:var(--muted);font-size:.78rem}
.grow .gn strong{font-weight:600}
.grow .gs{font-size:.85rem;font-weight:600}
.grow .gs.ok{color:#1a7f4b}
.grow .gs.no{color:#a33}
.grow .gb{height:4px;border-radius:99px;background:var(--line);overflow:hidden}
.grow .gb i{display:block;height:100%;background:var(--purple)}
.grow .gc{font-size:.82rem;color:var(--muted);text-align:right}
.warnlist li{background:none;border-left:0;border-top:1px solid var(--line);border-radius:0;padding:10px 0;margin:0}
.warnlist li:last-child{border-bottom:1px solid var(--line)}
.warnlist strong{font-weight:500}
.ok{background:none;padding:0;color:var(--muted)}
table{font-size:.9rem}
th{background:none;font-size:.78rem;letter-spacing:.04em;text-transform:uppercase;color:var(--muted);border-bottom:1px solid var(--ink)}
td{border-bottom:1px solid var(--line)}
.chip,.idc,.idtag{font-weight:700;font-size:.74rem;padding:3px 7px}
details.help{background:none;border:0;border-top:1px solid var(--line);border-radius:0;padding:14px 0;margin:44px 0 0}
details.help summary{font-weight:600;color:var(--muted)}
.banner{background:var(--tint);color:var(--ink);font-size:.88rem;border-radius:var(--r);padding:10px 14px}
.side{font-size:.88rem}
.jcard,.acard{background:none}
.reading{max-width:70ch}
footer.foot{margin-top:48px}
@media (max-width:640px){.grow{grid-template-columns:1fr 1fr;gap:6px 12px}.grow .gb{grid-column:1/-1}}
/* sidebar: five sections; each opens a page of cards */
.side{padding:14px 12px}
.nav2 a{display:flex;align-items:center;gap:8px;padding:9px 12px;font-weight:600;font-size:.95rem}
.nav2 a .nm{margin-left:auto;font-weight:500;font-size:.78rem;color:var(--muted)}
.nav2 a[aria-current=page] .nm{color:var(--on-purple);opacity:.85}
/* item page */
.ihead{display:block;margin:0 0 6px}
.ihead .idtag{display:inline-block;font-size:.78rem;padding:3px 8px;margin:0 0 10px}
.ihead .kind{display:block;margin:0 0 6px;font-size:.74rem;font-weight:600;letter-spacing:.06em;color:var(--muted)}
.ihead h1{font-size:1.6rem;margin:0;line-height:1.3}
.ihead>div{display:block}
.path{margin:14px 0 18px;font-size:.84rem}
.path>span:first-child{display:block;margin-bottom:4px}
.warnbox{background:none;border:0;border-left:2px solid var(--purple);border-radius:0;padding:2px 0 2px 12px;margin:0 0 10px;font-size:.88rem}
table.props{margin:0 0 8px}
table.props th{width:11em;padding:7px 12px 7px 0;font-size:.82rem;text-transform:none;letter-spacing:0;font-weight:500;color:var(--muted);border-bottom:1px solid var(--line)}
table.props td{padding:7px 0}
.backlinks{background:none;border:0;border-top:1px solid var(--line);border-radius:0;padding:14px 0 0;margin-top:36px}
.backlinks h2{font-size:.78rem;letter-spacing:.09em;text-transform:uppercase;color:var(--muted);margin:0 0 6px}
.backlinks .lbl{font-weight:500}
.reading h2{margin-top:30px}
/* trace tree */
.pane-tree{margin-top:0}
.tsearch{background:none;border:0;border-bottom:1px solid var(--line);border-radius:0;padding:8px 0;font-size:.95rem}
.filters{margin:2px 0 14px;gap:4px}
.filters button{border:0;background:none;color:var(--muted);padding:4px 10px;font-weight:600}
.filters button:hover{background:var(--tint)}
.filters button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
.tree ul{margin-left:11px;padding-left:12px;border-left:1px solid var(--line)}
.tree a.node{padding:4px 6px;font-size:.92rem}
.tree a.node:hover{background:var(--tint)}
.tree a.node.sel{background:var(--tint);font-weight:600}
.tree .cnt{display:inline;margin-left:8px;font-size:.76rem;color:var(--muted)}
.tree .idc{font-size:.68rem;padding:2px 5px;border-width:1px}
.tree summary{padding:2px 0}
.tree .gh{font-weight:700;font-size:.78rem;letter-spacing:.06em;text-transform:uppercase}
/* cards: documents, journey pages, insights */
.acards,.jcards,.icards{display:grid;grid-template-columns:repeat(auto-fill,minmax(250px,1fr));gap:12px;margin-top:6px;border:0}
.acard,.jcard,.icard{display:flex;flex-direction:column;gap:4px;padding:16px;border:1px solid var(--line);border-radius:var(--r);background:none;text-decoration:none;color:var(--ink);overflow:hidden;min-height:112px}
.acard:hover,.jcard:hover,.icard:hover{border-color:var(--ink);box-shadow:none;background:none}
.acard[hidden],.icard[hidden]{display:none}
.acard>*:not(.thumb),.icard>*{margin:0}
.acard:not(:has(.thumb))>.atype{margin:0}
.acard .thumb{display:block;align-self:stretch;width:auto;max-width:none;margin:-16px -16px 10px;height:110px;object-fit:cover;object-position:top;border-bottom:1px solid var(--line);background:var(--tint)}
.acard .atype,.jcard .wk,.icard .itype{font-size:.7rem;font-weight:700;letter-spacing:.09em;text-transform:uppercase;color:var(--muted)}
.acard h3,.jcard h3,.icard h3{margin:2px 0 0;font-size:1rem;line-height:1.35}
.acard p,.jcard p,.icard p{margin:0;color:var(--muted);font-size:.86rem;line-height:1.5}
.acard .ameta{font-size:.76rem;color:var(--muted);margin-top:auto;padding-top:8px}
.icard .top{display:flex;align-items:center;gap:8px}
.icard .top .w{margin-left:auto}
.st{background:none;border:1px solid var(--line);color:var(--muted);font-weight:600;padding:0 7px}
.st-simulated,.st-planned,.st-draft{background:none;border:1px solid var(--ink);color:var(--ink)}
.ahead .kind{font-size:.74rem;letter-spacing:.09em}
.ahead h1{margin:4px 0 6px}
.ahead .sum{font-size:1rem;margin:0 0 12px}
.ahead p:has(.st){margin:0 0 10px}
.supports{margin:10px 0 0}
.mcard{background:none;margin:14px 0}
.mhead{padding:10px 14px}
.btn{background:none;color:var(--link);padding:0;font-weight:600;border-radius:0}
.btn:hover{text-decoration:underline}
.mcard iframe{height:520px}
.fig{border-radius:var(--r)}
.srcnote{margin-top:32px;font-size:.8rem}
.trow{display:flex;gap:28px;align-items:center;margin:0 0 10px}
.trow .tsearch{flex:0 1 320px;min-width:0;width:auto;margin:0}
#v-trace .tsearch,#v-docs .tsearch{padding-left:38px;background-repeat:no-repeat;background-position:12px center;background-size:16px;background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%23919eab' stroke-width='2' stroke-linecap='round'%3E%3Ccircle cx='11' cy='11' r='7'/%3E%3Cpath d='m20 20-3.5-3.5'/%3E%3C/svg%3E")}
.trow .vmode{flex:none;margin:0 0 0 auto}
.vmode{display:inline-flex;gap:2px;margin:0 0 14px;border:1px solid var(--line);border-radius:var(--r);padding:2px}
.vmode button{border:0;background:none;font:inherit;font-size:.82rem;font-weight:600;color:var(--muted);padding:4px 12px;border-radius:calc(var(--r) - 2px);cursor:pointer}
.vmode button[aria-pressed=true]{background:var(--ink);color:var(--bg)}
#v-trace .tree{display:none}
.tabs2{display:flex;gap:2px;border-bottom:1px solid var(--line);margin:0 0 14px;overflow-x:auto;overflow-y:hidden;scrollbar-width:none}
.tabs2::-webkit-scrollbar{display:none}
.tabs2 button{border:0;background:none;font:inherit;font-weight:600;font-size:.9rem;color:var(--muted);padding:10px 14px;margin-bottom:-1px;border-bottom:2px solid transparent;cursor:pointer;white-space:nowrap}
.tabs2 button:hover{color:var(--ink)}
.tabs2 button[aria-selected=true]{color:var(--ink);border-bottom-color:var(--purple)}
.tabs2 .n{margin-left:7px;font-size:.72rem;font-weight:700;padding:1px 7px;border-radius:99px;background:rgba(145,158,171,.16);color:var(--muted)}
.tabs2 button[aria-selected=true] .n{background:var(--tint2);color:var(--link)}
#v-trace.mode-tree .tree{display:block}
#v-trace.mode-tree .icards{display:none}
.atable{display:none}
.tbar{display:flex;flex-wrap:wrap;gap:8px 18px;align-items:center;margin:0 0 12px;font-size:.88rem;color:var(--muted)}
.tbar select{font:inherit;padding:4px 8px;border:1px solid var(--line);border-radius:var(--r);background:var(--surface);color:var(--ink)}
.tbar input{margin-right:6px}
#v-trace.mode-table .atable{display:block}
#v-trace.mode-table .icards,#v-trace.mode-table .tree{display:none}
.astats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;margin:0 0 10px}
.astat{padding:12px 14px;border:1px solid var(--line);border-radius:var(--r);background:var(--surface)}
.astat b{display:block;font-size:1.5rem;font-weight:600;line-height:1.2}
.astat span{font-size:.84rem;color:var(--muted)}
.stgate{margin:0 0 18px;font-size:.88rem;color:var(--muted)}
.stsrc{margin:0 0 26px}
.sthead{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin:0 0 10px;padding:6px 0;border-top:1px solid var(--line);font-size:.8rem;color:var(--muted)}
.sthead a{margin-left:auto;font-weight:600}
.ststatus{padding:1px 8px;border-radius:99px;font-size:.72rem;font-weight:700;background:rgba(145,158,171,.16)}
.ststatus.ok{background:rgba(34,197,94,.16);color:#118d57}
.ststatus.w{background:rgba(255,171,0,.16);color:#b76e00}
html{overflow-x:hidden;overflow-y:scroll;scrollbar-gutter:stable}
.top-in{max-width:1480px;padding-left:24px;padding-right:24px}
.nav2 a[data-nav=guide]{margin-top:10px;border-top:1px dashed var(--line);border-radius:0 0 var(--r) var(--r);padding-top:12px}
.guide pre{position:relative;padding-right:84px}
.guide .copybtn{position:absolute;top:8px;right:8px;font:inherit;font-size:.74rem;font-weight:600;padding:3px 10px;border:1px solid var(--line);border-radius:6px;background:var(--bg);color:var(--ink);cursor:pointer}
.guide .copybtn:hover{border-color:var(--ink)}
.stale{margin:0 0 18px;padding:10px 14px;border-left:3px solid #ffab00;background:rgba(255,171,0,.1);border-radius:var(--r);font-size:.88rem;color:var(--ink)}
.where{margin:10px 0 18px;padding:8px 12px;border-left:3px solid var(--line);background:var(--surface);font-size:.86rem;color:var(--muted);line-height:1.7}
.where .wl{display:inline-block;min-width:5.5em;font-size:.72rem;font-weight:700;letter-spacing:.06em;text-transform:uppercase}
.where code{font-size:.84rem}
.srcfile{margin:28px 0 0;font-size:.82rem;color:var(--muted)}
.foot-tech{margin-top:6px;font-size:.84rem}
.foot-tech summary{cursor:pointer}
.linkbtn{font:inherit;font-size:.9rem;color:var(--link);background:none;border:0;padding:0;cursor:pointer;text-decoration:underline;text-underline-offset:2px}
/* reference and journey pages */
html[data-theme] th{background:none}
.reference .reading,.journey .reading{max-width:none}
.reference .reading>p,.journey .reading>p,.journey .reading>ul,.journey .reading>ol{max-width:72ch}
.reference .reading>p>em:only-child,.journey .reading>p>em:only-child{font-style:normal;color:var(--muted)}
.reference .reading h2,.journey .reading h2{margin-top:36px}
.reference table,.journey table{margin:8px 0 0}
.journey td a{text-decoration:none;font-weight:600}
.journey td a:hover{text-decoration:underline}
.journey .reading>blockquote{max-width:72ch}
.back{display:inline-block;margin:0 0 18px;font-size:.8125rem;font-weight:600;color:var(--muted);text-decoration:none}
.back:hover{color:var(--ink)}
.journey .reading>p>em:only-child{font-size:.875rem}
.journey .reading>p:first-child{font-size:1rem}
.journey .doc>.reading>h1:first-child{margin-bottom:6px}
.journey .reading code{font-size:.84em}
.pn{border-top:1px solid var(--line);margin-top:32px;padding-top:14px}
.pn a{text-decoration:none;font-weight:600}
.pn a:hover{text-decoration:underline}
.reference td:first-child{white-space:nowrap;color:var(--muted);font-weight:600;width:1%}
.reference table.bal td:first-child{white-space:normal;width:auto}
.gst{font-size:.82rem;font-weight:600;white-space:nowrap}
.gst::before{content:"";display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:7px;background:var(--muted);vertical-align:middle}
.gst-passed::before{background:#1a7f4b}
.gst-failed{color:#a33}
.gst-failed::before{background:#a33}
.dash{color:var(--muted)}
"""
CSS += MIN_CSS

# Item references (H1, D2, T1...) are plain underlined links, not badges.
# The extra .chip repeats make this win over the per-theme badge colours.
CSS += r"""
body .chip.chip.chip{display:inline;background:none;border:0;border-radius:0;padding:0;font-size:inherit;font-weight:400;letter-spacing:0;color:var(--link);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px}
a.chip:hover{filter:none;text-decoration-thickness:2px}
span.chip.chip.chip{color:inherit;text-decoration:none}
.chips{gap:4px 14px}
.irefs{display:flex;flex-direction:column;gap:2px;flex:1;min-width:0}
a.iref{display:inline;color:var(--link);text-decoration:underline;text-underline-offset:2px;text-decoration-thickness:1px;font-size:.92rem;line-height:1.5}
a.iref:hover{text-decoration-thickness:2px}
.irefs a.iref{display:block}
.idn{flex:none;font-size:.72rem;color:var(--muted);margin-right:8px;white-space:nowrap}
.icard .itype{font-size:.74rem;color:var(--muted);letter-spacing:.02em}
"""

JS = r"""
(function(){
  var root=document.documentElement; root.classList.add('js');
  var VIEWS=['overview','context','journey','docs','trace','reference','guide'];
  function $(s,c){return (c||document).querySelector(s)}
  function $$(s,c){return [].slice.call((c||document).querySelectorAll(s))}
  var docs={}; $$('.doc').forEach(function(d){docs[d.id]=d});
  $$('.nback').forEach(function(b){b.addEventListener('click',function(){showPanel('root')})});
  var caseName=document.body.getAttribute('data-case');
  function route(){
    var id=decodeURIComponent((location.hash||'').replace(/^#\/?/,''))||'overview';
    var doc=null, view='overview';
    if(VIEWS.indexOf(id)>-1){view=id}
    else if(docs[id]){doc=docs[id]; var v=doc.closest('.view'); view=v?v.id.slice(2):'overview'}
    $$('.view').forEach(function(v){v.classList.toggle('on',v.id==='v-'+view)});
    $$('.side a[data-nav]').forEach(function(a){
      if(a.getAttribute('data-nav')===view){a.setAttribute('aria-current','page')}else{a.removeAttribute('aria-current')}
    });
    var mn=$('.side details.menu'); if(mn&&window.innerWidth<=900){mn.open=false}
    $$('.doc').forEach(function(d){d.classList.remove('on')});
    if(doc){doc.classList.add('on')}
    var j=$('#v-journey'); if(j){j.classList.toggle('has-doc',view==='journey'&&!!doc)}
    var t=$('#v-trace'); if(t){t.classList.toggle('has-item',view==='trace'&&!!doc)}
    var rv=$('#v-reference'); if(rv){rv.classList.toggle('has-doc',view==='reference'&&!!doc)}
    var cv=$('#v-context'); if(cv){cv.classList.toggle('has-doc',view==='context'&&!!doc)}
    var dv=$('#v-docs'); if(dv){dv.classList.toggle('has-doc',view==='docs'&&!!doc)}
    $$('.subtabs a').forEach(function(a){
      if(doc&&a.getAttribute('href')==='#/'+doc.id){a.setAttribute('aria-current','page')}else{a.removeAttribute('aria-current')}
    });
    $$('.tree a.node').forEach(function(a){
      var on=view==='trace'&&doc&&a.getAttribute('data-id')===doc.id;
      a.classList.toggle('sel',!!on);
    });
    var sel=$('.tree a.node.sel');
    if(sel){var p=sel.parentElement; while(p&&p.id!=='tree'){if(p.tagName==='DETAILS'){p.open=true} p=p.parentElement}}
    document.title=(doc?doc.getAttribute('data-title')+' · ':'')+caseName;
    window.scrollTo(0,0);
  }
  window.addEventListener('hashchange',route);
  // guide page: a Copy button on every prompt
  $$('#v-guide pre').forEach(function(pre){
    var b=document.createElement('button'); b.type='button'; b.className='copybtn'; b.textContent='Copy';
    b.addEventListener('click',function(){
      var txt=pre.innerText.replace(/\s*Copy\s*$/,'');
      function done(){b.textContent='Copied'; setTimeout(function(){b.textContent='Copy'},1500)}
      try{ if(navigator.clipboard&&navigator.clipboard.writeText){navigator.clipboard.writeText(txt).then(done,fallback)}else{fallback()} }catch(e){fallback()}
      function fallback(){
        var t=document.createElement('textarea'); t.value=txt; t.style.position='fixed'; t.style.opacity='0'; document.body.appendChild(t); t.select();
        try{document.execCommand('copy'); done()}catch(e){} document.body.removeChild(t);
      }
    });
    pre.appendChild(b);
  });

  // tree filtering
  var tree=$('#tree'), q=$('#tsearch'), types={}, warnOnly=false, area='', showClosed=false;
  function scoped(el){
    if(!showClosed&&el.getAttribute('data-closed')==='1') return false;
    var a=el.getAttribute('data-area'); if(area&&a&&a!==area) return false;
    return true;
  }
  var ta=$('#tarea'), tc=$('#tclosed');
  if(ta){ta.addEventListener('change',function(){area=ta.value;apply()})}
  if(tc){tc.addEventListener('change',function(){showClosed=tc.checked;apply()})}
  function applyCards(){
    var s=(q&&q.value||'').trim().toLowerCase(), any=!!s||warnOnly||area!==''||Object.keys(types).length>0, n=0;
    $$('.icard').forEach(function(c){
      var ok=scoped(c)&&(!s||c.getAttribute('data-text').indexOf(s)>-1)&&(Object.keys(types).length===0||types[c.getAttribute('data-type')])&&(!warnOnly||c.getAttribute('data-warn')==='1');
      c.hidden=!ok; if(ok){n++}
    });
    var tr=0;
    $$('.atable tbody tr').forEach(function(r){
      var ok=scoped(r)&&(!s||r.getAttribute('data-text').indexOf(s)>-1)&&(Object.keys(types).length===0||types['D'])&&(!warnOnly||r.getAttribute('data-warn')==='1');
      r.hidden=!ok; if(ok){tr++}
    });
    var t=$('#tcount'); if(t){t.textContent=any?((($('#v-trace')||{classList:{contains:function(){return false}}}).classList.contains('mode-table')?tr:n)+' matches'):''}
  }
  document.addEventListener('click',function(e){
    var b=e.target.closest&&e.target.closest('[data-open-table]'); if(!b) return;
    var tv=$('#v-trace'); tv.classList.remove('mode-tree'); tv.classList.add('mode-table');
    $$('.vmode button').forEach(function(x){x.setAttribute('aria-pressed',x.getAttribute('data-vmode')==='table'?'true':'false')});
    location.hash='#/trace';
  });
  $$('.vmode button').forEach(function(b){b.addEventListener('click',function(){
    var tv=$('#v-trace'); tv.classList.toggle('mode-tree',b.getAttribute('data-vmode')==='tree'); tv.classList.toggle('mode-table',b.getAttribute('data-vmode')==='table');
    $$('.vmode button').forEach(function(x){x.setAttribute('aria-pressed',x===b?'true':'false')});
  })});
  function apply(){
    applyCards();
    if(!tree) return;
    var s=(q.value||'').trim().toLowerCase(), any=!!s||warnOnly||area!==''||Object.keys(types).length>0, shown=0;
    function walk(ul){
      var vis=false;
      [].slice.call(ul.children).forEach(function(li){
        var own=scoped(li)&&(!s||(li.getAttribute('data-text')||'').indexOf(s)>-1)
          &&(Object.keys(types).length===0||types[li.getAttribute('data-type')])
          &&(!warnOnly||li.getAttribute('data-warn')==='1');
        var sub=li.querySelector(':scope > details > ul')||li.querySelector(':scope > ul');
        var cv=sub?walk(sub):false;
        var isItem=!!li.getAttribute('data-type');
        if(own&&isItem&&any){shown++}
        var show=(own&&(!sub||!any||true))||cv;
        if(any&&!own&&!cv){show=false}
        li.hidden=!show;
        if(any&&cv){var d=li.querySelector(':scope > details'); if(d){d.open=true}}
        vis=vis||show;
      });
      return vis;
    }
    walk(tree);
    var c=$('#tcount'); if(c&&$('#v-trace').classList.contains('mode-tree')){c.textContent=any?(shown+' matches'):''}
  }
  if(q){q.addEventListener('input',function(){apply()})}
  $$('#v-trace .filters button').forEach(function(b){
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')!=='true';
      b.setAttribute('aria-pressed',on?'true':'false');
      if(b.getAttribute('data-warn')){warnOnly=on}
      else{var k=b.getAttribute('data-type'); if(on){types[k]=true}else{delete types[k]}}
      apply();
    });
  });
  apply();
  var cards=$$('#acards .acard'), fs={}, ft={};
  function applyDocs(){
    var q=(($('#dsearch')||{}).value||'').trim().toLowerCase(), n=0;
    cards.forEach(function(c){
      var ok=(!q||c.getAttribute('data-text').indexOf(q)>-1)&&(!Object.keys(ft).length||ft[c.getAttribute('data-type')])&&(!Object.keys(fs).length||fs[c.getAttribute('data-stage')]);
      c.hidden=!ok; if(ok){n++}
    });
    var c=$('#dcount'); if(c){c.textContent=(q||Object.keys(ft).length||Object.keys(fs).length)?(n+' documents match'):''}
  }
  var ds=$('#dsearch'); if(ds){ds.addEventListener('input',applyDocs)}
  $$('#v-docs .filters button').forEach(function(b){
    b.addEventListener('click',function(){
      var on=b.getAttribute('aria-pressed')!=='true'; b.setAttribute('aria-pressed',on?'true':'false');
      var k=b.getAttribute('data-ftype');
      if(k){if(on){ft[k]=true}else{delete ft[k]}}
      applyDocs();
    });
  });
  function tabGroup(sel,onPick){
    $$(sel+' button').forEach(function(b){
      b.addEventListener('click',function(){
        $$(sel+' button').forEach(function(x){x.setAttribute('aria-selected',x===b?'true':'false')});
        onPick(b);
      });
    });
  }
  tabGroup('#v-docs .tabs2',function(b){fs={}; var s=b.getAttribute('data-fstage'); if(s){fs[s]=true} applyDocs()});
  tabGroup('#v-trace .tabs2',function(b){types={}; var t=b.getAttribute('data-type'); if(t){types[t]=true} apply()});
  var sel=$('#themeselect');
  if(sel){
    try{var saved=localStorage.getItem('hub-theme'); if(saved){sel.value=saved; root.setAttribute('data-theme',saved)}}catch(e){}
    sel.addEventListener('change',function(){
      root.setAttribute('data-theme',sel.value);
      try{localStorage.setItem('hub-theme',sel.value)}catch(e){}
    });
  }
  route();
})();
"""


THEMES = [("minimal", "Minimal (MUI, green)"), ("notion", "Notion (blue, compact)"), ("classic", "Classic (purple)"), ("editorial", "Editorial (serif, cream paper)"),
          ("swiss", "Swiss (black and white, strong grid)"), ("calm", "Calm (soft green)")]

# Each theme only overrides the colour tokens and a few details; layout is shared.
THEME_CSS = r"""
/* minimal: the Minimal UI kit look on top of Material UI: green primary, soft cards, dashed rules, soft "label" chips */
[data-theme=minimal]{--ink:#1c252e;--bg:#fff;--surface:#f4f6f8;--muted:#637381;--line:rgba(145,158,171,.28);--purple:#00a76f;--link:#007867;--tint:rgba(0,167,111,.08);--tint2:rgba(0,167,111,.16);--on-purple:#fff;--r:8px}
[data-theme=minimal] body{font-family:"Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
[data-theme=minimal] h1{font-weight:800;letter-spacing:-.01em}
[data-theme=minimal] h2{font-weight:700;color:#637381}
[data-theme=minimal] header.top{background:rgba(255,255,255,.86);backdrop-filter:blur(6px);border-bottom:1px dashed var(--line)}
[data-theme=minimal] .brand{font-weight:800;letter-spacing:-.01em}
[data-theme=minimal] .tsearch{background:#fff;border:1px solid rgba(145,158,171,.32);border-radius:8px;padding:9px 14px;color:var(--ink)}
[data-theme=minimal] .tsearch:focus{outline:0;border-color:#1c252e;box-shadow:0 0 0 1px #1c252e}
[data-theme=minimal] .side{border-right:1px dashed var(--line)}
[data-theme=minimal] .nav2 a{border-radius:8px;min-height:44px;font-weight:500;font-size:.9rem;color:#637381}
[data-theme=minimal] .nav2 a:hover{background:rgba(145,158,171,.08)}
[data-theme=minimal] .nav2 a[aria-current=page]{background:rgba(0,167,111,.08);color:#007867;font-weight:700}
[data-theme=minimal] .nav2 a[aria-current=page] .nm{color:#007867;opacity:1}
[data-theme=minimal] .acard,[data-theme=minimal] .jcard,[data-theme=minimal] .icard{border:0;border-radius:16px;background:#fff;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12);transition:box-shadow .2s,transform .2s}
[data-theme=minimal] .acard:hover,[data-theme=minimal] .jcard:hover,[data-theme=minimal] .icard:hover{border:0;box-shadow:0 0 2px 0 rgba(145,158,171,.24),0 20px 40px -4px rgba(145,158,171,.24);transform:translateY(-2px)}
[data-theme=minimal] .acard .thumb{border-radius:0}
[data-theme=minimal] .acard .atype,[data-theme=minimal] .jcard .wk,[data-theme=minimal] .icard .itype{color:#919eab}
[data-theme=minimal] .acard h3,[data-theme=minimal] .jcard h3,[data-theme=minimal] .icard h3{font-weight:700}
[data-theme=minimal] .stats b{font-weight:800;color:#1c252e}
[data-theme=minimal] .glist{border-top:0}
[data-theme=minimal] .grow{border-bottom:1px dashed var(--line)}
[data-theme=minimal] .grow .gb{height:6px;background:rgba(0,167,111,.16)}
[data-theme=minimal] .grow .gb i{background:#00a76f;border-radius:99px}
[data-theme=minimal] .grow .gs,[data-theme=minimal] .gst{display:inline-block;justify-self:start;font-size:.75rem;font-weight:700;line-height:24px;padding:0 8px;border-radius:6px;background:rgba(255,171,0,.16);color:#b76e00}
[data-theme=minimal] .grow .gs.ok,[data-theme=minimal] .gst-passed{background:rgba(34,197,94,.16);color:#118d57}
[data-theme=minimal] .grow .gs.no,[data-theme=minimal] .gst-failed{background:rgba(255,86,48,.16);color:#b71d18}
[data-theme=minimal] .gst::before{display:none}
[data-theme=minimal] table th{background:#f4f6f8;color:#637381;font-weight:600;font-size:.8125rem;text-transform:none;letter-spacing:0;border-bottom:0}
[data-theme=minimal] table th:first-child{border-radius:8px 0 0 8px}
[data-theme=minimal] table th:last-child{border-radius:0 8px 8px 0}
[data-theme=minimal] table td{border-bottom:1px dashed var(--line)}
[data-theme=minimal] table.props th{background:none;color:#637381;font-weight:500;border-radius:0;border-bottom:1px dashed var(--line)}
[data-theme=minimal] .chip,[data-theme=minimal] .idc,[data-theme=minimal] .idtag{border-radius:6px;font-weight:700;font-size:.75rem;border:1px solid transparent}
[data-theme=minimal] .t-O{background:#00a76f;color:#fff}
[data-theme=minimal] .t-H{background:transparent;border-color:rgba(0,167,111,.5);color:#007867}
[data-theme=minimal] .t-D{background:#1c252e;color:#fff}
[data-theme=minimal] .t-E{background:transparent;border-color:rgba(28,37,46,.35);color:#1c252e}
[data-theme=minimal] .t-M{background:rgba(145,158,171,.16);color:#454f5b}
[data-theme=minimal] .t-P{background:transparent;border:1px dashed rgba(145,158,171,.8);color:#637381}
[data-theme=minimal] .t-A{background:rgba(0,184,217,.16);color:#006c9c}
[data-theme=minimal] .filters button{border:1px solid rgba(145,158,171,.32);border-radius:8px;background:#fff;color:#454f5b;font-weight:600;padding:5px 12px}
[data-theme=minimal] .filters button:hover{background:rgba(145,158,171,.08)}
[data-theme=minimal] .filters button[aria-pressed=true]{background:#1c252e;border-color:#1c252e;color:#fff}
[data-theme=minimal] .tabs2 button[aria-selected=true]{color:#007867;border-bottom-color:#00a76f}
[data-theme=minimal] .vmode{border:1px solid rgba(145,158,171,.32);border-radius:8px;padding:3px}
[data-theme=minimal] .vmode button{border-radius:6px;font-weight:700}
[data-theme=minimal] .vmode button[aria-pressed=true]{background:#1c252e;color:#fff}
[data-theme=minimal] .btn{background:#1c252e;color:#fff;border-radius:8px;padding:6px 14px;font-weight:700;font-size:.8125rem}
[data-theme=minimal] .btn:hover{text-decoration:none;background:#454f5b}
[data-theme=minimal] .banner,[data-theme=minimal] .warnbox{background:rgba(255,171,0,.12);color:#7a4100;border:0;border-radius:8px;padding:12px 16px}
[data-theme=minimal] .warnlist li{border-top:0;border-bottom:1px dashed var(--line)}
[data-theme=minimal] details.help{border:1px dashed var(--line);border-radius:16px;padding:14px 20px}
[data-theme=minimal] .backlinks{border-top:1px dashed var(--line)}
[data-theme=minimal] .mcard{border:0;border-radius:16px;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12);background:#fff;overflow:hidden}
[data-theme=minimal] .fig{border:0;border-radius:16px;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12)}
[data-theme=minimal] .st{border:0;border-radius:6px;background:rgba(145,158,171,.16);color:#454f5b;font-weight:700;line-height:22px}
[data-theme=minimal] .st-verified{background:rgba(34,197,94,.16);color:#118d57}
[data-theme=minimal] .st-draft{background:rgba(255,171,0,.16);color:#b76e00;border:0}
[data-theme=minimal] .st-simulated,[data-theme=minimal] .st-planned{background:rgba(0,184,217,.16);color:#006c9c;border:0}
[data-theme=minimal] .pn{border-top:1px dashed var(--line)}
[data-theme=minimal] code{background:rgba(145,158,171,.16);border-radius:6px}
[data-theme=minimal] footer.foot{border-top:1px dashed var(--line)}
[data-theme=minimal] .tree ul{border-left:1px dashed var(--line)}
[data-theme=minimal] hr{border-top:1px dashed var(--line)}
[data-theme=minimal] .dlink,[data-theme=minimal] .sthead{border-top:1px dashed var(--line)}
[data-theme=minimal] .dlink:first-child{border-top:0}
[data-theme=minimal] .wgroup,[data-theme=minimal] .astat{border:0;border-radius:16px;background:#fff;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12)}
[data-theme=minimal] pre{background:rgba(145,158,171,.12);border-radius:8px}
[data-theme=minimal] pre code{background:none}

/* notion: neutral grey, one blue accent, small radius, almost no fill */
[data-theme=notion]{--ink:#37352f;--bg:#fff;--surface:#f7f6f3;--muted:rgba(55,53,47,.65);--line:rgba(55,53,47,.13);--purple:#2383e2;--link:#0b6bcb;--tint:rgba(35,131,226,.08);--tint2:rgba(35,131,226,.15);--r:6px}
[data-theme=notion] h1{font-size:2.1rem;font-weight:700}
[data-theme=notion] .tabs a{border-radius:6px;font-weight:500}
[data-theme=notion] .card,[data-theme=notion] .jcard,[data-theme=notion] details.help{background:transparent}
[data-theme=notion] .gate{background:var(--surface);color:var(--ink);border:1px solid var(--line)}
[data-theme=notion] .gate .bar{background:var(--line)}
[data-theme=notion] .gate .bar i{background:var(--purple)}
[data-theme=notion] .banner{background:var(--tint2);color:var(--ink)}
[data-theme=notion] th{background:var(--surface);font-weight:600}
[data-theme=notion] .chip,[data-theme=notion] .idc,[data-theme=notion] .idtag{border-radius:4px}

/* editorial: serif text on warm paper, terracotta accent, thin rules */
[data-theme=editorial]{--ink:#201c17;--bg:#fbf8f3;--surface:#f3eee5;--muted:rgba(32,28,23,.68);--line:rgba(32,28,23,.18);--purple:#9a3412;--link:#9a3412;--tint:rgba(154,52,18,.08);--tint2:rgba(154,52,18,.15);--r:2px}
[data-theme=editorial] body{font-family:Georgia,"Times New Roman",serif;font-size:17px}
[data-theme=editorial] h1,[data-theme=editorial] h2,[data-theme=editorial] h3{font-family:Georgia,"Times New Roman",serif;font-weight:700;letter-spacing:-.01em}
[data-theme=editorial] header.top{border-bottom:2px solid var(--ink)}
[data-theme=editorial] .tabs a{border-radius:0;text-transform:uppercase;letter-spacing:.08em;font-size:.78rem;font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
[data-theme=editorial] .card,[data-theme=editorial] .jcard,[data-theme=editorial] details.help,[data-theme=editorial] .pane-tree{background:transparent;border-color:var(--ink)}
[data-theme=editorial] .gate{background:transparent;color:var(--ink);border:1px solid var(--ink)}
[data-theme=editorial] .gate .bar{background:var(--line)}
[data-theme=editorial] .gate .bar i{background:var(--purple)}
[data-theme=editorial] .banner{background:var(--ink);color:var(--bg)}
[data-theme=editorial] .chip,[data-theme=editorial] .idc,[data-theme=editorial] .idtag,[data-theme=editorial] .filters button,[data-theme=editorial] .tsearch,[data-theme=editorial] table,[data-theme=editorial] .tree a.node,[data-theme=editorial] .card .lbl,[data-theme=editorial] .ihead .kind,[data-theme=editorial] .jcard .wk{font-family:-apple-system,"Segoe UI",Helvetica,Arial,sans-serif}
[data-theme=editorial] th{background:transparent;border-bottom:2px solid var(--ink)}

/* swiss: black on white, hard 1px frames, one signal colour, no rounding */
[data-theme=swiss]{--ink:#000;--bg:#fff;--surface:#fff;--muted:rgba(0,0,0,.62);--line:#000;--purple:#ff3b00;--link:#000;--tint:#f1f1f1;--tint2:#e3e3e3;--r:0}
[data-theme=swiss] body{font-family:"Helvetica Neue",Helvetica,Arial,sans-serif}
[data-theme=swiss] h1{font-size:2.3rem;font-weight:800;letter-spacing:-.03em}
[data-theme=swiss] h2{text-transform:uppercase;font-size:.85rem;letter-spacing:.1em;border-top:2px solid #000;padding-top:10px}
[data-theme=swiss] header.top{border-bottom:2px solid #000}
[data-theme=swiss] .tabs a{border-radius:0;text-transform:uppercase;font-size:.78rem;letter-spacing:.06em}
[data-theme=swiss] .tabs a[aria-current=page]{background:#000;color:#fff}
[data-theme=swiss] .tsearch,[data-theme=swiss] .filters button{border-radius:0;border-color:#000}
[data-theme=swiss] .filters button[aria-pressed=true]{background:#000;border-color:#000}
[data-theme=swiss] .card,[data-theme=swiss] .jcard,[data-theme=swiss] details.help,[data-theme=swiss] .pane-tree,[data-theme=swiss] .backlinks{border:1px solid #000}
[data-theme=swiss] .jcard:hover{border-color:var(--purple);box-shadow:4px 4px 0 var(--purple)}
[data-theme=swiss] .gate{background:#000;color:#fff}
[data-theme=swiss] .gate .bar{background:rgba(255,255,255,.3)}
[data-theme=swiss] .gate .bar i{background:var(--purple)}
[data-theme=swiss] .banner{background:var(--purple);color:#000;font-weight:700}
[data-theme=swiss] th{background:transparent;border-bottom:2px solid #000;text-transform:uppercase;font-size:.75rem;letter-spacing:.06em}
[data-theme=swiss] td{border-bottom:1px solid #000}
[data-theme=swiss] .warnlist li,[data-theme=swiss] blockquote{background:#f1f1f1;border-left:6px solid var(--purple)}
[data-theme=swiss] .t-H{color:#000;border-color:#000}
[data-theme=swiss] .t-E{border-color:#000}

/* calm: soft sage green, generous radius, quiet shadows */
[data-theme=calm]{--ink:#1f2a24;--bg:#fbfcfa;--surface:#f1f5f0;--muted:rgba(31,42,36,.66);--line:rgba(31,42,36,.12);--purple:#2f7d5b;--link:#256a4b;--tint:rgba(47,125,91,.10);--tint2:rgba(47,125,91,.18);--r:16px}
[data-theme=calm] h1{font-weight:700;letter-spacing:-.02em}
[data-theme=calm] .card,[data-theme=calm] .jcard,[data-theme=calm] details.help{box-shadow:0 1px 2px rgba(31,42,36,.06),0 4px 14px rgba(31,42,36,.04);border-color:transparent;background:#fff}
[data-theme=calm] .pane-tree{border-color:transparent;box-shadow:0 1px 2px rgba(31,42,36,.06),0 4px 14px rgba(31,42,36,.04);background:#fff}
[data-theme=calm] .gate{background:var(--purple);color:#fff}
[data-theme=calm] .banner{background:#fff;color:var(--ink);border:1px solid var(--line);border-left:6px solid var(--purple)}
[data-theme=calm] th{background:var(--surface)}
[data-theme=calm] .tabs a[aria-current=page]{box-shadow:0 2px 8px rgba(47,125,91,.35)}
"""


def theme_rules(theme, all_themes=False):
    """CSS overrides for one theme (or every theme when previewing with the switcher)."""
    keep = []
    for line in THEME_CSS.split("\n"):
        m = re.match(r"\[data-theme=(\w+)\]", line)
        if m and (all_themes or m.group(1) == theme):
            keep.append(line)
    return "\n" + "\n".join(keep) + "\n"


PLACEHOLDER_RE = re.compile(r"\[(?:EXAMPLE\]|[A-Z][A-Z0-9 ]{2,}[^\]]*\])")



# --------------------------------------------------------------------------- artifacts
ART_TYPES = {
    "competitor-analysis": "Competitor analysis", "persona": "Persona", "survey-results": "Survey results",
    "interview-synthesis": "Interview synthesis", "user-flow": "User flow", "process-map": "Process map", "ia-sitemap": "Information architecture",
    "prototype": "Prototype", "test-plan": "Test plan", "test-report": "Test report",
    "requirements": "Requirements (PRD)", "solution-pool": "Solution pool", "generic": "Document",
    "pestel-analysis": "PESTEL analysis", "research-plan": "Research plan", "interview-guide": "Interview guide",
    "journey-map": "Journey map", "measurement-plan": "Measurement plan", "stakeholder-map": "Stakeholder map",
    "usability-test-script": "Usability test script", "options": "Options",
    "problem-brief": "Problem brief", "prioritization": "Prioritization",
    "assumptions-map": "Assumptions map", "heuristic-evaluation": "Heuristic evaluation", "opportunity-solution-tree": "Opportunity solution tree",
}
STAGES = ["Setup", "Discover", "Define", "Develop", "Deliver", "Learn"]
ART_STATUS = {"verified": "Verified", "draft": "Draft", "simulated": "Simulated", "planned": "Planned"}
IMG_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif", ".bmp"}
HEAVY_BYTES = 2500 * 1024  # an image above this makes the report slow to open and to send
NOT_IN_BROWSERS = {".heic", ".heif", ".tif", ".tiff", ".psd", ".raw", ".ai", ".sketch", ".fig"}
VIDEO_EXT = {".mp4", ".webm", ".mov"}
PRIVATE_PARTS = ("_raw-private", "_personal", "/.git/", "_templates")
DRAFT_RE = re.compile(r"\bAI draft\b", re.I)


def _is_private(abs_path):
    n = abs_path.replace(os.sep, "/")
    return any(x in n for x in PRIVATE_PARTS) or os.path.basename(n) in ("AGENTS.md", ".DS_Store")


def _aslist(v):
    if v is None or v == "":
        return []
    return list(v) if isinstance(v, list) else [v]


class Artifact(object):
    def __init__(self, slug, md_path, folder):
        self.id, self.path, self.folder = slug, md_path, folder
        raw = open(md_path, encoding="utf-8").read()
        self.meta, self.body = _front(raw)
        hm = re.search(r"^#\s+(.+)$", self.body, flags=re.M)
        self.title = str(self.meta.get("title") or (hm.group(1) if hm else slug)).strip()
        self.type = str(self.meta.get("type") or "generic").strip().lower()
        self.stage = str(self.meta.get("stage") or "").strip()
        self.status = str(self.meta.get("status") or "").strip().lower()
        self.summary = str(self.meta.get("summary") or "").strip()
        self.takeaways = [str(x) for x in _aslist(self.meta.get("takeaways"))]
        self.supports = _ids(_aslist(self.meta.get("supports")))
        self.source = str(self.meta.get("source") or "").strip()
        self.links = [str(x) for x in _aslist(self.meta.get("links"))]
        self.media = [str(x) for x in _aslist(self.meta.get("media"))]
        self.embed = str(self.meta.get("embed") or "").lower() in ("true", "yes", "1")
        self.embed_url = str(self.meta.get("embed_url") or "").strip()


METHOD_ORDER = [
    # Discover
    "scope", "stakeholder-map", "assumptions-map", "evaluate-current-experience", "analytics-review", "field-observation",
    "survey-results", "user-voice-synthesis", "competitor-analysis",
    # Define
    "affinity-map", "personas", "journey-map", "frame-opportunity", "prioritization", "design-principles", "problem-brief",
    # Develop
    "ideation", "options", "user-flow", "information-architecture", "wireframes", "prototype", "concept-test", "alignment",
    # Deliver
    "test-plan", "usability-test-report", "findings", "design-qa", "handoff", "measurement-plan", "rollout-plan",
    # Learn
    "learning",
]


def collect_artifacts(case):
    base = os.path.join(case, "work")
    out = []
    if not os.path.isdir(base):
        return out
    for name in sorted(os.listdir(base), key=_natkey):
        if name.startswith(("_", ".")) or name.lower() == "readme.md":
            continue
        full = os.path.join(base, name)
        if os.path.isfile(full) and name.endswith(".md"):
            out.append(Artifact(name[:-3], full, None))
        elif os.path.isdir(full) and os.path.isfile(os.path.join(full, "index.md")):
            # a folder is a document only when it has an index.md (sources/, original-docs/ stay plain folders)
            out.append(Artifact(name, os.path.join(full, "index.md"), full))
    # Cards follow the double diamond: Discover, Define, Develop, Deliver, Learn; inside a stage, the usual order of the methods.
    stage_rank = {"setup": 0, "discover": 1, "define": 2, "develop": 3, "deliver": 4, "learn": 5}
    seq = {k: n for n, k in enumerate(METHOD_ORDER)}
    out.sort(key=lambda a: (stage_rank.get(a.stage.strip().lower(), 9), seq.get(a.id, 999), _natkey(a.id)))
    return out


def media_kind(path):
    ext = os.path.splitext(path)[1].lower()
    if ext in IMG_EXT:
        return "image"
    if ext in VIDEO_EXT:
        return "video"
    if ext == ".pdf":
        return "pdf"
    if ext in (".html", ".htm"):
        return "html"
    if ext == ".csv":
        return "csv"
    if ext == ".md":
        return "doc"
    return "file"


def render_md(md, src, resolver, problems, team=False):
    """Render markdown; sections whose H2 mentions 'AI draft' are dropped (default) or folded (team mode)."""
    segs, cur = [], []
    for line in md.replace("\r\n", "\n").split("\n"):
        if re.match(r"##\s+\S", line):
            segs.append(cur)
            cur = [line]
        else:
            cur.append(line)
    segs.append(cur)
    out = []
    for seg in segs:
        if not any(l.strip() for l in seg):
            continue
        head = seg[0] if re.match(r"##\s+\S", seg[0]) else ""
        draft = bool(head and DRAFT_RE.search(head))
        if draft and not team:
            continue
        h = Renderer(src, resolver, problems).render("\n".join(seg))
        if draft:
            h = '<details class="draft"><summary>AI draft, not verified: %s</summary>%s</details>' % (
                html.escape(re.sub(r"^#+\s*", "", head), quote=False), h)
        out.append(h)
    return "\n".join(out)


def plural(n, one, many):
    return "%d %s" % (n, one if n == 1 else many)


def esc(s):
    return html.escape(s, quote=True)


def build(case, out_path, theme="minimal", switcher=False, team=False, bundle=False):
    problems = []
    overview, weekly, items, ref, ctx = collect(case)
    _sidx0 = os.path.join(case, "stages", "README.md")
    _smd0 = open(_sidx0, encoding="utf-8").read() if os.path.isfile(_sidx0) else ""
    problems.extend(stage_table_issues(_smd0))
    if not weekly:
        problems.append("Stages: the Pages table in stages/README.md has no pages, so Stages is empty")
    for p_ in weekly:  # a stage page and a Work file can share a file name (scope.md): the stage id gets a prefix
        p_.slug, p_.id = p_.id, "stage-" + p_.id
    arts = collect_artifacts(case)
    A = {a.id: a for a in arts}
    used_media = set()
    name, agreement = case_info(overview.md, case)
    _sidx = os.path.join(case, "stages", "README.md")
    winfo = week_info(open(_sidx, encoding="utf-8").read() if os.path.isfile(_sidx) else "")
    pr_md = next((p.md for p in ref if p.id == "principles"), "")
    gates_md = next((p.md for p in ref if p.id == "gates"), "")
    principles = parse_principles(pr_md)
    gates = parse_gates(gates_md)
    G = Graph(items, principles)

    # Case log: every ID it mentions must exist, and every decision should have a line.
    _clp = next((q for q in (os.path.join(case, "insights", "case-log.md"), os.path.join(case, "standards", "case-log.md"),
                             os.path.join(case, "reference", "case-log.md")) if os.path.isfile(q)), None)
    log_rows = parse_case_log(open(_clp, encoding="utf-8").read()) if _clp else []
    logged = {i for r in log_rows for i in r[3]}
    unknown_ids = sorted({i for i in logged if i not in G.items and i not in principles}, key=_natkey)
    if unknown_ids:
        G.warnings.append(("log-unknown-id", unknown_ids, "The case log mentions IDs that have no file"))
    G.flag("no-log", [d for d in G.D if d not in logged], "This decision has no line in the case log")

    # Gates: what the data says, next to what a person set. A gate marked passed while the data disagrees is a warning.
    auto = auto_checks(G, principles)
    for g_ in gates:
        for cid, _, status in g_["checks"]:
            if status == "passed" and cid in auto and auto[cid][0] is False:
                G.warnings.append(("gate-mismatch", [cid], "Check %s is marked passed but the data shows: %s" % (cid, auto[cid][1])))
    gp = next((p for p in ref if p.id == "gates"), None)
    if gp:
        lines = []
        for ln in gp.md.split("\n"):
            c = _split_row(ln) if ln.strip().startswith("|") else None
            if c and len(c) >= 3 and re.fullmatch(r"\d[a-z]", c[0]):
                a = auto.get(c[0])
                cell = ("Met: " if a[0] else "Not met: ") + a[1] if a and a[0] is not None else "Manual check"
                ln = ln.rstrip() + " %s |" % cell
            elif c and len(c) >= 3 and c[0].lower() == "check":
                ln = ln.rstrip() + " Auto check |"
            elif c and len(c) >= 3 and set(c[0]) <= set("-: "):
                ln = ln.rstrip() + "---|"
            lines.append(ln)
        gp.md = "\n".join(lines)

    pages = weekly + ref + ctx + items
    by_path = {os.path.normcase(os.path.abspath(p.path)): p.id for p in pages}
    by_path[os.path.normcase(os.path.abspath(overview.path))] = "overview"
    case_abs = os.path.abspath(case)
    out_dir = os.path.dirname(os.path.abspath(out_path))
    for a in arts:
        by_path[os.path.normcase(os.path.abspath(a.path))] = a.id
    for p_ in weekly:  # a file only a stage page shows (e.g. insights/case-log.md) links to that stage page
        for path_, _m, _b in p_.parts:
            by_path.setdefault(os.path.normcase(os.path.abspath(path_)), p_.id)
    for a in arts:  # a link to a working file that backs an artifact opens that artifact
        if a.source:
            sp = os.path.normcase(os.path.abspath(os.path.join(os.path.dirname(a.path), a.source)))
            by_path.setdefault(sp, a.id)

    media_abs = set()
    for a in arts:
        for m in a.media:
            media_abs.add(os.path.abspath(os.path.normpath(os.path.join(os.path.dirname(a.path), m))))

    def href_for(abs_path):
        used_media.add(abs_path)
        base = case_abs if bundle else out_dir
        return urllib.parse.quote(os.path.relpath(abs_path, base).replace(os.sep, "/"), safe="/")

    def resolver(src, url, is_img):
        if re.match(r"(https?:|mailto:)", url):
            return "web", url
        if url.startswith("#/"):  # a link to another page of the report, e.g. [Insights](#/trace)
            return "page", url[2:]
        if url.startswith("#"):
            return "anchor", url
        target = os.path.normpath(os.path.join(os.path.dirname(src), url.split("#")[0]))
        key = os.path.normcase(os.path.abspath(target))
        if key in by_path:
            return "page", by_path[key]
        if os.path.isfile(target):
            if _is_private(target):
                return "outside", os.path.relpath(target, case_abs)
            if target.lower().endswith(".md") and os.path.abspath(target) not in media_abs:
                # raw working files are not published unless an artifact lists them in `media`
                return "outside", os.path.relpath(target, case_abs)
            if not os.path.abspath(target).startswith(case_abs + os.sep):
                return "outside", os.path.basename(target)
            return "file", href_for(os.path.abspath(target))
        if os.path.isdir(target):
            return "outside", os.path.relpath(target, case_abs) + "/"
        return "broken", url

    # --- consistency checks
    folder_of = {t[0]: {"O": "opportunities", "H": "hypotheses", "M": "metrics", "D": "decisions", "E": "evidence", "F": "findings"}.get(t[0]) for t in TYPES}
    for p in items:
        parent = os.path.basename(os.path.dirname(p.path))
        if parent != "insights" and folder_of.get(p.letter) and parent != folder_of[p.letter]:
            problems.append("%s is in folder %s/, should be in %s/" % (os.path.basename(p.path), parent, folder_of[p.letter]))
        if not p.meta:
            problems.append("%s: missing the properties block (--- ... ---) at the top of the file" % os.path.basename(p.path))
        elif not p.meta.get("title"):
            problems.append("%s: missing the title property" % os.path.basename(p.path))
        tp = str(p.meta.get("type", "")).lower()
        if p.meta and tp and tp != TYPE_WORD[p.letter]:
            problems.append("%s: type property is '%s' but ID %s is a %s" % (p.id, tp, p.id, TYPE_WORD[p.letter]))
    for f in G.F:
        if G.severity[f] is None:
            problems.append("%s: severity must be a number from 0 to 4" % f)
        if G.resolution[f] not in ("open", "fixed", "accepted", "deferred"):
            problems.append("%s: resolution is '%s', must be open, fixed, accepted or deferred" % (f, G.resolution[f]))
    seen = {}
    for p in pages:
        if p.id in seen:
            problems.append("Duplicate ID: %s" % p.id)
        seen[p.id] = 1
    for i, p in G.items.items():
        for label, val in p.meta.items():
            if label not in REL_KEYS:
                continue
            for t in _ids(val):
                if t not in G.items and t not in principles:
                    problems.append("%s points to %s but there is no matching file or principle row" % (i, t))

    def item_name(i):
        """Reader-facing name for an item ID: 'Decision 4' instead of 'D4'. The ID stays the key in files and links."""
        n = re.search(r"\d+", i)
        if i in G.items and n:
            return "%s %s" % (VI_SHORT[G.items[i].letter], n.group())
        if i in principles and n:
            return "Principle %s" % n.group()
        return i

    _title_count = {}
    for _p in G.items.values():
        _title_count[_p.title] = _title_count.get(_p.title, 0) + 1

    def chip(i, cls="chip"):
        if i in A:
            return '<a class="%s t-A" href="#/%s" title="%s">%s</a>' % (cls, i, esc(A[i].title), esc(A[i].title if len(A[i].title) < 28 else A[i].title[:26] + "…"))
        if i in G.items:
            p = G.items[i]
            return '<a class="%s t-%s" href="#/%s" title="%s">%s</a>' % (cls, p.letter, i, esc(p.title), esc(item_name(i)))
        if i in principles:
            return '<a class="%s t-P" href="#/principles" title="%s">%s</a>' % (cls, esc(principles[i][0]), esc(item_name(i)))
        return '<span class="%s">%s</span>' % (cls, esc(i))

    def iref(i):
        """Where there is room: the item's full title as the link. Two items with the same title get their name appended."""
        if i in G.items:
            t = G.items[i].title
            if _title_count.get(t, 0) > 1:
                t = "%s (%s)" % (t, item_name(i))
            return '<a class="iref" href="#/%s"><span class="irt">%s</span></a>' % (i, esc(t))
        return chip(i)

    def val_html(x, r):
        def link(m):
            tid = (m.group(2) or m.group(1)).strip()
            return chip(tid) if (tid in G.items or tid in principles) else esc(tid)
        if re.search(r"\[\[", x):
            return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: "\x00" + link(m) + "\x00", esc(x)).replace("\x00", "")
        return r.inline(x)

    def prop_table(p, r):
        rows_ = ""
        for k, v in p.meta.items():
            if k in ("title", "type"):  # both already shown in the page header
                continue
            vals = v if isinstance(v, list) else [v]
            if k == "type" and p.letter in VI_NAME:
                vals = [VI_NAME[p.letter][0]]
            vl = VALUE_LABEL.get(k, {})
            cell = " ".join((esc(vl[str(x).strip().lower()]) if str(x).strip().lower() in vl else val_html(str(x), r)) for x in vals if str(x).strip()) or "—"
            rows_ += '<tr><th scope="row">%s</th><td>%s</td></tr>' % (esc(PROP_LABEL.get(k, k.replace("_", " ").capitalize())), cell)
        return ('<div class="table-wrap"><table class="props"><tbody>%s</tbody></table></div>' % rows_) if rows_ else ""

    def chips(ids):
        return '<span class="chips">%s</span>' % "".join(chip(i) for i in ids) if ids else '<span class="missing">none yet</span>'

    placeholders = sum(len(PLACEHOLDER_RE.findall(p.md)) for p in [overview] + weekly + ctx)

    art_for = {}
    for a in arts:
        for s in a.supports:
            if s in G.items:
                art_for.setdefault(s, []).append(a.id)
            elif s not in principles:
                problems.append("Document %s points to %s but that item does not exist" % (a.id, s))
        if a.id in seen:
            problems.append("Duplicate ID: %s (document and page)" % a.id)
        if not a.supports and a.status != "planned":  # a method card not started yet is not an orphan
            G.warnings.append(("art-orphan", [a.id], "This document is not linked to any item (supports is empty)"))

    _media_cache, media_notes = {}, {}

    def media_of(a):
        """(kind, abs, name) in a stable order: explicit `media` first, then files dropped in the artifact folder."""
        if a.id in _media_cache:
            return _media_cache[a.id]
        seen_, out = set(), []
        notes = media_notes.setdefault(a.id, [])
        base = os.path.dirname(a.path)

        def note(msg):
            if msg not in notes:
                notes.append(msg)
                problems.append("Document %s: %s" % (a.id, msg))
        for m in a.media:
            ab = os.path.abspath(os.path.normpath(os.path.join(base, m)))
            if not os.path.isfile(ab):
                note("file %s not found (check the path in media)" % m)
                continue
            if _is_private(ab):
                note("skipped %s because it is in a private area" % m)
                continue
            if ab not in seen_:
                seen_.add(ab)
                out.append((media_kind(ab), ab, os.path.basename(ab)))
        if a.folder:
            for fn in sorted(os.listdir(a.folder), key=_natkey):
                ab = os.path.abspath(os.path.join(a.folder, fn))
                if os.path.isfile(ab) and ab != os.path.abspath(a.path) and not fn.startswith(".") and ab not in seen_ and not _is_private(ab):
                    seen_.add(ab)
                    out.append((media_kind(ab), ab, fn))
        for kind_, ab, nm in out:
            ext_ = os.path.splitext(nm)[1].lower()
            if ext_ in NOT_IN_BROWSERS:
                note("%s: browsers usually cannot show %s; export to PNG or JPG (images) or PDF (documents)" % (nm, ext_))
            elif kind_ == "image" and os.path.getsize(ab) > HEAVY_BYTES:
                note("%s is %.1f MB; compress it (under 2 MB) so the report opens fast and can be emailed" % (nm, os.path.getsize(ab) / 1048576.0))
            elif ext_ == ".mov":
                note("%s: .mov does not play in every browser; export to .mp4" % nm)
        order = {"image": 0, "html": 1, "video": 2, "pdf": 3, "csv": 4, "doc": 5, "file": 6}
        _media_cache[a.id] = sorted(out, key=lambda x: order.get(x[0], 9))
        return _media_cache[a.id]

    def where(folders, how):
        """One quiet line under a section title: which folder it shows, and how to add something to it."""
        return ('<div class="where"><span class="wl">Folder</span> %s<br><span class="wl">Add new</span> %s</div>'
                % (" ".join("<code>%s</code>" % esc(f) for f in folders), how))

    def srcfile(path):
        rel_ = os.path.relpath(os.path.abspath(path), case_abs).replace(os.sep, "/")
        return '<p class="srcfile">Source file: <code>%s</code></p>' % esc(rel_)

    # --- overview
    w_rows = {"block": set(), "review": set(), "info": set()}
    for kd_, ids_, _t in G.warnings:
        for i_ in ids_:
            w_rows[warn_tier(kd_)].add((kd_, i_))
    n_block, n_review = len(w_rows["block"]), len(w_rows["review"])
    stats = "".join('<span><b>%d</b>%s</span>' % (len(getattr(G, L)), pl.lower()) for L, _, _, pl in TYPES)
    measured_ = [m for m in G.M if str(G.items[m].meta.get("verdict") or "pending").strip().lower() in ("met", "missed", "inconclusive")]
    if measured_:
        hit_ = sum(1 for m in measured_ if str(G.items[m].meta.get("verdict")).strip().lower() == "met")
        stats += '<span><b>%d/%d</b>metrics on target</span>' % (hit_, len(measured_))
    if n_block:
        stats += '<span class="w bad"><b>%d</b>to fix</span>' % n_block
    if n_review or not n_block:
        stats += '<span class="w%s"><b>%d</b>to review</span>' % ("" if n_review else " ok", n_review)
    gate_html = ""
    for g in gates:
        pct = int(100 * g["passed"] / g["total"]) if g["total"] else 0
        stc = "ok" if g["status"] == "passed" else ("no" if g["status"] == "failed" else "")
        gate_html += ('<div class="grow"><div class="gn"><small>%s</small><strong>%s</strong></div><div class="gs %s">%s</div>'
                      '<div class="gb"><i style="width:%d%%"></i></div><div class="gc">%d/%d checks</div></div>') % (
            esc(g["name"].split("(")[0].strip()), esc(g["name"].split("(")[-1].rstrip(")")) if "(" in g["name"] else "",
            stc, STATUS_VI.get(g["status"], g["status"]), pct, g["passed"], g["total"])
    rows = ""
    for d in G.D:
        hs = G.tests.get(d, [])
        os_ = []
        for h in hs:
            for o in G.serves.get(h, []):
                if o not in os_:
                    os_.append(o)
        ts = []
        for h in hs:
            for t_ in G.tests_of(h):
                if t_ not in ts:
                    ts.append(t_)
        rows += '<tr data-type="D" data-warn="%s" data-closed="%s" data-area="%s" data-text="%s"><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>' % (
            "1" if d in G.warn else "0", "1" if d in G.closed else "0", esc(G.area[d]), esc((d + " " + G.items[d].title).lower()),
            '<a class="iref" href="#/%s"><span class="irt">%s</span></a>' % (d, esc(G.items[d].title)), chips(hs), chips(os_), chips(ts),
            chips(G.follows.get(d, [])) if G.follows.get(d) else "—",
            chips(G.strains.get(d, [])) if G.strains.get(d) else "—")
    align_table = ('<div class="table-wrap atable"><table><thead><tr><th>Decision</th><th>Hypothesis</th><th>Opportunity</th><th>Evidence</th><th>Follows principle</th><th>Pulls against principle</th></tr></thead><tbody>%s</tbody></table></div>' % rows) if rows else '<p class="ok">No decisions yet.</p>'
    n_dec = len(G.D)
    n_traced = sum(1 for d in G.D if any(G.serves.get(h) for h in G.tests.get(d, [])))
    n_tested = sum(1 for d in G.D if any(G.tests_of(h) for h in G.tests.get(d, [])))
    n_strain = sum(1 for d in G.D if G.strains.get(d))
    n_bad_f = sum(1 for f in G.F if G.is_open_finding(f) and (G.severity[f] or 0) >= 3)
    if n_dec:
        def stat(n, label):
            return '<div class="astat"><b>%d</b><span>%s</span></div>' % (n, label)
        align = ('<div class="astats">%s%s%s%s%s</div>'
                 '<p><button type="button" class="linkbtn" data-open-table="1">Open the full alignment table in Insights</button></p>') % (
            stat(n_dec, "decisions"), stat(n_traced, "traced to an opportunity"),
            stat(n_tested, "have evidence"), stat(n_strain, "pull against a principle"),
            stat(n_bad_f, "severity 3 or 4 findings unresolved"))
    else:
        align = '<p class="ok">No decisions yet.</p>'
    if G.warnings:
        # One group per kind of problem, so the section stays scannable however many items are added.
        # Each group says what is wrong once, then lists the items in a compact grid.
        W_KINDS = [
            ("no-need", "Decision not traced to an opportunity", "Link the decision to a hypothesis that serves an opportunity, or cut it."),
            ("strain", "Decision pulls against a principle", "Change the decision, or record why you accept the trade-off."),
            ("unserved", "Opportunity without a decision", "Add a decision for this opportunity, or lower its rank."),
            ("untested", "Hypothesis without a test", "Plan a test for this hypothesis."),
            ("nometric", "Hypothesis without a metric", "Attach a metric to tell if the hypothesis is right."),
            ("planned", "Evidence only planned", "Run the test or study, then record the result."),
            ("simulated", "Evidence uses simulated people", "Does not count as real evidence. Run it again with real users."),
            ("no-real-evidence", "Hypothesis without real-user evidence", "Needs at least one test with real users."),
            ("f-sev4", "Severity 4 finding unresolved", "Blocks handoff. Fix it, or accept it and record why in the case log."),
            ("f-sev3", "Severity 3 finding unresolved", "Needs a decision: fix it, or accept it as a trade-off and record it in the case log."),
            ("d-open-finding", "Decision has serious unresolved findings", "See the findings on the decision page, then fix or record why you accept them."),
            ("f-nosev", "Finding without a valid severity", "Set severity from 0 to 4 (see Severity levels)."),
            ("f-noevidence", "Finding not linked to evidence", "Set found_in to the evidence where it was found."),
            ("m-missed", "Metric missed its target", "Open the Learning page: record what you learned and which opportunity to revisit."),
            ("m-no-result", "Metric has a verdict but no result", "Fill in result (and measured_on) in the metric file."),
            ("m-no-target", "Metric without a target", "Fill in target: the threshold that shows the hypothesis is right."),
            ("d-no-owner", "Accepted decision without an owner", "Fill in owner (who is responsible) and decided_on."),
            ("o-no-reason", "Opportunity without a rank reason", "Fill in impact, confidence and rank_reason so others understand the rank."),
            ("no-log", "Decision not in the case log", "Add a line to insights/case-log.md and put the decision ID in the Items column."),
            ("log-unknown-id", "Case log mentions an ID that does not exist", "Fix the ID in the Items column or create the missing item file."),
            ("gate-mismatch", "Gate set by hand differs from the data", "See the Auto check column on the Gates page; fix the data or change the check status."),
            ("art-orphan", "Document not linked to any item", "Fill in the supports property in the document."),
            ("principles", "Principle without a check question", "Write a yes/no question for each principle."),
        ]
        by_kind = {}
        for kd, ids, text in G.warnings:
            by_kind.setdefault(kd, []).append((ids, text))
        known_ = {k2 for k2, _, _ in W_KINDS}
        ordered = [k for k, _, _ in W_KINDS if k in by_kind] + [k for k in by_kind if k not in known_]
        meta_ = {k: (t, h) for k, t, h in W_KINDS}

        def group_html(kd, open_):
            seen_, rows_ = set(), []
            for ids, text in by_kind[kd]:
                for i in ids:
                    note = ""
                    if kd == "strain":
                        m_ = re.search(r"principle (P\d+)", text)
                        note = m_.group(1) if m_ else ""
                    if (i, note) in seen_:
                        continue
                    seen_.add((i, note))
                    title = G.items[i].title if i in G.items else ""
                    rows_.append('<li>%s%s%s</li>' % (
                        chip(i),
                        ('<span class="wt">%s</span>' % esc(title)) if title else "",
                        ('<span class="wn">pulls against %s</span>' % chip(note)) if note else ""))
            ttl, hint = meta_.get(kd, (by_kind[kd][0][1], ""))
            return ('<details class="wgroup" id="wg-%s"%s><summary><span class="wtitle">%s</span><span class="wcount">%d</span></summary>'
                    '%s<ul class="wgrid">%s</ul></details>') % (
                kd, " open" if open_ else "", esc(ttl), len(rows_),
                ('<p class="whint">%s</p>' % esc(hint)) if hint else "", "".join(rows_))

        warn_html = ""
        if not (n_block or n_review):
            warn_html += '<p class="ok">Nothing to fix: every decision traces back to an opportunity, and serious findings have a way forward.</p>'
        for tr in ("block", "review", "info"):
            kinds_ = [k for k in ordered if warn_tier(k) == tr]
            if not kinds_:
                continue
            cnt = len(w_rows[tr]) if tr != "info" else sum(len({i for ids, _ in by_kind[k] for i in ids}) for k in kinds_)
            open_ = tr == "block" or (tr == "review" and cnt <= 12)
            inner = "".join(group_html(k, open_) for k in kinds_)
            if tr == "info":
                warn_html += ('<details class="winfo"><summary>%s <span class="wcount">%d</span></summary><div class="wgroups">%s</div></details>'
                              % (esc(TIER_LABEL[tr]), cnt, inner))
            else:
                warn_html += '<h3 class="wtier wtier-%s">%s <span class="wcount">%d</span></h3><div class="wgroups">%s</div>' % (tr, esc(TIER_LABEL[tr]), cnt, inner)
    else:
        warn_html = '<p class="ok">Nothing to fix: every decision traces back to an opportunity, and every hypothesis has a test and a metric.</p>'
    banner = ""
    if placeholders:
        banner = '<div class="banner" role="note"><strong>This report still has sample content or blanks</strong> (about %d, including items labelled [EXAMPLE]). Fill them in or delete them before sharing.</div>' % placeholders
    howto = (
        '<details class="help"><summary>How to read the report, and key terms</summary>'
        '<p>Key idea: <strong>every decision traces back to the user need behind it.</strong> '
        'Use the left menu to move between pages. Open the items marked ⚠ in Insights to see what needs a look.</p>'
        '<dl><dt>Opportunity</dt><dd>What users need or struggle with, backed by evidence. Not a feature.</dd>'
        '<dt>Hypothesis</dt><dd>What the team believes, with how it will know if it is right.</dd>'
        '<dt>Decision</dt><dd>A specific design choice, with the reason.</dd>'
        '<dt>Evidence</dt><dd>A test or study that checks a hypothesis, with its result. A <em>planned</em> or <em>simulated</em> label means it is not evidence from real users yet.</dd>'
        '<dt>Metric</dt><dd>The number that tells if a hypothesis is right. An <em>assumed</em> label means the product owner has not confirmed it.</dd>'
        '<dt>Principle</dt><dd>A design rule every decision should meet, for example the 10 usability heuristics by Nielsen (P1 to P10).</dd>'
        '<dt>Gate</dt><dd>A check before moving to the next stage.</dd>'
        '<dt>Alignment</dt><dd>How well each decision traces to a user need and meets the principles.</dd></dl></details>')
    docs_section = ""
    v_overview = (
        '<section class="view" id="v-overview"><div class="wrap">%s<h1>%s</h1><p class="lede">Agreement with product and business: <strong>%s</strong></p>'
        '<p class="where"><span class="wl">Source</span> <code>README.md</code> (project card), the items in <code>insights/</code> and <code>standards/gates.md</code>. To change content, edit the source file and rebuild the report.</p>'
        '<div class="stats">%s</div>'
        '<h2>Gates</h2><div class="glist">%s</div>'
        '<h2>Warnings</h2>%s'
        '<h2>Decision alignment</h2>%s'
        '%s</div></section>'
    ) % (banner, esc(name), esc(AGREE_VI.get((agreement or "").lower(), agreement or "not recorded")), stats, gate_html, warn_html, align, howto)

    # --- journey
    def doc_html(p, extra_pre="", extra_post="", reading=True):
        return render_md(p.md, p.path, resolver, problems, team)

    STAGE_TABLE_TITLE = {"opportunities": "Opportunities (ranked)", "hypotheses": "Hypotheses", "metrics": "Success metrics",
                         "decisions": "Design decisions", "evidence": "Evidence", "outcomes": "Outcomes: metric, result and the need behind it",
                         "findings": "Findings (by severity)"}
    stage_tables = _gen_tables(G, os.path.dirname(os.path.join(case_abs, "stages", "README.md")))
    SRC_STATUS = {"verified": ("Verified", "ok"), "draft": ("Draft, not verified", "w"),
                  "simulated": ("Simulated people", "w"), "planned": ("Planned only", "w")}

    def stage_html(p):
        out = ""
        want = p.spec["stage"].lower()
        gate = next((g for g in gates if want and g["name"].lower().startswith(want)), None)
        if gate:
            out += '<p class="stgate"><a href="#/gates">Gate %s</a>: %d/%d checks passed · %s</p>' % (
                esc(gate["name"]), gate["passed"], gate["total"], esc(STATUS_VI.get(gate["status"], gate["status"])))
        for ref in p.missing:
            problems.append("Stages · %s: work/%s not found (check the From work column in stages/README.md)" % (p.id, ref))
        def link_log_ids(h):
            def one(m):
                inner = re.sub(r"\b([OHMDEFP]\d+)\b", lambda t: chip(t.group(1)) if (t.group(1) in G.items or t.group(1) in principles) else t.group(1), m.group(2))
                return m.group(1) + inner + m.group(3)
            return re.sub(r"(<td[^>]*>)(.*?)(</td>)", one, h, flags=re.S).replace("<td></td>", '<td class="dash">—</td>')

        for path, meta, body in p.parts:
            rel = os.path.relpath(path, case_abs).replace(os.sep, "/")
            wid = by_path.get(os.path.normcase(os.path.abspath(path)))
            lab, cls = SRC_STATUS.get(str(meta.get("status", "")).strip().lower(), ("", ""))
            head = '<code>%s</code>' % esc(rel)
            if lab:
                head += '<span class="ststatus %s">%s</span>' % (cls, esc(lab))
            if wid:
                head += '<a href="#/%s">Open in Work →</a>' % esc(wid)
            body_html = render_md(body, path, resolver, problems, team)
            if os.path.basename(path) == "case-log.md":
                body_html = link_log_ids(body_html)
            out += '<section class="stsrc"><div class="sthead">%s</div>%s</section>' % (head, body_html)
        for key in p.spec["tables"]:
            if key not in stage_tables:
                problems.append("Stages · %s: no item table named '%s' (use: %s)" % (p.id, key, ", ".join(STAGE_TABLE_TITLE)))
                continue
            out += "<h2>%s</h2>%s" % (esc(STAGE_TABLE_TITLE[key]), render_md(stage_tables[key], p.path, resolver, problems, team))
        if not p.parts and not p.spec["tables"]:
            out += '<p class="empty">This page has no sources yet: add a file to the From work column, or pick a table in the Item tables column, in <code>stages/README.md</code>.</p>'
        return out

    def stage_src(p):
        bits = ["<code>work/%s</code>" % esc(os.path.relpath(path, os.path.join(case_abs, "work")).replace(os.sep, "/")) for path, _m, _b in p.parts]
        if p.spec["tables"]:
            bits.append("item tables from <code>insights/</code>")
        return '<p class="srcfile">This page is built from: %s</p>' % (", ".join(bits) if bits else "no sources yet")

    jcards, jdocs = "", ""
    for k, p in enumerate(weekly):
        wk, desc, label = winfo.get(p.slug, ("", "", p.heading))
        jcards += '<a class="jcard" href="#/%s"><span class="wk">%s</span><h3>%s</h3><p>%s</p></a>' % (
            p.id, "%02d · %s" % (k + 1, esc(wk if wk else "Trang")), esc(p.heading), esc(desc))
        prev = '<a href="#/%s">← %s</a>' % (weekly[k - 1].id, esc(weekly[k - 1].heading)) if k else "<span></span>"
        nxt = '<a href="#/%s">%s →</a>' % (weekly[k + 1].id, esc(weekly[k + 1].heading)) if k + 1 < len(weekly) else "<span></span>"
        jdocs += '<section class="doc" id="%s" data-title="%s"><a class="back" href="#/journey">← Stages</a><div class="reading"><h1>%s</h1>%s</div>%s<nav class="pn" aria-label="Previous and next page">%s%s</nav></section>' % (
            p.id, esc(p.heading), esc(p.heading),
            ('<p class="lede">%s</p>' % esc(desc)) + stage_html(p), stage_src(p), prev, nxt)
    v_journey = '<section class="view journey" id="v-journey"><div class="wrap"><div class="jlist"><h1>Stages</h1><p class="lede">Selected and kept up to date automatically from <code>work/</code> and <code>insights/</code>.</p>%s<div class="jcards">%s</div></div>%s</div></section>' % (
        "",
        jcards, jdocs)

    # --- reference
    ref_desc = {"gates": "The four gates and the checks in each", "principles": "10 usability heuristics (Heuristic Evaluation): principles every decision should meet", "severity": "Severity scale for usability problems, 0 to 4", "case-log": "One line per decision, with the reason"}
    def ref_blurb(p):
        # pages that are not built in: use the first plain or italic line under the title
        for ln in p.md.split("\n")[1:]:
            ln = ln.strip()
            if ln and not ln.startswith(("#", "|", ">", "-", "<", "```")):
                return re.sub(r"[*_`]", "", ln)[:130]
        return ""
    rcards = "".join('<a class="jcard" href="#/%s"><h3>%s</h3><p>%s</p></a>' % (
        p.id, esc(p.label), esc(ref_desc.get(p.id) or ref_blurb(p))) for p in ref)
    def ref_html(p):
        h = doc_html(p)
        # status words become quiet coloured labels; empty cells show a dash instead of a hole
        h = re.sub(r"<td>\s*(passed|open|failed)\s*</td>", lambda m: '<td><span class="gst gst-%s">%s</span></td>' % (m.group(1), STATUS_VI[m.group(1)]), h)
        if p.id == "case-log":
            def link_ids(m):
                inner = re.sub(r"\b([OHMDEFP]\d+)\b", lambda t: chip(t.group(1)) if (t.group(1) in G.items or t.group(1) in principles) else t.group(1), m.group(2))
                return m.group(1) + inner + m.group(3)
            h = re.sub(r"(<td[^>]*>)(.*?)(</td>)", link_ids, h, flags=re.S)
        return h.replace("<td></td>", '<td class="dash">—</td>')
    rdocs = "".join('<section class="doc" id="%s" data-title="%s"><a class="back" href="#/reference">← Standards</a><div class="reading">%s</div>%s</section>' % (p.id, esc(p.label), ref_html(p), srcfile(p.path)) for p in ref)
    v_reference = ('<section class="view reference" id="v-reference"><div class="wrap"><div class="jlist"><h1>Standards</h1>'
                   '<p class="lede">Yardsticks to check the work against: gates, principle checks, severity levels.</p>%s<div class="jcards">%s</div></div>%s</div></section>') % (
        where(["standards/"], "drop a <code>.md</code> file into the folder and the page appears here."), rcards, rdocs)

    # --- context: product, users and rules (context/)
    ccards = "".join('<a class="jcard" href="#/%s"><h3>%s</h3><p>%s</p></a>' % (
        p.id, esc(p.label), esc(ref_blurb(p))) for p in ctx)
    cdocs = "".join('<section class="doc" id="%s" data-title="%s"><a class="back" href="#/context">← Context</a><div class="reading">%s</div>%s</section>' % (
        p.id, esc(p.label), ref_html(p), srcfile(p.path)) for p in ctx)
    v_context = ('<section class="view reference" id="v-context"><div class="wrap"><div class="jlist"><h1>Context</h1>'
                 '<p class="lede">Background for the project: product and users, rules, design system, open questions.</p>%s<div class="jcards">%s</div></div>%s</div></section>') % (
        where(["context/"], "drop a <code>.md</code> file into the folder and the page appears here. The AI tool reads this folder first."), ccards, cdocs) if ctx else ""

    # --- documents (artifacts)
    def domain_label(url):
        host = urllib.parse.urlparse(url).netloc.lower().replace("www.", "")
        names = {"figma.com": "Figma", "miro.com": "Miro", "notion.so": "Notion", "docs.google.com": "Google Docs",
                 "drive.google.com": "Google Drive", "github.com": "GitHub", "loom.com": "Loom", "youtube.com": "YouTube"}
        for k, v in names.items():
            if host.endswith(k):
                return v
        return host or "Link"

    def media_html(a):
        parts = []
        figs = []
        files_ = media_of(a)
        for n_ in media_notes.get(a.id, []):
            parts.append('<p class="warnbox">⚠ %s</p>' % esc(n_))
        for kind, ab, nm in files_:
            href = href_for(ab)
            label = esc(nm)
            if kind == "image":
                # caption from the file name: "2-discover.png" -> "2 discover"
                cap = esc(re.sub(r"\s+", " ", re.sub(r"[_-]+", " ", os.path.splitext(nm)[0])).strip() or nm)
                figs.append('<figure class="fig"><a href="%s" target="_blank" rel="noopener"><img loading="lazy" src="%s" alt="%s"></a><figcaption>%s</figcaption></figure>' % (href, href, cap, cap))
            elif kind == "html":
                emb = ('<iframe loading="lazy" src="%s" title="%s"></iframe>' % (href, label)) if a.embed else ""
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">Prototype / trang HTML</span>'
                             '<a class="btn" href="%s" target="_blank" rel="noopener">Open in new tab ↗</a></div>%s</div>' % (label, href, emb))
            elif kind == "video":
                parts.append('<div class="mcard"><video controls preload="metadata" src="%s"></video><p class="cap">%s</p></div>' % (href, label))
            elif kind == "pdf":
                emb = ('<iframe loading="lazy" src="%s" title="%s"></iframe>' % (href, label)) if a.embed else ""
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">PDF</span>'
                             '<a class="btn" href="%s" target="_blank" rel="noopener">Open PDF ↗</a></div>%s</div>' % (label, href, emb))
            elif kind == "csv":
                try:
                    with open(ab, encoding="utf-8", newline="") as f:
                        rows_ = list(csv.reader(f))[:41]
                    th = "".join("<th>%s</th>" % esc(c) for c in rows_[0]) if rows_ else ""
                    tb = "".join("<tr>%s</tr>" % "".join("<td>%s</td>" % esc(c) for c in r) for r in rows_[1:])
                    parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">CSV table</span><a class="btn" href="%s" target="_blank" rel="noopener">Download ↗</a></div><div class="table-wrap"><table><thead><tr>%s</tr></thead><tbody>%s</tbody></table></div></div>' % (label, href, th, tb))
                except Exception:
                    parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><a class="btn" href="%s" target="_blank" rel="noopener">Download ↗</a></div></div>' % (label, href))
            else:
                tag = "Source document" if kind == "doc" else "Attachment"
                parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">%s</span><a class="btn" href="%s" target="_blank" rel="noopener">Open ↗</a></div></div>' % (label, tag, href))
        for ln in a.links:
            lab, _, url = ln.partition("|")
            url = (url or lab).strip(); lab = lab.strip() if "|" in ln else domain_label(url)
            parts.append('<div class="mcard"><div class="mhead"><strong>%s</strong><span class="mtag">%s</span>'
                         '<a class="btn" href="%s" target="_blank" rel="noopener">Open link ↗</a></div></div>' % (esc(lab), esc(domain_label(url)), esc(url)))
        if a.embed_url:
            parts.append('<div class="mcard"><iframe loading="lazy" src="%s" title="%s" allowfullscreen></iframe></div>' % (esc(a.embed_url), esc(a.title)))
        out = ""
        if figs:
            out += '<div class="figs">%s</div>' % "".join(figs)
        return out + "".join(parts)

    def art_card(a):
        thumb = ""
        for kind, ab, nm in media_of(a):
            if kind == "image":
                thumb = '<img class="thumb" loading="lazy" src="%s" alt="">' % href_for(ab)
                break
        n_media = len(media_of(a)) + len(a.links)
        badge = ('<span class="st st-%s">%s</span>' % (a.status, esc(ART_STATUS.get(a.status, a.status)))) if a.status else ""
        return ('<a class="acard" href="#/%s" data-type="%s" data-stage="%s" data-text="%s">%s<h3>%s</h3><p>%s</p>'
                '<span class="ameta">%s%s%s</span></a>') % (
            a.id, esc(a.type), esc(a.stage), esc((a.title + " " + a.summary + " " + a.type).lower()), thumb,
            esc(a.title), esc(a.summary),
            esc(a.stage) if a.stage else "", (" · " + badge) if badge else "", (" · %d files/links" % n_media) if n_media else "")

    adocs = ""
    for a in arts:
        label = ART_TYPES.get(a.type, a.type.replace("-", " ").capitalize())
        badge = ('<span class="st st-%s">%s</span>' % (a.status, esc(ART_STATUS.get(a.status, a.status)))) if a.status else ""
        warn = ""
        if a.status in ("simulated", "draft", "planned"):
            warn = '<p class="warnbox">⚠ This document is <strong>%s</strong>: %s</p>' % (esc(ART_STATUS.get(a.status, a.status)),
                {"simulated": "results come from simulated people, not real users.", "draft": "content has not been verified.", "planned": "only planned, not carried out yet."}[a.status])
        take = ("<h2>Key takeaways</h2><ul>%s</ul>" % "".join("<li>%s</li>" % Renderer(a.path, resolver, problems).inline(x) for x in a.takeaways)) if a.takeaways else ""
        sup = ('<div class="supports"><span class="lbl">Supports</span><span class="irefs">%s</span></div>' % "".join(iref(s) for s in a.supports)) if a.supports else ""
        med = media_html(a)
        med = ("<h2>Media</h2>%s" % med) if med else ""
        src_note = ('<p class="srcnote">Source: <code>%s</code></p>' % esc(a.source)) if a.source else ""
        own = re.sub(r"^\s*#\s+.*\n", "", a.body, count=1)
        body_html = render_md(own, a.path, resolver, problems, team) if own.strip() else ""
        if a.source:
            sp = os.path.abspath(os.path.join(os.path.dirname(a.path), a.source))
            if os.path.isfile(sp):
                sraw = open(sp, encoding="utf-8").read()
                _, sbody = _front(sraw)
                sbody = re.sub(r"^\s*#\s+.*\n", "", sbody, count=1)
                body_html += ("<h2>Full content</h2>" if body_html else "") + render_md(sbody, sp, resolver, problems, team)
            else:
                problems.append("Document %s: source %s not found" % (a.id, a.source))
        adocs += ('<section class="doc" id="%s" data-title="%s"><a class="back" href="#/docs">← Work</a>'
                  '<header class="ahead"><p class="kind">%s%s</p><h1>%s</h1>%s</header>%s%s%s%s<div class="reading">%s</div>%s</section>') % (
            esc(a.id), esc(a.title), esc(label), (" · " + esc(a.stage)) if a.stage else "", esc(a.title),
            ('<p class="sum">%s</p>' % esc(a.summary)) if a.summary else "", ('<p>%s</p>' % badge) if (badge and not warn) else "", warn, sup,
            take + med, body_html, src_note + srcfile(a.path))

    stage_order = {s: i for i, s in enumerate(STAGES)}
    _seq = {k: n for n, k in enumerate(METHOD_ORDER)}
    arts_sorted = sorted(arts, key=lambda a: (stage_order.get(a.stage, 99), _seq.get(a.id, 999), a.title.lower()))
    types_present = sorted({a.type for a in arts})
    stages_present = [s for s in STAGES if any(a.stage == s for a in arts)]
    dfilters = "".join('<button type="button" aria-pressed="false" data-ftype="%s">%s</button>' % (esc(x), esc(ART_TYPES.get(x, x.replace("-", " ").capitalize()))) for x in types_present)
    sfilters = '<button type="button" role="tab" aria-selected="true" data-fstage="">All<span class="n">%d</span></button>' % len(arts)
    sfilters += "".join('<button type="button" role="tab" aria-selected="false" data-fstage="%s">%s<span class="n">%d</span></button>' % (
        esc(s), esc(s), sum(1 for a in arts if a.stage == s)) for s in stages_present)
    if arts_sorted:
        grid = '<div class="acards" id="acards">%s</div>' % "".join(art_card(a) for a in arts_sorted)
    else:
        grid = '<div class="empty"><p><strong>No documents yet.</strong></p><p>Drop images, PDFs or a <code>.md</code> file into <code>work/</code>, or ask the AI tool to "add this document to the project" (see <code>work/README.md</code>).</p></div>'
    v_docs = ('<section class="view docs" id="v-docs"><div class="wrap"><div class="jlist"><h1>Work</h1>'
              '<p class="lede">Everything made in the project: analysis, personas, surveys, flows, wireframes, prototypes. Each document links to the decisions it supports.</p>'
              '%s'
              '<input id="dsearch" class="tsearch" type="search" placeholder="Search documents" aria-label="Search documents">'
              '<div class="tabs2" role="tablist" aria-label="Filter by stage">%s</div>'
              '<p class="tcount" id="dcount" aria-live="polite"></p>%s</div>%s</div></section>') % (
        where(["work/"], "drop a single <code>.md</code> file into the folder; for several files (images, PDFs, video) create a subfolder with an <code>index.md</code>. Or ask the AI tool: \"add this document to the project\"."), sfilters, grid, adocs)

    # --- trace: tree
    def tnode(i, kids="", cnt="", leaf=True, opened=False):
        p = G.items[i]
        w = i in G.warn
        a = '<a class="node" href="#/%s" data-id="%s"><span class="idn">%s</span><span class="nt">%s%s</span>%s</a>' % (
            i, i, esc(item_name(i)), esc(p.title), ('<span class="cnt">%s</span>' % cnt) if cnt else "",
            ('<span class="wb" title="%s" aria-label="has a warning">⚠</span>' % esc("; ".join(G.warn[i]))) if w else "")
        attrs = 'class="n%s" data-type="%s" data-warn="%s" data-closed="%s" data-area="%s" data-text="%s"' % (" leaf" if not kids else "", p.letter, "1" if w else "0", "1" if i in G.closed else "0", esc(G.area[i]), esc((i + " " + p.title).lower()))
        if kids:
            return '<li %s><details%s><summary>%s</summary><ul>%s</ul></details></li>' % (attrs, " open" if opened else "", a, kids)
        return "<li %s>%s</li>" % (attrs, a)

    placed = set()
    top = ""
    first_open = next((k for k, o in enumerate(G.O) if G.hyps_of(o)), 0)
    for k, o in enumerate(G.O):
        placed.add(o)
        hk = ""
        for h in G.hyps_of(o):
            placed.add(h)
            ds, ts, ms = G.decisions_of(h), G.tests_of(h), G.metric.get(h, [])
            kids = ""
            for x in ds + ts + ms:
                placed.add(x)
                fk = ""
                for f in (G.findings_of(x) if x in G.E else []):
                    placed.add(f)
                    fk += tnode(f)
                kids += tnode(x, fk, plural(len(G.findings_of(x)), "finding", "findings") if fk else "")
            cnt = " · ".join(s for s in [plural(len(ds), "decision", "decisions") if ds else "", plural(len(ts), "evidence", "evidence") if ts else "", plural(len(ms), "metric", "metrics") if ms else ""] if s) or "no decisions or tests yet"
            hk += tnode(h, kids, cnt)
        n_h = len(G.hyps_of(o))
        top += tnode(o, hk, plural(n_h, "hypothesis", "hypotheses") if n_h else "no hypothesis yet", opened=(k == first_open))
    loose = [i for i in sorted(G.items, key=_natkey) if i not in placed]
    if loose:
        lk = "".join(tnode(i) for i in loose)
        top += '<li class="n" data-type="" data-warn="0" data-text=""><details open><summary><span class="gh">Not linked to any opportunity (%d)</span></summary><ul>%s</ul></details></li>' % (len(loose), lk)
    ttabs = '<button type="button" role="tab" aria-selected="true" data-type="">All<span class="n">%d</span></button>' % len(G.items)
    ttabs += "".join('<button type="button" role="tab" aria-selected="false" data-type="%s">%s<span class="n">%d</span></button>' % (
        L, pl, len(getattr(G, L))) for L, _, _, pl in TYPES)
    filters = '<button type="button" aria-pressed="false" data-warn="1">⚠ Warnings only</button>'
    areas_ = sorted({a for a in G.area.values() if a})
    tbar = ""
    if areas_ or G.closed:
        tbar = '<div class="tbar">'
        if areas_:
            tbar += '<label>Area <select id="tarea"><option value="">All</option>%s</select></label>' % "".join(
                '<option value="%s">%s</option>' % (esc(a), esc(a)) for a in areas_)
        if G.closed:
            tbar += '<label><input type="checkbox" id="tclosed"> Show closed items (%d)</label>' % len(G.closed)
        tbar += "</div>"

    # --- trace: item docs
    idocs = ""
    for i in sorted(G.items, key=_natkey):
        p = G.items[i]
        r = Renderer(p.path, resolver, problems)
        body = re.sub(r"^<h1>.*?</h1>\n?", "", r.render(getattr(p, "body", p.md)), count=1)
        body = prop_table(p, r) + body
        warn = "".join('<p class="warnbox">⚠ %s</p>' % esc(w) for w in G.warn.get(i, []))
        chains = G.paths(i)
        path = ""
        if chains and p.letter != "O":
            more = ('<span class="more">and %d more paths</span>' % (len(chains) - 3)) if len(chains) > 3 else ""
            path = '<div class="path"><span>From the user need:</span>%s%s</div>' % ("".join(
                '<span class="chips chain">%s</span>' % " › ".join(chip(x) for x in c) for c in chains[:3]), more)
        bl = ""
        if G.back.get(i):
            groups = {}
            for src, label in G.back[i]:
                groups.setdefault(label, []).append(src)
            rows_ = "".join('<div class="row"><span class="lbl">%s</span><span class="irefs">%s</span></div>' % (
                esc(BACK_LABEL.get(lb, lb.replace("_", " "))), "".join(iref(s) for s in sorted(srcs, key=_natkey))) for lb, srcs in groups.items())
            bl = '<aside class="backlinks"><h2>Linked from</h2>%s</aside>' % rows_
        if art_for.get(i):
            dl = ""
            for x in art_for[i]:
                a_ = A[x]
                dl += ('<a class="dlink" href="#/%s"><span class="dtype">%s</span><span class="dtitle">%s</span>%s<span class="darr" aria-hidden="true">→</span></a>') % (
                    esc(x), esc(ART_TYPES.get(a_.type, a_.type.replace("-", " ").capitalize())), esc(a_.title),
                    ('<span class="st st-%s">%s</span>' % (a_.status, esc(ART_STATUS.get(a_.status, a_.status)))) if a_.status else "")
            bl += '<aside class="backlinks"><h2>Related documents</h2><div class="dlist">%s</div></aside>' % dl
        idocs += ('<section class="doc" id="%s" data-title="%s"><a class="back back-tree" href="#/trace">← Insights</a>'
                  '<header class="ihead"><div><p class="kind">%s · %s</p><h1>%s</h1></div></header>%s%s<div class="reading">%s</div>%s%s</section>') % (
            i, esc(i + " " + p.title), esc(VI_NAME[p.letter][0]), esc(i), esc(p.title), warn, path, body, bl, srcfile(p.path))
    def icard(i):
        p = G.items[i]
        w = i in G.warn
        meta = ""
        if p.letter == "O":
            n_h = len(G.hyps_of(i))
            meta = plural(n_h, "hypothesis", "hypotheses") if n_h else "no hypothesis yet"
        elif p.letter == "F":
            sv = G.severity[i]
            meta = " · ".join(x for x in [
                ("Level %d" % sv) if sv is not None else "no severity",
                ", ".join(item_name(x) for x in G.principle_of[i]),
                RESOLUTION_LABEL.get(G.resolution[i], G.resolution[i])] if x)
        elif p.letter == "M":
            vd_ = str(p.meta.get("verdict") or "pending").strip().lower()
            meta = " · ".join(x for x in [VERDICT_LABEL.get(vd_, vd_), ("target " + str(p.meta.get("target")).strip()) if str(p.meta.get("target") or "").strip() else ""] if x)
        elif p.letter == "D" and (str(p.meta.get("owner") or "").strip() or G.state.get(i)):
            meta = " · ".join(x for x in [STATE_LABEL.get(G.state.get(i, ""), G.state.get(i, "")), str(p.meta.get("owner") or "").strip()] if x)
        elif p.letter == "H":
            ds_, ts_, ms_ = G.decisions_of(i), G.tests_of(i), G.metric.get(i, [])
            meta = " · ".join(x for x in [plural(len(ds_), "decision", "decisions") if ds_ else "", plural(len(ts_), "evidence", "evidence") if ts_ else "", plural(len(ms_), "metric", "metrics") if ms_ else ""] if x) or "no decisions or tests yet"
        else:
            for k_ in REL_KEYS:
                ids_ = _ids(p.meta.get(k_, ""))
                if ids_:
                    meta = "%s: %s" % (PROP_LABEL.get(k_, k_), ", ".join(ids_))
                    break
        if w:
            meta = G.warn[i][0]
        return ('<a class="icard" href="#/%s" data-type="%s" data-warn="%s" data-closed="%s" data-area="%s" data-text="%s"><span class="top">'
                '<span class="itype">%s</span>%s</span><h3>%s</h3><p>%s</p></a>') % (
            i, p.letter, "1" if w else "0", "1" if i in G.closed else "0", esc(G.area[i]), esc((i + " " + p.title).lower()),
            esc(item_name(i) + ((" · " + G.area[i]) if G.area[i] else "") + ((" · " + STATE_LABEL.get(G.state[i], G.state[i])) if i in G.closed else "")),
            '<span class="w" title="has a warning">⚠</span>' if w else "", esc(p.title), esc(meta))
    def _card_order(L):
        if L == "F":  # worst findings first
            return sorted(G.F, key=lambda f: (-(G.severity[f] if G.severity[f] is not None else -1), _natkey(f)))
        return sorted(getattr(G, L), key=_natkey)
    icards = "".join(icard(i) for L, _, _, _pl in TYPES for i in _card_order(L))
    v_trace = (
        '<section class="view" id="v-trace"><div class="wrap"><div class="trace">'
        '<div class="pane-tree"><h1>Insights</h1><p class="lede">Opportunities, hypotheses, decisions, evidence, findings and metrics, linked to each other. Filter by type, or switch to Tree to see the chain of reasons from need to decision.</p>'
        '%s'
        '<div class="trow"><input id="tsearch" class="tsearch" type="search" placeholder="Search by ID or name" aria-label="Search insights">'
        '<div class="vmode" role="group" aria-label="View"><button type="button" data-vmode="cards" aria-pressed="true">Cards</button><button type="button" data-vmode="tree" aria-pressed="false">Tree</button><button type="button" data-vmode="table" aria-pressed="false">Matrix</button></div></div>'
        '<div class="tabs2" role="tablist" aria-label="Filter by type">%s</div>'
        '%s'
        '<p class="tcount" id="tcount" aria-live="polite"></p>'
        '<div class="icards">%s</div>%s'
        '<ul class="tree" id="tree">%s</ul></div>'
        '<div class="pane-detail">%s</div>'
        '</div></div></section>'
    ) % (where(["insights/"], "copy a template from <code>insights/_templates/</code> into the matching type folder (one file per card)."), ttabs, tbar, icards or '<div class="empty"><p><strong>Nothing here yet.</strong></p></div>', align_table, top or '<li class="n"><span class="nt">Nothing here yet.</span></li>', idocs)

    # --- guide: how to use this report (guide.md at the case root; optional)
    v_guide = ""
    _gp = os.path.join(case_abs, "guide.md")
    if os.path.isfile(_gp):
        _gm, _gb = _front(open(_gp, encoding="utf-8").read())
        v_guide = ('<section class="view journey guide" id="v-guide"><div class="wrap"><div class="jlist"><div class="reading">%s</div></div></div></section>'
                   % render_md(_gb, _gp, resolver, problems, team))

    # --- sidebar (same structure as the website: Overview, Journey, Documents by stage, Trace by type, Reference)
    def nlink(target, inner, cls=""):
        return '<a%s href="#/%s" data-nav="%s">%s</a>' % ((' class="%s"' % cls) if cls else "", esc(target), esc(target), inner)

    sec_counts = {"context": len(ctx), "journey": len(weekly), "docs": len(arts), "trace": len(items), "reference": len(ref)}
    nav = "".join('<a href="#/%s" data-nav="%s">%s%s</a>' % (
        k, k, t, ('<span class="nm">%d</span>' % sec_counts[k]) if k in sec_counts else "")
        for k, t in [("overview", "Overview")] + ([("context", "Context")] if ctx else []) + [("journey", "Stages"), ("docs", "Work"), ("trace", "Insights"), ("reference", "Standards")] + ([("guide", "Guide")] if v_guide else []))
    sidebar = '<details class="menu" open><summary>Menu</summary><nav class="nav2" aria-label="Report sections">%s</nav></details>' % nav

    now = ""  # no timestamp: the report is a pure function of the project files, so rebuilding never creates a diff
    theme_select = ""
    if switcher:
        theme_select = '<label class="themepick">Theme <select id="themeselect" aria-label="Choose a theme">%s</select></label>' % "".join(
            '<option value="%s"%s>%s</option>' % (k, " selected" if k == theme else "", esc(v)) for k, v in THEMES)
    doc = ("""<!doctype html>
<html lang="en" data-theme="{{THEME}}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{{NAME}} · Case report</title>
<style>{{CSS}}</style>
</head>
<body data-case="{{NAME}}">
<a class="skip" href="#main">Skip the menu</a>
<header class="top"><div class="top-in">
<div class="brand"><svg class="logo" viewBox="18 50 214 150" fill="currentColor" aria-hidden="true"><path d="M80.5165 60.4055C76.2827 67.7288 75.4817 70.1317 74.9096 77.2261C74.5663 81.8032 74.7952 87.5244 75.4817 90.0418C76.8548 94.7332 76.0921 95.8546 74.4519 95.191C72.8194 94.5455 67.7008 93.4746 47.4474 93.0169C33.1442 92.6736 21.244 92.5592 21.0151 92.5592C20.7862 92.6736 23.1892 96.1064 26.1643 100.226C29.1393 104.345 45.8455 127.573 63.1238 151.832L94.4764 196L96.4216 192.338C97.4515 190.279 101.228 183.184 104.889 176.548C108.436 169.911 112.899 161.215 114.844 157.21C117.705 151.26 118.62 150.23 119.65 151.603C120.337 152.518 128.575 162.931 138.073 174.602L155.236 196L157.296 193.483C158.44 191.995 161.415 186.732 163.933 181.811C169.311 170.941 169.769 163.732 165.992 154.807L163.59 149.2L188.077 112.24C201.579 91.8726 215.081 71.3904 218.171 66.699C221.26 62.0075 224.693 56.9728 225.837 55.7141L228.126 53.1967H207.071C180.296 53.0823 173.316 54.4554 163.475 62.0075C155.122 68.1865 150.888 74.3655 140.247 94.9621L132.351 110.295L130.292 107.663C129.033 106.176 126.63 103.201 124.914 101.027C108.78 81.0022 87.9541 54.4554 87.4964 53.1967C86.4666 50.6794 85.5512 51.7092 80.5165 60.4055ZM213.365 62.0075C212.22 62.8085 184.758 103.544 169.54 127.116C160.958 140.389 157.91 142.982 156.953 141.076C156.601 140.364 155.292 138.4 154.092 136.727C152.49 135.011 149.286 131.006 146.883 127.688C142.65 121.738 141.547 122.036 140.933 122.996C140.292 124 139.583 125.309 138.988 126.429C137.845 128.582 137.272 128.718 140.59 132.265C147.456 139.588 156.953 152.289 158.669 156.294C161.072 162.244 160.843 171.055 157.983 177.806C156.61 180.896 155.236 183.413 154.779 183.299C154.435 183.299 148.485 175.976 141.505 167.165C134.64 158.24 127.431 149.314 125.715 147.255L122.396 143.364L125.829 137.414C127.66 134.096 131.894 126.2 135.212 119.907C158.669 75.2809 162.445 69.7885 171.599 65.5547C174.574 64.1816 178.007 62.5796 179.266 62.0075C181.44 60.9777 211.419 59.9478 213.479 60.8633C213.937 61.0921 213.937 61.5498 213.365 62.0075ZM98.7102 79.8579C104.66 87.41 113.7 98.8526 118.849 105.26L128.346 117.046L123.541 126.658C120.794 132.036 118.277 136.384 117.819 136.384C117.133 136.499 110.954 128.832 90.9292 103.315C83.0338 93.2457 80.9742 87.5244 81.6607 78.7137C82.3473 72.077 85.6656 63.495 87.0387 65.097C87.4964 65.6691 92.76 72.3058 98.7102 79.8579ZM77.3125 103.315C83.4915 106.405 88.5263 111.668 100.999 127.917C105.69 133.981 110.382 140.046 111.64 141.533C113.7 144.165 113.7 144.28 108.78 153.205C106.148 158.24 101.571 166.821 98.7102 172.428C94.362 180.896 93.3322 182.269 92.3023 180.553C91.7302 179.408 89.3273 176.09 87.1532 173C84.9791 169.911 80.6309 163.732 77.427 159.269C74.3375 154.692 67.2431 144.852 61.7507 137.185C56.2582 129.519 50.0792 121.051 48.0196 118.191C46.0743 115.33 42.4127 110.41 40.0098 107.206C37.6068 104.002 35.6616 101.027 35.6616 100.569C35.6616 99.9968 43.7858 99.8824 53.7409 100.111C70.1037 100.455 72.1634 100.798 77.3125 103.315Z"/></svg><span>{{NAME}}</span></div>
{{THEME_SELECT}}
</div></header>
<div class="shell">
<aside class="side">{{SIDEBAR}}</aside>
<main id="main">
{{V_OVERVIEW}}
{{V_CONTEXT}}
{{V_JOURNEY}}
{{V_DOCS}}
{{V_TRACE}}
{{V_REFERENCE}}
{{V_GUIDE}}
<div class="wrap" style="padding-top:0"><footer class="foot">This report is generated automatically from the project files{{MODE}}.<details class="foot-tech"><summary>For whoever updates the report</summary><p>Edit the project source files, then ask the AI tool to rebuild the report, or run the export script of the product-workspace skill.</p></details></footer></div>
</main>
</div>
<script>{{JS}}</script>
</body>
</html>
""").replace("{{NAME}}", esc(name)).replace("{{NOW}}", now).replace("{{MODE}}", " · team version (includes AI drafts)" if team else "").replace("{{V_OVERVIEW}}", v_overview).replace("{{V_CONTEXT}}", v_context) \
        .replace("{{V_JOURNEY}}", v_journey).replace("{{V_DOCS}}", v_docs).replace("{{V_TRACE}}", v_trace).replace("{{V_REFERENCE}}", v_reference).replace("{{V_GUIDE}}", v_guide) \
        .replace("{{CSS}}", CSS + theme_rules(theme, switcher)).replace("{{JS}}", JS).replace("{{THEME}}", theme).replace("{{THEME_SELECT}}", theme_select).replace("{{SIDEBAR}}", sidebar)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(doc)
    return G, weekly, ref, problems, placeholders, name, arts, used_media


def main():
    ap = argparse.ArgumentParser(description="Export the markdown hub to one self-contained HTML file.")
    ap.add_argument("--case", default="", help="case folder (default: the case you are standing in)")
    ap.add_argument("--out", default=None)
    ap.add_argument("--theme", default="minimal", choices=[k for k, _ in THEMES], help="visual theme of the report")
    ap.add_argument("--preview-themes", action="store_true", help="add a theme switcher to the report (for choosing a theme)")
    ap.add_argument("--team", action="store_true", help="team version: show AI-draft sections, folded and labelled")
    ap.add_argument("--bundle", default=None, metavar="DIR", help="write a clean folder (index.html + only the files it uses) to send to others")
    ap.add_argument("--zip", action="store_true", help="with --bundle: also make DIR.zip")
    a = ap.parse_args()
    case = os.path.abspath(a.case) if a.case else find_case()
    if not case:
        sys.exit("Case folder not found. Run inside a case (a folder with AGENTS.md and insights/), or pass --case <path>.")
    bundle_dir = os.path.abspath(a.bundle) if a.bundle else None
    if bundle_dir:
        os.makedirs(bundle_dir, exist_ok=True)
        out = os.path.join(bundle_dir, "index.html")
    else:
        out = a.out or os.path.join(case, "index.html")
    G, weekly, ref, problems, placeholders, name, arts, used = build(case, out, a.theme, a.preview_themes, a.team, bool(bundle_dir))
    if bundle_dir:
        total = os.path.getsize(out)
        for ab in sorted(used):
            if not os.path.isfile(ab):
                continue
            dest = os.path.join(bundle_dir, os.path.relpath(ab, case))
            os.makedirs(os.path.dirname(dest), exist_ok=True)
            shutil.copy2(ab, dest)
            total += os.path.getsize(ab)
        print("Bundle: %s (%d files, %.1f MB)" % (bundle_dir, len(used) + 1, total / 1048576.0))
        if a.zip:
            z = shutil.make_archive(bundle_dir, "zip", bundle_dir)
            print("Zip: %s (%.1f MB)" % (z, os.path.getsize(z) / 1048576.0))
    print("Case: %s" % name)
    print("Included in the report: %d stage pages, %d standards, %d documents (artifacts), %d items (O %d, H %d, M %d, D %d, E %d)" % (
        len(weekly), len(ref), len(arts), len(G.items), len(G.O), len(G.H), len(G.M), len(G.D), len(G.E)))
    if a.team:
        print("  Team version: AI-draft sections are shown (collapsed). Do not send this version to stakeholders.")
    if G.warnings:
        print("Warnings (%d):" % len(G.warnings))
        for tr in ("block", "review", "info"):
            rows = [(kd, ids, text) for kd, ids, text in G.warnings if warn_tier(kd) == tr]
            if rows:
                print("  [%s]" % TIER_LABEL[tr])
                for _, ids, text in rows:
                    print("  - %s: %s" % (", ".join(ids), text))
    for p in problems:
        print("  ! %s" % p)
    if placeholders:
        print("  ! At least %d places still have sample or blank data" % placeholders)
    print("Written: %s" % out)
    print("Open index.html in a browser (double-click) to view the hub.")
    # keep the workspace home page (one card per case) in step with this report, when this script
    # is the workspace's shared copy (toolkit/skills/)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        home = os.path.join(here, "export-home.py")
        ws = os.path.dirname(os.path.abspath(case))
        if not bundle_dir and os.path.isfile(home) and os.path.join(ws, "toolkit", "skills") == here:
            import subprocess
            subprocess.run([sys.executable, home, "--workspace", ws], capture_output=True, text=True, timeout=60)
    except Exception:
        pass


if __name__ == "__main__":
    main()
