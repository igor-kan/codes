import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stellar_hydrostatic import central_pressure_estimate

def test_central_pressure():
    p = central_pressure_estimate(1e30, 1e9, G=1.0)
    assert np.isclose(p, 1e24)
