"""Geocentric Magnetic Dipole Field."""

from typing import Tuple
import numpy as np


class GeomagneticDipole:
    """Earth's magnetic dipole field in spherical coordinates (r, theta) where theta is colatitude."""

    R_E = 6.371e6     # Earth radius (m)
    B_0 = 3.12e-5     # Equatorial surface field ~ 31.2 microTesla

    @classmethod
    def field_components(cls, r: float, colatitude_rad: float) -> Tuple[float, float, float]:
        """Calculates (B_r, B_theta, B_total).
        B_r = -2 * B_0 * (R_E / r)^3 * cos(colatitude)
        B_theta = -B_0 * (R_E / r)^3 * sin(colatitude)
        """
        scale = cls.B_0 * ((cls.R_E / r) ** 3)
        br = -2.0 * scale * np.cos(colatitude_rad)
        bt = -scale * np.sin(colatitude_rad)
        b_tot = np.sqrt(br**2 + bt**2)
        return float(br), float(bt), float(b_tot)

    @classmethod
    def magnetic_inclination(cls, latitude_rad: float) -> float:
        """tan(I) = 2 * tan(latitude)."""
        return float(np.arctan(2.0 * np.tan(latitude_rad)))
