import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from adaptive_simpson import adaptive_simpson

def test_adaptive_simpson_gaussian():
    # int_{-2}^2 exp(-x^2) dx = sqrt(pi) * erf(2)
    from scipy.special import erf
    val = adaptive_simpson(lambda x: np.exp(-x**2), -2.0, 2.0, tol=1e-8)
    expected = np.sqrt(np.pi) * erf(2.0)
    assert np.isclose(val, expected, atol=1e-7)
