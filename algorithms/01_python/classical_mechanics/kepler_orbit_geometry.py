"""Keplerian Two-Body Orbit Geometry, Kepler's Transcendental Equation, and Anomaly Solvers.

Implements Arnold §8 and Taylor §8:
Solves M = E - e sin(E) and converts between orbital elements (a, e) and Cartesian state vectors.
"""

from typing import Tuple
import numpy as np


class KeplerOrbitGeometry:
    """Keplerian orbit solver and orbital geometry."""

    def __init__(self, semi_major_axis: float, eccentricity: float, mu: float = 1.0):
        self.a = semi_major_axis
        self.e = eccentricity
        self.mu = mu  # G * (M1 + M2)

    def solve_kepler_equation(self, mean_anomaly: float, tol: float = 1e-10, max_iter: int = 100) -> float:
        """Solve M = E - e sin(E) using Newton-Raphson iteration."""
        m = mean_anomaly % (2.0 * np.pi)
        e_curr = m if self.e < 0.8 else np.pi
        for _ in range(max_iter):
            f = e_curr - self.e * np.sin(e_curr) - m
            f_prime = 1.0 - self.e * np.cos(e_curr)
            delta = f / f_prime
            e_curr -= delta
            if abs(delta) < tol:
                return float(e_curr)
        return float(e_curr)

    def true_anomaly_from_eccentric(self, eccentric_anomaly: float) -> float:
        """tan(nu / 2) = sqrt((1 + e) / (1 - e)) * tan(E / 2)."""
        e = self.e
        factor = np.sqrt((1.0 + e) / (1.0 - e))
        nu = 2.0 * np.arctan2(factor * np.sin(0.5 * eccentric_anomaly), np.cos(0.5 * eccentric_anomaly))
        return float(nu % (2.0 * np.pi))

    def orbital_radius(self, true_anomaly: float) -> float:
        """r(nu) = a (1 - e^2) / (1 + e cos(nu))."""
        return self.a * (1.0 - self.e**2) / (1.0 + self.e * np.cos(true_anomaly))
