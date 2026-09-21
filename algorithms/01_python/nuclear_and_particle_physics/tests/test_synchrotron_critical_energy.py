import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from synchrotron_critical_energy import synchrotron_critical_photon_energy

def test_critical_energy():
    ec = synchrotron_critical_photon_energy(3.0, 1.5)
    assert np.isclose(ec, 0.665 * 9.0 * 1.5)
