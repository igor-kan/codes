"""Kerr Metric for Rotating Black Holes in Boyer-Lindquist Coordinates (t, r, theta, phi).

Handles frame dragging, event horizon, ergosphere, and Carter constant.
"""

from typing import Tuple
import numpy as np


class KerrMetric:
    """Kerr rotating black hole metric with mass M and angular momentum parameter a = J / M."""

    def __init__(self, m: float, a: float, g_const: float = 1.0, c: float = 1.0):
        self.m = m
        self.a = a
        self.g_const = g_const
        self.c = c
        if abs(a) > m:
            raise ValueError("Kerr naked singularity: spin parameter |a| must be <= M")

    @property
    def horizons(self) -> Tuple[float, float]:
        """Outer (r+) and inner (r-) event horizons."""
        disc = np.sqrt(self.m**2 - self.a**2)
        return self.m + disc, self.m - disc

    def ergosphere_outer_radius(self, theta: float) -> float:
        """Outer ergosphere radius: r_E(theta) = M + sqrt(M^2 - a^2 cos^2(theta))."""
        return self.m + np.sqrt(self.m**2 - (self.a**2) * (np.cos(theta)**2))

    def frame_dragging_angular_velocity(self, r: float, theta: float) -> float:
        """Angular velocity of frame dragging omega = -g_{t phi} / g_{phi phi}."""
        sigma = r**2 + (self.a**2) * (np.cos(theta)**2)
        omega = 2.0 * self.m * self.a * r / ((r**2 + self.a**2) * sigma + 2.0 * self.m * (self.a**2) * r * np.sin(theta)**2)
        return omega
