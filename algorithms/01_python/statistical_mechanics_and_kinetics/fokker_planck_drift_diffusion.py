"""Fokker-Planck 1D Drift-Diffusion PDE Solver."""
import numpy as np


def fokker_planck_step(P: np.ndarray, drift: np.ndarray, D: float, dx: float, dt: float) -> np.ndarray:
    """Update probability density P_t = -(drift * P)_x + D * P_xx via forward Euler."""
    flux_drift = drift * P
    d_drift = (np.roll(flux_drift, -1) - np.roll(flux_drift, 1)) / (2.0 * dx)
    d2_diff = D * (np.roll(P, -1) - 2.0 * P + np.roll(P, 1)) / (dx**2)
    P_next = P + dt * (-d_drift + d2_diff)
    return np.maximum(P_next, 0.0)
