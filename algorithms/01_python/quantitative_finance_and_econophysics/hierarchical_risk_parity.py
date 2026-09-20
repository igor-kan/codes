"""
Hierarchical Risk Parity (HRP) Portfolio Allocation.
References: Marcos Lopez de Prado - Advances in Financial Machine Learning (Ch. 16).
"""
import numpy as np
from scipy.cluster.hierarchy import linkage

def correl_dist(corr: np.ndarray) -> np.ndarray:
    """Distance matrix d_ij = sqrt(0.5 * (1 - rho_ij))."""
    return np.sqrt(np.maximum(0.0, 0.5 * (1.0 - corr)))

def inverse_variance_weights(cov: np.ndarray) -> np.ndarray:
    """Inverse variance allocation weights."""
    diag = np.diag(cov)
    inv_var = 1.0 / np.maximum(diag, 1e-10)
    return inv_var / np.sum(inv_var)
