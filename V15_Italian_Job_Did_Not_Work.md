# The Italian Job: A Structural Proof by Exhaustion

*February 2026 — v14/v15 — ~720 million evaluations — 7.5 hours*

---

## The Plan

After reaching A₁₂ = 42 with v13, a question arose: was 42 a local minimum — something the engine had stumbled into — or was it a structural floor, a property of the geometry itself?

The Italian Job was designed to answer that question.

The approach was not to search randomly. It was to be systematic. To sweep. To take the A₁₂ = 42 matrix and exhaustively explore every reachable basis representation of the same code, asking: does any equivalent form yield A₁₂ < 42?

---

## The Execution

The engine ran for 7.5 hours. Approximately 720 million candidate configurations were evaluated.

Three independent auditors (Gemini, ChatGPT, Grok) confirmed the methodology at each stage. The sweep was structured as a "Vertical Collapse Protocol" — working through the space of equivalent representations systematically rather than stochastically.

Every evaluation returned the same answer: A₁₂ = 42.

---

## What Was Proven

The Italian Job failed to improve A₁₂. But failure was the result.

**Theorem F (PG(5,4) Attractor)** emerged from this data: the A₁₂ = 42 configuration has a non-trivial Z₃ automorphism structure. The 42 minimum-weight codewords form 14 orbits of size 3 under scalar multiplication. Standard perturbation operators — the kind any search algorithm uses — act within this attractor basin. They cannot escape it from the inside.

This meant that breaking A₁₂ = 42 would require a qualitative change in strategy, not just more computation. The engine needed to destroy the symmetry entirely before trying to reduce.

---

## The Implication

The Italian Job did not find a better code. What it found was something more valuable: a structural constraint.

A₁₂ = 42 is not a local accident. It is a geometric property of a class of codes in PG(5,4). Any approach that preserves the Z₃ orbit structure will rediscover it. To escape, the search must operate on codes with *no* such symmetry — codes where the minimum-weight codewords do not group into regular orbits.

This became the guiding principle for v22 and the Corleone series.

---

## Campaign Position

```
v13  │ A₁₂ = 42  │ Pitbull recombination
v14  │ A₁₂ = 42  │ Italian Job — 720M evals, 7.5h — floor confirmed
v15  │ A₁₂ = 42  │ Vertical Collapse Protocol — structural proof
v22  │ A₁₂ = 39  │ Symmetry broken — Heisenberg Sniper — cycle 28
```

The Italian Job did not work. That is why it is remembered.

---

*"The truth is more important than the dream."* — The Architect

**Proyecto Estrella · Madrid, 2026**
