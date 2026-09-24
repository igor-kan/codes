"""Quantum Density Matrix, Purity, and von Neumann Entropy."""
import numpy as np


def density_matrix_purity(rho: np.ndarray) -> float:
    """Evaluate Tr(rho^2)."""
    return float(np.trace(rho @ rho).real)


def von_neumann_entropy(rho: np.ndarray) -> float:
    """Evaluate S = -sum lambda_i ln(lambda_i)."""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = eigvals[eigvals > 1e-15]
    return float(-np.sum(eigvals * np.log(eigvals)))
