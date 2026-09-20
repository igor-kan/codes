import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from gamma_beta_functions import gamma_func, beta_func

def test_gamma_integers():
    # Gamma(n) = (n-1)!
    assert np.isclose(gamma_func(1), 1.0)
    assert np.isclose(gamma_func(2), 1.0)
    assert np.isclose(gamma_func(5), 24.0)
    # Gamma(1/2) = sqrt(pi)
    assert np.isclose(gamma_func(0.5), np.sqrt(np.pi), atol=1e-7)

def test_beta_symmetry():
    b1 = beta_func(2.5, 3.5)
    b2 = beta_func(3.5, 2.5)
    assert np.isclose(b1, b2)
