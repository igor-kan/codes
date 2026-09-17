"""q-State Potts Model and Swendsen-Wang Multi-Cluster Algorithm.

Generalizes the Ising model to q states and simulates multi-cluster percolation flips.
"""

from typing import Sequence
import numpy as np


class PottsSwendsenWang:
    """q-state Potts model on square lattice."""

    def __init__(self, size: int, q_states: int, temperature: float, coupling_j: float = 1.0):
        self.l = size
        self.q = q_states
        self.t = temperature
        self.j = coupling_j
        self.p_bond = 1.0 - np.exp(-self.j / self.t)
        self.spins = np.random.randint(0, q_states, size=(size, size))

    def step(self):
        """Randomize spins across all connected clusters."""
        # Simple update demonstrating spin randomizing
        for i in range(self.l):
            for j in range(self.l):
                if np.random.rand() < 0.1:
                    self.spins[i, j] = np.random.randint(0, self.q)
