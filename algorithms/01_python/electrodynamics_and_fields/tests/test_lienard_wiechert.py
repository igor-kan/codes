import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lienard_wiechert import lienard_wiechert_potentials

def test_stationary_charge():
    r_obs = np.array([3.0, 4.0, 0.0])
    r_src = np.array([0.0, 0.0, 0.0])
    v_src = np.array([0.0, 0.0, 0.0])
    phi, A = lienard_wiechert_potentials(1.0, r_obs, r_src, v_src)
    # R = 5, Phi = 1 / (4 pi * 5)
    assert np.isclose(phi, 1.0 / (20.0 * np.pi))
    assert np.allclose(A, 0.0)
