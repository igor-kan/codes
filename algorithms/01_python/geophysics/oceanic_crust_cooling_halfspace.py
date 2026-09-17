"""Oceanic Lithosphere Cooling Half-Space Model."""

from scipy.special import erf
import numpy as np


class OceanicLithosphereCooling:
    """Cooling of semi-infinite half-space:
    T(z, t) = T_s + (T_m - T_s) * erf( z / (2 * sqrt(kappa * t)) )
    """

    KAPPA = 1.0e-6  # Thermal diffusivity (m^2 / s)

    @classmethod
    def temperature(
        cls, depth_z: float, age_seconds: float, t_surface: float = 0.0, t_mantle: float = 1350.0
    ) -> float:
        if age_seconds <= 0:
            return t_surface
        arg = depth_z / (2.0 * np.sqrt(cls.KAPPA * age_seconds))
        return float(t_surface + (t_mantle - t_surface) * erf(arg))

    @classmethod
    def seafloor_subsidence(cls, age_myr: float, d_ridge: float = 2500.0, c_const: float = 350.0) -> float:
        """Boundary layer bathymetry: d(t) = d_ridge + C * sqrt(t_Myr) [meters]."""
        return float(d_ridge + c_const * np.sqrt(age_myr))
