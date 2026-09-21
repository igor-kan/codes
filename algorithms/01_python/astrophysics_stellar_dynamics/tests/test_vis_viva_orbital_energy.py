import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vis_viva_orbital_energy import orbital_velocity

def test_circular_velocity():
    # For r = a, v = sqrt(GM / r)
    assert np.isclose(orbital_velocity(1.0, 1.0, GM=4.0), 2.0)
