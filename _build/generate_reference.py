#!/usr/bin/env python3
"""Build the judge-only grounding file (reference_answers.json) from the cleaned
answer keys, plus official-solution pointers for the proof contests. This is mounted
at grading time only and is NEVER visible to the benchmark agent.
"""

import json
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
OUT = os.path.join(os.path.dirname(__file__), "reference_answers.json")

SHORT = {
    "2025 AIME I": ("2025_AIME_I", "integer_000_999"),
    "2025 AIME II": ("2025_AIME_II", "integer_000_999"),
    "2024 AIME I": ("2024_AIME_I", "integer_000_999"),
    "2024 AIME II": ("2024_AIME_II", "integer_000_999"),
    "2025 AMC 12A": ("2025_AMC_12A", "multiple_choice_letter"),
    "2025 AMC 12B": ("2025_AMC_12B", "multiple_choice_letter"),
    "2024 AMC 12A": ("2024_AMC_12A", "multiple_choice_letter"),
    "2024 AMC 12B": ("2024_AMC_12B", "multiple_choice_letter"),
}
LINE = re.compile(r"^\s*(\d{1,2})\.\s*(.+?)\s*$")


def parse_key(cdir: str) -> dict:
    answers = {}
    with open(os.path.join(ROOT, cdir, "answer_key.md"), encoding="utf-8") as f:
        for ln in f:
            m = LINE.match(ln)
            if m:
                answers[m.group(1)] = m.group(2).strip()
    return answers


def main():
    contests = {}
    for name, (cdir, atype) in SHORT.items():
        contests[name] = {"answer_type": atype, "answers": parse_key(cdir)}
    contests["2025 USAMO"] = {
        "answer_type": "proof",
        "source": "https://web.evanchen.cc/exams/USAMO-2025-notes.pdf",
        "note": "Six proof problems. Grade the agent's worked proofs and its audits of the "
                "posted community solutions on mathematical rigor against the official solution notes.",
    }
    contests["2024 USAMO"] = {
        "answer_type": "proof",
        "source": "https://web.evanchen.cc/exams/USAMO-2024-notes.pdf",
        "note": "Six proof problems. Grade on rigor against the official solution notes.",
    }
    ref = {
        "_comment": "Judge-only grounding (mounted at grading time, NEVER shown to the agent). "
                    "Official answer keys for the short-answer contests and official-solution "
                    "pointers for the proof contests, used to anchor the LLM judge against "
                    "hallucination. AMC Problem 25 for 2025 AMC 12A was officially voided (no "
                    "correct choice); a correct treatment notes this rather than inventing an answer.",
        "contests": contests,
    }
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(ref, f, indent=2)
    n = sum(len(c.get("answers", {})) for c in contests.values())
    print(f"wrote {OUT}  contests={len(contests)} keyed_answers={n}")


if __name__ == "__main__":
    main()
