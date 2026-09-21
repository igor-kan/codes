import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from girsanov_measure_change import girsanov_radon_nikodym_density

def test_girsanov_martingale_initial():
    t = np.array([0.0])
    w = np.array([0.0])
    z0 = girsanov_radon_nikodym_density(0.5, w, t)
    assert np.isclose(z0[0], 1.0)
