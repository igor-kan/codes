"""Lattice Boltzmann Method (LBM) with D2Q9 Velocity Stencil and BGK Collision.

Simulates microscopic streaming and collision steps to solve macroscopic Navier-Stokes flow.
"""

from typing import Tuple
import numpy as np


class LatticeBoltzmannD2Q9:
    """D2Q9 LBM solver."""

    C_DIRS = np.array([
        [0, 0], [1, 0], [0, 1], [-1, 0], [0, -1],
        [1, 1], [-1, 1], [-1, -1], [1, -1]
    ], dtype=int)

    WEIGHTS = np.array([4.0 / 9.0] + [1.0 / 9.0] * 4 + [1.0 / 36.0] * 4, dtype=np.float64)

    def __init__(self, nx: int, ny: int, tau: float = 0.6):
        self.nx = nx
        self.ny = ny
        self.tau = tau
        self.f = np.zeros((9, nx, ny), dtype=np.float64)
        for i in range(9):
            self.f[i] = self.WEIGHTS[i]

    def macroscopic_density_and_velocity(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
        """rho = sum f_i, u = 1/rho sum f_i c_i."""
        rho = np.sum(self.f, axis=0)
        ux = np.zeros((self.nx, self.ny))
        uy = np.zeros((self.nx, self.ny))
        for i in range(9):
            ux += self.C_DIRS[i, 0] * self.f[i]
            uy += self.C_DIRS[i, 1] * self.f[i]
        ux /= rho
        uy /= rho
        return rho, ux, uy
