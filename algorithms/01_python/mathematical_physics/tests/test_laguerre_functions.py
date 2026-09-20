import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from laguerre_functions import laguerre_l, hydrogenic_radial_wf

def test_laguerre_recurrence():
    x = np.linspace(0, 10, 100)
    # L_2^0(x) = 0.5 * (x^2 - 4x + 2)
    l2 = laguerre_l(2, 0.0, x)
    assert np.allclose(l2, 0.5 * (x**2 - 4 * x + 2))

def test_hydrogen_1s_norm():
    r = np.linspace(0, 20, 2000)
    # R_10(r) = 2 * e^{-r}
    r10 = hydrogenic_radial_wf(1, 0, r)
    norm = np.trapezoid(r10**2 * r**2, r)
    assert np.isclose(norm, 1.0, atol=1e-3)
