"""
Buckingham Pi Theorem for Dimensional Analysis.
Reference: Polya, Mathematical Methods in Science; Barenblatt, Scaling.
"""
import numpy as np

def compute_dimensionless_groups(dimension_matrix: np.ndarray) -> np.ndarray:
    """
    Given a matrix M of shape (n_fundamental_dimensions, n_variables),
    computes a basis of nullspace vectors corresponding to independent Pi groups:
    M @ pi = 0.
    """
    u, s, vh = np.linalg.svd(dimension_matrix)
    rank = np.sum(s > 1e-10)
    null_basis = vh[rank:].T
    return null_basis
