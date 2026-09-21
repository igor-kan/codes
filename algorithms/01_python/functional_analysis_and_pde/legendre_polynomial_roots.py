"""
Gauss-Legendre Quadrature Nodes and Weights via Golub-Welsch Algorithm.
Reference: Hassani, Mathematical Methods for Physics, Ch. 18.
"""
import numpy as np
from typing import Tuple

def gauss_legendre_nodes_weights(n: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Computes zeros of Legendre polynomial P_n(x) and Christoffel weights using symmetric tridiagonal matrix eigenvalues.
    """
    beta = [i / np.sqrt(4.0 * i**2 - 1.0) for i in range(1, n)]
    T = np.zeros((n, n))
    for i in range(n - 1):
        T[i, i+1] = beta[i]
        T[i+1, i] = beta[i]
        
    eigenvalues, eigenvectors = np.linalg.eigh(T)
    # Weights are 2 * (first component of eigenvector)^2
    weights = 2.0 * (eigenvectors[0, :]**2)
    return eigenvalues, weights
