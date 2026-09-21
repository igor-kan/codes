"""
Hierarchical Risk Parity (HRP) Portfolio Allocation.
Reference: Marcos Lopez de Prado, Machine Learning for Asset Managers, Ch. 2.
"""
import numpy as np

def inverse_variance_weights(cov_matrix: np.ndarray) -> np.ndarray:
    """Allocates capital inversely proportional to asset variance."""
    inv_var = 1.0 / np.diag(cov_matrix)
    return inv_var / np.sum(inv_var)

def cluster_variance(cov_matrix: np.ndarray, weights: np.ndarray) -> float:
    return float(weights @ cov_matrix @ weights)
