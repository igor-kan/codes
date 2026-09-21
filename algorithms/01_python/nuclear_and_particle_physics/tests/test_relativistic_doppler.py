import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from relativistic_doppler import relativistic_longitudinal_doppler, relativistic_transverse_doppler

def test_transverse_redshift():
    f = relativistic_transverse_doppler(100.0, beta=0.6)
    # gamma = 1 / sqrt(1 - 0.36) = 1 / 0.8 = 1.25 -> f = 100 * 0.8 = 80.0
    assert np.isclose(f, 80.0)
