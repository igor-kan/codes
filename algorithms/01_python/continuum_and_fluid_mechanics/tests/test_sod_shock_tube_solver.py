import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sod_shock_tube_solver import lax_friedrichs_step

def test_sod_initial_condition():
    # Sod shock tube: left (rho=1, p=1), right (rho=0.125, p=0.1)
    N = 100
    gamma = 1.4
    rho = np.where(np.arange(N) < 50, 1.0, 0.125)
    p = np.where(np.arange(N) < 50, 1.0, 0.1)
    u = np.zeros(N)
    E = p / (gamma - 1.0) + 0.5 * rho * u**2
    U = np.array([rho, rho * u, E])

    U_next = lax_friedrichs_step(U, dx=0.01, dt=0.001)
    assert U_next.shape == (3, N)
    assert np.all(U_next[0] > 0.0)  # Density remains positive
