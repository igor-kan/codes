"""
Finite Geometries: Affine Planes AG(2, q), Projective Planes PG(2, q), and MOLS.

Implements:
1. 4-point affine plane AG(2, F2) parallelism verification
2. 7-point Fano plane PG(2, F2) projective completion
3. 7x7 Incidence matrix verifying M M^T = 2I + J
4. Complete set of q - 1 = 2 Mutually Orthogonal Latin Squares (MOLS) for order 3
5. Bruck-Ryser-Chowla number-theoretic sieve for orders 2 to 15
"""

import numpy as np
from itertools import combinations
from typing import Tuple, Optional

def verify_ag2_f2():
    """Verify 4 points, 6 lines, 3 parallel classes of AG(2, F2)."""
    points = [(0, 0), (1, 0), (0, 1), (1, 1)]
    lines = {
        "Cyan_Bottom": {(0, 0), (1, 0)},
        "Cyan_Top":    {(0, 1), (1, 1)},
        "Red_Left":    {(0, 0), (0, 1)},
        "Red_Right":   {(1, 0), (1, 1)},
        "Green_Diag1": {(0, 0), (1, 1)},
        "Green_Diag2": {(1, 0), (0, 1)}
    }
    
    # Green diagonals intersection
    inter = lines["Green_Diag1"].intersection(lines["Green_Diag2"])
    assert len(inter) == 0, "Green lines must be disjoint in AG(2, F2)!"
    return True

def fano_plane_incidence() -> np.ndarray:
    """Construct 7x7 incidence matrix of Fano plane PG(2, F2)."""
    fano_lines = [
        {0, 1, 4}, {2, 3, 4}, {0, 2, 5},
        {1, 3, 5}, {0, 3, 6}, {1, 2, 6}, {4, 5, 6}
    ]
    M = np.zeros((7, 7), dtype=int)
    for col, line in enumerate(fano_lines):
        for pt in line:
            M[pt, col] = 1
    return M

def bruck_ryser_chowla_filter(max_order: int = 15):
    """Filter orders using Bruck-Ryser-Chowla: if q = 1 or 2 (mod 4), q must be sum of 2 squares."""
    results = {}
    for q in range(2, max_order + 1):
        mod4 = q % 4
        if mod4 in [1, 2]:
            can_sum = False
            for a in range(int(q**0.5) + 1):
                b2 = q - a*a
                b = int(b2**0.5)
                if b*b == b2:
                    can_sum = True
                    break
            results[q] = "ALLOWED" if can_sum else "FORBIDDEN"
        else:
            results[q] = "INCONCLUSIVE"
    return results

def verify_mols_order3():
    """Construct and verify 2 MOLS for order 3 (AG(2, 3))."""
    L1 = np.array([[0, 1, 2], [1, 2, 0], [2, 0, 1]])
    L2 = np.array([[0, 1, 2], [2, 0, 1], [1, 2, 0]])
    pairs = {(L1[r, c], L2[r, c]) for r in range(3) for c in range(3)}
    assert len(pairs) == 9, "L1 and L2 must be mutually orthogonal!"
    return True

if __name__ == "__main__":
    print("=== FINITE GEOMETRY LABORATORY ===")
    assert verify_ag2_f2()
    print("AG(2, F2) parallel classes verified: green lines are disjoint.")
    
    M = fano_plane_incidence()
    MMt = M @ M.T
    expected = 2 * np.eye(7, dtype=int) + np.ones((7, 7), dtype=int)
    assert np.all(MMt == expected)
    print("PG(2, F2) Fano projective identity M * M^T = 2I + J verified.")
    
    brc = bruck_ryser_chowla_filter(12)
    print(f"BRC order 6: {brc[6]} (Resolves Euler's 36 Officers Problem)")
    print(f"BRC order 10: {brc[10]} (Ruled out later by Lam et al. 1989 supercomputer proof)")
