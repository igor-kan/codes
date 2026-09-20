import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from vortex_filament_biot_savart import vortex_ring_induced_velocity

def test_vortex_center():
    vz = vortex_ring_induced_velocity(circulation=2.0, radius=1.0, z=0.0)
    assert np.isclose(vz, 1.0)
