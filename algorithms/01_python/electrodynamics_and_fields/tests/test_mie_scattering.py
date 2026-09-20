import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mie_scattering import rayleigh_scattering_cross_section

def test_rayleigh_lambda_fourth():
    # Wavelength halved -> cross section increases by 2^4 = 16
    s1 = rayleigh_scattering_cross_section(1e-8, 600e-9, 1.5)
    s2 = rayleigh_scattering_cross_section(1e-8, 300e-9, 1.5)
    assert np.isclose(s2 / s1, 16.0, rtol=1e-4)
