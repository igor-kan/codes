"""Hertzsprung-Russell diagrams and fundamental stellar scaling laws."""

import numpy as np


class StellarHRRelations:
    """Calculates stellar luminosity, effective temperature, radius, and main-sequence scaling."""

    SIGMA_SB = 5.670374419e-8  # Stefan-Boltzmann constant (W m^-2 K^-4)
    R_SUN = 6.957e8            # Solar radius (m)
    L_SUN = 3.828e26           # Solar luminosity (W)
    T_SUN = 5772.0             # Solar effective temperature (K)

    @classmethod
    def stefan_boltzmann_luminosity(cls, radius_m: float, t_eff: float) -> float:
        """L = 4 * pi * R^2 * sigma * T_eff^4."""
        return 4.0 * np.pi * (radius_m**2) * cls.SIGMA_SB * (t_eff**4)

    @classmethod
    def effective_temperature(cls, luminosity_w: float, radius_m: float) -> float:
        """T_eff = (L / (4 * pi * R^2 * sigma))^(1/4)."""
        return ((luminosity_w / (4.0 * np.pi * (radius_m**2) * cls.SIGMA_SB)) ** 0.25)

    @classmethod
    def main_sequence_luminosity(cls, mass_solar: float) -> float:
        """Main sequence approximate mass-luminosity relation:
        L / L_sun ~ M^3.5 for intermediate mass stars (0.43 < M/M_sun < 2.0).
        """
        return (mass_solar**3.5) * cls.L_SUN
