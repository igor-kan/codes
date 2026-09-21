import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pair_production import electron_positron_threshold_energy

def test_pair_threshold():
    # 2 * 0.511 = 1.022 MeV
    assert np.isclose(electron_positron_threshold_energy(), 1.0219979)
