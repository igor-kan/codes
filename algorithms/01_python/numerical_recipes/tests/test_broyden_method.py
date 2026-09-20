import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from broyden_method import broyden_solve

def test_broyden():
    F = lambda x: np.array([x[0] + 2*x[1] - 2, x[0]**2 + 4*x[1]**2 - 4])
    sol = broyden_solve(F, [1.5, 0.5])
    assert np.allclose(F(sol), 0.0, atol=1e-5)
