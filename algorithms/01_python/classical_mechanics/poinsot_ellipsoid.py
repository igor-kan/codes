"""Poinsot's Ellipsoid and Geometric Construction of Torque-Free Rigid Body Motion.

Implements Landau & Lifshitz §37: inertia ellipsoid I_1 x^2 + I_2 y^2 + I_3 z^2 = 2E rolling on invariable plane L . omega = 2E.
"""

from typing import Sequence, Tuple
import numpy as np


class PoinsotConstruction:
    """Poinsot geometric representation of asymmetric top motion."""

    def __init__(self, principal_moments: Sequence[float], kinetic_energy: float, angular_momentum_sq: float):
        self.i1, self.i2, self.i3 = principal_moments
        self.energy = kinetic_energy
        self.l2 = angular_momentum_sq

        # Verify physical admissibility 2 E I_1 <= L^2 <= 2 E I_3 (assuming I_1 <= I_2 <= I_3)
        if not (2.0 * self.energy * self.i1 <= self.l2 + 1e-9 and self.l2 <= 2.0 * self.energy * self.i3 + 1e-9):
            raise ValueError("Kinetic energy and angular momentum violate Poinsot dynamical bounds")

    def polhode_cone_semiaxes(self) -> Tuple[float, float, float]:
        """Semiaxes of the inertia ellipsoid: a_i = sqrt(2E / I_i)."""
        return (
            np.sqrt(2.0 * self.energy / self.i1),
            np.sqrt(2.0 * self.energy / self.i2),
            np.sqrt(2.0 * self.energy / self.i3)
        )

    def invariable_plane_distance(self) -> float:
        """Distance from center of inertia to invariable plane: h = 2E / ||L||."""
        l_norm = np.sqrt(self.l2)
        return 2.0 * self.energy / l_norm
