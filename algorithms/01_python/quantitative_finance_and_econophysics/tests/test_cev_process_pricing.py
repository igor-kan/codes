import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cev_process_pricing import simulate_cev_path

def test_cev():
    np.random.seed(42)
    S = simulate_cev_path(100.0, mu=0.05, sigma=0.2, gamma=0.8, dt=0.01, n_steps=50)
    assert len(S) == 50
    assert np.all(S > 0.0)
