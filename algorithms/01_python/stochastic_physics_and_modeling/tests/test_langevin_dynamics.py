import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from langevin_dynamics import langevin_overdamped_step

def test_langevin_step():
    np.random.seed(42)
    x = 1.0
    x_next = langevin_overdamped_step(x, lambda q: -q, gamma=1.0, kBT=0.1, dt=0.01)
    assert np.isfinite(x_next)
