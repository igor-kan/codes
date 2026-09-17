"""Gravitational Free-Air and Bouguer Anomalies."""

import numpy as np


class GravityAnomalies:
    """Gravity corrections and anomaly calculations in milligals (mGal)."""

    G = 6.67430e-11  # m^3 kg^-1 s^-2

    @classmethod
    def free_air_correction(cls, elevation_h_meters: float) -> float:
        """Delta g_FA = (2 * g_0 / R_E) * h ~ 0.3086 * h [mGal]."""
        return 0.3086 * elevation_h_meters

    @classmethod
    def bouguer_plate_correction(cls, elevation_h_meters: float, rho: float = 2670.0) -> float:
        """Delta g_BP = 2 * pi * G * rho * h.
        In mGal (1 mGal = 1e-5 m/s^2): 2 * pi * G * rho * 1e5 * h ~ 0.04193 * (rho/1000) * h.
        """
        # G in SI, convert SI (m/s^2) to mGal (* 1e5)
        factor = 2.0 * np.pi * cls.G * rho * 1e5
        return float(factor * elevation_h_meters)

    @classmethod
    def bouguer_anomaly(
        cls, g_observed_mgal: float, g_theoretical_mgal: float, elevation_h: float, rho: float = 2670.0
    ) -> float:
        """Delta g_B = g_obs - g_theor + Delta g_FA - Delta g_BP."""
        fa = cls.free_air_correction(elevation_h)
        bp = cls.bouguer_plate_correction(elevation_h, rho)
        return float(g_observed_mgal - g_theoretical_mgal + fa - bp)
