import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from quantum_scattering_partial_waves import hard_sphere_phase_shift, total_cross_section

def test_hard_sphere_low_energy():
    # At low energy k -> 0, sigma -> 4 pi a^2
    a = 1.0
    k = 1e-4
    d0 = hard_sphere_phase_shift(k, a, l=0)
    sigma = total_cross_section(k, [d0])
    assert np.isclose(sigma, 4.0 * np.pi * a**2, rtol=1e-3)
