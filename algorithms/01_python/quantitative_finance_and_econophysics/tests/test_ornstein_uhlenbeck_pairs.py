import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ornstein_uhlenbeck_pairs import estimate_ou_parameters

def test_ou_calibration():
    np.random.seed(42)
    # Synthetic AR(1)
    spread = np.zeros(500)
    for t in range(1, 500):
        spread[t] = 0.9 * spread[t - 1] + np.random.normal(0, 0.1)
    theta, mu, sigma = estimate_ou_parameters(spread, dt=1.0)
    assert theta > 0.0
