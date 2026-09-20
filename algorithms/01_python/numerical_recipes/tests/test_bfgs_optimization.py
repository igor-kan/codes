import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bfgs_optimization import bfgs_optimize

def test_quadratic_bowl():
    f = lambda x: 0.5 * (x[0]**2 + 4.0 * x[1]**2)
    grad = lambda x: np.array([x[0], 4.0 * x[1]])
    sol = bfgs_optimize(f, grad, [3.0, 2.0])
    assert np.allclose(sol, 0.0, atol=1e-5)
