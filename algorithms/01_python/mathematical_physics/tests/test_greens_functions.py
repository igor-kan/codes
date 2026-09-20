import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from greens_functions import solve_poisson_1d

def test_constant_source():
    # -y'' = 1 with y(0) = y(1) = 0 -> y(x) = 0.5 * x * (1 - x)
    x, y = solve_poisson_1d(lambda s: np.ones_like(s), L=1.0, n_points=100)
    expected = 0.5 * x * (1.0 - x)
    assert np.allclose(y, expected, atol=1e-3)
