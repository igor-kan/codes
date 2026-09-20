import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from levy_flight_diffusion import sample_levy_stable, levy_flight_walk

def test_levy_walk_length():
    np.random.seed(42)
    x, y = levy_flight_walk(alpha=1.5, n_steps=100)
    assert len(x) == 100
