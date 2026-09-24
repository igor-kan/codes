"""Mean-Field Coordinate Ascent Variational Inference (CAVI) for 1D Gaussian."""
import numpy as np


def cavi_gaussian_update(data: np.ndarray, mu0: float, sigma0_sq: float, sigma_sq: float) -> tuple:
    """Update variational parameters m and s^2 for q(mu) ~ Normal(m, s^2)."""
    n = len(data)
    s2 = 1.0 / (1.0 / sigma0_sq + n / sigma_sq)
    m = s2 * (mu0 / sigma0_sq + np.sum(data) / sigma_sq)
    return float(m), float(s2)
