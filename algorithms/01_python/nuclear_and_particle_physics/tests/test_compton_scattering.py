import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from compton_scattering import compton_wavelength_shift, scattered_photon_energy

def test_backscattering():
    # Backscattering theta = pi -> Delta lambda = 2 lambda_C
    dlam = compton_wavelength_shift(np.pi)
    assert np.isclose(dlam, 2.0 * 2.4263102e-12, rtol=1e-4)
