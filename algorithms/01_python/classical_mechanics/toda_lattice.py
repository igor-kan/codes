"""Toda Non-Linear Integrable Lattice and Flaschka Tridiagonal Lax Pair.

Implements Toda chain with exponential potential V = sum exp(-(q_{n+1} - q_n)) and solitary waves.
"""

from typing import Sequence
import numpy as np


class TodaLattice:
    """Toda lattice in Flaschka coordinates:
    a_n = 1/2 exp(-(q_{n+1} - q_n) / 2)
    b_n = - 1/2 p_n
    """

    def __init__(self, positions: Sequence[float], momenta: Sequence[float]):
        self.q = np.array(positions, dtype=np.float64)
        self.p = np.array(momenta, dtype=np.float64)
        self.n = len(self.q)

    def flaschka_variables(self) -> np.ndarray:
        """Returns tridiagonal symmetric Lax matrix L."""
        # a_k for k = 0 .. n-2
        a = 0.5 * np.exp(-0.5 * (self.q[1:] - self.q[:-1]))
        b = -0.5 * self.p

        l_mat = np.zeros((self.n, self.n), dtype=np.float64)
        for i in range(self.n):
            l_mat[i, i] = b[i]
            if i < self.n - 1:
                l_mat[i, i + 1] = a[i]
                l_mat[i + 1, i] = a[i]
        return l_mat

    def conserved_quantities(self, max_k: int = 3) -> np.ndarray:
        """Integrals of motion I_k = Tr(L^k)."""
        l_mat = self.flaschka_variables()
        invs = np.zeros(max_k, dtype=np.float64)
        curr = np.eye(self.n)
        for k in range(1, max_k + 1):
            curr = curr @ l_mat
            invs[k - 1] = float(np.trace(curr))
        return invs
