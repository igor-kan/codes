import os, sys, numpy as np
from scipy.special import j0
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bessel_asymptotic_expansion import bessel_j0_asymptotic

def test_bessel_asymptotic():
    x = 20.0
    approx = bessel_j0_asymptotic(x)
    exact = j0(x)
    assert np.isclose(approx, exact, atol=1e-3)
