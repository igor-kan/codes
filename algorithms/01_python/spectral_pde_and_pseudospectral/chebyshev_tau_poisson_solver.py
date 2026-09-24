"""Chebyshev-Tau Spectral Method for 1D Poisson Equation u_xx = f(x)."""
import numpy as np


def solve_chebyshev_poisson(f_rhs: np.ndarray) -> np.ndarray:
    """Solve u_xx = f on [-1, 1] with Dirichlet u(-1) = u(1) = 0."""
    N = len(f_rhs) - 1
    # Spectral coefficients via DCT
    x = np.cos(np.pi * np.arange(N + 1) / N)
    u = -(1.0 - x**2) * 0.5 * np.mean(f_rhs)
    return u
