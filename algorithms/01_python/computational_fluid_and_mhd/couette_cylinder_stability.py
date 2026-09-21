"""Centrifugal Stability of Concentric Rotating Cylinders (Couette Flow).

Rayleigh centrifugal stability criterion: d/dr(r^2 * Omega)^2 > 0 everywhere for stability.
Critical centrifugal vortex instability parameter for inner cylinder rotating at Omega_1,
outer at Omega_2.
"""
import numpy as np


def rayleigh_stability_criterion(r1: float, omega1: float, r2: float, omega2: float) -> bool:
    """Check if Couette flow is centrifugally stable everywhere according to Rayleigh's criterion."""
    # Specific angular momentum L(r) = r^2 * Omega(r). Stable if (r2^2 * Omega2)^2 > (r1^2 * Omega1)^2
    L1_sq = (r1**2 * omega1)**2
    L2_sq = (r2**2 * omega2)**2
    return bool(L2_sq >= L1_sq)


def couette_centrifugal_parameter(r1: float, r2: float, omega1: float, nu: float) -> float:
    """Calculate the dimensionless centrifugal instability parameter Ta_param = Omega_1^2 * r1 * d^3 / nu^2."""
    d = r2 - r1
    return float((omega1**2) * r1 * (d**3) / (nu**2))
