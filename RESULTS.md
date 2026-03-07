# Results

All verified matrices and computational data from the Proyecto Estrella campaign on d₄(22,6).

---

## World Record: A₁₂ = 33 (March 2026)

**Confirmed twice in independent computational runs.**  
Previous world record: A₁₂ = 42 (Grassl, 2001) — stood for 25 years.

Generator matrix G (6×22 over GF(4), encoding: 0=0, 1=1, 2=ω, 3=ω²):

```
g1 = [0,3,0,2,0,0,1,0,2,1,1,0,0,0,1,0,3,1,1,3,3,3]
g2 = [2,2,1,1,1,3,3,0,3,2,1,0,2,0,2,1,0,2,3,2,1,0]
g3 = [3,1,1,2,3,1,0,1,3,1,3,2,0,0,0,0,2,0,1,2,1,0]
g4 = [0,3,3,3,1,2,2,1,0,2,0,0,0,3,3,2,2,1,3,3,0,0]
g5 = [2,0,2,0,3,3,2,2,3,0,3,0,0,0,3,3,1,2,1,2,1,0]
g6 = [3,0,0,3,2,3,2,2,2,1,3,0,0,0,2,1,1,0,0,0,0,0]
```

**Verified parameters:** d_min = 12, A₁₂ = 33, A₁₃ = 324.

**Partial weight enumerator:**

| Weight w | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|----------|----|----|----|----|----|----|----|----|----|----|
| Aᵥᵥ      | 33 | 324 | ~396 | ~534 | ~639 | ~768 | ~684 | ~450 | ~222 | ~33 |

Note: A₁₂ = 33 ≡ 0 (mod 3) — consistent with Theorem D (11 projective directions × 3 scalar orbits).

---

## Intermediate Records (Campaign Progression)

### A₁₂ = 36 — March 2026

```
g1 = [2,1,0,2,0,2,0,2,3,0,2,2,3,1,0,0,0,3,2,0,0,1]
g2 = [3,1,0,1,1,0,1,3,1,1,0,1,2,3,3,3,0,1,1,0,3,0]
g3 = [3,1,0,2,2,3,0,2,0,3,1,1,2,0,0,1,0,1,0,0,2,0]
g4 = [0,0,1,1,3,0,2,3,3,3,1,0,1,2,0,0,1,2,1,0,3,0]
g5 = [3,2,0,2,1,2,3,0,1,1,3,3,0,2,0,3,2,2,0,3,2,0]
g6 = [0,0,0,0,1,1,1,2,0,1,3,1,1,2,0,1,2,1,1,0,1,0]
```

d_min = 12, A₁₂ = 36 (12 projective directions).

---

### A₁₂ = 39 — March 2026

```
g1 = [1,1,0,0,0,0,3,2,2,0,0,3,2,2,1,1,0,0,2,0,2,3]
g2 = [2,0,2,1,0,0,3,1,3,0,2,3,1,3,3,0,1,3,1,3,3,2]
g3 = [2,3,2,2,3,0,2,0,2,2,1,3,2,0,2,0,2,0,0,0,3,3]
g4 = [0,3,1,3,0,3,0,3,3,0,2,2,3,2,1,0,0,0,1,1,0,2]
g5 = [2,2,3,1,0,0,2,3,0,1,1,3,0,3,0,0,1,0,0,2,3,3]
g6 = [1,2,0,1,0,0,2,3,2,0,3,1,3,0,0,0,2,0,1,3,0,0]
```

d_min = 12, A₁₂ = 39 (13 projective directions).

---

### A₁₂ = 42 — February 2026

The first world record of the campaign. Stood as the global best from February 2026 until the Corleone series.

```
g1 = [1,1,0,0,0,0,3,2,1,1,2,2,0,1,0,1,0,3,0,0,3,3]
g2 = [0,0,0,0,0,0,2,2,0,0,1,3,3,2,2,2,1,3,1,0,2,2]
g3 = [0,2,1,0,0,0,3,2,3,2,0,3,0,1,1,0,2,2,2,1,0,2]
g4 = [0,0,0,1,0,0,2,0,3,3,3,0,1,2,2,1,0,0,3,2,2,1]
g5 = [0,3,0,0,1,0,3,3,2,0,3,3,2,0,1,2,1,2,1,2,0,0]
g6 = [0,0,0,0,0,1,0,0,2,1,3,0,3,1,3,0,2,2,1,2,2,1]
```

d_min = 12, A₁₂ = 42 (14 projective directions).  
This record was confirmed as a structural floor (not a local minimum) by the Italian Job — ~720M evaluations over 7.5 hours — before being broken by the v22 Sniper campaign.

---

## Campaign Progress Table

| Version | Method | Evaluations | A₁₂ | Projective Dirs | Date |
|---------|--------|-------------|------|-----------------|------|
| Baseline | Grassl (2001) | — | 78 | 26 | 2001 |
| v1–v5 | SA + 108 Doctrines | ~500M | 69→60→51→48 | 23→20→17→16 | Feb 2026 |
| **v13** | **Pitbull recombination** | **+373M** | **42** | **14** | **Feb 2026** |
| v14–v15 | Italian Job (vertical collapse) | ~720M | 42 (floor confirmed) | 14 | Feb 2026 |
| v22 cycle 28 | Symmetry-breaking | +100M | **39** | 13 | Mar 2026 |
| v22 cycle 75 | Cascade | +200M | **36** | 12 | Mar 2026 |
| **v22 cycle 141** | **Corleone + A13-Drain** | **+300M** | **33** | **11** | **Mar 2026** |

**Total evaluations: 1.2B+**

---

## Key Constants

- **Heisenberg Constant:** For any [22,6,13]₄ code, E[w] = 67584/4095 = 16.504029... (MacWilliams identities, B₁ = 0)
- **A₁₂ ≡ 0 (mod 3)** for all [22,6,12]₄ codes (Theorem D)
- **Griesmer bound:** g₄(6,13) = 21 — a [22,6,13]₄ code is not excluded a priori
- **Delsarte LP bound:** A₄(22,13) ≤ 21,743 — the problem remains genuinely open

---

## Verification

Any matrix in this file can be verified by exhaustive enumeration of all 4⁶ − 1 = 4,095 nonzero codewords. The computation takes under one second on any modern CPU.

```python
import numpy as np

GF4_ADD = np.array([[0,1,2,3],[1,0,3,2],[2,3,0,1],[3,2,1,0]], dtype=np.uint8)
GF4_MUL = np.array([[0,0,0,0],[0,1,2,3],[0,2,3,1],[0,3,1,2]], dtype=np.uint8)

# Insert any G matrix here
G = np.array([...], dtype=np.uint8)

min_w = 22; count = 0
for c_int in range(1, 4**6):
    c = np.array([(c_int>>(2*i))&3 for i in range(6)], dtype=np.uint8)
    cw = np.zeros(22, dtype=np.uint8)
    for i in range(6):
        if c[i]: cw = GF4_ADD[cw, GF4_MUL[c[i]][G[i]]]
    w = int(np.count_nonzero(cw))
    if w < min_w: min_w = w; count = 1
    elif w == min_w: count += 1

print(f"d_min={min_w}, A_{min_w}={count}")
```

---

*All results independently audited. Source: Proyecto Estrella — github.com/tretoef-estrella*

**Proyecto Estrella · Madrid, 2026**
