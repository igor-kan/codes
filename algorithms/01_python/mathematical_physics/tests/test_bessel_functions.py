import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from bessel_functions import bessel_j0, bessel_jn_miller
from scipy.special import jv

def test_bessel_j0():
    for x in [0.0, 1.0, 2.4048255577, 5.0, 10.0]:
        assert np.isclose(bessel_j0(x), jv(0, x), atol=1e-5)

def test_bessel_jn_miller():
    for n in [1, 2, 3]:
        for x in [1.5, 3.83, 7.0]:
            assert np.isclose(bessel_jn_miller(n, x), jv(n, x), atol=1e-4)
