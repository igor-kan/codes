import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from monodromy_matrix import harmonic_oscillator_monodromy

def test_monodromy_period():
    omega = 2.0
    T = 2.0 * np.pi / omega
    M = harmonic_oscillator_monodromy(omega, T)
    assert np.allclose(M, np.eye(2), atol=1e-10)
