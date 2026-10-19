# INSTALL Checklist — Hunterseek Private Workshop

Follow top to bottom. Tick each box. One-time setup is Part 1–3; Part 4 repeats per post.

## Part 1 — Put the workshop somewhere permanent
- [x] Lives at `C:\Deepseek\hunterseek_pw` (permanent, not a temp folder).
- [x] **GitHub backup — done.** Private repo `ryanyeapbh/hunterseek_pw_team`, pushed; the
      scheduled task **"Hunterseek GitHub sync"** commits + pushes daily at 21:00 with
      catch-up. Manual run: `pwsh -NoProfile -File .\sync-github.ps1`.
- [x] `memory/` travels with the folder (that's where accumulated experience lives).

## Part 2 — Register the 5 Phase 1 skills

**DeepSeek Harness (current setup) — automatic.** DSH discovers skills at
`<workshop>\.dsh\skills\<name>\SKILL.md`. Those five entries are directory links to the real
role folders, so there is only ever one `SKILL.md` to maintain:
- [ ] Run `pwsh -NoProfile -File .\setup-skills.ps1` (already done on this machine; re-run it
      whenever the workshop moves to a new drive or machine, or a role is added).
- [ ] `AGENTS.md` in the workshop root is the persona/standing-rules layer and loads
      automatically with every session in this folder — nothing to install for it.

**Claude Desktop (the original route, still valid).** Open **Settings → Capabilities** and add
each role folder below (each contains a `SKILL.md`):
- [ ] `hunterseek_pw/sam-social`
- [ ] `hunterseek_pw/vans-video`
- [ ] `hunterseek_pw/pat-photo`
- [ ] `hunterseek_pw/mark-music`
- [ ] `hunterseek_pw/gale-gaming`

## Part 3 — Verify install
- [ ] Ask: "list my skills" — confirm Sam, Vans, Pat, Mark, and Gale all appear.
- [ ] Quick smoke test: "Sam, draft a caption for my latest build" — it should reference the
      content pillars, Ryan's voice rules, and the draft-and-hold rule.
- [ ] Confirm each role can read its own MEMORY file and `memory/content-log.md` **in this
      workshop folder** (paths inside the skills are relative, so they follow the folder).
- [ ] Memory is unreachable if the harness isn't open on this folder — check the workspace
      path in the app before asking for a draft.

## Part 4 — Run a piece of content (repeat per post/video)
- [ ] Tell the relevant role what you want (e.g. "Vans, script a video for my latest plamo build").
- [ ] Roles log any cross-role dependency (needs Pat's stills, Mark's track, etc.) in `content-log.md`.
- [ ] Review every draft yourself — nothing publishes without your explicit go-ahead.
- [ ] After posting, confirm the entry moved from Planned to Posted in `content-log.md`.

## Part 5 — Phase 2 (done)
- [x] Gale hired 2026-10-19: `gale-gaming/SKILL.md` + `memory/gale-gaming-MEMORY.md` added,
      roster row moved into the Phase 1 table, skill registered in `.dsh\skills\`.
- [ ] To hire a future role, repeat that pattern and add the folder to `setup-skills.ps1`.

## Part 6 — Golden rules (sanity check)
- [ ] Draft-and-hold, always — no role publishes anything without your explicit approval.
- [ ] Keep Hunterseek separate from A.I.R. — no work/company/client content, no shared memory.
- [ ] No secrets/credentials in memory, logs, or docs.

## Moving to a new device / account later
- [ ] Get `hunterseek_pw/` onto the new machine (git clone / sync the drive / copy).
- [ ] Re-register the skills there: run `.\setup-skills.ps1` (DSH) or add each role folder via
      Settings → Capabilities (Claude).
- [ ] Memory travels with the folder — the workshop resumes with full history.
