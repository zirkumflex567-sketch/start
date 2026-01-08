# WANDER / DRIFT — Living World Design Specification

## 1) Executive Summary
WANDER / DRIFT is a calm, living top‑down pixel world of endless open expanses where players simply **be**: walking, observing, and gently influencing pace and camera. There is no winning, no failure, and no pressure—only presence. The world is endless and collectively shaped over years through subtle community votes and shared milestones. A unique “Drift” system occasionally pulls the world backward in time, creating a poetic rhythm and a soft sense of mystery. Every walk is recorded; the **World Archive** website preserves this evolving history as a scrollable timeline and a proof of the world’s endlessness and co‑creation.

**Experience in one sentence:** A quiet ritual of walking through a living, endless pixel world—where the past can drift into view and the community gently nudges what comes next.

---

## 2) Full Feature List (Grouped by Systems)

### Movement & Camera
- Auto‑walk top‑down character
- Pace modulation: slow / normal / fast (soft comfort constraints)
- Camera pan within a soft radius; smooth snap‑back
- Input mapping for mobile and PC

### Drift (Signature System)
- Randomized drift events with subtle foreshadowing
- Multi‑phase drift flow: pre‑drift → onset → reverse → afterglow
- Player response tools: pace modulation + limited daily drift anchors
- Offline drift: poetic, non‑punitive backward progression

### World & Content
- Endless modular chunk/segment system
- Biomes with unique palettes, props, weather weights
- Weather & lighting layers (MVP vs later)
- Water/nature density systems and pixel‑appropriate animation

### Encounters
- Animals (companions, observers, rare herds)
- NPCs (silent, one‑liners, micro‑stories, optional micro‑quests)
- Environmental moments (auroras, fog walls, meteor trails)
- Rare treasures (verpassbar, non‑grindy, cosmetic/tokens/anchors)

### Familiarity & Lore
- Familiarity level per entity driven by sightings/observations
- Gradual text evolution from plain → recognition → lore fragments
- Some mysteries never resolve to maintain endless curiosity

### Social & Community
- Friends presence layer (gentle, not real‑time in MVP)
- Optional chat (off by default; safe, quiet, rate‑limited)
- Community votes and mood‑events (asynchronous)
- Collective milestones with commemorative rewards
- Player contribution pipeline (later)

### Cosmetics & Customization
- Large, long‑term cosmetic catalog (no gameplay advantage)
- Unlock sources: exploration, milestones, optional ads, later IAP
- Rarity system that is transparent and non‑predatory

### Monetization (Respectful)
- Optional “pause ads” framed as calm moments
- Cosmetic IAP only
- Supporter pack
- Optional cosmetic season/era pass (no FOMO)

### Web Archive (View‑Only)
- Scrollable, zoomable world timeline
- Segment detail panels (biome, weather, stats)
- Global dashboards and community memory highlights

---

## 3) Detailed System Specifications & Interactions

### 3.1 Movement & Camera
**Auto‑Walk:** The character always walks forward across the world at a gentle default pace (top‑down orientation), with the environment flowing past in all directions to emphasize endless breadth. The world presentation must **read clearly** so players intuit where the character came from and where they can go next: paths, river edges, road lines, and landmark alignment communicate directionality at a glance.

**Pace Control (Feel Goals):**
- **Slow:** a contemplative, softer step cadence; used to “linger.”
- **Normal:** default ritual pace.
- **Fast:** a brisk walk that still feels unhurried; not twitchy or competitive.
- **Soft constraints:** a subtle “comfort” model (not a hard bar). Repeated fast pacing nudges the player back to normal by gently easing speed rather than forcing a stop.

**Camera Pan:**
- Pan radius: ~20–35% of screen width/height.
- Camera snaps back smoothly when input ends (ease‑out).
- **Mobile:** drag to pan; optional pinch to nudge zoom later (not MVP).
- **PC:** mouse drag to pan; arrow keys or WASD optional.

**Readability & Realism in Top‑Down View (Non‑Negotiable):**
- **Grounded traversal surfaces:** always include a readable walkable surface (path, boardwalk, shoreline, bridge, or meadow trail) that visibly connects foreground to mid‑distance.
- **Directional composition:** use perspective cues (path taper, aligned props, shoreline flow, fence lines) so the player can infer **origin** and **destination**.
- **Landmark gating:** place distant silhouettes (tower, arch, light, grove) that act as “next‑step” magnets without turning into waypoints.
- **Occlusion hygiene:** avoid overly dense foreground that hides the path; foliage frames the route rather than blocking it.
- **Camera framing:** keep the character slightly lower than center so the “ahead” space is always visible; keep backward space readable but quieter.

**Why Look‑Ahead Matters (without competition):**
- Looking ahead reveals **non‑exclusive** moment hints (e.g., distant lanterns or a silhouette) that invite curiosity.
- Any “advantage” is aesthetic only; treasures and encounters can also appear behind or near the player, preventing a “rush to the front” mindset.

### 3.2 Drift System (Key Identity)
**Emotional Intention:** A soft, poetic sense of time folding—not danger. Drift makes the world feel alive and cyclical.

**What Drift Is NOT:**
- Not a punishment
- Not a timer
- Not a fail state

**Drift Randomness (Triggering Logic – Design Intent):**
- **Unpredictable intervals** weighted by play duration, biome mood, and recent pace choices.
- **Intensity distribution:** mild drifts common; intense drifts rare and memorable.

**Foreshadowing (Visual Only in MVP):**
- Particles drifting backward
- Subtle palette shimmer
- Wind direction mismatch
- Shadow/parallax “wrongness”

**Drift Phases:**
1) **Pre‑Drift (15–60s):** subtle cues only
2) **Onset (3–8s):** world hesitates, a soft visual “tension”
3) **Reverse (variable):** the world pulls backward; strength varies
4) **Afterglow (short):** palette shift, softened ambiance, calm reset

**Player Response Options:**
- **Pace modulation:** slowing reduces drift pull slightly; fast pacing can shorten duration but is not required.
- **Drift Anchors (limited daily):** items found rarely; they soften or delay drift but never disable it fully.

**Offline Drift:**
- If the player is away, their character drifts backward by a small amount.
- **No loss** of cosmetics or progress.
- Return messaging is poetic and non‑guilt: “The world took a slow breath while you were away.”
- **Soft cap:** offline drift never exceeds a reasonable distance (e.g., half a session).

### 3.3 World & Content Structure

#### A) Chunk / Segment Model
The world is generated as sequential **chunks**. Each chunk includes:
- Biome theme + palette
- Parallax background layers
- Mid/foreground props
- Ambient particles (fog, fireflies, rain)
- Optional water presence
- Encounter slots (0–2)
- Treasure slots (0–2)
- Landmark chance (rare)
- **Traversal spine:** a visible, continuous route element (path, shoreline, boardwalk, canyon floor, etc.) that links chunk‑to‑chunk.
- **Depth anchors:** mid‑distance landmarks to establish scale and a believable “next direction.”

**Beauty Through Variation:**
- Palette swaps across day/night or seasonal toggles
- Prop modularity and swapped silhouettes
- Layering (near/mid/far) to create depth
- Weather + mood overlays (e.g., rain + lanterns)

#### B) Biomes (Initial Set + Expansion Candidates)
Each biome lists **palette/mood**, **signature props/landmarks**, **weather weights**, **unique encounters**, and **drift feel**.

1) **Meadow Morning**
   - Palette: warm greens, soft gold
   - Props: wildflowers, windmills, stone fences
   - Weather: light breeze, light rain rare
   - Encounters: rabbits, field bard
   - Drift feel: soft sway, gentle pull

2) **Forest Rain**
   - Palette: deep greens, cool grays
   - Props: mossy trunks, puddles, hanging vines
   - Weather: frequent rain, fog
   - Encounters: foxes, umbrella‑bearing NPC
   - Drift feel: watery ripple effect

3) **Riverbank Dusk**
   - Palette: violet, indigo, warm orange highlights
   - Props: reed beds, small boats, lanterns
   - Weather: mist, light drizzle
   - Encounters: heron, fisher with one‑liner
   - Drift feel: reflective shimmer

4) **Mist Swamp**
   - Palette: gray‑green, muted cyan
   - Props: cypress roots, glowing fungi
   - Weather: fog heavy
   - Encounters: frog chorus, ghost‑lantern NPC
   - Drift feel: thick, slow pull

5) **Moonlit Ruins**
   - Palette: silver, deep blue, pale stone
   - Props: broken pillars, moon glyphs
   - Weather: clear nights, faint fog
   - Encounters: owl, silent historian NPC
   - Drift feel: starlight flicker

6) **Neon Night Market**
   - Palette: magenta, cyan, neon accents
   - Props: stalls, signs, hanging lights
   - Weather: rare drizzle, electric glow
   - Encounters: vendor NPC, stray cat
   - Drift feel: shimmering glitch‑pulse

7) **Winter Pines**
   - Palette: icy blues, white, pine green
   - Props: snowbanks, frosted branches
   - Weather: snow flurries
   - Encounters: deer herd, traveler with warm tea
   - Drift feel: muffled, quiet slow‑down

8) **Desert Bloom**
   - Palette: warm sands, pink blossoms
   - Props: cacti, oasis stones
   - Weather: heat shimmer
   - Encounters: lizard, wandering botanist
   - Drift feel: mirage‑like waves

9) **Glitch Fields**
   - Palette: shifting gradients, pixel noise
   - Props: broken grids, floating fragments
   - Weather: digital flicker
   - Encounters: “lost” NPC text fragments
   - Drift feel: jittery, pixel smear

10) **Canyon Echo**
    - Palette: rust red, deep shadow
    - Props: tall cliffs, rope bridges
    - Weather: wind gusts
    - Encounters: hawk, echoing singer NPC
    - Drift feel: echo‑snap reversal

11) **Old Highway Relics**
    - Palette: dusty gray, faded teal
    - Props: broken signs, overgrown cars
    - Weather: dry haze
    - Encounters: mechanic NPC, raccoon
    - Drift feel: nostalgic fade

12) **Lantern Village**
    - Palette: warm orange, gold, blue night
    - Props: lantern strings, small homes
    - Weather: calm nights
    - Encounters: child with lantern, storyteller
    - Drift feel: gentle lantern sway

13) **Crystal Cavern (Surface Cutaway)**
    - Palette: sapphire, teal, white crystal
    - Props: crystal growths, cavern cracks
    - Weather: internal glow
    - Encounters: crystal moths, silent miner
    - Drift feel: refractive glow pulse

14) **Storm Coast**
    - Palette: dark blue, gray, white spray
    - Props: cliffs, lighthouse silhouette
    - Weather: frequent storms
    - Encounters: seabird flocks, rain‑coat NPC
    - Drift feel: strong waves, dramatic pull

15) **Golden Autumn**
    - Palette: amber, red, brown
    - Props: leaf piles, wooden fences
    - Weather: crisp wind
    - Encounters: squirrel, leaf painter NPC
    - Drift feel: leaf swirl pull

16) **Ashen Afterlight**
    - Palette: charcoal, ember orange
    - Props: burnt stumps, faint glowing ash
    - Weather: ash fall
    - Encounters: ember spirit, old wanderer
    - Drift feel: slow, heavy pull

17) **Stargrass Plains**
    - Palette: deep navy, glowing green
    - Props: luminescent grasses, meteor stones
    - Weather: clear nights
    - Encounters: firefly swarms, astronomer NPC
    - Drift feel: star‑tide pulse

18) **Fog Harbor**
    - Palette: muted blue‑gray
    - Props: docks, bells, foghorn silhouette
    - Weather: dense fog
    - Encounters: dock worker, seal
    - Drift feel: slow‑rolling fog pull

19) **Glass Garden**
    - Palette: pastel, prismatic highlights
    - Props: glass flowers, reflective arches
    - Weather: soft shimmer
    - Encounters: hummingbird, garden keeper
    - Drift feel: refractive ripple

20) **Paper Grove**
    - Palette: sepia, warm white, ink black
    - Props: paper trees, ribbon leaves
    - Weather: light breeze
    - Encounters: origami crane, poet NPC
    - Drift feel: page‑turn sweep

#### C) Weather / Lighting (MVP vs Later)
**MVP:**
- Day/night blend
- Rain/fog overlays
- Simple glow for lanterns
- Animated water tiles

**Later:**
- Thunder flashes
- Wind layers with parallax leaves
- Volumetric‑style fog tricks
- Water shader/reflection tricks
- **Sound expansion later** (explicitly delayed)

#### D) Water / Nature
**Flowing Water in Pixel Style:**
- Tile animation with looping frames
- Parallax reflection layer
- Subtle ripple sprites
- Shoreline props (rocks, reeds, driftwood)

**Nature Density:**
- Grass/bush/tree variations
- Silhouette variations for background trees
- Density sets per biome and per weather state

### 3.4 Encounters

#### 1) Animals
- Brief companions that walk with the player for 10–60 seconds
- Rare herds (deer, birds) for quiet spectacle

#### 2) NPCs
- **Silent NPCs:** nod, wave, leave a small trace
- **One‑liners:** short poetic line, then move on
- **Micro‑story NPCs:** a few visit‑based lines
- **Optional micro‑quests:** non‑grindy, verpassbar (e.g., “bring a lantern seed”)

#### 3) Environmental Moments
- Aurora shimmer
- Meteor streak
- Sudden fog wall
- Lantern release
- Distant parade
- Broken radio transmission

#### 4) Rare Treasures
- Small, verpassbar pickups
- Contain cosmetics, tokens, anchors, memory fragments
- Not grindable; meant to feel like a lucky moment

### 3.5 Familiarity & Lore Through Presence
- Every entity has a **familiarity level** tied to sightings and observations.
- Text evolves:
  - **First:** plain description
  - **Later:** recognition line
  - **Later:** small lore fragment
- Some entities never resolve; mystery sustains endless curiosity.

### 3.6 Social & Community Systems

#### A) Friends
- Add friends; see them as **Nearby Walkers** (non‑real‑time in MVP)
- Friends can leave subtle traces (“X was here in the rain.”)
- No ranking or comparison UI

#### B) Chat (Optional, Safe)
- Off by default; can be disabled permanently
- MVP: Nearby Walkers + Campfire chat only
- Messages fade; rate‑limited
- No DMs in MVP
- Moderation principles: profanity filters, report, mute, shadow‑mute, small curated phrase prompts

#### C) Community Votes / Events
- Asynchronous, low‑friction votes
- Example prompts:
  - “Next biome: **Lantern Village** vs **Glass Garden**?”
  - “Week mood: **Long Rain** vs **Clear Skies**?”
  - “Encounter pack: **Forest Spirits** vs **Market Performers**?”
- Events operate in 12–24 hour windows (no synchronous pressure)

#### D) Collective Milestones
- Shared stats tracked (not in‑game leaderboards):
  - Total distance walked
  - Total time spent
  - Total drifts endured
  - Unique encounters discovered
- Milestone rewards:
  - Commemorative cosmetics
  - Titles (non‑competitive)
  - Memory tokens
- Retroactive rewards to late joiners

#### E) Player Contribution & Immortalization (Later)
Pipeline:
1) Submit art/props
2) Curated shortlist
3) Community vote
4) Integration into world chunks
5) Credit in archive
6) Permanent historical record

### 3.7 Cosmetics & Customization
**Slots:** hats, masks, outfits, shoes, capes, backpacks, trails, ambient FX, subtle auras.

**Unlock Sources:**
- Exploration finds
- Community milestones
- Optional calm “pause ads”
- Later: cosmetic IAP

**Rarity System (Non‑predatory):**
- Common / Uncommon / Rare / Mythic
- Transparent drop rates
- No aggressive gacha mechanics

### 3.8 Monetization
- Optional “pause ads” as calm vignettes (rain, fire, wind)
- Cosmetic‑only IAP
- Supporter pack (“Keep the world alive”)
- Optional “era pass” with **no expiration**; content remains viewable forever

### 3.9 Web Archive (View‑Only)
**Core Features:**
- Horizontally scrollable timeline of recorded segments
- Zoom out for eras, zoom in for moments
- Segment detail panel showing:
  - Biome, weather, time‑of‑day
  - Interaction stats (visits, observations)
  - Milestone markers and voted additions

**Community Memory:**
- Global dashboards (totals, drift counts, milestones)
- Highlight sections for rare events and community contributions

**Edge of the World Metaphor:**
- Farthest active player defines current “edge.”
- Archive shows fogged‑out space beyond the edge, hinting unknown.

---

## 4) Starter Content Bible

### 4.1 Biomes (12–20) — See Section 3.3B
(20 initial and expansion ideas listed above.)

### 4.2 Encounter Concepts (30+)
**Animals**
1) Rabbit pair
2) Deer herd
3) Owl sentinel
4) Fox companion
5) Heron by water
6) Cat from market
7) Seal by dock
8) Lizard on sun rock
9) Firefly swarm
10) Hummingbird in garden
11) Squirrel with nut
12) Crane in paper grove

**NPCs (Silent / One‑liners / Micro‑stories)**
13) Umbrella wanderer: “Rain makes the world soft.”
14) Old historian (silent)
15) Lantern child: “The light remembers.”
16) Market vendor: “Trade for a tale?”
17) Botanist: “This bloom waits years.”
18) Dock worker: “Fog keeps our secrets.”
19) Poet: “Pages rustle when you pass.”
20) Mechanic: “This road had a story once.”
21) Astronomer: “Stars drift too.”
22) Ember spirit: whispers only
23) River fisher: “The water returns everything.”
24) Storyteller with 3‑line arc

**Environmental Moments**
25) Aurora curtain
26) Meteor shower
27) Sudden fog wall
28) Lantern release
29) Broken radio voice
30) Distant parade silhouette
31) Wildflower bloom burst
32) Glitch ripple across horizon
33) Cliff echo chorus
34) Shoreline wave surge

**Treasures / Rare Finds**
35) Drift anchor charm
36) Memory fragment shard
37) Weathered scarf cosmetic
38) Lantern seed item
39) Glass bead charm
40) Hand‑stitched patch

### 4.3 Cosmetics (50+ Ideas)
**Hats / Headwear**
1) Straw hat
2) Rain hood
3) Lantern cap
4) Fox‑ear hood
5) Paper crown
6) Snow beanie
7) Stargazer hood
8) Desert turban

**Masks / Face**
9) Half‑moon mask
10) Glass visor
11) Ember mask
12) Leaf veil

**Outfits**
13) Meadow tunic
14) Market robe
15) Raincoat
16) Winter parka
17) River fisherman outfit
18) Canyon wanderer set
19) Crystal miner suit
20) Lantern festival kimono

**Shoes**
21) Trail sandals
22) Puddle boots
23) Snow treads
24) Desert wraps

**Capes / Outerwear**
25) Mist cloak
26) Star cloak
27) Ember shawl
28) Leaf cape

**Backpacks**
29) Canvas pack
30) Lantern carrier
31) Herbal satchel
32) Tool bag

**Trails / Ambient FX**
33) Firefly trail
34) Leaf swirl trail
35) Ember drift trail
36) Snow sparkle trail

**Auras / Subtle FX**
37) Soft glow aura
38) Lantern flicker aura
39) Rain halo
40) Prism shimmer

**Emotes / Poses (Later)**
41) Sit by fire
42) Quiet wave
43) Look to sky
44) Stretch walk

**Rare / Mythic**
45) Aurora mantle
46) Stormcoat shimmer
47) Crystal bloom aura
48) Neon market jacket
49) Paper grove halo
50) Fog harbor bell cape

---

## 5) Community Systems (Detailed)

### Votes / Events / Milestones / Achievements
- **Votes:** simple, infrequent, and skippable.
- **Events:** mood shifts rather than grind (e.g., “Long Rain Week”).
- **Milestones:** community totals unlock commemorative cosmetics and titles.
- **Achievements:** descriptive and commemorative only.

### Example Milestone Rewards
- “The First Million Steps” → commemorative scarf
- “Fifty Thousand Drifts” → drift‑tide cape
- “Lantern Era” → lantern aura

### Example Vote Questions
- “Next biome to add?”
- “Which seasonal mood should return this month?”
- “Which encounter pack should arrive next?”

---

## 6) Web Archive Spec (View‑Only)

### UI Sections
- **Timeline Strip:** scrollable, zoomable, horizontal
- **Segment Detail Panel:** biome, weather, time, encounter stats
- **Milestone Markers:** visual pins on timeline
- **Community Memory:** highlights of shared events
- **Global Dashboards:** total distance, total drifts, total encounters

### Interactions
- Scroll to move through history
- Zoom to view eras or specific moments
- Click segments to open detail panel

### Proof of Endlessness
- Timeline grows continuously
- Archive shows fog beyond the edge of the world

---

## 7) MVP Plan (2–3 Weeks) + Post‑MVP Roadmap

### MVP Scope
- Core auto‑walk + pace control
- Camera pan
- Chunk system with 2–3 biomes
- Drift system with subtle cues
- Basic encounters (animals + NPC one‑liners)
- Treasure pickups (verpassbar)
- Campfire mode (UI fade)
- Minimal social: optional chat toggle + global totals (quietly)
- Web archive MVP: last N segments, basic scroll + segment details + totals

### Post‑MVP Roadmap
**Stage 1:**
- More biomes and weather
- Expanded encounter types
- Familiarity system depth
- Friends presence layer

**Stage 2:**
- Community vote cycles
- Collective milestones
- Player contribution pipeline

**Stage 3:**
- Richer sound patch
- Optional real multiplayer walking (later)

---

## 8) Risks & Do‑Not‑Do List

**Risks:**
- Overloading with UI or stats in‑game
- Introducing competitive comparisons
- Making drift feel punitive
- Event design causing FOMO

**Do‑Not‑Do:**
- No in‑game leaderboards
- No timed exclusives that expire permanently
- No gameplay‑affecting monetization
- No loud or intrusive UI patterns

---

## 9) Content Strategy for Endless Variation
- **Palette swaps** for day/night and seasonal mood
- **Prop modularity** with swapped silhouettes
- **Layered parallax** for depth
- **Weather combos** (rain + lanterns + owl event)
- **Encounter pools** with biome‑specific weighting
- **Rare landmarks** as special moments

### Content Roadmap Cadence
- New biome additions every 4–6 weeks (initially small)
- Encounter packs every 2–3 weeks
- Mood events monthly
- Community votes aligned with each major content addition

### Preserving Old Eras
- Archive keeps all history accessible
- Old biomes continue to appear in weighted rotation
- “Era tags” in archive to explore past world states
