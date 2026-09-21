"""
Saitou-Nei Neighbor-Joining (NJ) Algorithm Q-Matrix Calculation.
Reference: Campbell Biology (12th Ed.), Ch. 26; Saitou & Nei (1987).
"""
import numpy as np
from typing import Tuple

def compute_q_matrix(D: np.ndarray) -> np.ndarray:
    """
    Q(i, j) = (n - 2) D(i, j) - sum_k D(i, k) - sum_k D(j, k) for i != j, 0 on diagonal.
    """
    n = D.shape[0]
    if n <= 2:
        return np.zeros_like(D)
    r = np.sum(D, axis=1)
    Q = (n - 2) * D - r[:, None] - r[None, :]
    np.fill_diagonal(Q, 0.0)
    return Q

def find_nj_pair(D: np.ndarray) -> Tuple[int, int]:
    """Finds pair (i, j) that minimizes Q(i, j)."""
    Q = compute_q_matrix(D)
    n = D.shape[0]
    min_val = np.inf
    pair = (0, 1)
    for i in range(n):
        for j in range(i + 1, n):
            if Q[i, j] < min_val:
                min_val = Q[i, j]
                pair = (i, j)
    return pair
