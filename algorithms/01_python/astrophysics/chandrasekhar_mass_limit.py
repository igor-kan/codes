"""Chandrasekhar Mass Limit calculation for relativistic electron degeneracy."""

import numpy as np


class ChandrasekharLimit:
    """Calculates the maximum theoretical mass of a non-rotating white dwarf."""

    # Fundamental constants (SI)
    G = 6.67430e-11        # m^3 kg^-1 s^-2
    C = 299792458.0        # m s^-1
    HBAR = 1.054571817e-34 # J s
    M_P = 1.672621923e-27  # kg (proton mass)
    M_SUN = 1.98847e30     # kg (solar mass)

    @classmethod
    def calculate_limit(cls, mu_e: float = 2.0) -> float:
        """Calculates the Chandrasekhar limiting mass in kg.

        For an ultra-relativistic electron degeneracy EOS: P = K * rho^(4/3)
        where K = (hbar * c / 4) * (3 * pi^2)^(1/3) * (mu_e * m_u)^(-4/3).
        The Lane-Emden n=3 mass is M_Ch = 4 * pi * (K / (pi * G))^(3/2) * omega_3^0
        where omega_3^0 = 2.01824 is the dimensionless mass parameter.
        """
        omega3 = 2.01824
        m_u = 1.66053906660e-27  # Atomic mass constant
        k = (cls.HBAR * cls.C / 4.0) * ((3.0 * (np.pi**2)) ** (1.0 / 3.0)) * ((mu_e * m_u) ** (-4.0 / 3.0))
        m_ch = 4.0 * np.pi * ((k / (np.pi * cls.G)) ** 1.5) * omega3
        return float(m_ch)

    @classmethod
    def in_solar_masses(cls, mu_e: float = 2.0) -> float:
        """Returns the Chandrasekhar mass limit in units of solar masses (M_sun)."""
        return cls.calculate_limit(mu_e) / cls.M_SUN
