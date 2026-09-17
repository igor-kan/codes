"""1D Electrostatic Particle-in-Cell (PIC) Simulation Engine.

Implements Cloud-in-Cell (CIC) charge deposition, Poisson solver, and leapfrog Boris pusher.
"""

from typing import Sequence, Tuple
import numpy as np


class ParticleInCell1D:
    """1D electrostatic PIC code."""

    def __init__(self, num_grid_nodes: int, box_length: float, num_particles: int):
        self.ng = num_grid_nodes
        self.l = box_length
        self.dx = box_length / num_grid_nodes
        self.n_part = num_particles
        self.x = np.random.uniform(0.0, box_length, num_particles)
        self.v = np.random.normal(0.0, 1.0, num_particles)

    def deposit_charge_cic(self) -> np.ndarray:
        """Cloud-In-Cell bilinear charge deposition onto grid."""
        rho = np.zeros(self.ng, dtype=np.float64)
        for xi in self.x:
            grid_pos = xi / self.dx
            idx = int(np.floor(grid_pos))
            frac = grid_pos - idx
            i1 = idx % self.ng
            i2 = (idx + 1) % self.ng
            rho[i1] += 1.0 - frac
            rho[i2] += frac
        return rho
