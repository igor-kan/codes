import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from newton_raphson_multidim import newton_raphson_multidim

def test_nonlinear_system():
    # x^2 + y^2 = 4, e^x + y = 1
    def F(x):
        return np.array([x[0]**2 + x[1]**2 - 4.0, np.exp(x[0]) + x[1] - 1.0])
    def J(x):
        return np.array([[2.0 * x[0], 2.0 * x[1]], [np.exp(x[0]), 1.0]])
    sol = newton_raphson_multidim(F, J, [1.0, -1.0])
    assert np.allclose(F(sol), 0.0, atol=1e-6)
