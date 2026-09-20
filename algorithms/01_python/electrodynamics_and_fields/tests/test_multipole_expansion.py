import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from multipole_expansion import multipole_moments

def test_dipole_pair():
    # +q at (0, 0, d/2) and -q at (0, 0, -d/2)
    charges = [1.0, -1.0]
    positions = [[0.0, 0.0, 1.0], [0.0, 0.0, -1.0]]
    q_tot, p, quad = multipole_moments(charges, positions)
    assert np.isclose(q_tot, 0.0)
    assert np.allclose(p, [0.0, 0.0, 2.0])
    # Quadrupole is traceless
    assert np.isclose(np.trace(quad), 0.0)
