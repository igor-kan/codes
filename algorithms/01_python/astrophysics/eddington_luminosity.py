"""Eddington Luminosity and Accretion Rate Limits."""

class EddingtonLimit:
    """Calculates the Eddington radiation pressure balance limit."""

    G = 6.67430e-11
    C = 299792458.0
    SIGMA_T = 6.65245873e-29  # Thomson scattering cross section (m^2)
    M_P = 1.672621923e-27      # Proton mass (kg)
    M_SUN = 1.98847e30         # Solar mass (kg)
    L_SUN = 3.828e26           # Solar luminosity (W)

    @classmethod
    def luminosity(cls, mass_kg: float, opacity_kappa: float = None) -> float:
        """Calculates Eddington luminosity L_Edd = 4 * pi * G * M * c / kappa.

        Args:
            mass_kg: Object mass in kg.
            opacity_kappa: Electron scattering opacity (m^2 / kg). Defaults to pure ionized hydrogen: sigma_T / m_p.
        """
        if opacity_kappa is None:
            opacity_kappa = cls.SIGMA_T / cls.M_P
        return (4.0 * 3.141592653589793 * cls.G * mass_kg * cls.C) / opacity_kappa

    @classmethod
    def eddington_accretion_rate(cls, mass_kg: float, radiative_efficiency: float = 0.1) -> float:
        """Calculates the maximum steady accretion rate M_dot_Edd = L_Edd / (eta * c^2)."""
        l_edd = cls.luminosity(mass_kg)
        return l_edd / (radiative_efficiency * (cls.C ** 2))
