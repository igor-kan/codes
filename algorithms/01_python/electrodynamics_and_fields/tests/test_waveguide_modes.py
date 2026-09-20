import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from waveguide_modes import rectangular_waveguide_cutoff, waveguide_propagation_constant

def test_te10_dominant_mode():
    a, b = 0.02, 0.01  # 2cm x 1cm standard X-band
    fc_10 = rectangular_waveguide_cutoff(1, 0, a, b)
    fc_01 = rectangular_waveguide_cutoff(0, 1, a, b)
    # TE10 cutoff should be half of TE01 cutoff
    assert np.isclose(fc_10 * 2.0, fc_01)
    beta = waveguide_propagation_constant(fc_10 * 1.5, fc_10)
    assert beta > 0.0
