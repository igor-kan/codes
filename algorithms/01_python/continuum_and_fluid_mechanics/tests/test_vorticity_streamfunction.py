import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vorticity_streamfunction import compute_velocities_from_streamfunction

def test_streamfunction_derivatives():
    # Linear shear: psi = y^2 / 2 -> u = y, v = 0
    y = np.linspace(0, 1, 10)
    x = np.linspace(0, 1, 10)
    X, Y = np.meshgrid(x, y)
    psi = 0.5 * Y**2
    u, v = compute_velocities_from_streamfunction(psi, dx=0.1, dy=0.1)
    assert np.allclose(v, 0.0)
