#!/usr/bin/env python3
"""
new-item.py - add an item (O, H, M, D, E, F) to insights/ and fill its relations.

Run it with no arguments and it asks one question at a time:

    python3 new-item.py

An AI tool (or you) can pass everything at once:

    python3 new-item.py D --title "Show the crowd signal instead of the badge" --tests H2 --follows P1 --pulls-against P8
    python3 new-item.py E --title "Task test with 5 people" --tests H1 --measures M1 --participants 5
    python3 new-item.py D --title "..." --tests H1 --state accepted --owner "Lan (PM)"
    python3 new-item.py O --title "..." --impact high --confidence medium --rank-reason "..."
    python3 new-item.py M --title "..." --target ">= 80% complete without help"
    python3 new-item.py F --title "..." --severity 3 --found-in E1 --affects D2 --principle P8

It picks the next free ID, writes the file in the right folder, checks that every ID you
point at exists, tells you what is still missing, and rebuilds index.html (--no-build to skip).
It never overwrites a file. Needs only Python 3.
"""
import argparse
import datetime
import importlib.util
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

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

CASE = None  # set in main() from --case or the current folder

KINDS = {
    "O": ("opportunity", "opportunities", "Opportunity: a user need backed by evidence"),
    "H": ("hypothesis", "hypotheses", "Hypothesis: something you believe and will test"),
    "M": ("metric", "metrics", "Metric: how you will know the hypothesis is right or wrong"),
    "D": ("decision", "decisions", "Decision: a design decision"),
    "E": ("evidence", "evidence", "Evidence: a test or a study"),
    "F": ("finding", "findings", "Finding: a usability problem found"),
}

# (field, targets, many, question)
RELATIONS = {
    "O": [],
    "H": [("serves", "O", True, "Which opportunity does this hypothesis serve?"),
          ("metric", "M", True, "Which metric measures it?")],
    "M": [],
    "D": [("tests", "H", True, "Which hypothesis does this decision test?"),
          ("follows", "P", True, "Which principle does it follow?"),
          ("pulls_against", "P", True, "Which principle does it pull against? (leave empty if none)")],
    "E": [("tests", "H", True, "Which hypothesis does this evidence test?"),
          ("measures", "M", True, "Which metric does it measure?")],
    "F": [("found_in", "E", True, "Found in which evidence?"),
          ("affects", "D", True, "Which decision does it affect? (leave empty if none)"),
          ("principle", "P", True, "Which principle does it violate? (leave empty if unknown)")],
}
FLAG = {"serves": "serves", "metric": "metric", "tests": "tests", "follows": "follows", "pulls_against": "pulls-against",
        "measures": "measures", "found_in": "found-in", "affects": "affects", "principle": "principle"}


def load_hub():
    spec = importlib.util.spec_from_file_location("export_hub", os.path.join(HERE, "export-hub.py"))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ask(prompt, default=""):
    try:
        v = input("%s%s: " % (prompt, (" [%s]" % default) if default else "")).strip()
    except EOFError:
        sys.exit("\nNo input. Pass all the arguments (see --help) when running non-interactively.")
    return v or default


def ids_of(text):
    return [t for t in re.split(r"[,\s]+", text.upper()) if t]


def pick(prompt, options, many=True):
    """options: list of (id, label). Accepts numbers or IDs, comma separated. Enter skips."""
    if not options:
        print("  (%s) nothing to choose from yet: skipped, the report will remind you to link it later." % prompt.rstrip("?").rstrip())
        return []
    print("\n%s" % prompt)
    for n, (i, lab) in enumerate(options, 1):
        print("  %d) %s  %s" % (n, i, lab[:90]))
    while True:
        raw = ask("  Choose (number or code, comma separated; Enter to skip)")
        if not raw:
            return []
        chosen, bad = [], []
        for tok in ids_of(raw):
            if tok.isdigit() and 1 <= int(tok) <= len(options):
                chosen.append(options[int(tok) - 1][0])
            elif tok in [o[0] for o in options]:
                chosen.append(tok)
            else:
                bad.append(tok)
        if bad:
            print("  Not found: %s. Try again." % ", ".join(bad))
            continue
        return list(dict.fromkeys(chosen))


def next_id(letter, existing):
    nums = [int(re.sub(r"\D", "", i)) for i in existing if i.startswith(letter) and re.sub(r"\D", "", i)]
    return "%s%d" % (letter, (max(nums) + 1) if nums else 1)


def yaml_str(v):
    return '"%s"' % str(v).replace("\\", "\\\\").replace('"', '\\"')


def yaml_list(key, ids, principle_ids):
    if not ids:
        return ["%s: []" % key]
    out = ["%s:" % key]
    for i in ids:
        out.append('  - "[[%s]]"' % (("principle-checks|%s" % i) if i in principle_ids else i))
    return out


def template_body(folder_kind):
    """The body of the matching template, without its 'How to use' line."""
    t = os.path.join(CASE, "insights", "_templates", "_template-%s.md" % folder_kind)
    if not os.path.isfile(t):
        return ""
    raw = open(t, encoding="utf-8").read()
    m = re.match(r"^---\n.*?\n---\n?", raw, re.S)
    body = raw[m.end():] if m else raw
    body = re.sub(r"^\*(?:Cách dùng|How to use)[^\n]*\n\n?", "", body, flags=re.M)
    return body.lstrip("\n")


def main():
    ap = argparse.ArgumentParser(description="Add an item to insights/ and link it to the items it relates to.")
    ap.add_argument("kind", nargs="?", help="O, H, M, D, E or F (leave empty to be asked)")
    ap.add_argument("--title", help="one sentence describing the item")
    ap.add_argument("--area", default="", help="topic (optional), for example: onboarding")
    for field, flag in FLAG.items():
        ap.add_argument("--" + flag, help="codes separated by commas, for example H1,H2")
    ap.add_argument("--severity", type=int, choices=range(0, 5), help="finding: 0 to 4")
    ap.add_argument("--resolution", default="open", help="finding: open, fixed, accepted, deferred")
    ap.add_argument("--rank", type=int, help="opportunity: rank (default: end of the list)")
    ap.add_argument("--evidence-note", dest="evidence_note", help="opportunity: source or quote ID")
    ap.add_argument("--participants", type=int, default=0, help="evidence: number of participants")
    ap.add_argument("--status", help="evidence: planned or run; metric: assumed or confirmed")
    ap.add_argument("--baseline", help="metric: current baseline (or unknown)")
    ap.add_argument("--reason", help="decision: one-sentence reason, also written to the case log")
    ap.add_argument("--solutions", help="decision: solution codes it implements, for example A4,P3 (flow diagrams use them to tag the decision)")
    ap.add_argument("--owner", help="decision: who is responsible")
    ap.add_argument("--decided-on", dest="decided_on", help="decision: date YYYY-MM-DD (default: today when state is accepted)")
    ap.add_argument("--state", choices=["proposed", "accepted", "shipped", "superseded", "dropped"], help="decision: default proposed")
    ap.add_argument("--impact", choices=["high", "medium", "low"], help="opportunity: impact")
    ap.add_argument("--confidence", choices=["high", "medium", "low"], help="opportunity: confidence in the evidence")
    ap.add_argument("--rank-reason", dest="rank_reason", help="opportunity: why it has this rank")
    ap.add_argument("--target", help="metric: what counts as met")
    ap.add_argument("--result", help="metric: the measured result")
    ap.add_argument("--verdict", choices=["pending", "met", "missed", "inconclusive"], help="metric: verdict against the target")
    ap.add_argument("--measured-on", dest="measured_on", help="metric: date measured YYYY-MM-DD")
    ap.add_argument("--no-log", action="store_true", help="decision: do not add a line to the case log")
    ap.add_argument("--no-build", action="store_true", help="do not rebuild index.html")
    ap.add_argument("--case", default="", help="case folder (default: the case you are standing in)")
    a = ap.parse_args()
    global CASE
    CASE = os.path.abspath(a.case) if a.case else find_case()
    if not CASE:
        sys.exit("Case folder not found. Run inside a case (a folder with AGENTS.md and insights/), or pass --case <path>.")
    interactive = a.kind is None

    hub = load_hub()
    _ov, _wk, items, _ref, _ctx = hub.collect(CASE)
    by_id = {p.id: p for p in items}
    pr_path = os.path.join(CASE, "standards", "principle-checks.md")
    if not os.path.isfile(pr_path):
        pr_path = os.path.join(CASE, "reference", "principle-checks.md")
    principles = hub.parse_principles(open(pr_path, encoding="utf-8").read()) if os.path.isfile(pr_path) else {}

    # 1. kind
    kind = (a.kind or "").upper()
    if not kind:
        print("New item. Choose a type:")
        for k, (_n, _f, lab) in KINDS.items():
            print("  %s) %s" % (k, lab))
        kind = ask("Type (O/H/M/D/E/F)").upper()
    if kind not in KINDS:
        sys.exit("Type must be one of: %s" % ", ".join(KINDS))
    type_name, folder, _lab = KINDS[kind]

    # 2. title
    title = a.title or ask("\nOne sentence describing this %s" % type_name)
    if not title:
        sys.exit("A title is required.")

    # 3. relations
    def options_for(target):
        if target == "P":
            return [(pid, nm) for pid, (nm, _chk) in principles.items()]
        return [(i, p.title) for i, p in sorted(by_id.items(), key=lambda kv: hub._natkey(kv[0])) if p.letter == target]

    rel = {}
    for field, target, many, question in RELATIONS[kind]:
        opts = options_for(target)
        valid = {o[0] for o in opts}
        given = getattr(a, field, None)
        if given is not None:
            ids = ids_of(given)
            bad = [i for i in ids if i not in valid]
            if bad:
                sys.exit("%s: no such code %s (available: %s)" % (FLAG[field], ", ".join(bad), ", ".join(sorted(valid)) or "nothing"))
        elif interactive:
            ids = pick(question, opts, many)
        else:
            ids = []
        rel[field] = ids

    # 4. extra fields
    extra = []
    if kind == "O":
        existing_ranks = [p.rank for p in items if p.letter == "O" and p.rank != 999]
        default_rank = max(existing_ranks or [0]) + 1
        rank = a.rank or (int(ask("\nRank (1 is the most important)", str(default_rank))) if interactive else default_rank)
        note = a.evidence_note if a.evidence_note is not None else (ask("Source or quote ID of the evidence", "none yet") if interactive else "none yet")
        impact = a.impact or (ask("Impact on users (high/medium/low)", "medium") if interactive else "")
        conf = a.confidence or (ask("Confidence in the evidence (high/medium/low)", "medium") if interactive else "")
        why = a.rank_reason if a.rank_reason is not None else (ask("Why it has this rank (one or two sentences)") if interactive else "")
        for v_, n_ in ((impact, "impact"), (conf, "confidence")):
            if v_ and v_ not in ("high", "medium", "low"):
                sys.exit("%s must be high, medium or low" % n_)
        extra = ["rank: %d" % rank] + (["impact: %s" % yaml_str(impact)] if impact else []) + (["confidence: %s" % yaml_str(conf)] if conf else []) \
            + ["rank_reason: %s" % yaml_str(why), "evidence: %s" % yaml_str(note)]
    elif kind == "M":
        base = a.baseline if a.baseline is not None else (ask("\nCurrent baseline (or unknown)", "unknown") if interactive else "unknown")
        st = a.status or "assumed"
        tgt = a.target if a.target is not None else (ask("Target: what counts as met (for example >= 80% complete)") if interactive else "")
        extra = ["status: %s" % yaml_str(st), "baseline: %s" % yaml_str(base), 'measured_by: "usability test / analytics"',
                 "target: %s" % yaml_str(tgt), "result: %s" % yaml_str(a.result or ""), "measured_on: %s" % yaml_str(a.measured_on or ""),
                 "verdict: %s" % yaml_str(a.verdict or "pending")]
    elif kind == "E":
        st = a.status or (ask("\nStatus (planned = not run yet, run = done)", "planned") if interactive else "planned")
        n = a.participants or (int(ask("Number of participants", "0") or 0) if interactive else 0)
        extra = ["participants: %d" % n, 'result: ""', "status: %s" % yaml_str(st)]
    elif kind == "F":
        sev = a.severity if a.severity is not None else (int(ask("\nSeverity 0 to 4 (see standards/severity-levels.md)", "2")) if interactive else 2)
        extra = ["severity: %d" % sev, "resolution: %s" % yaml_str(a.resolution)]

    if kind == "D":
        st_ = a.state or (ask("\nState (proposed/accepted/shipped/superseded/dropped)", "proposed") if interactive else "proposed")
        owner = a.owner if a.owner is not None else (ask("Who is responsible (owner)") if interactive else "")
        when = a.decided_on if a.decided_on is not None else (datetime.date.today().isoformat() if st_ in ("accepted", "shipped") else "")
        extra = ["state: %s" % yaml_str(st_), "owner: %s" % yaml_str(owner), "decided_on: %s" % yaml_str(when)]
        if a.solutions:
            extra.append("solutions: [%s]" % ", ".join(yaml_str(c) for c in ids_of(a.solutions)))

    # 5. write the file
    new_id = next_id(kind, by_id)
    d = os.path.join(CASE, "insights", folder)
    os.makedirs(d, exist_ok=True)
    path = os.path.join(d, new_id + ".md")
    if os.path.exists(path):
        sys.exit("File already exists: %s (not overwritten)" % path)
    fm = ["---", "type: %s" % yaml_str(type_name), "title: %s" % yaml_str(title)]
    if a.area:
        fm.append("area: %s" % yaml_str(a.area))
    fm += extra
    for field, _t, _m, _q in RELATIONS[kind]:
        fm += yaml_list(field, rel.get(field, []), set(principles))
    fm.append("---")
    body = template_body(type_name) or "## Why\n\n"
    open(path, "w", encoding="utf-8").write("\n".join(fm) + "\n" + body)
    rel_path = os.path.relpath(path, CASE)
    print("\nCreated %s  (%s)" % (new_id, rel_path))

    # 6. case log for decisions
    if kind == "D" and not a.no_log:
        reason = a.reason if a.reason is not None else (ask("\nOne-sentence reason for the case log (Enter to skip)") if interactive else "")
        log = os.path.join(CASE, "insights", "case-log.md")
        if not os.path.isfile(log):
            log = os.path.join(CASE, "reference", "case-log.md")
        if reason and os.path.isfile(log):
            row = "| %s | %s | %s | %s |\n" % (datetime.date.today().isoformat(), title.replace("|", "/"), reason.replace("|", "/"),
                                              ", ".join([new_id] + rel.get("tests", [])))
            txt = open(log, encoding="utf-8").read().rstrip("\n") + "\n"
            lines = txt.split("\n")
            if len(lines) > 1 and re.fullmatch(r"\|(\s*\|)+", lines[-2].strip()):  # the empty placeholder row
                lines.pop(-2)
            open(log, "w", encoding="utf-8").write("\n".join(lines).rstrip("\n") + "\n" + row)
            print("Added a line to insights/case-log.md")
        elif not reason:
            print("  Still missing: no line in insights/case-log.md yet (add --reason \"...\" or write it by hand)")

    # 7. what is still missing
    missing = []
    if kind == "D" and not rel.get("tests"):
        missing.append("not linked to any hypothesis (tests): this decision will be flagged as having no user need")
    if kind == "H" and not rel.get("serves"):
        missing.append("not linked to any opportunity (serves)")
    if kind == "H" and not rel.get("metric"):
        missing.append("no metric yet")
    if kind == "E" and not rel.get("tests"):
        missing.append("not linked to any hypothesis (tests)")
    if kind == "F" and not rel.get("found_in"):
        missing.append("not linked to any evidence (found_in)")
    if kind == "D" and extra and 'state: "accepted"' in extra[0] and 'owner: ""' in extra[1]:
        missing.append("decision accepted but has no owner")
    if kind == "M" and 'target: ""' in "\n".join(extra):
        missing.append("metric has no target")
    if kind == "O" and 'rank_reason: ""' in "\n".join(extra):
        missing.append("opportunity has no rank reason (--rank-reason)")
    for m_ in missing:
        print("  Still missing: " + m_)
    print("Open %s to write the content." % rel_path)

    # 8. rebuild
    if not a.no_build:
        r = subprocess.run([sys.executable, os.path.join(HERE, "export-hub.py"), "--case", CASE], cwd=CASE, capture_output=True, text=True)
        print("index.html: %s" % ("rebuilt" if r.returncode == 0 else "error, rebuild the report with export-hub.py"))
        if r.returncode != 0:
            print(r.stderr.strip()[-400:])


if __name__ == "__main__":
    main()
