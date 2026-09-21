import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from helmholtz_greens_function_3d import helmholtz_greens_function

def test_helmholtz_decay():
    r1 = np.array([0.0, 0.0, 1.0])
    r2 = np.array([0.0, 0.0, 2.0])
    origin = np.array([0.0, 0.0, 0.0])
    g1 = helmholtz_greens_function(r1, origin, k=1.0)
    g2 = helmholtz_greens_function(r2, origin, k=1.0)
    assert np.isclose(abs(g1) / abs(g2), 2.0)
