"""Legendre-Gauss-Lobatto (LGL) Quadrature Nodes and Weights.

Nodes are roots of (1 - x^2) * P_N'(x) = 0.
"""
import numpy as np
from scipy.special import legendre


def lgl_nodes_weights(N: int) -> tuple:
    """Compute N+1 LGL nodes and integration weights on [-1, 1]."""
    if N < 1:
        raise ValueError("N must be >= 1")
    # Initial guess using Chebyshev nodes
    x = np.cos(np.pi * np.arange(N + 1) / N)
    P_N = legendre(N)
    P_prime = P_N.deriv()
    
    # Newton iteration for interior roots
    for i in range(1, N):
        xi = x[i]
        for _ in range(20):
            p = P_N(xi)
            pp = P_prime(xi)
            ppp = P_prime.deriv()(xi)
            # f(x) = (1 - x^2) * P_prime(x)
            f = (1.0 - xi**2) * pp
            df = -2.0 * xi * pp + (1.0 - xi**2) * ppp
            step = f / df
            xi -= step
            if abs(step) < 1e-13:
                break
        x[i] = xi
        
    x[0] = 1.0
    x[-1] = -1.0
    w = 2.0 / (N * (N + 1) * (P_N(x)**2))
    return x, w
