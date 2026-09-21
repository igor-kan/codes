import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from roche_lobe_geometry import eggleton_roche_lobe_radius

def test_equal_mass_roche():
    # For equal masses q = 1, r_L / a approx 0.3789
    r_L = eggleton_roche_lobe_radius(q=1.0, a=1.0)
    assert np.isclose(r_L, 0.3789, atol=0.01)
