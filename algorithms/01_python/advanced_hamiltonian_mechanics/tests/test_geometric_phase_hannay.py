import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from geometric_phase_hannay import hannay_angle_circle

def test_hannay_angle():
    assert np.isclose(hannay_angle_circle(np.pi), -np.pi)
