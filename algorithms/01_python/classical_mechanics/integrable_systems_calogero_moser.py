"""Calogero-Moser Integrable Many-Body System and Lax Pair Formulation.

Implements Arnold integrable systems with inverse-square interaction:
H = 1/2 sum p_i^2 + sum_{i<j} g^2 / (q_i - q_j)^2, Lax equation dot{L} = [M, L], and trace invariants.
"""

from typing import Sequence, Tuple
import numpy as np


class CalogeroMoserSystem:
    """N-body Calogero-Moser integrable system."""

    def __init__(self, positions: Sequence[float], momenta: Sequence[float], coupling: float = 1.0):
        self.q = np.array(positions, dtype=np.float64)
        self.p = np.array(momenta, dtype=np.float64)
        self.g = coupling
        self.n = len(self.q)
        if len(self.p) != self.n:
            raise ValueError("Positions and momenta must have identical length")

    def lax_matrix_l(self) -> np.ndarray:
        """L_{jk} = p_j delta_{jk} + (1 - delta_{jk}) i g / (q_j - q_k)."""
        l_mat = np.zeros((self.n, self.n), dtype=np.complex128)
        for j in range(self.n):
            for k in range(self.n):
                if j == k:
                    l_mat[j, k] = self.p[j]
                else:
                    diff = self.q[j] - self.q[k]
                    if abs(diff) < 1e-12:
                        raise ZeroDivisionError("Calogero-Moser particles collided")
                    l_mat[j, k] = 1j * self.g / diff
        return l_mat

    def conserved_trace_invariants(self, max_power: int = 4) -> np.ndarray:
        """Involutive integrals of motion I_k = 1/k Tr(L^k)."""
        l_mat = self.lax_matrix_l()
        invariants = np.zeros(max_power, dtype=np.float64)
        current_power = np.eye(self.n, dtype=np.complex128)
        for k in range(1, max_power + 1):
            current_power = current_power @ l_mat
            tr = np.trace(current_power)
            invariants[k - 1] = float(np.real(tr) / k)
        return invariants
