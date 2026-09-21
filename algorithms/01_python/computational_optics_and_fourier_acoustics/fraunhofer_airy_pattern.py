"""Fraunhofer Diffraction from Circular Aperture (Airy Pattern).

I(theta) = I_0 * [ 2 * J_1(k * R * sin(theta)) / (k * R * sin(theta)) ]^2.
First zero (Airy disk radius): theta_1 = 1.21966989 * lambda / D (Rayleigh criterion).
"""
import numpy as np
from scipy.special import j1


def airy_pattern_intensity(theta: np.ndarray, wavelength: float, diameter: float, I0: float = 1.0) -> np.ndarray:
    """Calculate normalized angular intensity profile of circular aperture diffraction."""
    k = 2.0 * np.pi / wavelength
    R = diameter / 2.0
    x = k * R * np.sin(theta)

    # Handle zero angle limit x -> 0 where 2*J1(x)/x -> 1
    intensity = np.ones_like(x, dtype=float) * I0
    mask = np.abs(x) > 1e-12
    intensity[mask] = I0 * (2.0 * j1(x[mask]) / x[mask])**2
    return intensity


def rayleigh_angular_resolution(wavelength: float, diameter: float) -> float:
    """Rayleigh angular limit of resolution theta_min = 1.22 * lambda / D."""
    return float(1.21966989 * wavelength / diameter)
