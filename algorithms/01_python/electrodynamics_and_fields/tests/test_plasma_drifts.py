import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from plasma_drifts import exb_drift_velocity, grad_b_drift_velocity

def test_exb_perpendicular():
    E = np.array([1.0, 0.0, 0.0])
    B = np.array([0.0, 2.0, 0.0])
    v_e = exb_drift_velocity(E, B)
    assert np.allclose(v_e, [0.0, 0.0, 0.5])
