"""Bernoulli Equation for Steady Incompressible Streamlines.

Implements p + 1/2 rho v^2 + rho g z = const and Venturi tube pressure drop.
"""

import numpy as np


class BernoulliEquation:
    """Streamline energy conservation."""

    G = 9.80665

    @classmethod
    def venturi_speed_ratio(cls, area1: float, area2: float, pressure_drop: float, density: float) -> float:
        """v_1 = sqrt(2 Delta p / (rho ((A1/A2)^2 - 1)))."""
        area_ratio_sq = (area1 / area2)**2
        return float(np.sqrt(2.0 * pressure_drop / (density * (area_ratio_sq - 1.0))))

    @classmethod
    def torricelli_efflux_speed(cls, height: float) -> float:
        """v = sqrt(2 g h)."""
        return float(np.sqrt(2.0 * cls.G * height))
