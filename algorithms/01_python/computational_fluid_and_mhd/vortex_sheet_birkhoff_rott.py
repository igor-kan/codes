"""Birkhoff-Rott Integro-Differential Equation for 2D Vortex Sheet Roll-up.

Krasny desingularization delta-blob regularization:
dz*/dt = 1/(2*pi*i) * sum_j [ Gamma_j / (z - z_j + i * delta) ].
"""
import numpy as np


def vortex_sheet_velocity(z: np.ndarray, gammas: np.ndarray, delta: float = 0.05) -> np.ndarray:
    """Calculate complex conjugate velocities w = u - i*v for N sheet vortices."""
    n = len(z)
    w = np.zeros(n, dtype=complex)

    for i in range(n):
        diff = z[i] - z
        # Apply Krasny blob regularization to denominator: (z - z_j) / (|z - z_j|^2 + delta^2)
        r_sq = np.abs(diff)**2
        mask = np.arange(n) != i
        denom = r_sq[mask] + delta**2
        kernel = diff[mask] / denom
        w[i] = -0.5j / np.pi * np.sum(gammas[mask] * kernel)

    return np.conj(w)
