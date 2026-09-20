"""
Singular Value Decomposition and Moore-Penrose Pseudoinverse.
References: Press et al. - Numerical Recipes (Ch. 2).
"""
import numpy as np

def svd_pseudoinverse(A: np.ndarray, rcond: float = 1e-12) -> np.ndarray:
    """Compute Moore-Penrose pseudoinverse A^+ using SVD."""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    cutoff = rcond * np.max(s)
    s_inv = np.zeros_like(s)
    mask = s > cutoff
    s_inv[mask] = 1.0 / s[mask]
    return Vt.T @ np.diag(s_inv) @ U.T

def low_rank_svd_approx(A: np.ndarray, rank: int) -> np.ndarray:
    """Eckart-Young-Mirsky theorem optimal rank-k approximation."""
    U, s, Vt = np.linalg.svd(A, full_matrices=False)
    return (U[:, :rank] * s[:rank]) @ Vt[:rank, :]
