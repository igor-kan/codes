"""Griffith Energy Balance Criterion for Brittle Fracture.

Critical fracture stress for center crack of length 2a in an infinite plate:
sigma_c = sqrt(2 * E * gamma_s / (pi * a * (1 - nu^2)))  (plane strain)
Stress intensity factor: K_I = sigma * sqrt(pi * a).
Energy release rate: G_I = K_I^2 / E' = 2 * gamma_s.
"""
import numpy as np


def critical_fracture_stress(a: float, surface_energy: float, E: float, nu: float, plane_strain: bool = True) -> float:
    """Calculate Griffith critical fracture stress sigma_c."""
    if a <= 0:
        raise ValueError("Crack half-length a must be positive")
    
    E_prime = E / (1.0 - nu**2) if plane_strain else E
    return float(np.sqrt(2.0 * E_prime * surface_energy / (np.pi * a)))


def stress_intensity_factor_mode1(sigma: float, a: float) -> float:
    """K_I = sigma * sqrt(pi * a)."""
    return float(sigma * np.sqrt(np.pi * a))
