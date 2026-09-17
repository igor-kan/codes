"""Foucault Pendulum, Coriolis Forces, Hannay Angle, and Berry Geometric Phase on S^2.

Implements Arnold §24 and Berry's phase:
Precession rate dot{psi} = - Omega sin(lambda) and holonomy of the connection Delta psi = 2 pi (1 - sin(lambda)).
"""

import numpy as np


class FoucaultPendulumGeometricPhase:
    """Foucault pendulum precession rate and Hannay geometric phase on rotating Earth."""

    EARTH_OMEGA = 7.2921159e-5  # rad/s

    def __init__(self, latitude_radians: float):
        self.lat = latitude_radians

    def precession_rate(self) -> float:
        """dot{psi} = - Omega sin(lambda)."""
        return - self.EARTH_OMEGA * np.sin(self.lat)

    def geometric_phase_per_day(self) -> float:
        """Delta psi = 2 pi (1 - sin(lambda)) = solid angle enclosed on unit sphere."""
        return float(2.0 * np.pi * (1.0 - np.sin(self.lat)))
