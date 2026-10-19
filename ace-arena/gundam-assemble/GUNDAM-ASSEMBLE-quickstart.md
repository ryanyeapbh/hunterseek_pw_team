# GUNDAM ASSEMBLE — Quickstart Digest

**Source:** *GUNDAM ASSEMBLE Official Core Rulebook* v1.0, updated 14 Sep 2026 (the PDF you dropped in `source\`), cross-checked against the official Quick-Start Play Guide and the designer's *Learn to Play* video transcript (`video transcript\`).
**Everything below is from those official sources** — no guessing. Genuinely unstated things are flagged **GAP**.
**Cards:** unit stats, weapons, all ability texts and all 18 Tactics cards are in `GUNDAM-ASSEMBLE-cards.md`.
**Still missing:** the scenario goal cards and the board map. See §11.

---

## 1. The game in 60 seconds

Hex-grid skirmish, 3v3 (or 5v5) Mobile Suits, 2 Phases × 10 rounds. Kill units, rescue/hold Garrisons, control Objectives, score scenario goals.

The one idea that decides games: **your units are not "yours to move whenever" — they live on a Timeline track, and every action you take costs time.** Attack and you vanish for 3-4 rounds. Shoot the wrong moment and you hand the whole phase to your opponent.

```
Timeline track: spaces 1..10 = rounds 1..10 of the Phase
Your 3 units each sit on a space. When a space comes up, that unit activates.
Acting pushes its token forward by the action's TL cost.
Past 10 → wraps to 1 and keeps counting. Spend >10 TL in one activation → gone until next Phase.
```

## 2. Setup checklist

1. Board in the middle.
2. Scenario components on the board: Bases or Carriers, Garrisons, Upgrades, Energy, Objectives, Terrain.
3. Off-board within reach: spare Upgrades, status tokens, Energy, attack dice (d10s), objective control tokens.
4. Timeline track next to the board.
5. Both players reveal squads: miniature + unit card + Timeline token per unit.
6. Place Timeline tokens on each unit's **starting TL value**. Same space = stack, top goes first.
7. **Lowest starting TL acts first.** Tied → both roll one die, higher goes first.
8. Resolve **Setup abilities**, in activation order, starting with the first player.
9. Each player shuffles their 9-card Tactics deck and **draws 3**.
10. All units **start in Reserve** — off the board. First activation deploys them.

**Starter scenario is "Sleeping Leviathan."** Your own scenario card dictates terrain, objectives and special rules — I don't have it yet, so treat the board as scenario-defined until you send it.

**Terrain convention (from the designer's walkthrough):** the 3D hex pieces encode elevation by shade — **light pieces = level 1, dark pieces = level 2**, with the bare board as ground level.

**Upgrade tokens go face down and randomised** at setup, so neither player knows what's under them until a unit ends its move on one.

## 3. Activation anatomy

A round = one space on the Timeline. All units on that space activate (top of stack first; if both players have units there, alternate, with whoever acted most recently going last). Empty spaces are skipped.

Each activation gives you four slots — **A to D — one use each, in any order**:

| | Slot | Notes |
|---|---|---|
| **A** | **Advance** — move up to 3 hexes | **0 TL.** Confirmed: the designer says "you may advance and take a primary action in either order," and "other than attacking, all primary actions cost two timeline." |
| **B** | **One Primary Action** — Attack / Dash / Energize / Rescue | **Mandatory.** This is what pushes your Timeline along. |
| **C** | **Command abilities** | Each once per activation; only on the unit being activated. |
| **D** | **One Tactics card** | Attack / Command / Response, per its own timing. |

**Card-type timing:** a **Command** card is played on your turn *in addition* to your other actions. An **Attack** card **replaces your attack** for that activation (it still burns its weapon's TL). A **Response** card fires whenever its trigger condition is met — including on your opponent's turn.

Because it's *in any order*, you can shoot then Advance away, or Advance into position then strike. The Advance happens once per activation either way.

Deployed units must move at least one hex before ending (can't just sit on the Base).

### Primary Actions (pick one)

| Action | TL cost | Effect |
|---|---|---|
| **Attack** | weapon's TL cost | Attack with an equipped weapon or a card-granted weapon |
| **Dash** | 2 | Move up to 2 hexes |
| **Energize** | 2 | Gain 1 Energy on this unit |
| **Rescue** | 2 | Remove an adjacent **allied Garrison** → **+2 VP** |

Any ability that grants an "additional" action lets you take a second Primary Action — including a TL-0 action, which counts as additional, not as your Primary.

## 4. The Timeline is the whole game

**Pay TL immediately after declaring the action, before resolving it.** So a big attack commits you even if it misses.

Wrap rule: if the cost goes past space 10, move to 10, back to 1, keep counting. So Zeong at round 8 paying 4 TL ends on **space 2** — round 2 has already gone by in this Phase, so it does not act again in Phase 1; it comes back at round 2 of **Phase 2**. Spending more than 10 TL in one activation is the same thing pushed further: the unit doesn't act again until the next Phase.

**GAP:** the book never says whether tokens reset at the start of Phase 2. The examples (and the "advances into the next Phase" wording) imply **tokens carry over** and the track just restarts at round 1. Play it that way unless your reference sheet says otherwise.

- End of Phase 1: score Phase-1 objectives, **draw 3 Tactics**, restart at round 1.
- End of Phase 2: score, compare VP, done.

### The real cost table (what you're actually paying)

| You want to… | TL paid | What it buys |
|---|---|---|
| Shoot with a 3-TL weapon | 3 | ~3 rounds of being absent |
| Shoot with a 4-TL weapon | 4 | ~4 rounds — a whole phase segment |
| Dash | 2 | 2 hexes, repositioning |
| Energize | 2 | 1 Energy — expensive. Energy is a real investment |
| Rescue | 2 | 2 VP, one of the best ratios in the game if a Garrison is near |

**Tempo maths that matters:** an average 4-TL attack means your ~3-unit squad is getting a handful of activations per Phase. Every attack costs you board presence. Advance is free — the whole game is *where you stand for free* vs *what you spend time on*.

## 5. Attacking — exact sequence

1. **Declare** the attack (target + weapon). Abilities you want must be used before this.
2. **Check** range and Line of Sight.
3. **Pay TL.**
4. Responses that fire **before dice**.
5. **Roll** Strength d10s, all at once.
6. Responses **after dice**. *Disarm* triggers here, after the attacker's own abilities, then is removed.
7. Resolve **critical hit effects**.
8. **Damage** = hits − Shields. *Fracture* triggers on damage. 0 HP → defeated.
9. Responses **after damage**.

If both players want to respond at once: attacker resolves first.

### Dice math (worth memorising)

- Base: **4+ = hit** → 70% per die. Crit on natural **9-10** → 20%.
- **+1 Accuracy** → hit on 3+ → 80%. **−1** → 5+ → 60%. **−2** → 6+ → 50%.
- Accuracy modifiers don't touch natural 1 (always miss), 9, or 10 (always crit).
- Expected damage per Strength point = **0.7**. Strength 3 ≈ 2.1 damage; Strength 5 ≈ 3.5.
- Crits succeed **regardless of Accuracy modifiers**.

### Accuracy modifiers cheat-sheet

| Situation | Mod |
|---|---|
| Target at **lower** elevation | **+1** |
| Target at **higher** elevation | **−1** |
| Target in water / attacker in water | −1 each (−2 if both) |
| Target in debris / attacker in debris | −1 each (−2 if both) |
| Minovsky Particles, non-adjacent target | −2 (not cumulative) |

### Damage, Shields, crits

- **Each active Shield cancels 1 damage**, then flips face-down (deactivated). Reactivates at the start of that unit's next activation.
- Shields apply **last** — damage reduction effects resolve before Shields.
- **Crit effects apply even if Shields absorb all the damage.** That's the one people miss.
- Crit effects are once per attack unless stated otherwise.

## 6. Positioning rules that actually bite

**Engagement** (same elevation, adjacent to enemy unit or Garrison):
- −1 hex to all movement started while Engaged.
- You **must target at least one Engaged enemy** when you attack — no sniping past the unit in your face. (AoE is fine if it includes them.)

**Elevation:**
- Moving up costs **+1 movement per level**. Ground→2 = 3 movement.
- Moving down is free.
- If you start a move on elevated terrain you **Jump**: your starting elevation holds for the move, so you can cross gaps and shoot over low enemies. Can't jump at ground level.

**Line of Sight** (needed for range 2+; adjacent needs none):
- Blocked by terrain **higher than both** units.
- Blocked by enemies / enemy structures at **the same elevation as both**.
- Different elevations: blocked by terrain or enemies at the elevation of **whichever unit is higher**.
- Line passes exactly between two hexes → acting player picks.
- Allies, Garrisons, and **allied** structures never block. AoE attacks ignore units when drawing LOS.

**Terrain:** water −1 hex to movement started in it; impassable blocks movement entirely (unless Hover); debris like water.

## 7. Scoring

| Source | VP |
|---|---|
| Defeat an enemy unit | that unit's VP value (on card) |
| Defeat an enemy Garrison | 2 |
| Rescue an allied Garrison | 2 |
| End of each Phase | per Objective controlled + scenario goals |

Defeated unit: owner's VP on kill, unit goes to Reserve, **Timeline token +2 as a repair penalty**, HP reset, Energy/Upgrades kept. Redeploys next activation. If it dies during its own activation, the activation ends immediately.

**Objectives:** a unit **ending its activation** on/adjacent contests it. More of your units than theirs → you win the contest. Neutral → you take it. **Enemy-held → it returns to neutral** (you don't flip it to yourself). Control persists until someone else wins a contest. Units moved by card effects can't contest.

**Tie-break: the last player to act wins.**

## 8. Squad & deck building

- Squad size set by scenario: usually **3 or 5**.
- No duplicate unit card numbers — **unless Mass Produced** (then unlimited, but every copy must be distinguishable, including Timeline tokens).
- Tactics deck = **exactly 9 cards**, **max 1 copy** of each.
- **Signature cards** require the unit with the matching title in your squad (name alone isn't enough).
- **Faction-trait cards** require ≥1 unit with that trait.
- Draw 3 at start, 3 at end of Phase 1 → 3 left. Deck empty = no more draws.
- Beyond 2 Phases: +3 cards per extra Phase (3 phases = 12 cards).

## 9. The three rules most often misplayed

1. **TL is paid before the action resolves.** You can't decide after seeing the roll. Committing to a 4-TL whiff still costs 4 rounds.
2. **Winning a contest against a held Objective only neutralises it.** It does not become yours. You have to contest it again later.
3. **Crit effects land through Shields.** A shielded 1-HP unit can still eat the crit's status effect / Push / extra damage even though the damage was cancelled.

## 10. First-game traps

- **Attack from where you'll be next round, not where you are now.** A 3-4 TL attack means your unit is out for the rest of that Phase stretch. If it can't threaten anything when it comes back, the attack was probably wrong.
- **Energize feels cheap and isn't.** 2 TL for 1 Energy — that's the same price as a Dash. Only worth it if an ability is genuinely better than a shot.
- **Rescue is the best VP-per-TL in the base rules** (2 TL → 2 VP). If a Garrison is near, that's usually the boring correct play.
- **Getting Engaged locks your shooting.** Everyone assumes they can shoot past the Zaku in their face. You can't.
- **Elevation is a double-edged +1/−1.** Being high hurts you when enemies attack from below. Being low hurts you when you shoot up.
- **The defeat penalty (+2 TL) is small compared to an attack's own cost.** Trading a kill for a 3-TL whiff is usually good; killing with a 4-TL weapon while leaving the board is often not.
- **You only get 3 Tactics cards for the back half.** Don't burn all three in Phase 1.

## 11. Gaps (what's left)

- **Scenario goal cards** — the Starter Set runs **Sleeping Leviathan**, and its objective/goal text is printed on scenario components I don't have. Without it we can't score Phase-end objectives properly. One photo of the scenario card/leaflet closes this.
- **Map** — board size and the Sleeping Leviathan terrain layout, Base positions, Garrison/Objective/Energy placements.
- **Phase-2 token reset** — still genuinely unstated. Working assumption: tokens carry over, track restarts at round 1.

Resolved since the first draft: **Advance = 0 TL** (designer video), **all 6 unit ability texts** (your card photos), **terrain elevation convention** (light = lvl 1, dark = lvl 2), **Attack cards replace your attack, Command cards stack on your turn, Response cards fire any time** (designer video + rulebook).

Unit stats, weapons, every ability, and all 18 Tactics cards: **`GUNDAM-ASSEMBLE-cards.md`**.

---

## 12. Reading the Starter roster (my read, not rules)

**Expected damage per attack = Strength × 0.7** (before accuracy mods). So a Str 7 weapon averages 4.9 damage; most Starter units die in **three good hits**.

| Unit | TL | HP | VP | Best weapon | What it is |
|---|---|---|---|---|---|
| **Vidar** | **1** | 13 | 7 | Burst Saber 4/1/**8** = ~5.6 | Acts first every phase, two **free** Command abilities, cheapest VP on the board. Handguns crit → **repeat the attack at TL 0**. |
| **Gundam** | 2 | 15 | 8 | Beam Saber 3/1/**6** = 4.2 | Strips Shield Upgrades on hit. Frenzied Charge pays you to Rescue. |
| **Char's Zaku II** | 2 | 12 | 7 | Bazooka 4/4/**7** = 4.9 | Range 4 hole-puncher that **Dash-escapes at TL 0 after shooting**. Heat Hawk is the cheap option. |
| **Barbatos** | 2 | **17** | **10** | Tail Blade 4/2/7 = 4.9 | The mountain — and **gets stronger as it takes damage** (+1 Str at 6, +2 at 12). |
| **Wing Zero** | 3 | 12 | 9 | Twin Buster 4/**SP**/6 | **Zero System: crits on 7–8** → 40% per die, and crits add **+1 damage each (max +4)**. ~6.6 damage a shot. Fragile. |
| **Epyon** | 3 | 15 | 9 | Beam Sword 3/1/**7** = 4.9 | Hover ignores terrain costs; **Exploit Weakness is +2 Str vs. anything with a status effect** — and it applies Slow/Disarm itself. |

**Four things that fall out of the numbers:**

1. **Vidar is the best unit in the box** on rate: TL 1 means it activates earliest and often, its Commands are free, and it only gifts 7 VP when it dies. Kill it early.
2. **Barbatos is a trap in both directions.** Chewing 17 HP costs you 4-TL attacks, but ignoring it means 4.9 damage a turn — and **chipping it to half HP is the worst of both** because Fight to the End turns it up. Either commit to killing it or don't touch it.
3. **Wing Zero is the kill target.** 12 HP, 9 VP, and the scariest weapon in the set. Kill it before it fires twice.
4. **Free extra attacks decide games.** T10 (Zaku Dash + Heat Hawk at TL 0), T03 (Barbatos survives at 1 HP then swings at TL 0 + Move 2), Annihilate (Claws after Tail Blade at TL 0), and Vidar's Handguns repeat are all timeline-free damage. Everything else in the box costs you turns; these don't.

---

## Appendix A — how we'll play this over text (Versus protocol)

This game is turn-based on a hex grid, so a text match works properly. Rules of engagement:

**Board notation.** Rows lettered A–H, columns 1–12 (or whatever your board actually is), plus elevation in brackets and terrain tags:

```
D5 [0]        empty ground
C4 [1] water  elevation 1, water hex
E6 [0] debris · Base(A)
A3 [2] terrain
```

**State block every round:**

```
[SIM] Gundam Assemble v1.0 · Starter 3v3 · <mode> · Phase 1 · Round 4 · You to act
VP  You 0 / Ace 0        Deck You 6 / Ace 6     Tactics in hand: You 3 / Ace 3
Timeline
 1: —            2: —            3: —            4: You Char's Zaku II
 5: —            6: Ace Gundam   7: —            8: —            9: —            10: —
Board
  You: Gundam B4[0] 15/15 · Wing Zero C5[1] 12/12 · Char's Zaku II D6[0] 12/12
  Ace: Gundam C8[0] 15/15 · Epyon D9[0] 15/15 · Barbatos C9[0] 17/17
Known: Ace holds 3 Tactics, 0 Energy, no Upgrades
Hidden: your hand, Ace's hand (declared, not peeked)
Last: —
Now: <your activation or Ace's activation>
```

**Honesty rules I hold myself to:**
- Dice rolled in the shell (`d10s: 7, 3, 9`), not narrated. Bad rolls stand.
- Hands stay hidden — you tell me what you play, I tell you what I play, and of that only what's legally public.
- No retconning state. If I misplay a rule, I say so and we rewind explicitly.
- I don't play your side unless you ask.

**Modes:** **Sparring** (I play to win and explain after) · **Coach** (I warn you before a bad action) · **Referee** (rules calls only, no take-backs) · **Dry run** (decision-tree: "if you attack, here's the branch").

**What I need to start a match:** the **Sleeping Leviathan scenario card** and the **board layout**. Everything else — rules, all 6 units, all 18 Tactics cards — I have.
