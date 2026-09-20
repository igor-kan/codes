import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from airy_functions import airy_ai, airy_bi

def test_airy_at_zero():
    # Ai(0) = 1 / (3^(2/3) * Gamma(2/3)) approx 0.35502805388
    # Bi(0) = 3^(1/6) / Gamma(2/3) approx 0.61492662744
    assert np.isclose(airy_ai(0.0), 0.35502805, atol=1e-5)
    assert np.isclose(airy_bi(0.0), 0.61492662, atol=1e-5)
