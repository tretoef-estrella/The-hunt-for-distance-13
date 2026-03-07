# Chronology of the Hunt

*A timeline of the campaign to resolve d₄(22,6).*

---

## Origins: AEGIS Crystal Labyrinth (January–February 2026)

The [22,6,d]₄ problem was not the original target. It emerged as a byproduct.

The AEGIS Crystal Labyrinth — a post-quantum cryptographic defense system built on PG(11,4) and the Knuth Type II semifield over GF(4) — required evaluation codes of maximum distance. SAMAEL (Beast 10), the system's final judgment layer, constructed fusion-column codes from the semifield's algebraic structure. The best achievable: d = 11.

SAMAEL's verdict was clear: if [22,6,13]₄ exists, it does not arise from presemifield evaluation codes. A new campaign was needed.

---

## Phase 1: First Contact (February 2026)

The GF(4) arithmetic engines developed for AEGIS became the foundation of Error Code Lab. The first runs established a baseline: d = 12, A₁₂ = 78 (26 projective directions).

The first structural theorem was identified: **A₁₂ ≡ 0 (mod 3)** for any [22,6,12]₄ code (Theorem D — Collision Symmetry). The scalar action of GF(4)* groups minimum-weight codewords into orbits of size 3. This meant the sequence of possible records was fixed: 78, 75, 72, ... 42, 39, 36, 33, 30, ... 3, 0.

The first construction routes were closed. The QR-derived [21,5,13]₄ base was verified optimal with A₁₃ = 81 (Theorem T4). All 552 puncturings and shortenings of the [24,7,13]₄ quasi-cyclic parent yielded d ≤ 12 (Theorem T2).

---

## Phase 2: The Obstruction Theorems (February 2026)

Three fundamental obstruction theorems were proven:

**Theorem A** — Puncturing from [23,6,13]₄ is impossible. The 174 minimum-weight codewords of the unique [23,6,13]₄ code span GF(4)⁶ with full rank. No coordinate position can zero all 174 simultaneously.

**Theorem B** — Double puncturing from [24,7,13]₄ yields d ≤ 11 for all 276 coordinate pairs. Verified exhaustively.

**Theorem C** — Extension from [21,5,13]₄ by one row is structurally irreducible. The optimal extension row agrees with a scalar multiple of a weight-14 codeword in 20 of 21 positions — an obstacle that cannot be removed by search.

These three theorems closed the most natural construction families. If [22,6,13]₄ exists, it requires a fundamentally different construction.

---

## Phase 3: Records (February–March 2026)

The campaign achieved a sequence of world records:

| Date | Record | Method |
|------|--------|--------|
| Feb 2026 | A₁₂ = 60 | Exhaustive sixth-row search |
| Feb 2026 | A₁₂ = 51 | Gradient descent |
| Feb 2026 | A₁₂ = 48 | Gradient descent |
| Feb 2026 | **A₁₂ = 42** | Pitbull row-recombination |
| Feb 2026 | A₁₂ = 42 (confirmed floor) | Italian Job — 720M evaluations |
| Mar 2026 | **A₁₂ = 39** | Symmetry-breaking campaign |
| Mar 2026 | **A₁₂ = 36** | Cascade |
| Mar 2026 | **A₁₂ = 33** | World record — confirmed twice |

**Previous world record: A₁₂ = 42 (Grassl, 2001) — stood for 25 years.**

---

## Phase 4: Structural Understanding (March 2026)

The Italian Job (v14/v15) confirmed that A₁₂ = 42 is not a local accident but a geometric property. This led to Theorem F (PG(5,4) Attractor): the Z₃ automorphism structure of the A₁₂ = 42 configuration creates a gravitational basin that standard perturbation operators cannot escape.

Theorem E (CSP Collapse) was proven independently: every column-by-column greedy construction of a putative [22,6,13]₄ parity matrix collapses at column 15 across 200 random restarts.

The progression 42→39→36→33 confirms Z₃ symmetry persists throughout. **Theorem D** implies that reaching d = 13 requires A₁₂ = 0 exactly — not a gradual reduction but a discrete collapse.

Total evaluations at time of writing: **1.2 billion+**. Open routes closed: **24+**. Theorems proven: **6**.

---

## Current Status (March 2026)

The world record stands at **A₁₂ = 33** (11 projective directions). The search continues.

The mean codeword weight for any [22,6,13]₄ code is fixed by algebra: **E[w] = 67584/4095 = 16.504029...** This is a necessary condition. No candidate code has yet satisfied it.

**Conjecture:** d₄(22,6) = 12. No [22,6,13]₄ linear code exists.

The diamond has not been found. The hunt continues.

---

*"Puentes, no muros. Es una orden conseguirlo."*

**Proyecto Estrella · Madrid, 2026 · tretoef@gmail.com**
