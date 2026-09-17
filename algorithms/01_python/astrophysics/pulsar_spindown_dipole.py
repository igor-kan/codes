"""Pulsar Spindown via Magnetic Dipole Radiation."""

import numpy as np


class PulsarSpindown:
    """Spindown age, braking index, and surface magnetic field of pulsars."""

    @classmethod
    def characteristic_age(cls, period_s: float, period_derivative: float) -> float:
        """tau = P / (2 * P_dot)."""
        return period_s / (2.0 * period_derivative)

    @classmethod
    def surface_magnetic_field(cls, period_s: float, period_derivative: float) -> float:
        """B_surface approx 3.2e19 * sqrt(P * P_dot) [Gauss].
        In Tesla (SI): B_T = 3.2e15 * sqrt(P * P_dot).
        """
        return 3.2e15 * np.sqrt(period_s * period_derivative)
