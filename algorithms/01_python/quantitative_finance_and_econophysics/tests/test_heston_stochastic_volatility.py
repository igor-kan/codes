import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from heston_stochastic_volatility import simulate_heston_path

def test_heston_simulation():
    np.random.seed(42)
    S, v = simulate_heston_path(100.0, 0.04, kappa=2.0, theta=0.04, xi=0.2, rho=-0.7, r=0.02, dt=0.01, n_steps=100)
    assert len(S) == 100
    assert np.all(S > 0.0)
