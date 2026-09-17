"""Jeans Instability and Gravitational Collapse Timescales."""

import numpy as np


class JeansInstability:
    """Gravitational instability criteria for interstellar gas clouds."""

    G = 6.67430e-11
    K_B = 1.380649e-23
    M_P = 1.672621923e-27

    @classmethod
    def sound_speed(cls, temperature_k: float, mu: float = 2.3) -> float:
        """Isothermal sound speed c_s = sqrt(k_B * T / (mu * m_p))."""
        return np.sqrt(cls.K_B * temperature_k / (mu * cls.M_P))

    @classmethod
    def jeans_length(cls, sound_speed: float, density_kg_m3: float) -> float:
        """lambda_J = sqrt(pi * c_s^2 / (G * rho))."""
        return np.sqrt(np.pi * (sound_speed**2) / (cls.G * density_kg_m3))

    @classmethod
    def jeans_mass(cls, sound_speed: float, density_kg_m3: float) -> float:
        """M_J = (4/3) * pi * (lambda_J / 2)^3 * rho."""
        lj = cls.jeans_length(sound_speed, density_kg_m3)
        return (4.0 / 3.0) * np.pi * ((lj / 2.0)**3) * density_kg_m3

    @classmethod
    def free_fall_time(cls, density_kg_m3: float) -> float:
        """tau_ff = sqrt(3 * pi / (32 * G * rho))."""
        return np.sqrt(3.0 * np.pi / (32.0 * cls.G * density_kg_m3))
