"""3D Isotropic Linear Elastic Constitutive Law (Hooke's Law).

sigma_ij = lambda * tr(eps) * delta_ij + 2 * mu * eps_ij
Conversions between Lamé parameters (lambda, mu/G), Young's modulus E,
Poisson's ratio nu, and Bulk modulus K.
"""
import numpy as np
from typing import Dict, Tuple


def lame_from_young_poisson(E: float, nu: float) -> Tuple[float, float]:
    """Compute Lamé parameters lambda, mu from E and nu."""
    if nu >= 0.5 or nu <= -1.0:
        raise ValueError("Poisson ratio must be in (-1.0, 0.5)")
    lam = E * nu / ((1.0 + nu) * (1.0 - 2.0 * nu))
    mu = E / (2.0 * (1.0 + nu))
    return lam, mu


def bulk_modulus(E: float, nu: float) -> float:
    """K = E / (3 * (1 - 2*nu))."""
    return E / (3.0 * (1.0 - 2.0 * nu))


def stress_from_strain(eps: np.ndarray, E: float, nu: float) -> np.ndarray:
    """Calculate 3x3 Cauchy stress from 3x3 strain tensor."""
    lam, mu = lame_from_young_poisson(E, nu)
    tr_eps = np.trace(eps)
    return lam * tr_eps * np.eye(3) + 2.0 * mu * eps


def strain_from_stress(sigma: np.ndarray, E: float, nu: float) -> np.ndarray:
    """Calculate 3x3 strain from 3x3 stress tensor."""
    tr_sig = np.trace(sigma)
    return ((1.0 + nu) / E) * sigma - (nu / E) * tr_sig * np.eye(3)
