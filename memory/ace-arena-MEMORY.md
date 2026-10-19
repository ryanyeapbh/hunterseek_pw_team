# ace-arena — Memory

> Persistent working experience for Ace (Hunterseek Private Workshop). Read at the start of
> every session. Append reusable lessons after completion. Keep entries short and factual.
> Prune stale entries. Plain markdown; travels with the `hunterseek_pw` folder.
> Never store secrets, credentials, or work/company information.

## Games & rules sources

- Ryan's established range (from `HUNTERSEEK-CHARTER.md`): **FGC** fighting games, **TCG**
  (digital — Yu-Gi-Oh Master Duel), **RPG**, **mobile** (Tower of Saviors), and **Initial D
  Arcade Stage**. Hired to cover *any* game, not just these five.
- **GUNDAM ASSEMBLE** (BANDAI TABLETOP GAMES, launched Oct 2026) — learned 2026-10-19.
  - Source: *Official Core Rulebook* **v1.0, updated 2026-09-14** (PDF, now in
    `ace-arena\gundam-assemble\source\`), plus the official Quick-Start Play Guide and the
    Starter Set 01 card list. Card images cached in `ace-arena\gundam-assemble\cards\`.
  - Deliverables: `GUNDAM-ASSEMBLE-quickstart.md` (rules digest + versus protocol) and
    `GUNDAM-ASSEMBLE-cards.md` (unit stats, weapons, all 18 Tactics cards).
  - Still unverified: **Sleeping Leviathan scenario card** (objective/goal scoring) and the **board map**.
    Everything else is confirmed — Advance = 0 TL, all 6 unit ability texts, terrain convention
    (light = lvl 1, dark = lvl 2), card-type timing.
- **No edition recorded** for the FGC/TCG/mobile titles yet — ask before giving rules advice.
- Record for every new game: title, platform/format, edition or patch, where the rules came
  from, and the date. Rules drift; a lesson without a version is a trap.

## Ryan as a player

- No actual play session yet (hired 2026-10-19), so no style profile. Don't assume aggression,
  patience, meta-chasing, or budget preference — observe it.
- **How he briefs work (2026-10-19):** numbered asks, terse. Sent one local PDF plus a pile of
  URLs (official site, YouTube, FAQ, card lists) and pointed at a `source` folder. Wants a
  **short summary / step-by-step walkthrough in a .md file**, not a rulebook dump, and asked
  up front whether a **text simulation to play against Ace** is possible. Answer: yes for
  turn-based games, and say so plainly.
- Record as they show up: preferred input/format, patience for long simulations, how blunt he
  wants rules corrections, whether he wants the win-line explained or just the move.

## Modes & formats that landed

- Nothing confirmed yet. First real sparring match sets the baseline — record what he keeps,
  corrects, or asks to redo.

## Recurring pitfalls

- Don't answer rules from a half-remembered edition. Ask for the rulebook/version first.
- Don't turn a simulation into narration; keep the state block visible and the actions terse.
- Don't sandbag in sparring games, and don't peek at hidden information while playing both
  sides.
- Don't absorb Gale's content role (angles, clips, streams, titles) or Vans/Sam/Pat/Mark work.
  Hand off and log the dependency in `content-log.md`.
- **Extracting Japanese game PDFs:** no pdftotext/pypdf on this machine and PyPI is blocked, so
  `tools\pdftext.py` (stdlib zlib + ToUnicode CMaps) does the job. Rulebook text lands in
  `rulebook.txt`.
- **Bandai's global site** 403s plain fetch/CloudFront. What works: `https://r.jina.ai/<url>`
  for text pages, and Node `fetch` with a browser User-Agent + Referer for images. Card data is
  **images only** — crop the text bands, upscale ×1.5–2 with Pillow, then read the sheet.
  `tools\make_sheets.py` builds the contact sheets.

## Log

### 2026-10-19 — Hired
- What I did: joined the roster as the sixth role, hired by Ryan to learn new games (video,
  TCG, tabletop, board), plan strategy, simulate play in text, and play against him. Seed notes
  above come from the charter and the hire request, not from a play session yet.
- Lesson: nothing first-hand logged. First real output — a rules digest, strategy plan, or
  sparring match — starts the real memory.

### 2026-10-19 — Gundam Assemble rules digest + card reference
- What I did: read the 53-page Core Rulebook v1.0 end to end, rebuilt the card data from the
  official card-list images, cross-checked against the Quick-Start Play Guide, and wrote two
  files (quickstart + cards). Set up the text-match protocol for 3v3 versus play.
- What Ryan gave: rulebook PDF in `source\`, and URLs for the site/YouTube/FAQ/card lists.
  Videos were not watchable (no transcript tool) — said so rather than pretending.
- Lesson: the rulebook's **Timeline** rules are complete but its **Advance cost is never
  printed**; don't paper over silence in a game's core economy — flag it and ask for the
  reference sheet. Also: BANDAI's online unit cards omit ability text, so the ability boxes on
  physical cards are the only source. Ask for photos early instead of building a sim on gaps.
- Open: ability texts U02–U06, scenario goals, map. Nothing played yet.

### 2026-10-19 — Gaps closed (Gundam Assemble)
- What Ryan did: created `video transcript\` with two cleaned transcripts, and uploaded the six
  unit card faces as `cards\u01.png`–`u06.png`.
- Lesson: **when a gap is un-closable from the web, ask for the two cheapest things — a transcript
  and card photos.** He delivered both in ~15 minutes and the dataset went from "partial" to
  complete. Ask specifically ("photos of the ability boxes"), not generally ("more info").
- Lesson: the designer's learn-to-play video carries rules the rulebook omits — **Advance is 0 TL**
  ("other than attacking, all primary actions cost two timeline"). Written rules + designer video
  together beat either alone.
- Dataset now complete except the Sleeping Leviathan scenario card and the board map.

### 2026-10-19 — Board tracker built (Gundam Assemble)
- What I did: wrote `board\GUNDAM-ASSEMBLE-table.html` — one self-contained file, no build step:
  hex board (SVG), Timeline lanes, unit cards with HP/Energy/TL/Upgrades/Status, objectives,
  dice tray with real `crypto` rolls, undo, browser save. Preloaded with our live position.
- Lesson: keep Tier 1 a **state tracker, not a judge** — it stores what happened, I referee the
  rules. That split is what makes it trustworthy. A rules engine is a separate, bigger promise.
- Verification without a browser: shim `document`/`localStorage` in Node, run the page script,
  assert it renders and that the hex-distance maths matches the map doc (`node --check` too).
