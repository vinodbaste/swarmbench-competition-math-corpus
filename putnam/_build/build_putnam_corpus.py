#!/usr/bin/env python3
"""Build a Putnam solve-and-crux corpus from the Kedlaya archive.

Public (pushed): putnam/statements/<id>.txt  + putnam/manifest_putnam_60.json
Hidden (local only, copied into task tests/): putnam/_gt/solutions/<id>.txt
                                              putnam/_gt/cohort.json

Ground truth for the verifier is the FULL official solution text (authoritative,
Kedlaya/Bhargava/Ng). The judge reads it to score the agent's final answer and
decisive idea. We do NOT pre-extract a canonical answer string (Putnam answers
are expressions), which keeps the GT robust.
"""
import json, os, re, urllib.request, pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent                      # putnam/
STMT = ROOT / "statements"
GT = ROOT / "_gt"
GT_SOL = GT / "solutions"
CACHE = HERE / "cache"
for d in (STMT, GT_SOL, CACHE):
    d.mkdir(parents=True, exist_ok=True)

RAW_BASE = "https://raw.githubusercontent.com/vinodbaste/swarmbench-competition-math-corpus/main/putnam/statements"
ARCHIVE = "https://kskedlaya.org/putnam-archive"

# Years chosen to yield >=60 answer-bearing problems, dedup-distant from the
# AIME year ranges used by the other tasks.
YEARS = list(range(2000, 2020))
LABELS = ["A1", "A2", "A3", "A4", "A5", "A6", "B1", "B2", "B3", "B4", "B5", "B6"]

# A problem is "answer-bearing" (has a definite value/expression to report)
# when its statement asks to produce one. Pure "prove/show" problems are skipped.
ANSWER_CUES = re.compile(
    r"\b(find|compute|evaluate|determine|express|calculate|how many|"
    r"what is|what are|the value of|the number of|the largest|the smallest|"
    r"the minimum|the maximum|the sum of|in lowest terms)\b", re.I)
PROOF_ONLY = re.compile(r"\b(prove|show that|prove or disprove|prove that)\b", re.I)


def fetch(name):
    p = CACHE / name
    if p.exists():
        return p.read_text(encoding="utf-8", errors="replace")
    url = f"{ARCHIVE}/{name}"
    req = urllib.request.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0 Safari/537.36"})
    with urllib.request.urlopen(req, timeout=30) as r:
        txt = r.read().decode("utf-8", errors="replace")
    p.write_text(txt, encoding="utf-8")
    return txt


def split_items(tex):
    """Split a Putnam TeX body into {label: body} on \\item[LABEL]."""
    m = re.search(r"\\begin\{itemize\}(.*)\\end\{itemize\}", tex, re.S)
    body = m.group(1) if m else tex
    out = {}
    parts = re.split(r"\\item\[([AB][1-6])\]", body)
    # parts = [pre, label, chunk, label, chunk, ...]
    for i in range(1, len(parts) - 1, 2):
        lab = parts[i].strip()
        chunk = parts[i + 1]
        out[lab] = chunk.strip()
    return out


def clean_stmt(tex):
    s = tex
    s = re.sub(r"%.*", "", s)                      # tex comments
    s = re.sub(r"\\label\{[^}]*\}", "", s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    # drop a trailing lone \, spacer artifact
    s = re.sub(r"\n\\,\s*$", "", s).strip()
    return s


def is_answer_bearing(stmt):
    # must ask for a value and not be a pure proof problem
    if not ANSWER_CUES.search(stmt):
        return False
    # "Find all ... such that ... prove" style still counts if it asks to find;
    # exclude only when it is purely prove/show with no find/compute cue.
    if PROOF_ONLY.search(stmt) and not ANSWER_CUES.search(stmt):
        return False
    return True


def main():
    manifest = []
    cohort = []
    picked = 0
    TARGET = 60
    for y in YEARS:
        try:
            probs = split_items(fetch(f"{y}.tex"))
            sols = split_items(fetch(f"{y}s.tex"))
        except Exception as e:
            print(f"  skip {y}: {e}")
            continue
        for lab in LABELS:
            if picked >= TARGET:
                break
            if lab not in probs or lab not in sols:
                continue
            stmt = clean_stmt(probs[lab])
            sol = clean_stmt(sols[lab])
            if len(stmt) < 20 or len(sol) < 40:
                continue
            if not is_answer_bearing(stmt):
                continue
            pid = f"PUT-{y}-{lab}"
            (STMT / f"{pid}.txt").write_text(stmt + "\n", encoding="utf-8")
            (GT_SOL / f"{pid}.txt").write_text(sol + "\n", encoding="utf-8")
            manifest.append({
                "problem_id": pid,
                "title": f"Putnam {y} {lab}",
                "year": y,
                "label": lab,
                "text_url": f"{RAW_BASE}/{pid}.txt",
            })
            cohort.append({"problem_id": pid, "year": y, "label": lab})
            picked += 1
        if picked >= TARGET:
            break

    (ROOT / "manifest_putnam_60.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8")
    (GT / "cohort.json").write_text(
        json.dumps(cohort, indent=2), encoding="utf-8")
    print(f"picked {picked} answer-bearing problems across "
          f"{sorted({m['year'] for m in manifest})}")
    print(f"statements -> {STMT}")
    print(f"hidden solutions -> {GT_SOL}")
    print(f"manifest -> {ROOT/'manifest_putnam_60.json'}")


if __name__ == "__main__":
    main()
