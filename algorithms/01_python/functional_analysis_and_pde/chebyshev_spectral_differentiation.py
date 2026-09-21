"""
Chebyshev Pseudospectral Differentiation Matrix D_N on [-1, 1].
Reference: Trefethen, Spectral Methods in MATLAB; Blennow.
"""
import numpy as np
from typing import Tuple

def chebyshev_diff_matrix(N: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes Chebyshev-Gauss-Lobatto grid points x_j = cos(j pi / N) and differentiation matrix D.
    """
    if N == 0:
        return np.array([0.0]), np.array([[0.0]])
    x = np.cos(np.pi * np.arange(N + 1) / N)
    c = np.ones(N + 1)
    c[0] = 2.0
    c[-1] = 2.0
    c[1:-1] = 1.0
    c = c * ((-1.0)**np.arange(N + 1))
    
    dX = x[:, None] - x[None, :]
    D = (c[:, None] / c[None, :]) / (dX + np.eye(N + 1))
    D = D - np.diag(np.sum(D, axis=1))
    return x, D
