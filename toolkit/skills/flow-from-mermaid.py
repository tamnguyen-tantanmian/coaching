#!/usr/bin/env python3
"""
flow-from-mermaid.py - turn a Mermaid flowchart into archify diagrams, one per phase.

    python3 flow-from-mermaid.py work/user-flow.md --out work/user-flow --title "My product"

Layouts: `--layout scroll` (default) draws each phase as one horizontal row with a sideways scroll bar and only
drops a step to another row for a real branch. `--layout archify` writes checked archify diagrams instead
(long chains wrap into rows of 6).

Mermaid shapes it understands (the legend lists only those a diagram uses):
  [text] action or screen   {text} decision   ([text]) start or end   [[text]] sub-flow described elsewhere
  [(text)] data store   [/text/] input or output   ((text)) connector or jump   {{text}} preparation   >text] document

What it does
  - reads the first ```mermaid flowchart in the file (or a .mmd file)
  - every `subgraph` becomes its own diagram, so a long flow is never squeezed into one picture
  - adds one overview diagram of the phases when there is more than one
  - sizes nodes from their text, puts "· A4" style solution codes into a tag, wraps long chains
    into extra rows (6 columns per row), and shows links to other phases as small stub nodes
  - writes <slug>.json and runs `archify finalize` for each, so you get checked HTML files

Needs Python 3 and the archify skill (set ARCHIFY_BIN to its bin/archify.mjs if it lives elsewhere).
Without archify it still writes the .json files.
"""
import argparse
import json
import os
import re
import subprocess
import sys

COLS = 6
PILLAR_TYPES = ["frontend", "backend", "database", "cloud", "security"]

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



def slugify(s):
    s = re.sub(r"[^\w\s-]", "", s, flags=re.U).strip().lower()
    return re.sub(r"[\s_]+", "-", s) or "flow"


def strip_emoji(s):
    return re.sub(r"[^\w\s&/,.'’()+–—-]", "", s, flags=re.U).strip()


def short_phase(s):
    s = strip_emoji(s)
    return re.split(r"\s+[—–-]\s+", s)[0].strip() or s


# ---------------------------------------------------------------- parsing
ID_RE = re.compile(r"^\s*([A-Za-z_][\w]*)\s*(.*)$", re.S)
# Mermaid delimiter -> shape name
SHAPES = [
    (r'^\(\[\s*"?(.*?)"?\s*\]\)$', "terminator"),   # ([ ])  start or end
    (r'^\[\[\s*"?(.*?)"?\s*\]\]$', "subflow"),      # [[ ]]  defined elsewhere
    (r'^\[\(\s*"?(.*?)"?\s*\)\]$', "store"),        # [( )]  data store
    (r'^\(\(\s*"?(.*?)"?\s*\)\)$', "connector"),    # (( ))  jump or connector
    (r'^\{\{\s*"?(.*?)"?\s*\}\}$', "prep"),         # {{ }}  preparation or setup
    (r'^\[[/\\]\s*"?(.*?)"?\s*[/\\]\]$', "io"),   # [/ /]  input or output
    (r'^>\s*"?(.*?)"?\s*\]$', "doc"),                  # >  ]   document or report
    (r'^\{\s*"?(.*?)"?\s*\}$', "decision"),           # { }    decision
    (r'^\[\s*"?(.*?)"?\s*\]$', "step"),               # [ ]    action or screen
    (r'^\(\s*"?(.*?)"?\s*\)$', "step"),               # ( )    action or screen
]


class _NM(object):
    def __init__(self, nid, txt, kind):
        self.nid, self.txt, self.kind = nid, txt, kind


def match_node(item):
    m = ID_RE.match(item)
    if not m:
        return None
    nid, rest = m.group(1), m.group(2).strip()
    if not rest:
        return _NM(nid, None, "step")
    for pat, kind in SHAPES:
        mm = re.match(pat, rest, re.S)
        if mm:
            return _NM(nid, mm.group(1), kind)
    return _NM(nid, None, "step")


EDGE_SPLIT = re.compile(r"\s*(?:--\s*(?P<l1>[^->|]+?)\s*-->|-->\s*\|(?P<l2>[^|]+)\||-\.->|==>|-->)\s*")


class G(object):
    def __init__(self):
        self.nodes = {}          # id -> dict(text, kind, group)
        self.order = []
        self.edges = []          # (a, b, label)
        self.groups = []         # (id, title)


def parse(text):
    g = G()
    m = re.search(r"```mermaid\s*\n(.*?)```", text, re.S)
    body = m.group(1) if m else text
    stack = []
    for raw in body.split("\n"):
        line = raw.strip()
        if not line or line.startswith("%%") or re.match(r"(flowchart|graph)\b", line):
            continue
        sg = re.match(r'subgraph\s+(\w+)\s*(?:\[\s*"?(.*?)"?\s*\])?\s*$', line)
        if sg:
            gid, title = sg.group(1), sg.group(2) or sg.group(1)
            g.groups.append((gid, title))
            stack.append(gid)
            continue
        if line == "end":
            if stack:
                stack.pop()
            continue
        cur = stack[-1] if stack else None
        parts = EDGE_SPLIT.split(line)
        # re.split with named groups returns [text, l1, l2, text, ...]; rebuild sequentially
        items, labels = [], []
        pos = 0
        for mm in EDGE_SPLIT.finditer(line):
            items.append(line[pos:mm.start()])
            labels.append((mm.group("l1") or mm.group("l2") or "").strip())
            pos = mm.end()
        items.append(line[pos:])
        ids = []
        for it in items:
            it = it.strip()
            if not it:
                continue
            nm = match_node(it)
            if not nm:
                continue
            nid, txt, kind = nm.nid, nm.txt, nm.kind
            if nid not in g.nodes:
                g.nodes[nid] = {"text": txt if txt is not None else nid, "kind": kind, "group": cur}
                g.order.append(nid)
            elif txt is not None and g.nodes[nid]["text"] == nid:
                g.nodes[nid].update({"text": txt, "kind": kind})
                if cur and not g.nodes[nid]["group"]:
                    g.nodes[nid]["group"] = cur
            ids.append(nid)
        for i in range(len(ids) - 1):
            g.edges.append((ids[i], ids[i + 1], labels[i] if i < len(labels) else ""))
    return g


# ---------------------------------------------------------------- layout
def depths(nodes, edges):
    """longest-path depth, ignoring back edges so loops do not blow up"""
    out = {n: [] for n in nodes}
    for a, b, _ in edges:
        if a in out and b in out:
            out[a].append(b)
    state, back = {}, set()

    def dfs(n):
        state[n] = 1
        for m in out[n]:
            if state.get(m) == 1:
                back.add((n, m))
            elif m not in state:
                dfs(m)
        state[n] = 2
    incoming = {b for a, b, _ in edges if a in out and b in out}
    roots = [n for n in nodes if n not in incoming] or nodes[:1]
    for r in roots + nodes:
        if r not in state:
            dfs(r)
    d = {n: 0 for n in nodes}
    changed = True
    guard = 0
    while changed and guard < len(nodes) + 5:
        changed, guard = False, guard + 1
        for a, b, _ in edges:
            if a in d and b in d and (a, b) not in back and d[b] < d[a] + 1:
                d[b] = d[a] + 1
                changed = True
    return d, back


def split_text(text):
    """label, sublabel, tag from 'Free access granted · A1'"""
    tag = ""
    m = re.match(r"^(.*?)\s*[·|]\s*([A-Z]\d+(?:[–-][A-Z]?\d+)?(?:\s*,\s*[A-Z]\d+)*)\s*$", text)
    if m:
        text, tag = m.group(1).strip(), m.group(2).strip()
    sub = ""
    if len(text) > 24 and " " in text:
        words = text.split(" ")
        best, cut = 10 ** 9, 1
        for i in range(1, len(words)):
            a, b = len(" ".join(words[:i])), len(" ".join(words[i:]))
            if abs(a - b) < best:
                best, cut = abs(a - b), i
        text, sub = " ".join(words[:cut]), " ".join(words[cut:])
    return text, sub, tag


def node_width(label, sub, tag):
    n = max(len(label), len(sub))
    return int(min(176, max(124, n * 7.4 + 34)))


def phase_graph(g, gid):
    """members, nodes (with stubs), edges (merged), meta for one subgraph"""
    members = [n for n in g.order if g.nodes[n]["group"] == gid]
    mset = set(members)
    internal = [(a, b, l) for a, b, l in g.edges if a in mset and b in mset]
    nodes = list(members)
    stubs, extra_edges = {}, []
    outs, ins = [], []
    for a, b, l in g.edges:
        if a in mset and b not in mset and b in g.nodes:
            outs.append((a, short_phase(dict(g.groups).get(g.nodes[b]["group"], "next")), l))
        elif b in mset and a not in mset and a in g.nodes:
            ins.append((b, short_phase(dict(g.groups).get(g.nodes[a]["group"], "previous")), l))
    if outs:  # one stub for everything that leaves this phase
        names = sorted({t for _, t, _ in outs}, key=[t for _, t, _ in outs].index)
        stubs["to_next"] = {"text": "Continues: " + " / ".join(names), "kind": "link", "group": gid}
        nodes.append("to_next")
        for a, _t, l in outs:
            extra_edges.append((a, "to_next", l))
    if ins:   # one stub for everything that enters it
        names = sorted({t for _, t, _ in ins}, key=[t for _, t, _ in ins].index)
        stubs["from_prev"] = {"text": "From: " + " / ".join(names), "kind": "link", "group": gid}
        nodes.insert(0, "from_prev")
        for b, _t, l in ins:
            extra_edges.append(("from_prev", b, l))
    edges = internal + extra_edges
    meta = dict(g.nodes)
    meta.update(stubs)
    return members, nodes, edges, meta


def build_phase(g, gid, title, args, pillar_map, decision_codes=None, seen_codes=None):
    decision_codes = decision_codes or {}
    members, nodes, edges, meta = phase_graph(g, gid)
    d, back = depths(nodes, edges)

    seg_slots = {}
    place = {}
    for n in nodes:
        seg = d[n] // COLS
        slot = seg_slots.setdefault((seg, d[n]), [])
        k = len(slot)
        slot.append(n)
        col = d[n] % COLS
        place[n] = (seg, k, col)
    max_slot = {}
    for n, (seg, k, col) in place.items():
        max_slot[seg] = max(max_slot.get(seg, 0), k + 1)
    lanes, lane_of = [], {}
    nseg = max(max_slot) + 1 if max_slot else 1
    for seg in range(nseg):
        for k in range(max_slot.get(seg, 1)):
            lid = "r%d_%d" % (seg, k)
            if k == 0:
                label = title if nseg == 1 else "%s (%d/%d)" % (title, seg + 1, nseg)
            else:
                label = "Alternative" if nseg == 1 else "Alternative (%d/%d)" % (seg + 1, nseg)
            lanes.append({"id": lid, "label": label})
            lane_of[(seg, k)] = lid

    jn = []
    for n in nodes:
        seg, k, col = place[n]
        info = meta[n]
        label, sub, tag = split_text(strip_emoji(info["text"]) if n in ("to_next", "from_prev") else info["text"])
        t = "frontend"
        icon = None
        if info["kind"] == "decision":
            t, icon = "messagebus", "flag"
        elif info["kind"] in ("start", "link", "terminator"):
            t = "external"
            icon = "person" if n in members and d[n] == 0 else None
        elif tag:
            t = pillar_map.get(re.match(r"[A-Z]", tag).group(0), "frontend")
        codes_ = expand_codes(tag) if tag else []
        ds_ = []
        for c_ in codes_:
            for dd_ in decision_codes.get(c_, []):
                if dd_ not in ds_:
                    ds_.append(dd_)
        if ds_:  # show the decision on the node itself, not only in its detail panel
            sub = (sub + " " if sub else "") + "→ " + ",".join(ds_)
        node = {"id": n, "lane": lane_of[(seg, k)], "col": col, "type": t, "label": label,
                "width": node_width(label, sub, tag)}
        if sub:
            node["sublabel"] = sub
        if tag:
            codes = expand_codes(tag)
            if seen_codes is not None:
                seen_codes.update(codes)
            ds = []
            for c in codes:
                for dd in decision_codes.get(c, []):
                    if dd not in ds:
                        ds.append(dd)
            node["tag"] = ("SP-" + tag + " → " + ",".join(ds)) if ds else tag  # SP- keeps solution codes apart from decision IDs
            node["width"] = max(node["width"], int(len(node["tag"]) * 6.4 + 40))
        if icon:
            node["icon"] = icon
        jn.append(node)

    je = []
    merged = {}
    for a, b, l in edges:  # two edges between the same pair become one, with their labels joined
        if a in place and b in place:
            merged.setdefault((a, b), [])
            if l and l not in merged[(a, b)]:
                merged[(a, b)].append(l)
    edges = [(a, b, " / ".join(ls)) for (a, b), ls in merged.items()]
    for i, (a, b, l) in enumerate(edges):
        e = {"id": "e%d" % i, "from": a, "to": b, "variant": "default"}
        if l:
            e["label"] = l
        if (a, b) in back:
            e["variant"], e["role"] = "dashed", "return"
        elif place[a][0] != place[b][0]:  # wraps to the next row: columns restart, so it is drawn as a return
            e["role"] = "return"
        je.append(e)

    main = longest_path(nodes, [(a, b) for a, b, _ in edges if (a, b) not in back and place[a][0] == place[b][0] and place[b][2] > place[a][2]])
    if len(main) < 2:
        main = [nodes[0], nodes[-1]] if len(nodes) > 1 else nodes
    return jn, je, lanes, main


def longest_path(nodes, edges):
    out = {n: [] for n in nodes}
    for a, b in edges:
        out[a].append(b)
    best = {}

    def go(n, seen):
        if n in best:
            return best[n]
        r = [n]
        for m in out[n]:
            if m in seen:
                continue
            c = [n] + go(m, seen | {n})
            if len(c) > len(r):
                r = c
        best[n] = r
        return r
    incoming = {b for _, b in edges}
    roots = [n for n in nodes if n not in incoming] or nodes[:1]
    path = []
    for r in roots:
        p = go(r, set())
        if len(p) > len(path):
            path = p
    return path



TYPE_COLORS = {
    "frontend": "#00a76f", "backend": "#00b8d9", "database": "#1c252e", "cloud": "#ffab00",
    "security": "#ff5630", "messagebus": "#637381", "external": "#919eab",
}
NW, NH, GAPX, GAPY, MX, MY = 200, 88, 64, 56, 32, 70
DEC = 64          # half of a decision's side: it is a 128 x 128 square turned 45 degrees (ratio 1:1)
CON = 30          # radius of a connector circle

SHAPE_NAMES = [
    ("step", "Action or screen"), ("decision", "Decision"), ("terminator", "Start or end"),
    ("link", "Link to another phase"), ("subflow", "Sub-flow, described elsewhere"), ("store", "Data store"),
    ("io", "Input or output"), ("connector", "Connector, jump"), ("prep", "Preparation or setup"),
    ("doc", "Document or report"),
]


def _esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;"))


def _rounded(points, r=9):
    """orthogonal polyline with rounded corners"""
    if len(points) < 3:
        return "M" + " L".join("%.1f %.1f" % p for p in points)
    out = ["M%.1f %.1f" % points[0]]
    for i in range(1, len(points) - 1):
        (x0, y0), (x1, y1), (x2, y2) = points[i - 1], points[i], points[i + 1]
        l1 = abs(x1 - x0) + abs(y1 - y0)
        l2 = abs(x2 - x1) + abs(y2 - y1)
        rr = min(r, l1 / 2.0, l2 / 2.0)
        if rr <= 0.5:
            out.append("L%.1f %.1f" % (x1, y1))
            continue
        ux, uy = ((x1 - x0) / l1, (y1 - y0) / l1) if l1 else (0, 0)
        vx, vy = ((x2 - x1) / l2, (y2 - y1) / l2) if l2 else (0, 0)
        out.append("L%.1f %.1f Q%.1f %.1f %.1f %.1f" % (x1 - ux * rr, y1 - uy * rr, x1, y1, x1 + vx * rr, y1 + vy * rr))
    out.append("L%.1f %.1f" % points[-1])
    return " ".join(out)


def _wrap(text, width_chars):
    words, lines, cur = text.split(), [], ""
    for w in words:
        if cur and len(cur) + 1 + len(w) > width_chars:
            lines.append(cur)
            cur = w
        else:
            cur = (cur + " " + w).strip()
    if cur:
        lines.append(cur)
    return lines[:3] or [""]


def _shape_svg(shape, x, y, cx, cy):
    """outline of a node of the given shape, inside the cell at x,y (NW x NH) centred on cx,cy"""
    if shape == "decision":
        return '<polygon class="card dec" points="%.1f,%.1f %.1f,%.1f %.1f,%.1f %.1f,%.1f"/>' % (
            cx, cy - DEC, cx + DEC, cy, cx, cy + DEC, cx - DEC, cy)
    if shape == "terminator":
        return '<rect class="card" x="%d" y="%d" width="%d" height="%d" rx="%d"/>' % (x, y + 12, NW, NH - 24, (NH - 24) // 2)
    if shape == "link":
        return '<rect class="card pill" x="%d" y="%d" width="%d" height="%d" rx="%d"/>' % (x, y + 14, NW, NH - 28, (NH - 28) // 2)
    if shape == "subflow":
        return ('<rect class="card" x="%d" y="%d" width="%d" height="%d" rx="6"/>'
                '<path class="inner" d="M%d %d v%d M%d %d v%d"/>') % (x, y, NW, NH, x + 14, y, NH, x + NW - 14, y, NH)
    if shape == "store":
        ry = 9
        return ('<path class="card" d="M%d %d a%d %d 0 0 1 %d 0 v%d a%d %d 0 0 1 -%d 0 z"/>'
                '<path class="inner" d="M%d %d a%d %d 0 0 0 %d 0"/>') % (
            x, y + ry, NW / 2, ry, NW, NH - 2 * ry, NW / 2, ry, NW, x, y + ry, NW / 2, ry, NW)
    if shape == "connector":
        return '<circle class="card" cx="%.1f" cy="%.1f" r="%d"/>' % (cx, cy, CON)
    if shape == "prep":
        k = 22
        return '<polygon class="card" points="%d,%.1f %d,%d %d,%d %d,%.1f %d,%d %d,%d"/>' % (
            x, cy, x + k, y, x + NW - k, y, x + NW, cy, x + NW - k, y + NH, x + k, y + NH)
    if shape == "io":
        k = 20
        return '<polygon class="card" points="%d,%d %d,%d %d,%d %d,%d"/>' % (x + k, y, x + NW, y, x + NW - k, y + NH, x, y + NH)
    if shape == "doc":
        return '<path class="card" d="M%d %d h%d v%d q-%d -12 -%d 0 t-%d 0 v-%d z"/>' % (
            x, y, NW, NH - 8, NW / 4, NW / 2, NW / 2, 0) if False else (
            '<path class="card" d="M%d %d H%d V%d C%d %d %d %d %d %d C%d %d %d %d %d %d Z"/>' % (
                x, y, x + NW, y + NH - 10, x + NW * 0.75, y + NH - 22, x + NW * 0.65, y + NH + 2, x + NW / 2, y + NH - 10,
                x + NW * 0.35, y + NH - 22, x + NW * 0.25, y + NH + 2, x, y + NH - 10))
    return '<rect class="card" x="%d" y="%d" width="%d" height="%d" rx="8"/>' % (x, y, NW, NH)


def scroll_html(title, nodes, edges, legend):
    """nodes: [{id,label,sub,note,type,shape}] in reading order; edges: [(a,b,label)]; legend: [(type,label)]"""
    ids = [n["id"] for n in nodes]
    by = {n["id"]: n for n in nodes}
    d, back = depths(ids, edges)
    main_path = longest_path(ids, [(a, b) for a, b, _ in edges if (a, b) not in back])
    main = set(main_path)
    cell, rows = {}, {}
    for n in ids:           # main path stays on row 0; everything else drops only when it must
        if n in main and (d[n], 0) not in cell:
            cell[(d[n], 0)] = n
            rows[n] = 0
    for n in ids:
        if n in rows:
            continue
        r = 0 if (d[n], 0) not in cell else 1
        while (d[n], r) in cell:
            r += 1
        cell[(d[n], r)] = n
        rows[n] = r
    maxd = max(d.values()) if d else 0
    maxr = max(rows.values()) if rows else 0
    pos = {n: (MX + d[n] * (NW + GAPX), MY + rows[n] * (NH + GAPY)) for n in ids}
    width = MX * 2 + (maxd + 1) * NW + maxd * GAPX
    base_bottom = MY + maxr * (NH + GAPY) + NH + (DEC - NH // 2 if any(by[n]["shape"] == "decision" and rows[n] == maxr for n in ids) else 0)
    n_back = sum(1 for e in edges if (e[0], e[1]) in back)
    height = base_bottom + 40 + n_back * 14 + 24

    def half(n):
        sh = by[n]["shape"]
        return DEC if sh == "decision" else CON if sh == "connector" else NW / 2

    def port_in(n):
        x, y = pos[n]
        return x + NW / 2 - half(n), y + NH // 2

    def port_out(n):
        x, y = pos[n]
        return x + NW / 2 + half(n), y + NH // 2

    paths, texts = [], []
    k_up, k_dn = 0, 0
    for a, b, lab in edges:
        if a not in pos or b not in pos:
            continue
        ax, ay = port_out(a)
        bx, by_ = port_in(b)
        is_back = (a, b) in back
        if is_back:
            k_dn += 1
            cy = base_bottom + 24 + k_dn * 14
            pts = [(ax, ay), (ax + 18, ay), (ax + 18, cy), (bx - 18, cy), (bx - 18, by_), (bx, by_)]
            lx, ly = (ax + bx) / 2, cy - 6
        elif d[b] - d[a] == 1 and rows[a] == rows[b]:
            pts = [(ax, ay), (bx, by_)]
            lx, ly = (ax + bx) / 2, ay - 8
        elif d[b] - d[a] == 1:
            mx = ax + (bx - ax) / 2
            pts = [(ax, ay), (mx, ay), (mx, by_), (bx, by_)]
            lx, ly = mx + 6, by_ - 8
        else:               # skips over columns: goes above the main row
            k_up += 1
            cy = MY - 34 - (k_up % 3) * 10
            pts = [(ax, ay), (ax + 18, ay), (ax + 18, cy), (bx - 18, cy), (bx - 18, by_), (bx, by_)]
            lx, ly = (ax + bx) / 2, cy - 6
        cls = "e" + (" back" if is_back else "") + (" main" if (a in main and b in main and not is_back) else "")
        paths.append('<path class="%s" data-a="%s" data-b="%s" d="%s" marker-end="url(#ah)"/>' % (cls, _esc(a), _esc(b), _rounded(pts)))
        if lab:
            anchor = "middle" if (is_back or d[b] - d[a] >= 1 and rows[a] == rows[b]) else "start"
            texts.append('<text class="el" x="%.0f" y="%.0f" text-anchor="%s">%s</text>' % (lx, ly, anchor, _esc(lab)))
    nodes_svg = []
    for n in nodes:
        x, y = pos[n["id"]]
        col = TYPE_COLORS.get(n["type"], TYPE_COLORS["frontend"])
        cx, cy = x + NW / 2, y + NH / 2
        sh = n["shape"]
        g = ['<g class="n" data-id="%s" style="--c:%s">' % (_esc(n["id"]), col)]
        if n.get("note"):
            g.append("<title>%s</title>" % _esc(n["note"]))
        g.append(_shape_svg(sh, x, y, cx, cy))
        label, sub = n["label"], n.get("sub", "")
        if sh == "decision":                # the question sits inside the square-turned diamond
            lines = _wrap(label + ((" " + sub) if sub else ""), 14)
            y0 = cy - (len(lines) - 1) * 8 + 5
            for i, ln in enumerate(lines):
                g.append('<text class="nl dl" x="%.0f" y="%.0f" text-anchor="middle">%s</text>' % (cx, y0 + i * 16, _esc(ln)))
        elif sh == "connector":
            g.append('<text class="ns" x="%.0f" y="%.0f" text-anchor="middle">%s</text>' % (cx, cy + CON + 18, _esc(label)))
        else:
            has_sub = bool(sub)
            ty = cy + (-2 if has_sub else 5)
            cls = "nl pl" if sh == "link" else "nl"
            g.append('<text class="%s" x="%.0f" y="%.0f" text-anchor="middle">%s</text>' % (cls, cx, ty, _esc(label)))
            if has_sub:
                g.append('<text class="ns" x="%.0f" y="%.0f" text-anchor="middle">%s</text>' % (cx, ty + 19, _esc(sub)))
        g.append("</g>")
        nodes_svg.append("".join(g))

    used_shapes = {n["shape"] for n in nodes}
    icons = {
        "step": '<rect x="1" y="1" width="20" height="12" rx="3" class="lg"/>',
        "decision": '<polygon points="8,1 15,8 8,15 1,8" class="lg"/>',
        "terminator": '<rect x="1" y="2" width="22" height="10" rx="5" class="lg"/>',
        "link": '<rect x="1" y="2" width="22" height="10" rx="5" class="lg dash"/>',
        "subflow": '<rect x="1" y="1" width="20" height="12" rx="2" class="lg"/><path d="M5 1 v12 M17 1 v12" class="lg"/>',
        "store": '<path d="M2 4 a9 3 0 0 1 18 0 v6 a9 3 0 0 1 -18 0 z M2 4 a9 3 0 0 0 18 0" class="lg"/>',
        "io": '<polygon points="5,1 21,1 17,13 1,13" class="lg"/>',
        "connector": '<circle cx="8" cy="8" r="6" class="lg"/>',
        "prep": '<polygon points="1,7 6,1 16,1 21,7 16,13 6,13" class="lg"/>',
        "doc": '<path d="M1 1 H21 V10 C16 6 12 14 1 10 Z" class="lg"/>',
    }
    shapes = []
    for key, name in SHAPE_NAMES:
        if key in used_shapes:
            w, h = (16, 16) if key in ("decision", "connector") else (24, 14)
            shapes.append('<span><svg width="%d" height="%d" viewBox="0 0 %d %d">%s</svg>%s</span>' % (w, h, w, h, icons[key], name))
    if n_back:
        shapes.append('<span><svg width="24" height="10" viewBox="0 0 24 10"><path d="M1 5 H20" class="lg dash"/><path d="M17 1 L23 5 L17 9" class="lg"/></svg>Returns to an earlier step</span>')
    colours = "".join('<span><i style="background:%s"></i>%s</span>' % (
        TYPE_COLORS.get(t, TYPE_COLORS["frontend"]), _esc(l)) for t, l in legend if t not in ("messagebus", "external"))
    leg = '<div class="lgroup"><b>Shapes</b>%s</div>' % "".join(shapes)
    if colours:
        leg += '<div class="lgroup"><b>Colour = solution group</b>%s</div>' % colours
    n_dec = sum(1 for n in nodes if n["shape"] == "decision")
    n_steps = sum(1 for n in nodes if n["shape"] not in ("link", "terminator", "connector"))
    summary = "%d steps" % n_steps + (" · %d decision%s" % (n_dec, "" if n_dec == 1 else "s") if n_dec else "")
    return """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>%(title)s</title>
<style>
:root{--bg:#fff;--panel:#fff;--ink:#1c252e;--muted:#637381;--line:#919eab;--card:#fff;--cardline:rgba(145,158,171,.32);--dots:rgba(145,158,171,.28)}
html,body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}
.wrap{max-width:100%%;margin:0;padding:18px 20px}
header{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;padding:0 4px 8px}
h1{margin:0;font-size:1.2rem;font-weight:800;letter-spacing:-.01em}
.sum{color:var(--muted);font-size:.85rem}
.leg{display:flex;flex-wrap:wrap;gap:8px 28px;align-items:center;margin:0 4px 12px;font-size:.78rem;color:var(--muted)}
.lgroup{display:flex;flex-wrap:wrap;align-items:center;gap:6px 16px}
.lgroup b{font-size:.68rem;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:var(--muted);opacity:.85;margin-right:2px}
.lgroup span{display:inline-flex;align-items:center;gap:6px;color:var(--ink)}
.leg i{display:inline-block;width:10px;height:10px;border-radius:50%%}
.lg{fill:none;stroke:var(--muted);stroke-width:1.4}.lg.dash{stroke-dasharray:3 3}
.panel{background:var(--panel);border:0;border-radius:16px;overflow:hidden;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12)}
.scroll{overflow-x:auto;overflow-y:hidden;background-image:radial-gradient(var(--dots) 1px,transparent 1px);background-size:18px 18px;scrollbar-width:thin}
svg{display:block}
.e{fill:none;stroke:var(--line);stroke-width:1.6}
.e.main{stroke:var(--muted);stroke-width:2}
.e.back{stroke-dasharray:6 5}
.e.hi{stroke:var(--ink);stroke-width:2.4}
.el{font-size:11px;fill:var(--muted);paint-order:stroke;stroke:var(--panel);stroke-width:4px;stroke-linejoin:round}
.card{fill:var(--card);stroke:var(--cardline);stroke-width:1.3}
.inner{fill:none;stroke:var(--cardline);stroke-width:1.3}
.card.dec{stroke:var(--c);stroke-width:1.5}
.card.pill{fill:none;stroke:var(--line);stroke-dasharray:3 4}
.nl{font-size:14px;font-weight:600;fill:var(--ink)}
.nl.dl{font-size:13px}
.nl.pl{font-weight:500;fill:var(--muted)}
.ns{font-size:12px;fill:var(--muted)}
.n:hover .card{stroke:var(--ink)}
.hint{padding:10px 6px 0;font-size:.78rem;color:var(--muted)}
</style></head><body><div class="wrap">
<header><h1>%(title)s</h1><span class="sum">%(summary)s</span></header>
<div class="leg">%(leg)s</div>
<div class="panel"><div class="scroll"><svg xmlns="http://www.w3.org/2000/svg" width="%(w)d" height="%(h)d" viewBox="0 0 %(w)d %(h)d" role="img" aria-label="%(title)s">
<defs><marker id="ah" viewBox="0 0 10 10" refX="8.5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 1 L9 5 L0 9 z" fill="#919eab"/></marker></defs>
%(paths)s
%(texts)s
%(nodes)s
</svg></div></div>
<p class="hint">Scroll sideways to follow the flow. Hover a step to light up its connections; the solution code and decision are in its tooltip.</p>
</div>
<script>
document.querySelectorAll('.n').forEach(function(g){var id=g.getAttribute('data-id');
g.addEventListener('mouseenter',function(){document.querySelectorAll('.e').forEach(function(e){if(e.getAttribute('data-a')===id||e.getAttribute('data-b')===id)e.classList.add('hi')})});
g.addEventListener('mouseleave',function(){document.querySelectorAll('.e.hi').forEach(function(e){e.classList.remove('hi')})});});
</script>
</body></html>
""" % {"title": _esc(title), "summary": _esc(summary), "leg": leg, "w": width, "h": height,
       "paths": "\n".join(paths), "texts": "\n".join(texts), "nodes": "\n".join(nodes_svg)}


def build_scroll(g, gid, title, pillar_map, names, decision_codes, seen_codes):
    members, nodes, edges, meta = phase_graph(g, gid)
    out_nodes = []
    for n in nodes:
        info = meta[n]
        text = strip_emoji(info["text"]) if n in ("to_next", "from_prev") else info["text"]
        label, sub, tag = split_text(text)
        kind = info["kind"]
        shape = {"link": "link", "start": "terminator", "terminator": "terminator", "decision": "decision", "subflow": "subflow",
                 "store": "store", "connector": "connector", "prep": "prep", "io": "io", "doc": "doc"}.get(kind, "step")
        t = "frontend"
        if shape == "decision":
            t = "messagebus"
        elif shape in ("link", "terminator"):
            t = "external"
        elif tag:
            t = pillar_map.get(re.match(r"[A-Z]", tag).group(0), "frontend")
        note = ""
        if tag:
            codes = expand_codes(tag)
            seen_codes.update(codes)
            ds = []
            for c in codes:
                for dd in decision_codes.get(c, []):
                    if dd not in ds:
                        ds.append(dd)
            note = "SP-" + tag + ((" → decision " + ", ".join(ds)) if ds else " (no decision yet)")
        out_nodes.append({"id": n, "label": label, "sub": sub, "note": note, "type": t, "shape": shape})
    merged = {}
    for a, b, l in edges:
        merged.setdefault((a, b), [])
        if l and l not in merged[(a, b)]:
            merged[(a, b)].append(l)
    out_edges = [(a, b, " / ".join(ls)) for (a, b), ls in merged.items()]
    used = {n["type"] for n in out_nodes if n["shape"] == "step"}
    legend = []
    for letter, t in pillar_map.items():
        if t in used:
            legend.append((t, names.get(letter, "Solutions %s" % letter)))
    return scroll_html(title, out_nodes, out_edges, legend)


def legend_for(nodes, names, pillar_map):
    entries = {"messagebus": {"label": "Decision"}, "external": {"label": "Start or link to another phase"}}
    used = {n["type"] for n in nodes}
    for letter, t in pillar_map.items():
        if t in used:
            entries[t] = {"label": names.get(letter, "Solutions %s" % letter)}
    if "frontend" in used and "frontend" not in entries:
        entries["frontend"] = {"label": "Step"}
    return {"entries": {k: v for k, v in entries.items() if k in used}}


def diagram(title, jn, je, lanes, main, legend, out_name):
    return {
        "schema_version": 2,
        "diagram_type": "workflow",
        "meta": {"title": title, "locale": "en", "quality_profile": "showcase", "legend": legend, "output": out_name},
        "lanes": lanes,
        "mainPath": main,
        "nodes": jn,
        "edges": je,
    }


def load_decision_codes(case_dir):
    """solution code -> [decision IDs], from the `solutions` property of insights/decisions/*.md"""
    out = {}
    d = os.path.join(case_dir, "insights", "decisions")
    if not os.path.isdir(d):
        return out
    for fn in sorted(os.listdir(d)):
        m = re.match(r"([A-Z]\d+)\.md$", fn)
        if not m:
            continue
        txt = open(os.path.join(d, fn), encoding="utf-8").read()
        fm = re.match(r"^---\n(.*?)\n---", txt, re.S)
        if not fm:
            continue
        sm = re.search(r"^solutions:\s*\[(.*?)\]\s*$", fm.group(1), re.M)
        if not sm:
            continue
        for code in re.findall(r"[A-Z]\d+", sm.group(1)):
            out.setdefault(code, []).append(m.group(1))
    return out


def expand_codes(tag):
    """'D1–D5' -> D1..D5; 'A4' -> A4; 'C1, C2' -> C1, C2"""
    codes = []
    for part in re.split(r"\s*,\s*", tag):
        r = re.match(r"^([A-Z])(\d+)\s*[–-]\s*[A-Z]?(\d+)$", part)
        if r:
            codes += ["%s%d" % (r.group(1), i) for i in range(int(r.group(2)), int(r.group(3)) + 1)]
        elif re.match(r"^[A-Z]\d+$", part):
            codes.append(part)
    return codes


def find_archify():
    for p in (os.environ.get("ARCHIFY_BIN"), os.path.expanduser("~/.claude/skills/archify/bin/archify.mjs")):
        if p and os.path.isfile(p):
            return p
    return None


def finalize(bin_path, json_path, html_path, cwd):
    r = subprocess.run(["node", bin_path, "finalize", "workflow", os.path.basename(json_path), os.path.basename(html_path),
                        "--quality", "showcase", "--json"], cwd=cwd, capture_output=True, text=True)
    try:
        d = json.loads(r.stdout)
    except Exception:
        return False, [r.stderr.strip()[-300:] or "archify did not return JSON"]
    msgs = [x.get("message", "") for x in d.get("diagnostics", [])]
    # keep the folder tidy: the receipts are not needed in a project
    base = os.path.splitext(os.path.basename(html_path))[0]
    for suf in (".finalize.json", ".finalize-summary.json", ".delivery.json", ".delivery-pending.json", ".browser-check.json"):
        p = os.path.join(cwd, base + suf)
        if os.path.exists(p):
            os.remove(p)
    return d.get("status") == "pass", msgs


# What the generated pages looked like before they followed the Minimal design system.
_RESTYLE = [
    ('@media (prefers-color-scheme:dark){:root{--bg:#0f1419;--panel:#161d25;--ink:#f1f3f5;--muted:#a7b0ba;--line:#5d6875;--card:#1d262f;--cardline:#34404c;--dots:#26303b}}\n', ""),
    (':root{--bg:#f6f7f9;--panel:#fff;--ink:#1c252e;--muted:#637381;--line:#b8c0ca;--card:#fff;--cardline:#d9dee5;--dots:#d8dde4}', ':root{--bg:#fff;--panel:#fff;--ink:#1c252e;--muted:#637381;--line:#919eab;--card:#fff;--cardline:rgba(145,158,171,.32);--dots:rgba(145,158,171,.28)}'),
    ('html,body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,sans-serif}', 'html,body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.5 "Public Sans",-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif}'),
    ('h1{margin:0;font-size:1.2rem;letter-spacing:-.01em}', 'h1{margin:0;font-size:1.2rem;font-weight:800;letter-spacing:-.01em}'),
    ('.panel{background:var(--panel);border:1px solid var(--cardline);border-radius:14px;overflow:hidden}', '.panel{background:var(--panel);border:0;border-radius:16px;overflow:hidden;box-shadow:0 0 2px 0 rgba(145,158,171,.2),0 12px 24px -4px rgba(145,158,171,.12)}'),
    ('fill="#8a96a3"', 'fill="#919eab"'),
]
_RESTYLE_COLORS = {"#3b7bd4": "#00a76f", "#2f9e5f": "#00b8d9", "#7b57d1": "#1c252e", "#d9822b": "#ffab00",
                   "#d0455a": "#ff5630", "#c9971a": "#637381", "#7b8494": "#919eab"}


def restyle(paths):
    """Rewrite generated diagram pages in place (.html files, or folders of them). Safe to run twice."""
    import glob
    files = []
    for p in paths:
        files += sorted(glob.glob(os.path.join(p, "*.html"))) if os.path.isdir(p) else [p]
    changed = 0
    for f in files:
        t = open(f, encoding="utf-8").read()
        if "flow-from-mermaid" not in t and 'class="panel"' not in t:
            continue
        o = t
        for a, b in _RESTYLE:
            t = t.replace(a, b)
        t = re.sub(r"#[0-9a-fA-F]{6}\b", lambda m: _RESTYLE_COLORS.get(m.group(0).lower(), m.group(0)), t)
        if t != o:
            open(f, "w", encoding="utf-8").write(t)
            changed += 1
            print("restyled", f)
    print("%d file(s) restyled, %d already up to date" % (changed, len(files) - changed))



def main():
    ap = argparse.ArgumentParser(description="Mermaid flowchart -> one archify diagram per phase")
    ap.add_argument("source", nargs="?", help="markdown file with a ```mermaid block, or a .mmd file")
    ap.add_argument("--out", help="folder for the .json and .html files")
    ap.add_argument("--restyle", nargs="+", metavar="PATH", help="bring already generated diagram pages (files or folders) "
                    "to the current look; no Mermaid source needed")
    ap.add_argument("--title", default="", help="product name used in diagram titles")
    ap.add_argument("--legend", default="", help='names for solution-code letters, e.g. "A=Onboarding,D=Discover,P=Plan"')
    ap.add_argument("--case", default="", help="case folder holding insights/decisions (default: the case you are standing in)")
    ap.add_argument("--layout", choices=["scroll", "archify"], default="scroll",
                    help="scroll: one horizontal row per phase with a sideways scroll bar (default); "
                         "archify: checked archify diagrams, long chains wrap into rows of 6")
    ap.add_argument("--no-overview", action="store_true", help="skip the phase overview diagram")
    ap.add_argument("--no-run", action="store_true", help="write the .json files only")
    a = ap.parse_args()
    if a.restyle:
        restyle(a.restyle)
        return
    if not a.source or not a.out:
        ap.error("source and --out are required (or use --restyle PATH)")

    text = open(a.source, encoding="utf-8").read()
    g = parse(text)
    if not g.nodes:
        sys.exit("No Mermaid flowchart found in %s" % a.source)
    os.makedirs(a.out, exist_ok=True)
    names = dict(kv.split("=", 1) for kv in a.legend.split(",") if "=" in kv)

    letters = []
    for n in g.order:
        m = re.search(r"[·|]\s*([A-Z])\d", g.nodes[n]["text"])
        if m and m.group(1) not in letters:
            letters.append(m.group(1))
    pillar_map = {l: PILLAR_TYPES[i % len(PILLAR_TYPES)] for i, l in enumerate(letters)}

    groups = g.groups or [("flow", a.title or "Flow")]
    if not g.groups:
        for n in g.nodes.values():
            n["group"] = "flow"
    prefix = (a.title + ": ") if a.title else ""
    if a.layout == "scroll":
        case_dir = a.case or find_case() or os.getcwd()
        decision_codes = load_decision_codes(case_dir)
        seen_codes = set()
        written = []
        if len(groups) > 1 and not a.no_overview:
            ov_nodes = [{"id": gid, "label": short_phase(t), "sub": "", "note": "", "type": "frontend", "shape": "step"} for gid, t in groups]
            merged = {}
            for x, y, l in g.edges:
                gx, gy = g.nodes[x]["group"], g.nodes[y]["group"]
                if gx and gy and gx != gy:
                    merged.setdefault((gx, gy), [])
                    if l and l not in merged[(gx, gy)]:
                        merged[(gx, gy)].append(l)
            html = scroll_html(prefix + "journey overview", ov_nodes, [(x, y, " / ".join(ls)) for (x, y), ls in merged.items()],
                               [])
            open(os.path.join(a.out, "overview.html"), "w", encoding="utf-8").write(html)
            written.append("overview")
        for gid, title in groups:
            html = build_scroll(g, gid, prefix + short_phase(title), pillar_map, names, decision_codes, seen_codes)
            slug = slugify(short_phase(title))
            open(os.path.join(a.out, slug + ".html"), "w", encoding="utf-8").write(html)
            written.append(slug)
        for slug in written:
            print("%-22s ok" % slug)
        if decision_codes or seen_codes:
            print("solution codes with no decision: %s" % (", ".join(sorted(c for c in seen_codes if c not in decision_codes)) or "none"))
        return
    jobs = []
    if len(groups) > 1 and not a.no_overview:
        ov_nodes = [{"id": gid, "lane": "phases", "col": i % COLS, "type": "frontend", "label": short_phase(t),
                     "width": 150} for i, (gid, t) in enumerate(groups)]
        idx = {gid: i for i, (gid, _) in enumerate(groups)}
        ov_edges, seen = [], set()
        for x, y, l in g.edges:
            gx, gy = g.nodes[x]["group"], g.nodes[y]["group"]
            if gx and gy and gx != gy and (gx, gy) not in seen:
                seen.add((gx, gy))
                e = {"id": "o%d" % len(ov_edges), "from": gx, "to": gy, "variant": "default"}
                if l:
                    e["label"] = l
                if idx[gy] < idx[gx]:
                    e["variant"], e["role"] = "dashed", "return"
                ov_edges.append(e)
        diag = diagram(prefix + "journey overview", ov_nodes, ov_edges, [{"id": "phases", "label": "Phases"}],
                       [gid for gid, _ in groups], {"entries": {"frontend": {"label": "Phase"}}}, "overview.html")
        jobs.append(("overview", diag))
    case_dir = a.case or find_case() or os.getcwd()
    decision_codes = load_decision_codes(case_dir)
    seen_codes = set()
    for gid, title in groups:
        jn, je, lanes, main_path = build_phase(g, gid, short_phase(title), a, pillar_map, decision_codes, seen_codes)
        diag = diagram(prefix + short_phase(title), jn, je, lanes, main_path, legend_for(jn, names, pillar_map), "%s.html" % slugify(short_phase(title)))
        jobs.append((slugify(short_phase(title)), diag))

    bin_path = None if a.no_run else find_archify()
    if not a.no_run and not bin_path:
        print("archify not found (set ARCHIFY_BIN); writing .json only")
    ok_all = True
    for slug, diag in jobs:
        jp = os.path.join(a.out, slug + ".json")
        diag["meta"]["output"] = slug + ".html"
        with open(jp, "w", encoding="utf-8") as f:
            json.dump(diag, f, indent=2, ensure_ascii=False)
            f.write("\n")
        if bin_path:
            ok, msgs = finalize(bin_path, jp, os.path.join(a.out, slug + ".html"), os.path.abspath(a.out))
            ok_all = ok_all and ok
            print("%-22s %s" % (slug, "ok" if ok else "FAILED: " + "; ".join(msgs)[:300]))
        else:
            print("%-22s json written" % slug)
    if decision_codes or seen_codes:
        no_decision = sorted(c for c in seen_codes if c not in decision_codes)
        print("solution codes with no decision: %s" % (", ".join(no_decision) or "none"))
    sys.exit(0 if ok_all else 1)


if __name__ == "__main__":
    main()
