import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_berry_phase import spin_half_berry_phase

def test_berry_phase_hemisphere():
    # Solid angle of hemisphere is 2 pi -> gamma = -pi
    gamma = spin_half_berry_phase(2.0 * np.pi)
    assert np.isclose(gamma, -np.pi)
