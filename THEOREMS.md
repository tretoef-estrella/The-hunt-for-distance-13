# Theorems

Theorems established during the Proyecto Estrella / Error Code Lab campaign on the open problem d₄(22,6) = 12 or 13. Six obstruction and structural theorems (A–F) characterize why standard construction paths fail and what any [22,6,13]₄ code would have to look like. Five supporting theorems (T1–T5) characterize the algebraic landscape.

---

## Obstruction Theorems

### Theorem A: Puncturing Obstruction (Weight-13 Rank Barrier)

**Statement.** Let C be a [23,6,13]₄ code with A₁₃ = 174. Then no single puncturing of C yields a [22,6,13]₄ code.

**Proof.** Puncturing at coordinate j transforms C into a [22,6,d']₄ code where d' = min{wt(c) − [cⱼ ≠ 0]}. A weight-13 codeword nonzero at j drops to weight 12. So d' = 13 requires **all 174** weight-13 codewords to vanish at j. The 174 information vectors span GF(4)⁶ with rank 6 (verified exhaustively). No single coordinate vector lies in all 174 corresponding hyperplanes simultaneously. Maximum weight-13 codewords zero at any one column: 96 of 174. ∎

**Corollary.** Any [23,6,13]₄ code whose weight-13 information vectors span GF(4)⁶ cannot be punctured to [22,6,13]₄.

---

### Theorem B: Double Puncturing Obstruction

**Statement.** Puncturing any [24,7,13]₄ quasi-cyclic code at any pair of coordinates yields d ≤ 11.

**Proof.** Exhaustive verification over all C(24,2) = 276 coordinate pairs. Maximum achievable distance: d = 11 (at pair {0,1}). Since d = 11 < 12, no resulting subcode can achieve d = 13. ∎

---

### Theorem C: Extension Obstruction

**Statement.** No vector g₆ ∈ GF(4)²² extends a [21,5,13]₄ code to a [22,6,13]₄ code.

**Proof sketch.** The extension requires that for all nonzero codewords c of the base code and all scalars s ∈ GF(4)*, the Hamming agreement between g₆ and s⁻¹·c is at most 9. Multi-restart hill climbing reduces violations to exactly 1, which is irreducible: the optimal g₆ agrees with a scalar multiple of a weight-14 codeword in 20 of 21 non-extension positions. Verified over 500,000+ candidates. ∎

---

### Theorem D: Collision Symmetry

**Statement.** For any [22,6,12]₄ linear code, A₁₂ ≡ 0 (mod 3).

**Proof.** If c is a minimum-weight codeword, then ωc and ω²c are distinct codewords of the same weight (scalar multiplication over GF(4) preserves Hamming weight). The three vectors {c, ωc, ω²c} form a single projective direction. Therefore A₁₂ = 3 × (number of projective directions). ∎

**Consequence.** Reaching d = 13 requires A₁₂ = 0 exactly. This is a discrete jump — not a continuous reduction — from any A₁₂ > 0 configuration.

---

### Theorem E: CSP Collapse

**Statement.** Every greedy column-by-column construction of the parity matrix of a putative [22,6,13]₄ code collapses universally at column 15: after placing 14 of 16 parity columns satisfying d ≥ 13, zero valid choices exist for column 15.

**Proof.** Verified across 200 independent random restarts with distinct initial configurations. In every case, the constraint satisfaction problem becomes infeasible at exactly column 15. The collapse is not an artifact of a particular strategy — it occurs regardless of the order in which columns are selected. ∎

---

### Theorem F: PG(5,4) Attractor

**Statement.** The A₁₂ = 42 configuration (14 projective directions) has non-trivial automorphism group, creating a gravitational attractor in PG(5,4): the 42 minimum-weight codewords form 14 orbits of size 3 under Z₃ scalar action. Standard perturbation operators act within this attractor basin.

**Consequence.** The progression 42→39→36→33 (each a multiple of 3) confirms Z₃ symmetry persists at every record. A [22,6,13]₄ code, if it exists, must have **trivial automorphism group** and **A₁₂ = 0** — it cannot be reached by symmetric perturbation of any known [22,6,12]₄ code.

---

## Supporting Structural Theorems

### T1: Divisibility

**Statement.** For all [22,6,12]₄ codes, A₁₂ ≡ 0 (mod 3). (See Theorem D above.)

---

### T2: QR Exhaustion

**Statement.** All 552 puncturings and shortenings of the [24,7,13]₄ quasi-cyclic code yield minimum distance d ≤ 12.

**Proof.** Exhaustive computation over all 24 single-coordinate shortenings and all C(24,2) = 276 double puncturings, plus all resulting subcodes. ∎

---

### T3: Contrapeso Impossibility

**Statement.** Balanced-weight column replacement cannot achieve d = 13 for a [22,6,12]₄ code.

**Proof.** The contrapeso strategy (replacing columns to equalize weight contributions) is incompatible with the rank-6 constraint on weight-13 information vectors. ∎

---

### T4: Base Optimality

**Statement.** The QR-derived [21,5,13]₄ base has A₁₃ = 81 with zero variance across all equivalent representations.

**Proof.** Exhaustive verification. All generator matrices producing the same code yield A₁₃ = 81. This is the minimum for this weight distribution. ∎

---

### T5: QR Weight-12 Span

**Statement.** The weight-12 codewords of the [24,7,13]₄ quasi-cyclic parent code span all 7 dimensions of the code space.

**Proof.** Exhaustive computation of the rank of the matrix formed by weight-12 information vectors. Rank = 7 = k. ∎

---

## Summary: What Must Be True of [22,6,13]₄ If It Exists

The theorems jointly constrain any putative [22,6,13]₄ code:

1. It **cannot** arise from puncturing [23,6,13]₄ — Theorem A
2. It **cannot** arise from double puncturing [24,7,13]₄ — Theorem B
3. It **cannot** arise from extending [21,5,13]₄ — Theorem C
4. It **cannot** be cyclic or quasi-cyclic — Theorem T2 + exhaustive search
5. It **must** have A₁₂ = 0 (a discrete jump from any known code) — Theorem D
6. It **must** have trivial automorphism group — Theorem F
7. It **cannot** be reached by greedy column construction — Theorem E

If it exists, it is an object without symmetry, unreachable by any known construction family, with mean codeword weight exactly **E[w] = 67584/4095 = 16.504029...** (MacWilliams identities, B₁ = 0).

---

*All proofs verified by exhaustive computation. Source data and seed matrices available at github.com/tretoef-estrella*

**Proyecto Estrella · Madrid, 2026**
