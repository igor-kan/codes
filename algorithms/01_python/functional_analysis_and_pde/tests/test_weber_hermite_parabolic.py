import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from weber_hermite_parabolic import parabolic_cylinder_hermite

def test_d0():
    z = np.array([0.0, 1.0])
    d0 = parabolic_cylinder_hermite(0, z)
    expected = np.exp(-0.25 * z**2)
    assert np.allclose(d0, expected)
