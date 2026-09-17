"""Cosmological Distance Ladder and Flat Lambda-CDM Distances."""

from typing import Callable
import numpy as np


class CosmologicalDistances:
    """Computes comoving distance, luminosity distance, and angular diameter distance."""

    C = 299792458.0  # m/s

    def __init__(self, h0_kms_mpc: float = 70.0, omega_m: float = 0.3, omega_lambda: float = 0.7):
        self.h0 = h0_kms_mpc * 1000.0 / (3.085677581e22)  # s^-1
        self.omega_m = omega_m
        self.omega_lambda = omega_lambda

    def e_z(self, z: float) -> float:
        """E(z) = sqrt(Omega_m * (1+z)^3 + Omega_Lambda)."""
        return np.sqrt(self.omega_m * ((1.0 + z)**3) + self.omega_lambda)

    def comoving_distance(self, z: float, n_steps: int = 1000) -> float:
        """d_C(z) = (c / H_0) * int_0^z dz' / E(z')."""
        z_grid = np.linspace(0, z, n_steps + 1)
        integrand = 1.0 / self.e_z(z_grid)
        trap_func = getattr(np, "trapezoid", getattr(np, "trapz", None))
        integral = trap_func(integrand, z_grid)
        return (self.C / self.h0) * integral

    def luminosity_distance(self, z: float) -> float:
        """d_L(z) = (1 + z) * d_C(z)."""
        return (1.0 + z) * self.comoving_distance(z)

    def angular_diameter_distance(self, z: float) -> float:
        """d_A(z) = d_C(z) / (1 + z)."""
        return self.comoving_distance(z) / (1.0 + z)
