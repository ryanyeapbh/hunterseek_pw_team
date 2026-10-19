# Generic House Map — "Sector 7 Drift" (not an official scenario)

Built 2026-10-19 because the Sleeping Leviathan scenario card isn't available yet. **This is a house map, not the box's map.** Geometry is legal under the Core Rulebook; the name is mine.

## Legend

| Symbol | Meaning |
|---|---|
| `.` | open ground, elevation 0 |
| `^1` | elevation 1 terrain |
| `^2` | elevation 2 terrain (peak) |
| `~` | water |
| `*` | debris field |
| `R` | **your Base** (west) |
| `X` | **Ace's Base** (east) |
| `O` | neutral Objective |
| `G` | Garrison (yours / mine, per side) |
| `E` | Energy token |
| `U` | Upgrade token (face down, randomised) |

## Board — 7 rows (A–G) × 13 columns (1–13), odd-row offset hexes

| Row | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **A** | . | . | . | . | . | . | **R** | . | . | . | . | . | . |
| **B** | . | . | . | . | . | . | . | . | ~ | ~ | . | . | . |
| **C** | . | . | . | . | **G** | ^1 | **U** | * | . | **E** | . | . | . |
| **D** | . | . | . | **O** | . | ^1 | ^2 | . | . | **O** | . | . | . |
| **E** | . | . | . | **E** | ~ | * | **U** | ^1 | **G** | . | . | . | . |
| **F** | . | . | . | ~ | ~ | . | . | . | . | . | . | . | . |
| **G** | . | . | . | . | . | . | **X** | . | . | . | . | . | . |

## Hex adjacency (odd-row offset)

For row `r`, column `c`:

- Same row: `(r, c-1)`, `(r, c+1)`
- **Even rows (A, C, E, G):** up `(r-1, c-1)`, `(r-1, c)`; down `(r+1, c-1)`, `(r+1, c)`
- **Odd rows (B, D, F):** up `(r-1, c)`, `(r-1, c+1)`; down `(r+1, c)`, `(r+1, c+1)`

If that's annoying to eyeball, ignore it — I'll state the hex distance for every move and attack, and you can sanity-check.

## The distances that matter

| From → To | Hexes | Why it matters |
|---|---|---|
| Your Base A7 → Objective D4 | 4 | Two activations of Advance gets you there |
| Your Base A7 → your Garrison C5 | 3 | Rescue is worth 2 VP for 2 TL |
| Your Base A7 → Upgrade C7 | 2 | Cheapest upgrade grab on the map |
| Your Base A7 → peak D7 | 3 | Reachable on turn 1, but you're then the highest target on the board |
| Your Base A7 → my Vidar's opening hex E8 | 4 | Your Zaku's Bazooka reaches exactly 4 — that shot was live on turn 1 |
| Your Base A7 → your Energy E4 | 5 | Closer to my side than yours; a detour, not a free pickup |
| Your Base A7 → my Base G7 | 6 | Nothing happens on turn 1 |
| Objective D4 ↔ Objective D10 | 6 | You cannot hold both with a 3-unit squad |
| Ridge: C6 ^1 — D7 ^2 — E8 ^1 | — | The only high ground. Standing on D7 gives +1 accuracy down, and makes you a target |

## Why this map

- **Symmetric** — mirrored about the centre column, so neither side gets a free flank.
- **One central hill** — rewards whoever commits to it, but elevation punishes as much as it helps (enemies shooting up at you get −1, but you're also shooting down into cover).
- **Water and debris on the same flank** — makes the southern approaches slow and inaccurate, so the north flank is the fast lane.
- **Two Objectives far apart** — forces a choice. With three units you defend one and contest the other, or you abandon one and go hunting for VP on kills.
- **Garrisons 3 hexes out** — reachable for a 2 VP Rescue, but it costs you a whole activation away from the Objectives.

## Deployment (both sides)

- All units start in **Reserve**. First activation: deploy onto the **same hex as your Base**, then activate immediately.
- A deployed unit **cannot end its activation on the Base** — it must move at least one hex.
- Base hexes: you **A7**, me **G7**. Overlapping deployment is legal only if we ever end up stacked, which we won't at the start.

## Scoring for this house game

Straight Core Rulebook: unit VP per kill, 2 VP per Garrison defeated, 2 VP per allied Garrison Rescued, control of Objectives scored at the end of each Phase. **Since there's no scenario card, I'm scoring 2 VP per Objective per Phase end** — that's a house number, flagged as such, and we'll change it if you say so.
