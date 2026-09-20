"""
Gauss-Legendre Quadrature via Golub-Welsch Algorithm.
References: Press et al. - Numerical Recipes (Ch. 4).
"""
import numpy as np

def gauss_legendre_nodes_weights(n: int):
    """Compute nodes and weights on [-1, 1] using symmetric tridiagonal eigenvalue problem."""
    # Subdiagonal beta_k = k / sqrt(4 k^2 - 1)
    k = np.arange(1, n)
    beta = k / np.sqrt(4.0 * k**2 - 1.0)
    J = np.diag(beta, 1) + np.diag(beta, -1)
    eigvals, eigvecs = np.linalg.eigh(J)
    nodes = eigvals
    # Weight w_i = 2 * (v_{i, 1})^2
    weights = 2.0 * (eigvecs[0, :]**2)
    return nodes, weights

def integrate_gauss_legendre(func, a: float, b: float, n: int = 10) -> float:
    """Evaluate definite integral int_a^b f(x) dx using Gauss-Legendre."""
    nodes, weights = gauss_legendre_nodes_weights(n)
    # Map from [-1, 1] to [a, b]
    x_mapped = 0.5 * ((b - a) * nodes + (b + a))
    return 0.5 * (b - a) * np.sum(weights * func(x_mapped))
