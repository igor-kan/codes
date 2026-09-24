"""Kuramoto-Sivashinsky Chaotic Flame Front PDE: u_t + u u_x + u_xx + u_xxxx = 0."""
import numpy as np


def kuramoto_sivashinsky_linear_dispersion(k: np.ndarray) -> np.ndarray:
    """Linear growth rate omega(k) = k^2 - k^4. Unstable for 0 < |k| < 1."""
    return k**2 - k**4
