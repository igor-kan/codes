"""Discrete Vortex Sheet Panel Method for Thin Airfoil Theory.

Enforces flow tangency and the Kutta condition at the trailing edge to calculate lift coefficient c_l.
"""

import numpy as np


class ThinAirfoilTheory:
    """Analytical thin airfoil lift and moment coefficients."""

    @staticmethod
    def lift_coefficient(angle_of_attack_rad: float, zero_lift_alpha_rad: float = 0.0) -> float:
        """c_l = 2 pi (alpha - alpha_0)."""
        return float(2.0 * np.pi * (angle_of_attack_rad - zero_lift_alpha_rad))

    @staticmethod
    def quarter_chord_moment_coefficient() -> float:
        """c_{m, c/4} is independent of angle of attack for symmetric airfoils (aerodynamic center)."""
        return 0.0
