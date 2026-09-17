"""Euler Precession and Elastic Chandler Wobble."""

import numpy as np


class EarthPrecession:
    """Euler free nutation of rigid Earth vs Chandler wobble of elastic Earth."""

    @classmethod
    def euler_period_days(cls, moment_a: float, moment_c: float) -> float:
        """tau_E = (A / (C - A)) * 1 day.
        For Earth, (C - A) / A ~ 1 / 304.
        """
        return float((moment_a / (moment_c - moment_a)))

    @classmethod
    def chandler_period_days(cls, euler_period_days: float, love_number_k2: float = 0.29) -> float:
        """Elastic deformation lengthens period to ~433 days via Love number k2."""
        # Simple elasticity factor approximation
        factor = 1.0 + love_number_k2 * 1.45
        return float(euler_period_days * factor)
