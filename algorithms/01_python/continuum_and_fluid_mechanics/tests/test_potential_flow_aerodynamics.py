import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from potential_flow_aerodynamics import point_vortex_velocity

def test_vortex_velocity():
    # Vortex at origin with Gamma = 2 pi
    # At (1, 0), v = (0, 1)
    v = point_vortex_velocity(2.0 * np.pi, np.array([0.0, 0.0]), np.array([1.0, 0.0]))
    assert np.allclose(v, [0.0, 1.0])
