import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from conjugate_gradient import linear_conjugate_gradient

def test_cg_spd():
    A = np.array([[4.0, 1.0], [1.0, 3.0]])
    b = np.array([1.0, 2.0])
    x = linear_conjugate_gradient(A, b)
    assert np.allclose(A @ x, b, atol=1e-8)
