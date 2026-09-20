import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from maximum_entropy_model import max_entropy_distribution

def test_maxent_mean():
    states = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
    target = 4.5
    p = max_entropy_distribution(target, states)
    assert np.isclose(np.sum(p), 1.0)
    assert np.isclose(np.sum(states * p), target, atol=1e-4)
