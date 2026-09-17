"""Tolman-Oppenheimer-Volkoff (TOV) relativistic hydrostatic equilibrium solver."""

from typing import Tuple, Callable
import numpy as np


class TOVSolver:
    """Integrates the General Relativistic TOV equation:
    dP/dr = - (G * m * rho / r^2) * [1 + P/(rho*c^2)] * [1 + 4*pi*r^3*P/(m*c^2)] / [1 - 2*G*m/(r*c^2)]
    dm/dr = 4 * pi * r^2 * rho
    """

    G = 6.67430e-11
    C = 299792458.0

    def __init__(self, eos_rho: Callable[[float], float], p_central: float, dr: float = 10.0, r_max: float = 30000.0):
        """
        Args:
            eos_rho: Equation of state function returning density rho(P) [kg/m^3] for given pressure P [Pa].
            p_central: Central pressure in Pascals.
            dr: Step size in meters.
            r_max: Maximum radius in meters.
        """
        self.eos_rho = eos_rho
        self.p_central = p_central
        self.dr = dr
        self.r_max = r_max

    def solve(self) -> Tuple[np.ndarray, np.ndarray, np.ndarray, float, float]:
        """Integrates from center outward.

        Returns:
            (r_array, p_array, m_array, stellar_radius, total_mass)
        """
        r = 1.0  # Avoid division by zero at r=0
        p = self.p_central
        rho = self.eos_rho(p)
        m = (4.0 / 3.0) * np.pi * (r**3) * rho

        r_list = [0.0, r]
        p_list = [p, p]
        m_list = [0.0, m]

        c2 = self.C ** 2

        while r < self.r_max and p > 1e-10:
            rho = self.eos_rho(p)
            if rho <= 0:
                break

            # Relativistic factors
            factor1 = 1.0 + p / (rho * c2)
            factor2 = 1.0 + (4.0 * np.pi * (r**3) * p) / (m * c2)
            factor3 = 1.0 - (2.0 * self.G * m) / (r * c2)

            if factor3 <= 0:
                # Black hole horizon crossed
                break

            dp_dr = - (self.G * m * rho / (r**2)) * (factor1 * factor2 / factor3)
            dm_dr = 4.0 * np.pi * (r**2) * rho

            p += dp_dr * self.dr
            m += dm_dr * self.dr
            r += self.dr

            if p > 0:
                r_list.append(r)
                p_list.append(p)
                m_list.append(m)

        return np.array(r_list), np.array(p_list), np.array(m_list), r_list[-1], m_list[-1]
