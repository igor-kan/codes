"""Navarro-Frenk-White (NFW) Dark Matter Halo Density Profile."""

import numpy as np


class NFWProfile:
    """NFW density profile: rho(r) = rho_0 / [ (r/r_s) * (1 + r/r_s)^2 ]."""

    G = 6.67430e-11

    def __init__(self, rho_0: float, r_s: float):
        self.rho_0 = float(rho_0)
        self.r_s = float(r_s)

    def density(self, r: float) -> float:
        x = r / self.r_s
        return self.rho_0 / (x * ((1.0 + x)**2))

    def enclosed_mass(self, r: float) -> float:
        """M(r) = 4 * pi * rho_0 * r_s^3 * [ ln(1 + x) - x / (1 + x) ], where x = r / r_s."""
        x = r / self.r_s
        factor = np.log(1.0 + x) - x / (1.0 + x)
        return 4.0 * np.pi * self.rho_0 * (self.r_s**3) * factor

    def circular_velocity(self, r: float) -> float:
        """v_c(r) = sqrt(G * M(r) / r)."""
        m = self.enclosed_mass(r)
        return np.sqrt(self.G * m / r)
