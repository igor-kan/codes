"""Sedov-Taylor Supernova Blast Wave self-similar solution."""

import numpy as np


class SedovTaylorBlastWave:
    """Self-similar blast wave radius and expansion velocity."""

    @classmethod
    def shock_radius(cls, time_s: float, energy_j: float, ambient_density_kg_m3: float, xi_0: float = 1.15) -> float:
        """R(t) = xi_0 * (E * t^2 / rho_0)^(1/5)."""
        return float(xi_0 * ((energy_j * (time_s**2) / ambient_density_kg_m3) ** 0.2))

    @classmethod
    def shock_velocity(cls, time_s: float, energy_j: float, ambient_density_kg_m3: float, xi_0: float = 1.15) -> float:
        """v_s(t) = dR/dt = (2/5) * R(t) / t."""
        r = cls.shock_radius(time_s, energy_j, ambient_density_kg_m3, xi_0)
        return (0.4 * r) / time_s
