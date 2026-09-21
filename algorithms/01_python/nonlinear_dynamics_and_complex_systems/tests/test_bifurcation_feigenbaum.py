import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bifurcation_feigenbaum import generate_orbit_diagram_slice

def test_period_1_fixed_point():
    # r = 2.0 -> fixed point at 1 - 1/r = 0.5
    orb = generate_orbit_diagram_slice(2.0)
    assert np.allclose(orb, 0.5)
