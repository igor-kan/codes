"""Wolff Cluster Monte Carlo Algorithm for the Ising Model.

Defeats critical slowing down near T_c via Fortuin-Kasteleyn bond probability p = 1 - exp(-2 beta J).
"""

from typing import List, Tuple
import numpy as np


class WolffIsing2D:
    """Wolff single-cluster update algorithm."""

    def __init__(self, size: int, temperature: float, coupling_j: float = 1.0):
        self.l = size
        self.t = temperature
        self.j = coupling_j
        self.p_add = 1.0 - np.exp(-2.0 * self.j / self.t)
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def cluster_step(self) -> int:
        """Grow and flip a single cluster. Returns cluster size."""
        seed_i = np.random.randint(0, self.l)
        seed_j = np.random.randint(0, self.l)
        old_spin = self.spins[seed_i, seed_j]
        new_spin = -old_spin

        cluster = [(seed_i, seed_j)]
        self.spins[seed_i, seed_j] = new_spin
        queue = [(seed_i, seed_j)]

        while queue:
            ci, cj = queue.pop(0)
            neighbors = [
                ((ci + 1) % self.l, cj),
                ((ci - 1) % self.l, cj),
                (ci, (cj + 1) % self.l),
                (ci, (cj - 1) % self.l)
            ]
            for ni, nj in neighbors:
                if self.spins[ni, nj] == old_spin:
                    if np.random.rand() < self.p_add:
                        self.spins[ni, nj] = new_spin
                        cluster.append((ni, nj))
                        queue.append((ni, nj))
        return len(cluster)
