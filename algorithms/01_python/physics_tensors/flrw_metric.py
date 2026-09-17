"""Friedmann-Lemaitre-Robertson-Walker (FLRW) Cosmological Metric.

Implements scale factor a(t), spatial curvature k in {-1, 0, 1}, and Friedmann equations.
"""

import numpy as np


class FLRWMetric:
    """Cosmological FLRW metric ds^2 = -c^2 dt^2 + a(t)^2 [dr^2 / (1 - k r^2) + r^2 dOmega^2]."""

    def __init__(self, k: int = 0, c: float = 1.0):
        if k not in (-1, 0, 1):
            raise ValueError("Curvature index k must be -1 (open), 0 (flat), or +1 (closed)")
        self.k = k
        self.c = c

    def hubble_parameter(self, a: float, a_dot: float) -> float:
        """H = a_dot / a."""
        return a_dot / a

    def deceleration_parameter(self, a: float, a_dot: float, a_ddot: float) -> float:
        """q = - a * a_ddot / (a_dot)^2."""
        return - a * a_ddot / (a_dot**2)

    def friedmann_acceleration(self, rho: float, p: float, a: float,
                               g_const: float = 1.0, lambd: float = 0.0) -> float:
        """a_ddot / a = - 4 pi G / 3 (rho + 3 p / c^2) + Lambda / 3."""
        term1 = - (4.0 * np.pi * g_const / 3.0) * (rho + 3.0 * p / (self.c**2))
        return term1 + lambd / 3.0
