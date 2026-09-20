import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bremsstrahlung_spectrum import bremsstrahlung_spectrum_kramer

def test_bremsstrahlung_cutoff():
    val = bremsstrahlung_spectrum_kramer(omega=5.0, e_initial=10.0, Z=1.0)
    assert np.isclose(val, 5.0)
    cutoff = bremsstrahlung_spectrum_kramer(omega=12.0, e_initial=10.0, Z=1.0)
    assert cutoff == 0.0
