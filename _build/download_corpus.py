#!/usr/bin/env python3
"""Download a frozen, math-intact mirror of AoPS competition pages via the Jina reader.

AoPS is Cloudflare-protected and 403s direct/agent fetches. r.jina.ai fetches
server-side (not blocked) and returns markdown where every rendered-LaTeX image
carries the original TeX in its alt text:  ![Image N: $...$](https://latex...png).
We extract that alt text back into inline/display math, drop video-solution and
navigation noise, and save one clean .md per page. This becomes the public GitHub
mirror the benchmark agent fetches (raw.githubusercontent.com returns 200).
"""

import os
import re
import subprocess
import sys
import time
import urllib.parse

OUT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
JINA = "https://r.jina.ai/"
AOPS = "https://artofproblemsolving.com/wiki/index.php/"

# (contest_dir, page_title_on_aops, output_filename)
PAGES: list[tuple[str, str, str]] = []


def add_range(contest_dir: str, page_prefix: str, lo: int, hi: int):
    for n in range(lo, hi + 1):
        PAGES.append((contest_dir, f"{page_prefix}/Problem_{n}", f"problem_{n:02d}.md"))


# Short-answer contests (rich community solutions to audit)
add_range("2025_AIME_I", "2025_AIME_I_Problems", 1, 15)
add_range("2025_AIME_II", "2025_AIME_II_Problems", 1, 15)
add_range("2025_AMC_12A", "2025_AMC_12A_Problems", 1, 25)
add_range("2025_AMC_12B", "2025_AMC_12B_Problems", 1, 25)
add_range("2024_AIME_I", "2024_AIME_I_Problems", 1, 15)
add_range("2024_AIME_II", "2024_AIME_II_Problems", 1, 15)
add_range("2024_AMC_12A", "2024_AMC_12A_Problems", 1, 25)
add_range("2024_AMC_12B", "2024_AMC_12B_Problems", 1, 25)
# Proof contests (rigor audits)
add_range("2025_USAMO", "2025_USAMO_Problems", 1, 6)
add_range("2024_USAMO", "2024_USAMO_Problems", 1, 6)

# Answer keys (public on the same wiki) for the short-answer contests
ANSWER_KEYS = [
    ("2025_AIME_I", "2025_AIME_I_Answer_Key", "answer_key.md"),
    ("2025_AIME_II", "2025_AIME_II_Answer_Key", "answer_key.md"),
    ("2025_AMC_12A", "2025_AMC_12A_Answer_Key", "answer_key.md"),
    ("2025_AMC_12B", "2025_AMC_12B_Answer_Key", "answer_key.md"),
    ("2024_AIME_I", "2024_AIME_I_Answer_Key", "answer_key.md"),
    ("2024_AIME_II", "2024_AIME_II_Answer_Key", "answer_key.md"),
    ("2024_AMC_12A", "2024_AMC_12A_Answer_Key", "answer_key.md"),
    ("2024_AMC_12B", "2024_AMC_12B_Answer_Key", "answer_key.md"),
]

LATEX_IMG = re.compile(
    r"!\[Image \d+:\s*(.*?)\]\(https://latex\.artofproblemsolving\.com/[^)]+\)",
    re.DOTALL,
)
OTHER_IMG = re.compile(r"!\[Image \d+[^\]]*\]\([^)]*\)")
# Sections we drop entirely (videos + nav footer); cut from the heading line to the next heading/EOF.
# The heading match is line-bounded ([^\n]*) so DOTALL only applies to the section body (.*?).
DROP_SECTION = re.compile(
    r"^#{2,}[^\n]*(?:Video Solution|Video solution|See also)[^\n]*\n.*?(?=^#{2,}\s|\Z)",
    re.MULTILINE | re.DOTALL,
)


def clean(md: str) -> str:
    # Strip the reader preamble (Title/URL Source/Markdown Content) keeping the body.
    idx = md.find("Markdown Content:")
    if idx != -1:
        md = md[idx + len("Markdown Content:"):]
    md = LATEX_IMG.sub(lambda m: m.group(1).strip(), md)
    md = OTHER_IMG.sub("", md)
    md = DROP_SECTION.sub("", md)
    # Drop bare youtube lines and user-attribution artifacts left behind.
    md = re.sub(r"^\s*\[https?://(www\.)?(youtube\.com|youtu\.be)[^\]]*\]\([^)]*\)\s*$", "", md, flags=re.MULTILINE)
    md = re.sub(r"\n{3,}", "\n\n", md).strip()
    return md + "\n"


ANS_LINE = re.compile(r"^\s*(\d{1,2})\.\s*(.+?)\s*$")


def clean_answer_key(raw: str, title: str) -> str:
    if "Markdown Content:" in raw:
        raw = raw.split("Markdown Content:", 1)[1]
    lines = raw.splitlines()
    answers: list[tuple[int, str]] = []
    for ln in lines:
        m = ANS_LINE.match(ln)
        if not m:
            continue
        num = int(m.group(1))
        val = m.group(2).strip()
        # Keep AIME (1-3 digit ints), AMC letters, or the AMC-25 withdrawal note.
        if re.fullmatch(r"\d{1,3}", val) or re.fullmatch(r"[A-E]", val) or "correct" in val.lower():
            if 1 <= num <= 25:
                answers.append((num, val))
    # Deduplicate by problem number, keep first, sort.
    seen, dedup = set(), []
    for num, val in answers:
        if num in seen:
            continue
        seen.add(num)
        dedup.append((num, val))
    dedup.sort()
    out = [f"# {title} Answer Key", ""]
    out += [f"{n}. {v}" for n, v in dedup]
    return "\n".join(out) + "\n"


def fetch(page_title: str, attempts: int = 4) -> str:
    url = JINA + AOPS + urllib.parse.quote(page_title)
    last = ""
    for k in range(attempts):
        out = subprocess.run(
            ["curl", "-s", "--max-time", "90", url],
            capture_output=True, text=True,
        ).stdout
        if len(out) > 400 and "Attention Required" not in out:
            return out
        last = out
        time.sleep(4 + k * 4)  # backoff on throttle/short response
    raise RuntimeError(f"short response after {attempts} tries (last len={len(last)})")


def main():
    jobs = [(c, p, f) for (c, p, f) in PAGES] + [(c, p, f) for (c, p, f) in ANSWER_KEYS]
    ok, fail = 0, []
    for i, (contest, page, fname) in enumerate(jobs, 1):
        outdir = os.path.join(OUT_ROOT, contest)
        os.makedirs(outdir, exist_ok=True)
        outpath = os.path.join(outdir, fname)
        if os.path.exists(outpath) and os.path.getsize(outpath) > 200:
            print(f"[{i}/{len(jobs)}] skip (exists) {contest}/{fname}")
            ok += 1
            continue
        try:
            raw = fetch(page)
            if fname == "answer_key.md":
                body = clean_answer_key(raw, contest.replace("_", " "))
            else:
                body = clean(raw)
            if len(body) < 120 or "Attention Required" in raw:
                raise RuntimeError(f"suspicious/blocked content len={len(body)}")
            with open(outpath, "w", encoding="utf-8") as fh:
                fh.write(body)
            print(f"[{i}/{len(jobs)}] OK   {contest}/{fname}  ({len(body)} chars)")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(jobs)}] FAIL {contest}/{page}: {e}", file=sys.stderr)
            fail.append((contest, page, str(e)))
        time.sleep(4)
    print(f"\nDONE ok={ok} fail={len(fail)}")
    for c, p, e in fail:
        print(f"  RETRY-NEEDED {c} {p}: {e}")


if __name__ == "__main__":
    main()
