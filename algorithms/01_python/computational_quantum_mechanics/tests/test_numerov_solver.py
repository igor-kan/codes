import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from numerov_solver import numerov_solve_bound_state

def test_infinite_well():
    # Infinite square well on [0, pi], E_1 = hbar^2 k^2 / 2m = 1/2 for k = 1
    L = np.pi
    x = np.linspace(0, L, 300)
    V = lambda x_val: np.zeros_like(x_val)
    psi = numerov_solve_bound_state(V, 0.5, x, hbar=1.0, m=1.0)
    # Expected is sqrt(2/pi) * sin(x)
    expected = np.sqrt(2.0 / L) * np.sin(x)
    assert np.isclose(np.abs(np.trapezoid(psi * expected, x)), 1.0, atol=1e-2)
