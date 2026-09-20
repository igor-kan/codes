import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from dipole_radiation import larmor_radiated_power, dipole_far_field_power_pattern

def test_larmor_power():
    p = larmor_radiated_power(q=1.0, acceleration=2.0)
    assert np.isclose(p, 4.0 / (6.0 * np.pi))
