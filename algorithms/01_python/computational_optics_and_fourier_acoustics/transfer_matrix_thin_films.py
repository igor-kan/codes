"""Abelès Characteristic Matrix Method for Multilayer Dielectric Thin Films.

Calculates optical reflectance R and transmittance T for normal incidence:
M_layer = [[cos(delta), -i/p * sin(delta)], [-i * p * sin(delta), cos(delta)]]
where delta = 2 * pi * n * d / lambda, p = n.
"""
import numpy as np
from typing import List, Tuple


def multilayer_film_transmittance_reflectance(
    wavelength: float,
    layer_indices: List[float],
    layer_thicknesses: List[float],
    n_substrate: float,
    n_ambient: float = 1.0
) -> Tuple[float, float]:
    """Calculate power reflectance R and transmittance T."""
    M_total = np.eye(2, dtype=complex)

    for n_layer, d in zip(layer_indices, layer_thicknesses):
        delta = 2.0 * np.pi * n_layer * d / wavelength
        M = np.array([
            [np.cos(delta), -1j / n_layer * np.sin(delta)],
            [-1j * n_layer * np.sin(delta), np.cos(delta)]
        ], dtype=complex)
        M_total = M_total @ M

    # Boundary conditions
    p0 = n_ambient
    ps = n_substrate
    B = M_total[0, 0] + M_total[0, 1] * ps
    C = M_total[1, 0] + M_total[1, 1] * ps

    r = (p0 * B - C) / (p0 * B + C)
    R = float(np.abs(r)**2)
    T = float(1.0 - R)  # Non-absorbing lossless dielectrics
    return R, T
