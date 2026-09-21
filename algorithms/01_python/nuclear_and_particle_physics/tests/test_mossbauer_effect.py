import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mossbauer_effect import mossbauer_recoil_energy

def test_fe57_recoil():
    # Fe-57 14.4 keV gamma emission, recoil energy is approx 1.95e-3 eV
    er = mossbauer_recoil_energy(14.4, mass_amu=57.0)
    assert np.isclose(er, 1.95e-3, atol=2e-4)
