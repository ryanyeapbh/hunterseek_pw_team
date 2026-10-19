# Memory & Transfer Guide

How the workshop's "working experience" is stored, and how to carry it between devices
and accounts. Everything here is plain markdown — no hidden or device-locked storage.

## 1. What memory exists

```
hunterseek_pw/
  memory/
    sam-social-MEMORY.md   <- Sam's private working experience
    vans-video-MEMORY.md   <- Vans's private working experience
    pat-photo-MEMORY.md    <- Pat's private working experience
    mark-music-MEMORY.md   <- Mark's private working experience
    gale-gaming-MEMORY.md  <- Gale's private working experience
    content-log.md         <- SHARED content log/calendar (all roles read; Ryan owns)
```

**Two layers, on purpose:**
- **Per-role memory** — each role accumulates its own lessons (what captions land, what
  shots work, what music fits, what titles perform). Private to that role, mirroring how a
  real specialist builds personal expertise.
- **Shared content log** (`content-log.md`) — cross-role knowledge: what's planned, what's
  posted, what performed well, and cross-role dependencies (e.g. Vans needs Mark's track
  before a video is ready for Sam to caption/cross-post).

## 2. How it's used (built into each SKILL.md)
- **Read at session start** — every role reads its own MEMORY file (and `content-log.md`
  for context) before working, so past experience shapes new drafts.
- **Append after completion** — after a post/video/photo/track is drafted or approved, the
  role records a dated lesson and promotes durable insights into the right section.
- **Prune** — wrong or stale entries get removed so memory stays trustworthy.

## 3. Why it's transferable
Because it's all plain `.md` files inside `hunterseek_pw/`, the memory moves wherever the
folder goes. Nothing lives in device-only or session-only storage. To move the workshop +
its accumulated experience to another device or account, just move the `hunterseek_pw/`
folder.

## 4. Version control — already set up (private GitHub, daily auto-sync)

**Option A is live.** This folder is a git repository pushed to a **private** GitHub repo:
`https://github.com/ryanyeapbh/hunterseek_pw_team`

- `sync-github.ps1` — commits any changes and pushes them. Run it by hand whenever you want:
  `pwsh -NoProfile -File .\sync-github.ps1`
- **Automatic:** Windows Task Scheduler task **"Hunterseek GitHub sync"** runs it daily at
  **21:00**, and catches up if the PC was off at that time.
- Log: `%LOCALAPPDATA%\hunterseek-pw\sync.log` (kept outside the repo so logging never creates
  commits).
- Credentials live in Windows Credential Manager (Git Credential Manager) — never in this
  folder. If a push ever asks you to sign in again, that's the expected renewal.
- `.dsh\skills\` is git-ignored on purpose: those are links, rebuilt by `setup-skills.ps1`.
- Recovered on another device by cloning the repo, then running `setup-skills.ps1`.
- To pause syncing: disable the task (`Disable-ScheduledTask -TaskName 'Hunterseek GitHub sync'`).

**Option B — Cloud drive (alternative)**
Put the `hunterseek_pw/` folder in Google Drive / Dropbox / OneDrive. It syncs across your
devices automatically; open it from whichever machine you're on. Don't combine this with the
git task unless you understand the conflict risk — `.git` directories and cloud sync can
fight.

**Option C — Manual copy**
Zip and copy `hunterseek_pw/` to the new device. Works, but you must remember to re-copy
after memory changes — easy to end up with stale copies. Prefer A or B.

## 5. Moving to another device / account
1. Get the `hunterseek_pw/` folder onto the new device (clone the repo, or sync the drive).
2. Re-register the roles there:
   - **DeepSeek Harness** — run `pwsh -NoProfile -File .\setup-skills.ps1`, which rebuilds the
     four `.dsh\skills\` links. `AGENTS.md` (persona + standing rules) loads by itself.
   - **Claude Desktop** — install each role folder via **Settings -> Capabilities**.
3. The memory files come with the folder — the workshop resumes with its full history.
   Keep one live copy of the workshop: memory written into a copy you're not using gets lost
   the next time the folders are synced.

## 6. Hygiene
- Never store secrets, credentials, or work/company information in memory files.
- Keep entries short and factual; memory is a cheat-sheet, not a diary.
- Review the files occasionally and prune — small, correct memory beats large, stale memory.
