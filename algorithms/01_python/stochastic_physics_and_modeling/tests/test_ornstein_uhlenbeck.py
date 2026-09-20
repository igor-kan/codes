import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ornstein_uhlenbeck import simulate_ornstein_uhlenbeck

def test_mean_reversion():
    np.random.seed(42)
    # Mean reverts towards mu = 3.0
    x = simulate_ornstein_uhlenbeck(theta=2.0, mu=3.0, sigma=0.2, x0=10.0, dt=0.1, n_steps=200)
    assert np.isclose(np.mean(x[-50:]), 3.0, atol=0.2)
