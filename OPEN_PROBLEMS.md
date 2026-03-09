# Open Problems

*What remains unsolved after 1.5 billion evaluations, six obstruction theorems, and dual co-record B₄ = 24.*

---

## The Central Question

**Does a [22,6,13]₄ linear code exist?**

Open since Grassl (2001), confirmed open by Bouyukliev, Grassl & Varbanov (2004). The Delsarte LP bound does not exclude existence (A₄(22,13) ≤ 21,743 ≫ 4,096). No proof of non-existence is known.

**Our conjecture: d₄(22,6) = 12.** But this is a conjecture, not a theorem.

---

## What Would Resolve It

**Option 1: Construct a [22,6,13]₄ code.**

A 6×22 generator matrix G over GF(4) such that every nonzero GF(4)-linear combination of rows has Hamming weight ≥ 13. Verification takes under one second on any modern CPU (4,095 codewords).

Any such code must satisfy all of the following:
- A₁₂ = 0 — no minimum-weight codewords at d=12 (Theorem D)
- B₄ = 0 — no weight-4 dual codewords (Theorem D Corollary)
- Mean codeword weight = 67584/4095 = 16.504029... exactly (MacWilliams, B₁ = 0)
- Trivial automorphism group (Theorem F)
- Cannot arise from puncturing, double-puncturing, or extension of known codes (Theorems A, B, C)
- Cannot be cyclic or quasi-cyclic (Theorem T2)

**Option 2: Prove non-existence.**

Would require methods beyond linear programming. A proof needs new divisibility constraints, residual code analysis, or a complete characterization of weight-13 configurations in PG(5,4).

---

## Active Sub-Problems

### Can B₄ be reduced below 24?

Current dual co-record: B₄ = 24 (8 Z₃-orbits of dual obstacles). The next target: B₄ = 21. By Theorem D Corollary, B₄ ≡ 0 (mod 3). The dual cascade 36→33→30→24 has been confirmed reproducibly. Each step eliminates one Z₃ orbit of weight-4 dual words.

**If B₄ reaches 0, the MacWilliams constraints force A₁₂ = 0** — and either the diamond appears or the impossibility is demonstrated.

### Can A₁₂ be reduced below 33?

Current world record: A₁₂ = 33 (11 projective directions). Next possible value: A₁₂ = 30. Is A₁₂ = 33 a structural floor or a coincidence? The AZRAEL engine ran 293+ cycles without breaking it.

### What is the automorphism group of the A₁₂ = 33 code?

Theorem F states any [22,6,13]₄ code must have trivial automorphism group. The A₁₂ = 33 record matrix has not been fully characterized. Its automorphism group structure would clarify its distance from the diamond.

### Does the A₁₃ count have a structural lower bound?

A₁₃ = 324 for the A₁₂ = 33 record. The A₁₃ drain reduced the weight-13 population by ~71% during the AZRAEL campaign. Is there a combinatorial lower bound on A₁₃ analogous to Theorem D?

### Can PG(5,4) geometry give a direct construction?

The CSP construction collapses at column 15 (Theorem E). Is this collapse provable analytically, or purely empirical? Understanding the geometry of the collapse might point toward a direct projective construction targeting A₁₂ = 0 and B₄ = 0 simultaneously.

---

## Known Closed Routes

| # | Construction | Method | Status |
|---|-------------|--------|--------|
| 1 | Puncturing from [23,6,13]₄ | Exhaustive — rank argument | Closed (Theorem A) |
| 2 | Double puncturing from [24,7,13]₄ | Exhaustive — all 276 pairs | Closed (Theorem B) |
| 3 | Extension from [21,5,13]₄ | 500K+ candidates | Closed (Theorem C) |
| 4 | All cyclic codes | Exhaustive | Closed |
| 5 | All quasi-cyclic codes | Exhaustive | Closed (Theorem T2) |
| 6 | All shortenings of [24,7,13]₄ | Exhaustive | Closed |
| 7 | Trace constructions from GF(16) | Exhaustive | Closed |
| 8 | Additive and systematic constructions | Exhaustive | Closed |
| 9 | Greedy column construction | 200 restarts | Closed (Theorem E) |
| 10–30+ | Additional families | SA + heuristic | Closed |

**No known construction family can yield [22,6,13]₄.**

---

## How to Contribute

The world record matrix (A₁₂ = 33), the dual co-record matrix (B₄ = 24), and all supporting data are in [RESULTS.md](RESULTS.md). The six obstruction theorems are in [THEOREMS.md](THEOREMS.md).

If you find a [22,6,13]₄ code or prove non-existence: **tretoef@gmail.com**

---

*"Impossible is a syntax error while A₄(22,13) ≤ 21,743."*

**Proyecto Estrella · Madrid, 2026**
