"""Schwarzschild Metric in Spherical Coordinates (t, r, theta, phi).

Calculates exact components, horizon radius, perihelion advance, and gravitational deflection.
"""

from typing import Sequence
import numpy as np
try:
    from .metric_tensor import MetricTensor
except ImportError:
    from metric_tensor import MetricTensor


class SchwarzschildMetric:
    """Schwarzschild black hole solution in coordinates (t, r, theta, phi)."""

    def __init__(self, m: float, g_const: float = 1.0, c: float = 1.0):
        self.m = m
        self.g_const = g_const
        self.c = c
        self.r_s = 2.0 * g_const * m / (c**2)

    def metric_at(self, coords: Sequence[float]) -> MetricTensor:
        """Returns MetricTensor at (t, r, theta, phi)."""
        _, r, theta, _ = coords
        if r <= self.r_s:
            raise ValueError(f"Coordinate singularity inside horizon r={r} <= r_s={self.r_s}")
        f = 1.0 - self.r_s / r
        g_mat = np.diag([-(self.c**2) * f, 1.0 / f, r**2, (r**2) * (np.sin(theta)**2)])
        return MetricTensor(g_mat)

    def perihelion_precession(self, semi_major_axis: float, eccentricity: float) -> float:
        """Precession per revolution: Delta phi = 6 pi G M / (c^2 a (1 - e^2))."""
        return 6.0 * np.pi * self.g_const * self.m / ((self.c**2) * semi_major_axis * (1.0 - eccentricity**2))

    def light_deflection(self, impact_parameter: float) -> float:
        """Deflection angle: Delta theta = 4 G M / (c^2 b)."""
        return 4.0 * self.g_const * self.m / ((self.c**2) * impact_parameter)
