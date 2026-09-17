"""Cyclotron Gyrofrequency and Larmor Radius (Gyroradius).

Implements Omega_c = q B / m and r_L = v_perp / Omega_c.
"""

import numpy as np


class CyclotronKinematics:
    """Charged particle gyration in magnetic fields."""

    @staticmethod
    def gyrofrequency(charge: float, magnetic_field: float, mass: float) -> float:
        """Omega_c = |q| B / m."""
        return float(abs(charge) * magnetic_field / mass)

    @staticmethod
    def larmor_radius(perpendicular_velocity: float, charge: float, magnetic_field: float, mass: float) -> float:
        """r_L = v_perp / Omega_c = m v_perp / (|q| B)."""
        wc = CyclotronKinematics.gyrofrequency(charge, magnetic_field, mass)
        return float(perpendicular_velocity / wc)
