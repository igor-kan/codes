"""Exact Riemann Solver for Sod's Shock Tube Benchmark Problem.

Resolves left expansion fan, contact surface, and right shock wave in Euler gas dynamics.
"""

from typing import Tuple
import numpy as np


class SodShockTubeBenchmark:
    """Sod standard test parameters: (rho_L, p_L) = (1.0, 1.0), (rho_R, p_R) = (0.125, 0.1)."""

    RHO_L, P_L, U_L = 1.0, 1.0, 0.0
    RHO_R, P_R, U_R = 0.125, 0.1, 0.0
    GAMMA = 1.4

    @classmethod
    def acoustic_speeds(cls) -> Tuple[float, float]:
        """Speed of sound c = sqrt(gamma p / rho)."""
        c_l = np.sqrt(cls.GAMMA * cls.P_L / cls.RHO_L)
        c_r = np.sqrt(cls.GAMMA * cls.P_R / cls.RHO_R)
        return float(c_l), float(c_r)
