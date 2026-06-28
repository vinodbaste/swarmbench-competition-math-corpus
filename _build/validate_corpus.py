#!/usr/bin/env python3
"""Validate the frozen corpus: every problem file must have a real statement and
posted solution(s), with no Cloudflare captures or silently-stripped inline math.

Exit code is non-zero if any HARD failure is found, so this can gate a build.
"""
import glob
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), os.pardir)


def statement(t: str) -> str:
    m = re.search(r"(?:^## Problem\s*)(.*?)(?=^## Solution|\Z)", t, re.S | re.M)
    if m:
        return m.group(1)
    return re.split(r"^## Solution", t, flags=re.M)[0]


def main() -> int:
    files = sorted(glob.glob(os.path.join(ROOT, "**", "problem_*.md"), recursive=True))
    hard, soft = [], []
    for f in files:
        rel = os.path.relpath(f, ROOT)
        t = open(f, encoding="utf-8").read()
        s = statement(t)
        sclean = re.sub(r"\s", "", s)
        has_sol = bool(re.search(r"^## Solution", t, re.M))
        # HARD failures (block the build)
        if "Performing security verification" in t or "Attention Required" in t:
            hard.append((rel, "cloudflare-capture")); continue
        if len(sclean) < 15:
            hard.append((rel, f"statement-too-short({len(sclean)}c)")); continue
        if not has_sol:
            hard.append((rel, "no-solution-section")); continue
        # SOFT signal: prose statement with dropped inline math (gap artifacts + no $)
        arts = (len(re.findall(r"\S  +\S", s)) + len(re.findall(r"[a-z] [.,)]", s))
                + s.count("$ $") + s.count("( )"))
        if s.count("$") == 0 and arts >= 4:
            soft.append((rel, f"possible-stripped-math(arts={arts})"))
    print(f"Validated {len(files)} problem files.")
    if hard:
        print(f"\nHARD FAILURES ({len(hard)}):")
        for r, why in hard:
            print(f"  FAIL {r}: {why}")
    if soft:
        print(f"\nSOFT WARNINGS ({len(soft)}) - review manually:")
        for r, why in soft:
            print(f"  warn {r}: {why}")
    if not hard and not soft:
        print("ALL CLEAN: every file has a real statement + solution; no captures or stripped math.")
    return 1 if hard else 0


if __name__ == "__main__":
    sys.exit(main())
