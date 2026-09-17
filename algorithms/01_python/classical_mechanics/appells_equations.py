"""Gibbs-Appell Equations of Motion using the Energy of Acceleration S = 1/2 sum m_i ddot{r}_i^2.

Generalizes Lagrangian mechanics to non-holonomic systems using quasi-accelerations: dS / d dot{u}_r = Pi_r.
"""

from typing import Sequence
import numpy as np


class AppellsMechanics:
    """Gibbs-Appell dynamics for systems with quasi-velocities."""

    @staticmethod
    def energy_of_acceleration_1d(masses: Sequence[float], accelerations: Sequence[float]) -> float:
        """Appellian function S = 1/2 sum m_i a_i^2."""
        m = np.array(masses, dtype=np.float64)
        a = np.array(accelerations, dtype=np.float64)
        return 0.5 * float(np.sum(m * (a**2)))

    @staticmethod
    def appell_equations_particle(mass: float, applied_force: float) -> float:
        """dS / d a = m a = F => a = F / m."""
        return applied_force / mass
