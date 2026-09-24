import numpy as np
from scipy.special import gammaln
from stirling_asymptotic_gamma_expansion import stirling_log_gamma


def test_stirling():
    n = 10.0
    exact = gammaln(n)
    approx = stirling_log_gamma(n)
    assert np.isclose(exact, approx, atol=1e-4)
