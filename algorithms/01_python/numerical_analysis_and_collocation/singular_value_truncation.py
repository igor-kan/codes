"""Truncated SVD and Low-Rank Eckart-Young Matrix Approximation."""
import numpy as np


def truncated_svd_approximation(A: np.ndarray, rank: int) -> tuple:
    """Compute optimal rank-k approximation A_k = U_k * Sigma_k * V_k^T."""
    U, S, Vt = np.linalg.svd(A, full_matrices=False)
    k = min(rank, len(S))
    A_approx = (U[:, :k] * S[:k]) @ Vt[:k, :]
    energy_captured = np.sum(S[:k]**2) / np.sum(S**2)
    return A_approx, float(energy_captured)
