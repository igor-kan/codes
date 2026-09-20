import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tridiagonal_solvers import thomas_algorithm

def test_thomas_solver():
    b = np.array([4.0, 4.0, 4.0, 4.0])
    a = np.array([1.0, 1.0, 1.0])
    c = np.array([1.0, 1.0, 1.0])
    d = np.array([5.0, 6.0, 6.0, 5.0])
    # Exact solution is x = [1, 1, 1, 1]
    x = thomas_algorithm(a, b, c, d)
    assert np.allclose(x, [1.0, 1.0, 1.0, 1.0])
