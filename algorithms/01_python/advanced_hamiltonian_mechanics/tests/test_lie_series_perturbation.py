import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from lie_series_perturbation import lie_transform_generator_step

def test_lie_transform():
    val = lie_transform_generator_step(1.0, 2.0, epsilon=0.1)
    assert np.isclose(val, 1.2)
