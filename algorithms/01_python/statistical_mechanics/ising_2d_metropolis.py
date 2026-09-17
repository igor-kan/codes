"""2D Ising Model via Metropolis-Hastings Monte Carlo Sampling.

Simulates square-lattice ferromagnet with exact Onsager critical temperature T_c approx 2.269 J/k_B.
"""

from typing import Tuple
import numpy as np


class Ising2DMetropolis:
    """Metropolis-Hastings algorithm for 2D Ising lattice."""

    ONSAGER_TC = 2.26918531421

    def __init__(self, size: int, temperature: float, coupling_j: float = 1.0):
        self.l = size
        self.t = temperature
        self.j = coupling_j
        self.spins = np.random.choice([-1, 1], size=(size, size))

    def sweep(self, sweeps: int = 1):
        """Execute Metropolis spin-flip sweeps with periodic boundary conditions."""
        beta = 1.0 / self.t
        for _ in range(sweeps):
            for _ in range(self.l * self.l):
                i = np.random.randint(0, self.l)
                j = np.random.randint(0, self.l)
                s = self.spins[i, j]
                nb = (
                    self.spins[(i + 1) % self.l, j] +
                    self.spins[(i - 1) % self.l, j] +
                    self.spins[i, (j + 1) % self.l] +
                    self.spins[i, (j - 1) % self.l]
                )
                delta_e = 2.0 * self.j * s * nb
                if delta_e <= 0.0 or np.random.rand() < np.exp(-beta * delta_e):
                    self.spins[i, j] = -s

    def magnetization(self) -> float:
        """Mean magnetization per spin: m = 1/N sum s_i."""
        return float(np.mean(self.spins))
