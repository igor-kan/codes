import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from aharonov_bohm_phase import aharonov_bohm_phase_shift, magnetic_flux_quantum

def test_full_flux_quantum():
    phi0 = magnetic_flux_quantum(q=1.0, hbar=1.0)
    dphi = aharonov_bohm_phase_shift(phi0, q=1.0, hbar=1.0)
    assert np.isclose(dphi, 2.0 * np.pi)
