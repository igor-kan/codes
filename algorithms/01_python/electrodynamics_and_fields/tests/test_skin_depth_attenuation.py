import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from skin_depth_attenuation import skin_depth

def test_skin_depth_scaling():
    # Frequency x4 -> skin depth / 2
    d1 = skin_depth(1.0, 1.0)
    d2 = skin_depth(4.0, 1.0)
    assert np.isclose(d1, 2.0 * d2)
