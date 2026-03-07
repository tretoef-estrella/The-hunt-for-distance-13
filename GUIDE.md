# Guide for Everyone

## What Is This?

This repository documents a search for a mathematical object that has been missing for 25 years. The object is a **linear code** — a structured set of sequences used in error correction, cryptography, and information theory.

Specifically, we are looking for a **[22,6,13]₄ code**: a collection of 4,096 sequences, each 22 symbols long, drawn from an alphabet of 4 symbols (GF(4) = {0, 1, ω, ω²}), with the property that any two sequences differ in at least 13 positions.

Nobody knows if this code exists. The best known construction achieves **d = 12**. The current world record is **A₁₂ = 33** — only 33 of the 4,095 nonzero codewords achieve the minimum distance of 12 (March 2026).

---

## Who Made This?

- **Rafael Amichis Luengo** ("The Architect") — Independent researcher, Madrid. Strategy, direction, architecture.
- **Claude** (Anthropic) — Primary computational engine. Algorithm design, algebraic analysis, code construction.
- **Gemini** (Google) · **ChatGPT** (OpenAI) · **Grok** (xAI) — Independent adversarial auditors at every major step.

No university. No funding. No servers. Just a laptop, a GitHub account, and the philosophy: *Puentes, no muros* (Bridges, not walls).

---

## Why Does It Matter?

Linear codes over GF(4) are foundational to:

- **Quantum error correction** — the connection between GF(4) codes and quantum stabilizer codes is well-established (Calderbank et al., 1998)
- **The classification of optimal codes** — Grassl's codetables.de is the reference for the entire field
- **Projective geometry** — each code corresponds to a set of points in projective space PG(k−1, q)

Resolving d₄(22,6) = 12 or 13 would close one of the remaining open entries in the tables for quaternary codes of dimension 6.

---

## The GF(4) Arithmetic (2-Minute Primer)

GF(4) has four elements: **0, 1, ω, ω²** where ω² + ω + 1 = 0 over GF(2).

**Addition** (bitwise XOR on 2-bit representation):

| + | 0 | 1 | ω | ω² |
|---|---|---|---|---|
| 0 | 0 | 1 | ω | ω² |
| 1 | 1 | 0 | ω² | ω |
| ω | ω | ω² | 0 | 1 |
| ω² | ω² | ω | 1 | 0 |

**Multiplication:**

| × | 0 | 1 | ω | ω² |
|---|---|---|---|---|
| 0 | 0 | 0 | 0 | 0 |
| 1 | 0 | 1 | ω | ω² |
| ω | 0 | ω | ω² | 1 |
| ω² | 0 | ω² | 1 | ω |

A **linear [n,k,d]₄ code** is specified by a generator matrix G (k rows × n columns over GF(4)). Every nonzero GF(4)-linear combination of rows is a **codeword**. The **minimum distance d** is the smallest Hamming weight among all 4ᵏ − 1 nonzero codewords.

**Encoding:** In this repository, 0=0, 1=1, 2=ω, 3=ω².

---

## Repository Contents

| File | Description |
|------|-------------|
| README.md | Project overview and world record matrix |
| GUIDE.md | This file |
| RESULTS.md | All verified matrices, weight enumerators, campaign data |
| THEOREMS.md | Six obstruction theorems + five structural theorems with proofs |
| CHRONOLOGY.md | Narrative timeline of the campaign |
| OPEN_PROBLEMS.md | What remains open and how to contribute |
| V13 RUNNING IN TERMINAL.md | Historical snapshot — the moment A₁₂=42 was first achieved |
| V15_Italian_Job_Did_Not_Work.md | How 720M evaluations proved A₁₂=42 is a geometric floor |
| CITATION.md | Citation metadata (BibTeX, APA, IEEE) |
| LICENSE.md | Business Source License 1.1 |

---

## The World Record (March 2026)

```
[22,6,12]₄ with A₁₂ = 33  (11 projective directions)
Previous record: A₁₂ = 42 (Grassl, 2001) — stood for 25 years
```

Generator matrix G (6×22 over GF(4), encoding: 0=0, 1=1, 2=ω, 3=ω²):

```
g1 = [0,3,0,2,0,0,1,0,2,1,1,0,0,0,1,0,3,1,1,3,3,3]
g2 = [2,2,1,1,1,3,3,0,3,2,1,0,2,0,2,1,0,2,3,2,1,0]
g3 = [3,1,1,2,3,1,0,1,3,1,3,2,0,0,0,0,2,0,1,2,1,0]
g4 = [0,3,3,3,1,2,2,1,0,2,0,0,0,3,3,2,2,1,3,3,0,0]
g5 = [2,0,2,0,3,3,2,2,3,0,3,0,0,0,3,3,1,2,1,2,1,0]
g6 = [3,0,0,3,2,3,2,2,2,1,3,0,0,0,2,1,1,0,0,0,0,0]
```

**Verification** — exhaustive enumeration of all 4⁶ − 1 = 4,095 nonzero codewords confirms d_min = 12, A₁₂ = 33. Takes under one second on any modern CPU.

---

## Frequently Asked Questions

**Q: Is [22,6,13]₄ proven not to exist?**  
A: No. We conjecture it doesn't exist, but we have not proved it. The Delsarte LP bound allows it. Our obstruction theorems close specific construction families, not all possibilities.

**Q: What is A₁₂?**  
A: The number of codewords with Hamming weight exactly 12 (the minimum weight). Lower A₁₂ = fewer minimum-weight codewords = structurally closer to d=13. Current record: A₁₂ = 33.

**Q: Why does A₁₂ always change by multiples of 3?**  
A: Theorem D (Collision Symmetry). The GF(4)* scalar action groups minimum-weight codewords into orbits of size 3. So A₁₂ = 3 × (number of projective directions) always.

**Q: What is the Heisenberg Constant?**  
A: For any [22,6,13]₄ code, MacWilliams identities with B₁ = 0 fix the mean codeword weight exactly: E[w] = 67584/4095 = 16.504029... Any candidate code must satisfy this.

**Q: Can I contribute?**  
A: Yes. The world record matrix, all seed matrices, and all verified data are in RESULTS.md. Independent verification of any result is welcome. If you find a [22,6,13]₄ code or prove non-existence, contact tretoef@gmail.com.

**Q: Where is the search methodology?**  
A: The search methodology is documented separately and will be made available upon request after arXiv publication.

---

## The Conjecture

> **Conjecture.** d₄(22,6) = 12. No [22,6,13]₄ linear code exists.

Supported by: 1.2B+ evaluations · 24+ closed construction routes · 6 obstruction theorems · Delsarte LP bound confirms the problem remains genuinely open.

---

*"Puentes, no muros. Es una orden conseguirlo."*

**Proyecto Estrella · Madrid, 2026 · tretoef@gmail.com · github.com/tretoef-estrella**
