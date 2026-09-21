import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from relativistic_invariant_mass import invariant_mass

def test_two_photons():
    # Two back-to-back 511 keV photons from positron annihilation
    p1 = [0.511, 0.511, 0.0, 0.0]
    p2 = [0.511, -0.511, 0.0, 0.0]
    m = invariant_mass([p1, p2])
    assert np.isclose(m, 1.022)
