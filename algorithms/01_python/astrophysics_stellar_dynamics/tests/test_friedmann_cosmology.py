import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from friedmann_cosmology import hubble_parameter_z

def test_hubble_today():
    H_0 = hubble_parameter_z(z=0.0, H0=70.0, Om_m=0.3, Om_lambda=0.7, Om_r=0.0)
    assert np.isclose(H_0, 70.0)
