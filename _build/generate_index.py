#!/usr/bin/env python3
"""Generate index.json (the navigation entry point the benchmark agent starts from).

Usage:
    python3 generate_index.py "https://raw.githubusercontent.com/<owner>/<repo>/main"

The agent is given ONLY the index URL. It fetches the index, discovers the contest
structure, and follows the per-problem URLs to gather statements + community
solutions. Run this after the repo/base URL is known and commit the result.
"""

import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), os.pardir)

CONTEST_META = {
    "2025_AIME_I": ("2025 AIME I", "short_answer", "integer_000_999"),
    "2025_AIME_II": ("2025 AIME II", "short_answer", "integer_000_999"),
    "2024_AIME_I": ("2024 AIME I", "short_answer", "integer_000_999"),
    "2024_AIME_II": ("2024 AIME II", "short_answer", "integer_000_999"),
    "2025_AMC_12A": ("2025 AMC 12A", "short_answer", "multiple_choice_letter"),
    "2025_AMC_12B": ("2025 AMC 12B", "short_answer", "multiple_choice_letter"),
    "2024_AMC_12A": ("2024 AMC 12A", "short_answer", "multiple_choice_letter"),
    "2024_AMC_12B": ("2024 AMC 12B", "short_answer", "multiple_choice_letter"),
    "2025_USAMO": ("2025 USAMO", "proof", "proof"),
    "2024_USAMO": ("2024 USAMO", "proof", "proof"),
}
ORDER = list(CONTEST_META.keys())


def main():
    base = (sys.argv[1] if len(sys.argv) > 1 else "__RAW_BASE__").rstrip("/")
    contests = []
    total = 0
    for cdir in ORDER:
        d = os.path.join(ROOT, cdir)
        if not os.path.isdir(d):
            continue
        name, kind, ans_type = CONTEST_META[cdir]
        probs = sorted(
            f for f in os.listdir(d) if re.fullmatch(r"problem_\d+\.md", f)
        )
        entry = {
            "contest": name,
            "kind": kind,
            "answer_type": ans_type,
            "num_problems": len(probs),
            "problems": [f"{base}/{cdir}/{p}" for p in probs],
        }
        key = os.path.join(d, "answer_key.md")
        if os.path.exists(key):
            entry["answer_key"] = f"{base}/{cdir}/answer_key.md"
        contests.append(entry)
        total += len(probs)
    index = {
        "title": "U.S. Competition-Math Problems & Community Solutions (2024-2025) — frozen mirror",
        "description": (
            "Frozen, public mirror of problem statements, posted community solutions, and "
            "official answer keys for the contests below. Each problem file contains the "
            "statement followed by the posted written solutions ('Solution 1', 'Solution 2', ...). "
            "Fetch each problem URL to read it."
        ),
        "source": "Art of Problem Solving Wiki (problems (c) Mathematical Association of America)",
        "total_contests": len(contests),
        "total_problems": total,
        "contests": contests,
    }
    out = os.path.join(ROOT, "index.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(index, f, indent=2)
    print(f"wrote {out}  contests={len(contests)} problems={total} base={base}")


if __name__ == "__main__":
    main()
