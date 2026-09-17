"""Supercritical and Subcritical Hopf Bifurcations."""

from typing import Tuple
import numpy as np


class HopfBifurcation:
    """Normal form of Hopf bifurcation:
    dr/dt = mu * r - a * r^3
    dtheta/dt = omega + b * r^2
    where a > 0 for supercritical (stable limit cycle for mu > 0)
    and a < 0 for subcritical.
    """

    def __init__(self, mu: float, omega: float = 1.0, a: float = 1.0, b: float = 0.0):
        self.mu = mu
        self.omega = omega
        self.a = a
        self.b = b

    def polar_derivatives(self, r: float, theta: float) -> Tuple[float, float]:
        dr = self.mu * r - self.a * (r**3)
        dtheta = self.omega + self.b * (r**2)
        return dr, dtheta

    def limit_cycle_radius(self) -> float:
        """Returns stable limit cycle radius r* = sqrt(mu / a) for mu > 0, else 0.0."""
        if self.mu > 0 and self.a > 0:
            return np.sqrt(self.mu / self.a)
        return 0.0
