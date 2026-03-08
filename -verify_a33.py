#!/usr/bin/env python3
"""
verify_a33.py — Independent verification of A12 = 33
=====================================================
Verifies the main result of:
  "A New World Record for [22,6,12]4 with A12 = 33"
  R. Amichis Luengo et al. — Proyecto Estrella, March 2026

No dependencies beyond numpy. Runtime: < 1 second.
Expected output:
  d    = 12
  A12  = 33
  A13  = 324

GF(4) encoding: 0=0, 1=1, 2=ω, 3=ω²  |  ω²+ω+1=0 over GF(2)
"""

import numpy as np

# ── GF(4) multiplication table ──────────────────────────────────────────────
GF4_MUL = np.array([
    [0, 0, 0, 0],
    [0, 1, 2, 3],
    [0, 2, 3, 1],
    [0, 3, 1, 2],
], dtype=np.uint8)

# ── Generator matrix G  (6 × 22 over GF(4)) ─────────────────────────────────
# Columns 1–22 of Table 1 in the paper.
# w = ω = 2,  w2 = ω² = 3
G = np.array([
#   1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22
    [0, 3, 0, 2, 0, 0, 1, 0, 2, 1, 1, 0, 0, 0, 1, 0, 3, 1, 1, 3, 3, 3],  # g1
    [2, 2, 1, 1, 1, 3, 3, 0, 3, 2, 1, 0, 2, 0, 2, 1, 0, 2, 3, 2, 1, 0],  # g2
    [3, 1, 1, 2, 3, 1, 0, 1, 3, 1, 3, 2, 0, 0, 0, 0, 2, 0, 1, 2, 1, 0],  # g3
    [0, 3, 3, 3, 1, 2, 2, 1, 0, 2, 0, 0, 0, 3, 3, 2, 2, 1, 3, 3, 0, 0],  # g4
    [2, 0, 2, 0, 3, 3, 2, 2, 3, 0, 3, 0, 0, 0, 3, 3, 1, 2, 1, 2, 1, 0],  # g5
    [3, 0, 0, 3, 2, 3, 2, 2, 2, 1, 3, 0, 0, 0, 2, 1, 1, 0, 0, 0, 0, 0],  # g6
], dtype=np.uint8)

# ── Enumerate all 4^6 - 1 = 4095 nonzero codewords ──────────────────────────
def enumerate_weights(G):
    k, n = G.shape
    weights = []
    for coeff in range(1, 4**k):          # skip the zero codeword
        c = np.zeros(n, dtype=np.uint8)
        x = coeff
        for i in range(k):
            s = x & 3
            x >>= 2
            if s:
                c ^= GF4_MUL[s][G[i]]    # vectorised GF(4) row × scalar
        weights.append(int(np.count_nonzero(c)))
    return np.array(weights, dtype=np.int32)

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("Proyecto Estrella — Result Verification")
    print("=" * 42)
    print("Enumerating 4,095 nonzero codewords...")

    weights = enumerate_weights(G)

    d   = int(weights.min())
    A12 = int((weights == 12).sum())
    A13 = int((weights == 13).sum())

    print(f"  d    = {d}")
    print(f"  A12  = {A12}")
    print(f"  A13  = {A13}")
    print()

    # Full weight enumerator
    print("Weight enumerator:")
    for w in range(12, 22):
        count = int((weights == w).sum())
        if count > 0:
            print(f"  A{w:2d} = {count}")
    print()

    # Verdict
    # Correct weight enumerator (exhaustive, verified):
    # A12=33, A13=324, A14=435, A15=510, A16=678, A17=672,
    # A18=717, A19=486, A20=216, A21=24  — sums to 4095 ✓
    # Note: Table 2 in paper v5 contains a transcription error (sums to 4083).
    # The values below are the ground truth from exhaustive enumeration.
    expected = {12:33, 13:324, 14:435, 15:510, 16:678,
                17:672, 18:717, 19:486, 20:216, 21:24}
    ok = all((weights == w).sum() == expected[w] for w in expected)
    if ok:
        print("✅ VERIFIED — A12 = 33 confirmed.")
        print("   All 4,095 codeword weights match ground truth.")
    else:
        print("❌ MISMATCH — check GF(4) encoding.")
        print(f"   Expected: d=12, A12=33, A13=324")
        print(f"   Got:      d={d}, A12={A12}, A13={A13}")

    print()
    print("Proyecto Estrella | github.com/tretoef-estrella | March 2026")
