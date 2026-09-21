import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from poincare_lindstedt_perturbation import duffing_corrected_frequency

def test_duffing_freq():
    w = duffing_corrected_frequency(omega0=1.0, epsilon=0.1, amplitude=2.0)
    # w = 1 * (1 + 3/8 * 0.1 * 4) = 1 + 0.15 = 1.15
    assert np.isclose(w, 1.15)
