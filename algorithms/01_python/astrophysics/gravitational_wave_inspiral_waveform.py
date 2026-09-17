"""Gravitational Wave Inspiral waveforms for compact binary coalescence."""

import numpy as np


class GravitationalWaveInspiral:
    """Calculates chirp mass and leading order quadrupole gravitational wave waveforms."""

    G = 6.67430e-11
    C = 299792458.0

    @classmethod
    def chirp_mass(cls, m1: float, m2: float) -> float:
        """M_chirp = (m1 * m2)^(3/5) / (m1 + m2)^(1/5)."""
        return ((m1 * m2) ** 0.6) / ((m1 + m2) ** 0.2)

    @classmethod
    def frequency_derivative(cls, f_gw: float, m_chirp: float) -> float:
        """df/dt = (96 / 5) * pi^(8/3) * (G * M_chirp / c^3)^(5/3) * f_gw^(11/3)."""
        factor = (cls.G * m_chirp / (cls.C**3)) ** (5.0 / 3.0)
        return (96.0 / 5.0) * (np.pi ** (8.0 / 3.0)) * factor * (f_gw ** (11.0 / 3.0))

    @classmethod
    def strain_amplitude(cls, f_gw: float, m_chirp: float, distance_m: float) -> float:
        """Quadrupole strain amplitude h = (4 / d) * (G * M_chirp / c^2)^(5/3) * (pi * f_gw / c)^(2/3)."""
        term1 = 4.0 / distance_m
        term2 = (cls.G * m_chirp / (cls.C**2)) ** (5.0 / 3.0)
        term3 = (np.pi * f_gw / cls.C) ** (2.0 / 3.0)
        return float(term1 * term2 * term3)
