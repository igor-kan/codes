"""
Density Matrix, Partial Trace, and von Neumann Entanglement Entropy.
References: Izaac & Wang - Computational Quantum Mechanics.
"""
import numpy as np

def partial_trace_b(rho_ab: np.ndarray, dim_a: int, dim_b: int) -> np.ndarray:
    """Compute partial trace over subsystem B of bipartite state rho_ab."""
    rho_tensor = rho_ab.reshape((dim_a, dim_b, dim_a, dim_b))
    return np.trace(rho_tensor, axis1=1, axis2=3)

def von_neumann_entropy(rho: np.ndarray) -> float:
    """Compute von Neumann entropy S = -Tr(rho ln rho)."""
    eigvals = np.linalg.eigvalsh(rho)
    eigvals = eigvals[eigvals > 1e-12]
    return float(-np.sum(eigvals * np.log2(eigvals)))
