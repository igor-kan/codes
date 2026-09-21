"""Non-Diffracting Zero-Order Bessel Beam and Axicon Parameters.

Field profile: E(r, z) = E_0 * J_0(k_r * r) * exp(i * k_z * z).
Axicon cone angle alpha, refractive index n: k_r = k * (n - 1) * alpha.
Non-diffracting range: z_max = R_beam / ((n - 1) * alpha).
"""
import numpy as np
from scipy.special import j0


def bessel_beam_radial_profile(r: np.ndarray, kr: float, E0: float = 1.0) -> np.ndarray:
    """Intensity profile I(r) = |E0 * J0(kr * r)|^2."""
    return E0**2 * (j0(kr * r)**2)


def axicon_nondiffracting_range(beam_radius: float, axicon_angle_rad: float, n_axicon: float = 1.5) -> float:
    """Maximum non-diffracting propagation distance z_max."""
    return float(beam_radius / ((n_axicon - 1.0) * axicon_angle_rad))
