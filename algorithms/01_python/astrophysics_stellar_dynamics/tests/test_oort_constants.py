import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from oort_constants import oort_constants, radial_velocity_oort

def test_flat_rotation_curve():
    # Flat curve dTheta/dr = 0 -> A = -B = 0.5 * Theta0 / r0
    A, B = oort_constants(theta0=220.0, r0=8.0, dtheta_dr=0.0)
    assert np.isclose(A, -B)
    assert np.isclose(A, 13.75)
