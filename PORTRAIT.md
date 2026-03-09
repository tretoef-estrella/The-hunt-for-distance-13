# Portrait of the Diamond

*What we know about [22,6,13]₄ — if it exists.*

---

## The Diamond

A **[22,6,13]₄ code** — if it exists — is a 6-dimensional subspace of GF(4)²² where every nonzero vector has Hamming weight at least 13. It would close a problem open since 2001. We call it the diamond.

After 1.5 billion evaluations, six obstruction theorems, and two independent world records, here is what the diamond must look like.

---

## Necessary Conditions (All Proven)

| Property | Value | Source |
|----------|-------|--------|
| A₁₂ | **= 0** | Theorem D — discrete jump required |
| B₄ | **= 0** | Theorem D Corollary — all dual obstacles eliminated |
| Automorphism group | **Trivial** | Theorem F — structural isolation |
| Mean codeword weight | **16.504029...** | MacWilliams identities, B₁=0 |
| Griesmer bound | **Satisfied** (g₄(6,13)=21 < 22) | Griesmer 1960 |
| Delsarte LP bound | **Not excluded** (A₄(22,13) ≤ 21,743) | Delsarte 1973 |

---

## What It Cannot Be (All Proven)

| Excluded family | Reason |
|----------------|--------|
| Punctured from [23,6,13]₄ | Theorem A — weight-13 rank barrier |
| Double-punctured from [24,7,13]₄ | Theorem B — all 276 pairs yield d≤11 |
| Extended from [21,5,13]₄ | Theorem C — structurally irreducible |
| Cyclic | Exhaustive verification |
| Quasi-cyclic | Theorem T2 — all 552 shortenings yield d≤12 |
| Greedy column construction | Theorem E — collapses at column 15 universally |
| Symmetric perturbation of A₁₂=33 | Theorem F — geometric isolation |

**Every known construction family has been eliminated.**

---

## The Distance to the Diamond

Two independent measurements from two directions:

**Primal distance:** A₁₂ = 33 → 0 requires eliminating 11 projective directions from PG(5,4). Current record: 11 remain.

**Dual distance:** B₄ = 24 → 0 requires eliminating 8 Z₃-orbits of weight-4 dual words. Current co-record: 8 remain.

Both cascades are governed by Theorem D and its corollary: every step must be divisible by 3. Both have been confirmed at every step.
```
Primal cascade:  78 → 42 → 39 → 36 → [33] → 30 → ... → 0
Dual cascade:         36 → 33 → 30 → [24] → 21 → ... → 0
                                              ↑
                                         active frontier
```

---

## The Conjecture

> **Conjecture (Proyecto Estrella, 2026).** The diamond does not exist. d₄(22,6) = 12.

P(non-existence) ≈ 80–90% based on dual-spectrum evidence, March 2026.

But the conjecture is not a theorem. The diamond has not been found. It has not been ruled out. The hunt continues.

---

## If It Appears

If a [22,6,13]₄ code is found during this campaign, it will be saved immediately as:
```
DIAMOND_d13_[timestamp].txt
```

with the header:
```
THE AMICHIS CODE
[22,6,13]_4 — EXISTENCE CONFIRMED
```

The generator matrix, weight enumerator, and full verification will be published without delay.

---

*"Puentes, no muros. Es una orden conseguirlo."*

**Proyecto Estrella · Madrid, 2026 · tretoef@gmail.com**
