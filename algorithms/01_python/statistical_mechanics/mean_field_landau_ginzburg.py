"""Landau-Ginzburg Mean Field Theory of Second-Order Phase Transitions.

Free energy expansion F(m) = a(T - T_c) m^2 + b m^4 - h m and critical exponents.
"""

import numpy as np


class LandauGinzburgMeanField:
    """Landau phase transition mean field analysis."""

    def __init__(self, t_critical: float, a_coeff: float = 1.0, b_coeff: float = 1.0):
        self.tc = t_critical
        self.a = a_coeff
        self.b = b_coeff

    def spontaneous_magnetization(self, temperature: float) -> float:
        """m_0 = sqrt(a(T_c - T) / (2 b)) for T < T_c, and 0 for T >= T_c."""
        if temperature >= self.tc:
            return 0.0
        return float(np.sqrt(self.a * (self.tc - temperature) / (2.0 * self.b)))
