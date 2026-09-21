import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sedov_von_neumann_blast_scaling import blast_radius

def test_blast_wave_scaling():
    t1 = 0.01
    t2 = 0.04
    r1 = blast_radius(np.array([t1]), 1e14, 1.2)[0]
    r2 = blast_radius(np.array([t2]), 1e14, 1.2)[0]
    # (4)^(0.4) approx 1.7411
    ratio = r2 / r1
    assert np.isclose(ratio, 4.0**0.4)
