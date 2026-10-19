# mark-music — Memory

> Persistent working experience for Mark (Hunterseek Private Workshop, Phase 1). Read at the
> start of every session. Append reusable lessons after completion. Keep entries short and
> factual. Prune stale entries. Plain markdown; travels with the `hunterseek_pw` folder.
> Never store secrets, credentials, or work/company information.

## Ryan's voice / preferences
- Genre: gaming-style — exciting, epic, high-energy. Confirmed directly by Ryan (2026-08-16).
- **Scope updated 2026-08-16: original composition is now the priority**, aiming for a
  higher bar than generic stock tracks — Ryan explicitly asked for Mark to be able to
  compose, and to sound better than off-the-shelf options.
- **Sourcing:** any reference source is fair game for inspiration, but license conflicts must
  be actively avoided (no lifting melodies/riffs/lyrics from copyrighted work). Epidemic
  Sound and NCS remain the fallback when original isn't the right call this time.
- **No audio-generation tool is connected yet** (checked the MCP connector registry
  2026-08-16 — nothing relevant found). Until one is connected, "composing" means a full,
  concrete composition brief (key/tempo/chords/structure/instrumentation), not a rendered
  audio file. Say this plainly each time rather than implying a finished track exists.
- See `HUNTERSEEK-CHARTER.md` → Voice & Style for the wider brand baseline.

## Reusable patterns / templates that worked
- **Prompt formula for external generators** (Ryan's source, shared 2026-08-16): Genre +
  Emotion + Instruments + Tempo + Structure. See `mark-music/SKILL.md` for the full formula
  and generic example shapes. Generate a short 2–3 min track first, then use the platform's
  "Extend" feature to grow it — smoother than one long generation.
- **Note on that source's Suno/Udio take vs. this file's own platform research:** Ryan's
  shared source rated Udio "best audio quality" for instrumental game soundtracks with no
  mention of export/download limits. That conflicts with the licensing research below (Udio
  closed/subscription-only post-UMG-settlement, no export to YouTube/social as of this
  check). Don't resolve this by picking one — **verify Udio's actual current export/
  download status directly before ever recommending it**, since the two sources disagree and
  this is a fast-moving situation.

## Platform comparison (rendering a composition brief into audio) — checked 2026-08-16
Web-checked, not from training memory — recheck periodically, this space moves fast and
pricing/licensing terms change.
- **Suno** — full-song/vocal generator. Free tier: no commercial use. Paid plans (~$8–10/mo)
  add commercial rights with download caps; Suno Studio tier = unlimited downloads. Models
  reportedly being phased out for new licensed versions in 2026. Best fit: a track that
  needs vocals/lyrics (e.g. a fun theme song), not typical instrumental background scoring.
- **Udio** — Ryan named this one specifically, but it's **not practical right now**: after
  the Oct-2025 UMG settlement it relaunched as a closed, subscription-only system (Q2 2026)
  where tracks can't be downloaded/exported to YouTube or social — preview-only. Flag this
  rather than recommending it as the actual tool; recheck later since a UMG x Udio service
  is expected to open up more.
- **AIVA** — Standard plan (~€11/mo) permits commercial use on YouTube/TikTok/IG/Twitch;
  full copyright ownership only on the Pro plan (~€49/mo). Good for orchestral/epic moods.
- **Beatoven.ai** — perpetual, royalty-free commercial license on all paid plans, doesn't
  expire if the subscription lapses. Strong default for background/instrumental scoring.
- **Soundraw** — royalty-free on all paid tiers, licensed for all platforms including
  monetized content, persistent license survives cancellation. Also a strong default.
- **Loudly** — "100% royalty-free for personal and commercial use" across paid plans,
  licensed for monetized content including ads.
- **Mubert** — Creator tier (~$14/mo) excludes paid ads; Pro tier needed for full commercial
  use including ads.
- **ElevenMusic** — commercially cleared via Merlin/Kobalt partnerships; licensed for paid
  social, ads, branded video.
- **Epidemic Sound** (existing fallback source) — separate Commercial plan (~$16.99+/mo)
  required; "comprehensive" license covering YouTube/TikTok/Instagram/Twitch.
- **Bottom line for Hunterseek's use case** (instrumental background score, gaming-epic
  energy, needs to go on YouTube/Instagram/Facebook commercially): AIVA, Beatoven.ai,
  Soundraw, and Loudly are the cleanest starting recommendations. Suno only if vocals are
  wanted. Udio isn't usable yet for exportable files — don't suggest it as-is.
- Sources checked: [WaveSpeed — Best AI Music Generators 2026](https://wavespeed.ai/blog/posts/best-ai-music-generators-2026/),
  [Dubspot — Best AI Music Generators 2026: Suno, Udio, Stable Audio 3](https://blog.dubspot.com/best-ai-music-generators-2026),
  [PostEverywhere — 13 Best AI Music Generators for Videos 2026](https://posteverywhere.ai/blog/13-best-ai-music-generators-for-videos).
  Always verify current pricing/licensing directly on the platform before Ryan commits —
  these terms change often and this was one point-in-time check.

## Recurring pitfalls to avoid
- Don't claim a rendered audio file exists — no generation tool is connected; output is a
  composition brief until that changes.
- Don't reproduce a copyrighted melody/riff/lyric when using a reference track for mood.
- Don't skip noting licensing terms when falling back to Epidemic Sound / NCS.

## Log
### 2026-08-16 — Confirmed sourcing directly from Ryan
- What I did: recorded Ryan's direct answer on music genre and sourcing.
- Lesson: genre = gaming excitement/epic; sourced from Epidemic Sound and NCS, no original
  composition — this replaces any earlier guesswork.

### 2026-08-16 — Scope expanded to original composition
- What I did: Ryan asked for Mark to be able to compose original music (aiming for better
  quality than generic sources), sourced from any reference as long as license conflicts are
  avoided. Checked the MCP connector registry for an audio-generation tool — none found.
- Lesson: composition is now the priority over curation, but the real deliverable today is a
  detailed composition brief (not a rendered file) until an audio-generation tool is
  connected — be upfront about that gap every time.

### 2026-08-16 — Researched external rendering platforms (Ryan asked for Suno, etc.)
- What I did: web-checked the 2026 AI music generation landscape to give real platform
  recommendations for turning a composition brief into audio (Ryan specifically asked about
  Suno). Findings logged above in "Platform comparison."
- Lesson: Udio — the platform Ryan named — isn't actually usable yet for exportable files;
  AIVA/Beatoven.ai/Soundraw/Loudly are the better recommendation for instrumental background
  scoring. Always name the specific paid tier needed for commercial rights, since these
  platforms often gate that behind a tier above the cheapest paid plan.

### 2026-08-16 — Ryan shared a prompt-formula source for Suno/Udio-style generators
- What I did: read a ChatGPT conversation Ryan shared covering AI music picks for gaming
  and a "Genre + Emotion + Instruments + Tempo + Structure" prompt formula with example
  prompt shapes for boss-battle/infiltration/heroic-finale moods, plus a tip to generate
  short then use "Extend." Added the formula to `mark-music/SKILL.md` as the standard way
  to turn a composition brief into an actual generator prompt — genericized the examples
  (dropped specific franchise names like naming a game to imitate) to stay clear of the
  license-conflict guardrail.
- Lesson: that source's platform take (Udio = best audio quality, no caveats) conflicts with
  this file's own licensing research (Udio currently closed/no-export). Flagged as an open
  discrepancy above rather than silently trusting either source — verify before recommending
  Udio to Ryan.
