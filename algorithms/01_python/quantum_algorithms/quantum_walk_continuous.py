"""Continuous-Time Quantum Walk on Graphs via Matrix Exponentiation.

Evolution is governed by Schrodinger equation |psi(t)> = exp(-i H t) |psi(0)> with Hamiltonian H = L.
"""

from typing import Sequence
import numpy as np
from scipy.linalg import expm


class ContinuousQuantumWalk:
    """Continuous quantum walk on graph with Laplacian L."""

    def __init__(self, adjacency_matrix: Sequence[Sequence[float]]):
        adj = np.array(adjacency_matrix, dtype=np.float64)
        degree = np.diag(np.sum(adj, axis=1))
        self.laplacian = degree - adj
        self.n = len(adj)

    def transition_matrix(self, t: float) -> np.ndarray:
        """U(t) = exp(-i L t)."""
        return expm(-1.0j * self.laplacian * t)

    def probability_distribution(self, initial_node: int, t: float) -> np.ndarray:
        """P(j) = |<j| U(t) |initial>|^2."""
        u_t = self.transition_matrix(t)
        state_t = u_t[:, initial_node]
        return np.abs(state_t)**2
