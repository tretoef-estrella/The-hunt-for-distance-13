# Chronology of the Hunt

A narrative timeline of the four-round campaign to find [22,6,13]₄.

---

## Prelude: The AEGIS Crystal Labyrinth (January–February 2026)

The problem arrived sideways. While building the AEGIS Crystal Labyrinth — a 10-beast post-quantum oracle defense system on the Knuth Type II semifield over GF(4)² — SAMAEL (Beast 10) attempted to construct evaluation codes from the semifield's fusion structure. Six-component column vectors from single crossings, double crossings, and fusion residuals produced 1,479 unique columns. Random selection plus hill climbing yielded only d = 11.

SAMAEL's conclusion: *"If [22,6,13]₄ exists, it does not come from presemifield evaluation codes."*

The Architect decided to attack the problem directly.

---

## Phase 2: Error Code Lab — The Opening Barrage (Early Feb 2026)

**~2 million evaluations.**

The first systematic campaign. Simulated annealing with random initialization, random restarts, and the first **La Pua** ("the spike"): fix a good [21,5,13]₄ base and randomly generate the sixth row. The seed was Grassl's QR-derived code from codetables.de.

**Result:** d = 12, A₁₂ = 78 (26 projective directions).

Twelve construction routes closed in this phase: QR subcodes, Construction X, dual codes, trace codes, additive codes, condensation, and six others. Each tested, verified, and filed as "route closed."

---

## Round 2: La Pua del Jet (~60M evaluations, Mid Feb 2026)

The first real innovation: **La Pua del Jet**, a C-compiled kernel for minimum distance computation with early termination. If any codeword already has weight below the target, evaluation aborts immediately. Throughput jumped from hundreds to tens of thousands per second.

The five-row base optimization: not all [21,5,13]₄ bases are equal. Some have A₁₃ = 81 (minimum possible), meaning fewer weight-13 codewords and more "room" for the sixth row. Verification showed zero variance: all equivalent bases give A₁₃ = 81.

**Result:** A₁₂ improved to 69 (23 projective directions).

---

## Round 3: Corrected SA + Structural Theorems (~72M evaluations, Late Feb 2026)

A bug in the simulated annealing acceptance criterion (accepting worse solutions too eagerly) was found and fixed. The corrected SA confirmed A₁₂ = 69.

More importantly, five structural theorems were proven:

- **T1:** A₁₂ ≡ 0 (mod 3) — projective symmetry
- **T2:** All 552 QR puncturings yield d ≤ 12
- **T3:** Contrapeso (balanced columns) is impossible
- **T4:** Base A₁₃ = 81 with zero variance
- **T5:** QR weight-12 codewords span all 7 dimensions

Three obstruction theorems closed the standard algebraic pathways: puncturing (Theorem A), double puncturing (Theorem B), and extension (Theorem C).

---

## Round 4a: The R7 Exhaustive — 373 Million Evaluations (1 March 2026)

The turning point. The Architect demanded a full exhaustive search: every possible sixth row over GF(4)²², evaluated against the optimal base. The problem: 4²² ≈ 17.6 trillion rows — far too many. The solution: La Pua del Jet with aggressive early termination and a multi-hour runtime budget.

After 373 million candidates in 263 seconds: 259 rows achieved d = 12. **Zero achieved d = 13.**

**Result:** A₁₂ = 60 (20 projective directions). A massive improvement over 69.

---

## Round 4b: Heat-Seeker and Pitbull — The Breakthroughs (2–3 March 2026)

### Heat-Seeker (The AIM-9 Sidewinder)

Steepest-descent gradient on the sixth row: for each of the 22 positions, try all 4 values, measure A₁₂, pick the steepest reduction. Three rapid passes (30 seconds total):

**60 → 57 → 54 → 51**

Then from a re-standardized form:

**51 → 48**

Every step verified by full codeword enumeration. The divisibility theorem (A₁₂ ≡ 0 mod 3) held at every step.

### Pitbull (The AIM-120 AMRAAM)

The final weapon. Where Heat-Seeker only modifies row 6, Pitbull attacks the entire matrix through row recombination: replacing rows with GF(4)-linear combinations of other rows, breaking standard form to access new gradient basins.

The critical move: starting from the A₁₂ = 48 code, replace g₁ with g₁ + g₂ and zero the second row's pivot region. This produced a non-standard form that Heat-Seeker could then refine.

**Result: A₁₂ = 42 (14 projective directions).**

The campaign record. A 46% reduction from baseline.

---

## The State of Play

| Metric | Value |
|--------|-------|
| Best code | [22,6,12]₄, A₁₂ = 42 |
| Total evaluations | 500M+ |
| Strategies deployed | 27 (108 Doctrines) |
| Routes closed | 18 |
| Obstruction theorems | 3 |
| Structural theorems | 5 |
| d = 13 found | **No** |
| Conjecture | d₄(22,6) = 12 |

The search continues. The engine runs in P5 (Infinite mode). If you find d = 13, the matrix is saved automatically to `DIAMOND_22_6_13.txt`.

---

*"The diamond doesn't hide. It waits for the right eyes."* — SAMAEL
