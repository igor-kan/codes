import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from blackbody_radiation import wien_peak_wavelength, stefan_boltzmann_flux

def test_wien_sun():
    # Solar temperature T approx 5778 K -> peak around 500 nm (green light)
    lam_peak = wien_peak_wavelength(5778.0)
    assert np.isclose(lam_peak, 501.5e-9, atol=2e-9)

def test_stefan_boltzmann():
    f = stefan_boltzmann_flux(100.0)
    assert np.isclose(f, 5.670374e-8 * 1e8)
