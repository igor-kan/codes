"""Synchrotron Radiation from ultra-relativistic charged particles."""

import numpy as np


class SynchrotronRadiation:
    """Formulas for power and characteristic emission frequency of relativistic electrons in magnetic fields."""

    SIGMA_T = 6.65245873e-29
    C = 299792458.0
    MU_0 = 1.25663706212e-6
    Q_E = 1.602176634e-19
    M_E = 9.1093837e-31

    @classmethod
    def total_emitted_power(cls, gamma: float, magnetic_field_t: float) -> float:
        """P_synch = (4/3) * sigma_T * c * beta^2 * gamma^2 * U_B
        where U_B = B^2 / (2 * mu_0). For gamma >> 1, beta ~ 1.
        """
        u_b = (magnetic_field_t**2) / (2.0 * cls.MU_0)
        return (4.0 / 3.0) * cls.SIGMA_T * cls.C * (gamma**2) * u_b

    @classmethod
    def critical_frequency(cls, gamma: float, magnetic_field_t: float) -> float:
        """nu_c = (3 / 4*pi) * (e * B / m_e) * gamma^2."""
        omega_c = cls.Q_E * magnetic_field_t / cls.M_E
        return (3.0 / (4.0 * np.pi)) * omega_c * (gamma**2)
