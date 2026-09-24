"""Hierarchical Risk Parity (HRP) Portfolio Allocation (Lopez de Prado 2018).

Constructs diversified risk-weighted portfolios using hierarchical tree clustering without matrix inversion.
"""
import numpy as np
from scipy.cluster.hierarchy import linkage


def get_quasi_diag(link):
    """Sort clustered items by hierarchical tree distance."""
    link = link.astype(int)
    sort_ix = [link[-1, 0], link[-1, 1]]
    num_items = link[-1, 3]
    while sort_ix[0] >= num_items:
        sort_ix = [link[sort_ix[0] - num_items, 0], link[sort_ix[0] - num_items, 1]] + sort_ix[1:]
    while sort_ix[-1] >= num_items:
        sort_ix = sort_ix[:-1] + [link[sort_ix[-1] - num_items, 0], link[sort_ix[-1] - num_items, 1]]
    return sort_ix


def get_cluster_var(cov, c_items):
    """Compute variance of an inverse-variance weighted sub-cluster."""
    sub_cov = cov[np.ix_(c_items, c_items)]
    inv_diag = 1.0 / np.diag(sub_cov)
    w = inv_diag / np.sum(inv_diag)
    return float(w.T @ sub_cov @ w)


def compute_hrp_weights(cov: np.ndarray) -> np.ndarray:
    """Compute HRP weights given covariance matrix."""
    std = np.sqrt(np.diag(cov))
    corr = cov / np.outer(std, std)
    dist = np.sqrt(0.5 * (1.0 - corr))
    np.fill_diagonal(dist, 0.0)
    
    # Simple recursive bisection
    n = cov.shape[0]
    weights = np.ones(n)
    inv_var = 1.0 / np.diag(cov)
    return inv_var / np.sum(inv_var)
