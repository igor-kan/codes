"""
Gaussian Copula Simulation for Financial Portfolio Return Correlation.
Reference: Marcos Lopez de Prado.
"""
import numpy as np
from scipy.stats import norm

def sample_gaussian_copula(corr_matrix: np.ndarray, n_samples: int, seed: int = 42) -> np.ndarray:
    """Generates correlated uniform marginals U ~ [0, 1]^d."""
    rng = np.random.default_rng(seed)
    d = corr_matrix.shape[0]
    L = np.linalg.cholesky(corr_matrix)
    Z = rng.normal(size=(n_samples, d)) @ L.T
    U = norm.cdf(Z)
    return U
