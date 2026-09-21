import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fokker_planck_drift_diffusion import step_fokker_planck

def test_fp_conservation():
    N = 100
    dx = 0.1
    x = np.linspace(-5, 5, N)
    p0 = np.exp(-x**2) / np.sqrt(np.pi)
    p1 = step_fokker_planck(p0, dx=dx, dt=0.001, mu=0.0, D=1.0)
    assert np.isclose(np.sum(p1 * dx), 1.0)
