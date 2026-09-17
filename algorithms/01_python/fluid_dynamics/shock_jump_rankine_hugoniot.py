"""Rankine-Hugoniot Jump Conditions Across Normal Shock Waves.

Calculates pressure, density, and temperature ratios as functions of upstream Mach number M_1.
"""

from typing import Tuple
import numpy as np


class RankineHugoniotShock:
    """1D normal shock wave relations for ideal gas with ratio of specific heats gamma."""

    def __init__(self, gamma: float = 1.4):
        self.gamma = gamma

    def downstream_mach(self, m1: float) -> float:
        """M_2^2 = (2 + (gamma - 1) M_1^2) / (2 gamma M_1^2 - (gamma - 1))."""
        if m1 < 1.0:
            raise ValueError("Normal shock waves only exist for supersonic upstream flow M_1 >= 1")
        g = self.gamma
        num = 2.0 + (g - 1.0) * (m1**2)
        denom = 2.0 * g * (m1**2) - (g - 1.0)
        return float(np.sqrt(num / denom))

    def pressure_ratio(self, m1: float) -> float:
        """p_2 / p_1 = 1 + 2 gamma / (gamma + 1) * (M_1^2 - 1)."""
        g = self.gamma
        return float(1.0 + (2.0 * g / (g + 1.0)) * (m1**2 - 1.0))

    def density_ratio(self, m1: float) -> float:
        """rho_2 / rho_1 = (gamma + 1) M_1^2 / (2 + (gamma - 1) M_1^2)."""
        g = self.gamma
        return float(((g + 1.0) * (m1**2)) / (2.0 + (g - 1.0) * (m1**2)))
