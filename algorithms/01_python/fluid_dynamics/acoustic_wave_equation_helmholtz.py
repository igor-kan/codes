"""Acoustic Wave Equation and Helmholtz Equation Solver.

Models acoustic perturbations nabla^2 p - 1/c^2 d^2 p / dt^2 = 0 and acoustic impedance Z = rho * c.
"""

import numpy as np


class AcousticHelmholtz:
    """Linear acoustics relations."""

    @staticmethod
    def characteristic_impedance(fluid_density: float, sound_speed: float) -> float:
        """Z_0 = rho * c (Rayl)."""
        return fluid_density * sound_speed

    @staticmethod
    def wavenumber(frequency_hz: float, sound_speed: float) -> float:
        """k = 2 pi f / c."""
        return float(2.0 * np.pi * frequency_hz / sound_speed)
