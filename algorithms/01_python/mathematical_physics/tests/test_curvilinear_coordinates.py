import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from curvilinear_coordinates import CurvilinearSystem

def test_spherical_laplacian_1_over_r():
    sys_sph = CurvilinearSystem("spherical")
    # For f(r, theta, phi) = r^2, div(grad r^2) = 1/r^2 d/dr (r^2 * 2r) = 6
    lap = sys_sph.laplacian_scalar(lambda r, t, p: r**2, 2.0, np.pi / 4.0, 0.0)
    assert np.isclose(lap, 6.0, atol=1e-3)
