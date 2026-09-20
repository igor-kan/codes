import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kelvin_helmholtz_instability import kh_growth_rate

def test_kh_rate():
    sigma = kh_growth_rate(k=1.0, rho1=1.0, rho2=1.0, U1=2.0, U2=-2.0)
    assert np.isclose(sigma, 2.0)
