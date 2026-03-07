# V13 Running in Terminal

*A snapshot from February 2026 — the moment the campaign first broke A₁₂ = 60.*

---

## The Scene

Madrid. A MacBook Air. A terminal window open on a kitchen table.

The first engine capable of sustained improvement was running. After weeks of building the algebraic infrastructure — GF(4) arithmetic, the C-compiled kernel, the exhaustive evaluator — the search had finally stabilized into something that could hold d=12 across thousands of random restarts.

The output came in cycles. Each cycle: a phase of exploration, a phase of consolidation, a phase of surgical refinement. The numbers dropped slowly, then sometimes suddenly.

---

## The Progression

The terminal recorded what the formulas predicted: A₁₂ is always divisible by 3 (Theorem D — the scalar orbits of GF(4)* group minimum-weight codewords in triples). So the sequence was never random. It was always: 78 → 69 → 60 → 51 → 48 → 42.

Each step was a contraction of the search space. Each number represented a configuration: a 6×22 matrix over GF(4) where a certain number of codewords hit the minimum weight boundary.

The moment that mattered came when **Pitbull** activated — a row-recombination strategy that broke standard form entirely, replacing g₁ with a GF(4)-linear combination of rows. The evaluator saw it: A₁₂ = 42. 14 projective directions. A new campaign record.

The terminal printed the matrix. The session was saved.

---

## What the Numbers Meant

```
Cycle 1  │ A₁₂ = 78  │ 26 projective directions
Cycle 4  │ A₁₂ = 69  │ 23 projective directions
Cycle 12 │ A₁₂ = 60  │ 20 projective directions  ← R7 Exhaustive
Cycle 14 │ A₁₂ = 51  │ 17 projective directions  ← Heat-Seeker
Cycle 14 │ A₁₂ = 48  │ 16 projective directions
Cycle 15 │ A₁₂ = 42  │ 14 projective directions  ← Pitbull
```

Each "projective direction" is an orbit of 3 codewords under the GF(4)* scalar action. 14 orbits × 3 = 42. The number that had stood in Grassl's codetables.de since 2001 — unchanged for 25 years — had finally moved.

---

## What Came Next

v13 was the first engine. The campaign continued through v14, v15 (the Italian Job), v22, and eventually the Corleone series. The A₁₂ = 42 floor was not the end — it was the beginning of understanding that A₁₂ = 42 was itself a structural property, a gravitational attractor in PG(5,4), not a coincidence.

The search is ongoing. The diamond has not been found.

---

*"La belleza de las matemáticas es que lo permiten todo. Y si crees que no, es que aún no has encontrado la manera."* — The Architect

**Proyecto Estrella · Madrid, 2026**
