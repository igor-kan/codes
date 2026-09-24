"""Expectation-Maximization (EM) Algorithm for 1D Two-Component Gaussian Mixture."""
import numpy as np


def em_gmm_e_step(x: np.ndarray, mu1: float, sig1: float, mu2: float, sig2: float, pi1: float) -> np.ndarray:
    """Compute posterior responsibility gamma_1."""
    pdf1 = np.exp(-0.5 * ((x - mu1) / sig1)**2) / (sig1 * np.sqrt(2.0 * np.pi))
    pdf2 = np.exp(-0.5 * ((x - mu2) / sig2)**2) / (sig2 * np.sqrt(2.0 * np.pi))
    resp1 = pi1 * pdf1 / (pi1 * pdf1 + (1.0 - pi1) * pdf2)
    return resp1
