"""Rayleigh-Schrodinger Degenerate Perturbation Theory (Subspace Diagonalization)."""
import numpy as np


def degenerate_subspace_split(H0_val: float, V_subspace: np.ndarray) -> np.ndarray:
    """Eigenvalues of perturbed degenerate subspace H_0 + V."""
    eigvals = np.linalg.eigvalsh(V_subspace)
    return H0_val + eigvals
