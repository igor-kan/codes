"""
Calogero-Moser Lax Pair and Integrable Invariants.
References: V. I. Arnold - Mathematical Methods of Classical Mechanics.
"""
import numpy as np

def calogero_lax_matrix(q: np.ndarray, p: np.ndarray, g: float = 1.0) -> np.ndarray:
    """Lax matrix L for rational Calogero-Moser system: L_jj = p_j, L_jk = i g / (q_j - q_k)."""
    n = len(q)
    L = np.diag(p).astype(complex)
    for j in range(n):
        for k in range(n):
            if j != k:
                L[j, k] = 1j * g / (q[j] - q[k])
    return L

def calogero_conserved_quantities(L: np.ndarray) -> list:
    """Tr(L^k) are constants of motion."""
    n = L.shape[0]
    invariants = []
    L_pow = np.eye(n, dtype=complex)
    for k in range(1, n + 1):
        L_pow = L_pow @ L
        invariants.append(np.real(np.trace(L_pow)) / k)
    return invariants
