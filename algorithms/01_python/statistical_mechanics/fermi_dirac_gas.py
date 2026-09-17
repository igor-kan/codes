"""Fermi-Dirac Quantum Gas and Sommerfeld Heat Capacity Expansion.

Calculates Fermi energy E_F, Fermi temperature T_F, and linear electronic heat capacity C_V = gamma T.
"""

import numpy as np


class FermiDiracGas:
    """Degenerate Fermi gas calculations."""

    HBAR = 1.054571817e-34
    K_B = 1.380649e-23
    M_E = 9.1093837e-31

    @classmethod
    def fermi_energy_3d(cls, number_density: float) -> float:
        """E_F = (hbar^2 / 2m) (3 pi^2 n)^{2/3}."""
        k_f = (3.0 * (np.pi**2) * number_density)**(1.0 / 3.0)
        return float((cls.HBAR**2 / (2.0 * cls.M_E)) * (k_f**2))

    @classmethod
    def electronic_heat_capacity_coefficient(cls, number_density: float, volume: float) -> float:
        """gamma = pi^2/2 N k_B / T_F."""
        ef = cls.fermi_energy_3d(number_density)
        tf = ef / cls.K_B
        total_n = number_density * volume
        return float(0.5 * (np.pi**2) * total_n * cls.K_B / tf)
