import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from fractional_brownian_motion import fractional_brownian_motion_circulant

def test_fbm_shape():
    np.random.seed(42)
    fbm = fractional_brownian_motion_circulant(100, H=0.7)
    assert len(fbm) == 100
