#!/usr/bin/env python3
"""Rebuild the frozen corpus from AoPS MediaWiki *raw wikitext* (action=raw) via Jina.

Why: the previous build fetched Jina-*rendered* markdown and recovered LaTeX from image
alt-text. On some pages Jina silently dropped the problem statement's inline-math images
(leaving gap-ridden prose), captured Cloudflare challenge pages, or returned See-Also-only
stubs. The MediaWiki raw wikitext is the authoritative source: it carries the real LaTeX
(<math>/<imath>/<cmath>/\\(..\\)/\\[..\\]) and omits the rendered nav/footer entirely.

This fetches action=raw for every problem page, converts wikitext -> the same markdown
conventions the good files already use ($...$ inline, \\[...\\] display, [asy]...[/asy]),
and writes one clean .md per problem. Answer keys are left as-is (already validated).

Usage:
  python3 rebuild_raw.py            # rebuild all problem pages
  python3 rebuild_raw.py --only 2024_AIME_II/Problem_14 2025_USAMO/Problem_1   # test subset
"""

import argparse
import os
import re
import subprocess
import sys
import time
import urllib.parse

OUT_ROOT = os.path.join(os.path.dirname(__file__), os.pardir)
JINA = "https://r.jina.ai/"
AOPS = "https://artofproblemsolving.com/wiki/index.php?title="

# (contest_dir, page_prefix, count)
CONTESTS = [
    ("2025_AIME_I", "2025_AIME_I_Problems", 15),
    ("2025_AIME_II", "2025_AIME_II_Problems", 15),
    ("2024_AIME_I", "2024_AIME_I_Problems", 15),
    ("2024_AIME_II", "2024_AIME_II_Problems", 15),
    ("2025_AMC_12A", "2025_AMC_12A_Problems", 25),
    ("2025_AMC_12B", "2025_AMC_12B_Problems", 25),
    ("2024_AMC_12A", "2024_AMC_12A_Problems", 25),
    ("2024_AMC_12B", "2024_AMC_12B_Problems", 25),
    ("2025_USAMO", "2025_USAMO_Problems", 6),
    ("2024_USAMO", "2024_USAMO_Problems", 6),
]


def jobs():
    out = []
    for contest, prefix, n in CONTESTS:
        for i in range(1, n + 1):
            out.append((contest, f"{prefix}/Problem_{i}", f"problem_{i:02d}.md"))
    return out


# ----------------------------- fetch -----------------------------
CF_MARKERS = ("Performing security verification", "Attention Required",
              "Just a moment", "Enable JavaScript and cookies", "cf-browser-verification")


def fetch_raw(page_title: str, attempts: int = 5) -> str:
    url = JINA + AOPS + urllib.parse.quote(page_title, safe="/") + "&action=raw"
    last = ""
    for k in range(attempts):
        out = subprocess.run(
            ["curl", "-s", "--max-time", "90", url],
            capture_output=True, text=True,
        ).stdout
        body = out.split("Markdown Content:", 1)[1] if "Markdown Content:" in out else out
        if len(body) > 150 and not any(m in out for m in CF_MARKERS):
            return body
        last = out
        time.sleep(5 + k * 5)
    raise RuntimeError(f"blocked/short after {attempts} tries (last len={len(last)})")


# ------------------------- wikitext -> md -------------------------
def strip_templates(s: str) -> str:
    # iteratively remove innermost {{...}} (handles nesting)
    prev = None
    while prev != s:
        prev = s
        s = re.sub(r"\{\{[^{}]*\}\}", "", s)
    return s


def conv_links(s: str) -> str:
    # drop file/image embeds
    s = re.sub(r"\[\[(?:File|Image):[^\]]*\]\]", "", s, flags=re.IGNORECASE)
    # [[Page|Text]] -> Text ; [[Page]] -> Page
    s = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", s)
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)
    # [http://x text] -> text ; [http://x] -> ''
    s = re.sub(r"\[https?://[^\s\]]+\s+([^\]]+)\]", r"\1", s)
    s = re.sub(r"\[https?://[^\s\]]+\]", "", s)
    return s


def conv_math(s: str) -> str:
    s = re.sub(r"<asy>(.*?)</asy>", lambda m: "[asy]" + m.group(1) + "[/asy]", s, flags=re.DOTALL)

    def cmath(m):
        inner = m.group(1).strip()
        # Already a delimited display block: keep as-is.
        if "\\[" in inner or "\\]" in inner:
            return "\n" + inner + "\n"
        # Otherwise wrap in display delimiters (covers plain TeX and \begin{...} envs).
        return "\n\\[" + inner + "\\]\n"

    s = re.sub(r"<cmath>(.*?)</cmath>", cmath, s, flags=re.DOTALL)
    s = re.sub(r"<i?math>(.*?)</i?math>", lambda m: "$" + m.group(1).strip() + "$", s, flags=re.DOTALL)
    s = re.sub(r"\\\((.+?)\\\)", lambda m: "$" + m.group(1).strip() + "$", s, flags=re.DOTALL)
    return s


def conv_headers(s: str) -> str:
    def h(m):
        eq, title = m.group(1), m.group(2).strip()
        level = "###" if len(eq) >= 3 else "##"
        return f"{level} {title}"
    return re.sub(r"^(={2,})\s*(.*?)\s*=+\s*$", h, s, flags=re.MULTILINE)


def wikitext_to_md(s: str, contest: str) -> str:
    s = re.sub(r"<!--.*?-->", "", s, flags=re.DOTALL)
    s = re.sub(r"__[A-Z]+__", "", s)
    s = strip_templates(s)
    s = conv_math(s)
    s = conv_links(s)
    s = conv_headers(s)
    s = re.sub(r"'''(.+?)'''", r"**\1**", s, flags=re.DOTALL)
    s = re.sub(r"''(.+?)''", r"*\1*", s, flags=re.DOTALL)
    # ensure a Problem header: if none but a Solution exists, the statement is the lead text
    if not re.search(r"^## Problem", s, re.MULTILINE) and re.search(r"^## Solution", s, re.MULTILINE):
        head, _, rest = s.partition("## Solution")
        s = "## Problem\n\n" + head.strip() + "\n\n## Solution" + rest
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s).strip()
    return s + "\n"


# ----------------------------- main -----------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*", help="page titles like 2024_AIME_II/Problem_14")
    ap.add_argument("--force", action="store_true", help="overwrite existing files")
    args = ap.parse_args()

    all_jobs = jobs()
    if args.only:
        want = set(args.only)
        all_jobs = [(c, p, f) for (c, p, f) in all_jobs
                    if p in want or p.replace("_Problems", "") in want
                    or f"{c}/{os.path.basename(p)}" in want]

    ok, fail = 0, []
    for i, (contest, page, fname) in enumerate(all_jobs, 1):
        outdir = os.path.join(OUT_ROOT, contest)
        os.makedirs(outdir, exist_ok=True)
        outpath = os.path.join(outdir, fname)
        try:
            raw = fetch_raw(page)
            body = wikitext_to_md(raw, contest)
            stmt = re.search(r"## Problem\s*(.*?)(?=## Solution|\Z)", body, re.DOTALL)
            slen = len(re.sub(r"\s", "", stmt.group(1))) if stmt else 0
            if slen < 10:
                raise RuntimeError(f"statement too short ({slen}c) after convert")
            with open(outpath, "w", encoding="utf-8") as fh:
                fh.write(body)
            print(f"[{i}/{len(all_jobs)}] OK   {contest}/{fname}  ({len(body)}c, stmt={slen}c)")
            ok += 1
        except Exception as e:  # noqa: BLE001
            print(f"[{i}/{len(all_jobs)}] FAIL {contest}/{page}: {e}", file=sys.stderr)
            fail.append((contest, page, str(e)))
        time.sleep(3)
    print(f"\nDONE ok={ok} fail={len(fail)}")
    for c, p, e in fail:
        print(f"  RETRY-NEEDED {c} {p}: {e}")


if __name__ == "__main__":
    main()
