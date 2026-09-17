"""Microcanonical (NVE) Molecular Dynamics with Lennard-Jones 6-12 Potential.

Implements velocity Verlet integration, minimum image convention, and periodic boundary conditions.
"""

from typing import Sequence, Tuple
import numpy as np


class LennardJonesMD:
    """Lennard-Jones molecular dynamics in 3D box."""

    def __init__(self, positions: np.ndarray, velocities: np.ndarray, box_length: float, epsilon: float = 1.0, sigma: float = 1.0):
        self.r = np.array(positions, dtype=np.float64)
        self.v = np.array(velocities, dtype=np.float64)
        self.l = box_length
        self.eps = epsilon
        self.sigma = sigma
        self.n = len(self.r)

    def forces_and_potential(self) -> Tuple[np.ndarray, float]:
        """Compute pairwise LJ forces F = -grad V with minimum image convention."""
        forces = np.zeros_like(self.r)
        pot_energy = 0.0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                dr = self.r[i] - self.r[j]
                # Periodic wrap
                dr -= self.l * np.round(dr / self.l)
                r2 = float(np.dot(dr, dr))
                if r2 < 1e-12:
                    continue
                s2 = (self.sigma**2) / r2
                s6 = s2**3
                s12 = s6**2
                pot_energy += 4.0 * self.eps * (s12 - s6)
                f_mag = 24.0 * self.eps * (2.0 * s12 - s6) / r2
                f_vec = f_mag * dr
                forces[i] += f_vec
                forces[j] -= f_vec
        return forces, pot_energy

    def verlet_step(self, dt: float) -> float:
        """Velocity Verlet integration step. Returns total energy."""
        forces0, pot0 = self.forces_and_potential()
        # Half-step velocity and full-step position
        self.v += 0.5 * dt * forces0
        self.r += dt * self.v
        # Wrap positions inside box
        self.r = self.r % self.l

        forces1, pot1 = self.forces_and_potential()
        self.v += 0.5 * dt * forces1

        kin_energy = 0.5 * float(np.sum(self.v**2))
        return kin_energy + pot1
