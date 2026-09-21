import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from neumann_series_fredholm import solve_fredholm_neumann

def test_neumann_convergence():
    N = 50
    x = np.linspace(0, 1, N)
    dx = x[1] - x[0]
    # K(x, y) = x * y
    K = np.outer(x, x)
    f = np.ones(N)
    # Small lambda for guaranteed contractive mapping
    phi = solve_fredholm_neumann(K, f, lam=0.5, dx=dx)
    assert np.all(phi >= f)
