# U.S. Competition-Math Problems & Community Solutions (2024–2025) — frozen mirror

A frozen, publicly hosted mirror of problem statements, posted community solutions, and official
answer keys for ten U.S. math competitions from the 2024 and 2025 cycle. Captured from the
Art of Problem Solving wiki (problems © the Mathematical Association of America), with rendered
LaTeX restored to its TeX source.

This mirror exists because the live AoPS site is bot-protected (Cloudflare returns HTTP 403 /
challenge pages to automated clients). Hosting a verbatim public copy lets automated readers fetch
the real content reliably.

## Layout

- `index.json` — start here. Lists every contest and the raw URL of each problem file and answer key.
- `<contest>/problem_NN.md` — one file per problem: the statement followed by the posted written
  solutions (`Solution 1`, `Solution 2`, …).
- `<contest>/answer_key.md` — official answer key (short-answer contests).
- `_build/` — the scripts used to capture and clean this mirror (provenance / reproducibility).

## Contests (172 problems)

2025/2024 AIME I, 2025/2024 AIME II, 2025/2024 AMC 12A, 2025/2024 AMC 12B, 2025 USAMO, 2024 USAMO.

Note: the 2025 AMC 12A Problem 25 was officially voided by the MAA (no answer choice correct); the
answer key records this.
