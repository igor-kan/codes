import os, sys, numpy as np
from scipy.special import gammaln
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from stirling_asymptotic_series import stirling_ln_gamma

def test_stirling_accuracy():
    z = 10.0
    approx = stirling_ln_gamma(z)
    exact = gammaln(z)
    assert np.isclose(approx, exact, atol=1e-7)
