"""Shakura-Sunyaev thin accretion disk model."""

import numpy as np


class ShakuraSunyaevDisk:
    """Stationary, geometrically thin, optically thick accretion disk model."""

    G = 6.67430e-11
    C = 299792458.0
    SIGMA_SB = 5.670374419e-8

    @classmethod
    def temperature_profile(cls, radius_m: float, mass_kg: float, m_dot_kg_s: float, r_in_m: float) -> float:
        """Effective surface temperature T_eff(r):
        T_eff(r) = [ (3 * G * M * M_dot) / (8 * pi * sigma * r^3) * (1 - sqrt(r_in / r)) ]^(1/4)
        """
        if radius_m <= r_in_m:
            return 0.0
        term1 = (3.0 * cls.G * mass_kg * m_dot_kg_s) / (8.0 * np.pi * cls.SIGMA_SB * (radius_m**3))
        term2 = 1.0 - np.sqrt(r_in_m / radius_m)
        return float((term1 * term2) ** 0.25)
