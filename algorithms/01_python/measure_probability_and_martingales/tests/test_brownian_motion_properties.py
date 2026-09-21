import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from brownian_motion_properties import simulate_brownian_path, quadratic_variation

def test_quadratic_variation_convergence():
    T = 2.0
    path = simulate_brownian_path(t_end=T, n_steps=10000, seed=42)
    qv = quadratic_variation(path)
    # Quadratic variation over [0, T] converges to T
    assert np.isclose(qv, T, rtol=0.05)
