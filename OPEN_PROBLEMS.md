# Open Problems

*What remains unsolved after 1.2 billion evaluations and six obstruction theorems.*

---

## The Central Question

**Does a [22,6,13]₄ linear code exist?**

This is the problem d₄(22,6) = 12 or 13. It has been open since Grassl (2001) and was confirmed open by Bouyukliev, Grassl & Varbanov (2004). The Delsarte LP bound does not exclude existence (A₄(22,13) ≤ 21,743 ≫ 4,096). No proof of non-existence is known.

Our conjecture: **d₄(22,6) = 12**. But this is a conjecture, not a theorem.

---

## What Would Resolve It

**Option 1: Construct a [22,6,13]₄ code.**

This would be a 6×22 generator matrix G over GF(4) such that every nonzero GF(4)-linear combination of rows has Hamming weight ≥ 13. Verification takes under one second on any modern CPU (4095 codewords to check).

Necessary conditions any such code must satisfy:
- All 4095 nonzero codewords have weight ≥ 13
- Mean codeword weight = 67584/4095 = 16.504029... exactly (from MacWilliams identities with B₁ = 0)
- The code must be asymmetric: no non-trivial automorphism group (Theorem F)
- The code cannot arise from puncturing, double puncturing, or extension of known codes (Theorems A, B, C)
- The code cannot be cyclic or quasi-cyclic (Theorem T2 + exhaustive verification)

**Option 2: Prove non-existence.**

This would require methods beyond linear programming. The Delsarte LP bound allows the code. A proof would need new divisibility constraints, residual code analysis, or a complete characterization of weight-13 configurations in PG(5,4).

---

## Sub-Problems

### Can A₁₂ be reduced below 33?

The current world record is A₁₂ = 33 (11 projective directions). By Theorem D, the next possible value is A₁₂ = 30 (10 directions). Can it be achieved? Is A₁₂ = 33 itself a structural floor, or a coincidence?

### What is the automorphism group of the A₁₂ = 33 code?

Theorem F states that any [22,6,13]₄ code must have trivial automorphism group. The A₁₂ = 33 record matrix has unknown automorphism group. Characterizing it would clarify how close (or far) the record is from the putative diamond.

### Does the A₁₃ count have a structural lower bound?

The A₁₃ count for the A₁₂ = 33 seed is 324. As A₁₂ decreases, does A₁₃ necessarily decrease? Is there a constraint analogous to Theorem D that bounds A₁₃ from below?

### Can PG(5,4) geometry give a direct construction?

The failed CSP construction (Theorem E) collapses at column 15 of the parity matrix. Is this collapse provable analytically, or merely empirical? Understanding the geometry of the collapse might point toward a direct projective construction.

---

## Known Closed Routes

The following construction families are provably unable to yield [22,6,13]₄:

1. Puncturing from [23,6,13]₄ — Theorem A
2. Double puncturing from [24,7,13]₄ — Theorem B
3. Extension from [21,5,13]₄ — Theorem C
4. All cyclic and quasi-cyclic codes — exhaustive verification
5. All shortenings of [24,7,13]₄ — Theorem T2
6. Trace constructions from GF(16) — exhaustive verification
7. Additive and systematic constructions — exhaustive verification
8. All greedy column constructions — Theorem E (CSP Collapse)

A [22,6,13]₄ code, if it exists, cannot be constructed by any of these 24+ known methods.

---

## How to Contribute

The world record matrix (A₁₂ = 33) and all supporting data are in [RESULTS.md](RESULTS.md). The six obstruction theorems are in [THEOREMS.md](THEOREMS.md).

If you find a [22,6,13]₄ code or prove non-existence, contact: **tretoef@gmail.com**

---

*"Impossible is a syntax error while A₄(22,13) ≤ 21,743."* — Napoléon Doctrine

**Proyecto Estrella · Madrid, 2026**
