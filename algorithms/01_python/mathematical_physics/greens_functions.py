"""
1D Green's Function Solver for Boundary Value Problems.
References: Riley, Hobson, Bence - Mathematical Methods for Physics and Engineering.
"""
import numpy as np

def dirichlet_poisson_greens_func(x: float, xi: float, L: float = 1.0) -> float:
    """
    Green's function for -y''(x) = f(x) on [0, L] with y(0) = y(L) = 0:
    G(x, xi) = x (L - xi) / L   for x <= xi
             = xi (L - x) / L   for x > xi
    """
    if x <= xi:
        return x * (L - xi) / L
    else:
        return xi * (L - x) / L

def solve_poisson_1d(source_func, L: float = 1.0, n_points: int = 200) -> tuple:
    """Solve -y''(x) = source_func(x) on [0, L] via Green's function integral."""
    x = np.linspace(0, L, n_points)
    xi = np.linspace(0, L, n_points)
    s_vals = source_func(xi)
    
    y = np.zeros_like(x)
    for i, xi_val in enumerate(x):
        G_vals = np.array([dirichlet_poisson_greens_func(xi_val, s, L) for s in xi])
        y[i] = np.trapezoid(G_vals * s_vals, xi)
    return x, y
