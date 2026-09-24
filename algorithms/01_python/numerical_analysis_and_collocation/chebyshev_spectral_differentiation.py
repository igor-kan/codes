"""Chebyshev Spectral Differentiation Matrix (Kincaid & Cheney, Schorghofer).

Exact collocation derivative at Gauss-Lobatto nodes x_j = cos(pi * j / N).
"""
import numpy as np


def chebyshev_nodes(N: int) -> np.ndarray:
    """Chebyshev-Gauss-Lobatto grid nodes in [-1, 1]."""
    return np.cos(np.pi * np.arange(N + 1) / N)


def chebyshev_differentiation_matrix(N: int) -> np.ndarray:
    """Construct (N+1)x(N+1) Chebyshev collocation derivative matrix D."""
    if N == 0:
        return np.zeros((1, 1))
    x = chebyshev_nodes(N)
    c = np.ones(N + 1)
    c[0] = 2.0
    c[-1] = 2.0
    c[1:-1] = 1.0
    c = c * ((-1.0) ** np.arange(N + 1))
    
    X = np.tile(x, (N + 1, 1))
    dX = X.T - X
    
    D = np.outer(c, 1.0 / c) / (dX + np.eye(N + 1))
    D = D - np.diag(np.sum(D, axis=1))
    return D
