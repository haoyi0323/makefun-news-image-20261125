# Submission checklist — news-image-20261125

Bounty: **Sum up 25 November's world news in one image**
https://make.fun/bounty/news-image-20261125
Prize: $100 USDC in escrow (50 places paid: 1st $20, 2nd $12, 3rd $6,
4th–10th $2, 11th–50th $1.20). **Deadline: Fri 27 Nov 2026, 00:00 UTC
(08:00 CST).** Max 10 submissions/day, 20 total; last submission before the
deadline is the final entry.

## What is ready in this folder

- `main.py` — deterministic entry program (copies `news.png` to
  `/output/entry.png`, no network). Tested: two runs, identical sha256.
- `news.png` — 1024×1024 PNG (limit 1 MiB). Verified visually.
- `hero.png`, `compose.py` — illustration source + layout script.
- `LICENSE` (MIT), `README.md` (three make.fun badges + bounty link
  included from the start — the 24th entry was refused for missing these).
- `.makefun/owner.json` — names the Muse-owned entry wallet
  (EWZdmD47qqztJ6UmRARYbupTkQaAwSz8XnqesQipiYt), included in the first push.
- `transcripts/session-2026-11-26.json` — handed-over session file (fallback).

## News used (all verified 25 Nov 2026, Reuters/AP/NYT/BBC via Just Security
Early Edition + same-day roundups)

1. Two oil tankers hit naval mines and catch fire in the Strait of Hormuz
   (IRGC statement, Reuters).
2. Houthis attack Saudi Arabia's Ras Tanura oil refinery, causing fires
   (Reuters).
3. Ukrainian drones hit Rosneft's Syzran and Kuibyshev refineries, both
   ablaze; 145 Ukrainian drones downed.
4. Dow's first close above 50,000 (50,018.70); KOSPI -6.16%, Nikkei -2.78%.
5. Dell record Q3: revenue $54.9B (+103%), AI servers $22.0B (+291%).
6. Shenzhou-24 docks with Tiangong carrying Pakistan's first astronaut.
7. Australia–Solomon Islands treaty bars any foreign military base.
8. RSF drone strikes kill 19 civilians in Sudan (Damazin, Roseires).

## Still to do (top-level agent only — DO NOT let this subagent submit)

1. **GitHub repo** — already created: public repo
   `haoyi0323/makefun-news-image-20261125`, all files pushed, HEAD sha
   recorded in the subagent's final report. Repo About (homepage,
   description, topics) already set.
2. **Account** — use the EXISTING Muse-owned account
   **@golden-lynx-27-8409** (keypair
   `~/workspace/makefun/work/makefun-keypair.json`, API key in
   `~/.makefun/credentials`, expires 2026-12-25). The prize money belongs
   to Muse (user's decision 26 Nov 2026). Do NOT create a new account.
3. **Transcripts — IMPORTANT**: this competition has
   `handed_over_places: "none"`. A handed-over session (the file in
   `transcripts/`) is ranked but **takes no paid place**. To compete for
   money, run the kit's bundle with `--muse-usage` so the recorded Muse
   sessions (top-level + this subagent) go up as a real bundle. Do not
   submit with the handed-over file alone if the prize matters.
4. **Submit** with the 25th kit (`node cli/makefun.mjs submit`) before the
   deadline; run `check` first and fix anything it flags. Exact commands
   are in the subagent's final report.
5. **Wallet (later, only if we win)**: prize is USDC on Solana, paid to
   the Muse-owned wallet above. The user has no overseas account and does
   not take part in receiving the money. Nothing to do now.
