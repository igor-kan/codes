import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from navier_stokes_chorin import IncompressibleNavierStokes2D

def test_chorin_step():
    solver = IncompressibleNavierStokes2D(20, 20)
    u = np.zeros((20, 20))
    v = np.zeros((20, 20))
    p = np.zeros((20, 20))
    u[-1, :] = 1.0  # Lid velocity
    u_new, v_new, p_new = solver.step(u, v, p, dt=0.001)
    assert u_new.shape == (20, 20)
    assert np.all(np.isfinite(u_new))
