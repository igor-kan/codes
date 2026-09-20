import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from landau_levels import landau_level_energies, magnetic_length

def test_landau_levels():
    B = 2.0
    energies = landau_level_energies(3, B=B)
    assert np.allclose(energies, [1.0, 3.0, 5.0])
    l_b = magnetic_length(B=1.0)
    assert np.isclose(l_b, 1.0)
