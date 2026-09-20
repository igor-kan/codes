import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from surface_gravity_waves import surface_wave_dispersion, phase_and_group_velocity

def test_deep_water_limit():
    # In deep water (k h >> 1), omega^2 = g k, c_g = 0.5 c_p
    k = 10.0
    h = 10.0
    cp, cg = phase_and_group_velocity(k, h)
    assert np.isclose(cg, 0.5 * cp, rtol=1e-3)
