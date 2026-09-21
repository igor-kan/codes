import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from cosmological_distances import luminosity_distance

def test_dl_hubble_law():
    # At very small z, d_L approx c z / H0
    dl = luminosity_distance(0.01, H0=70.0)
    expected = 299792.458 * 0.01 / 70.0
    assert np.isclose(dl, expected, rtol=0.02)
