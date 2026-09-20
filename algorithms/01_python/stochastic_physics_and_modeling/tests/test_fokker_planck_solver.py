import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fokker_planck_solver import solve_fokker_planck_step

def test_fokker_planck_conservation():
    x = np.linspace(-5, 5, 100)
    dx = x[1] - x[0]
    P0 = np.exp(-x**2) / np.sqrt(np.pi)
    drift = -x
    diff = np.ones_like(x) * 2.0
    P1 = solve_fokker_planck_step(P0, drift, diff, dx, dt=0.001)
    # Total probability remains 1.0
    assert np.isclose(np.sum(P1) * dx, 1.0, atol=1e-3)
