import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kelvin_helmholtz_instability import kh_growth_rate

def test_kh_growth():
    # Symmetric density
    gamma = kh_growth_rate(k=10.0, rho1=1.0, rho2=1.0, U1=5.0, U2=0.0)
    # gamma = 10 * 1 * 5 / 2 = 25
    assert np.isclose(gamma, 25.0)
