import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from merton_jump_diffusion import simulate_merton_jumps

def test_merton_simulation():
    np.random.seed(42)
    S = simulate_merton_jumps(100.0, mu=0.05, sigma=0.15, lambda_jump=1.0, mu_jump=-0.05, sigma_jump=0.1, dt=0.01, n_steps=100)
    assert len(S) == 100
    assert np.all(S > 0.0)
