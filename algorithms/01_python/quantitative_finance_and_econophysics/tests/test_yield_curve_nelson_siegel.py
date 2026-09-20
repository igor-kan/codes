import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from yield_curve_nelson_siegel import nelson_siegel_zero_rate

def test_yield_curve_asymptote():
    # As t -> inf, y(t) -> beta0
    rates = nelson_siegel_zero_rate(np.array([1000.0]), beta0=0.05, beta1=-0.02, beta2=0.01, tau=2.0)
    assert np.isclose(rates[0], 0.05, atol=1e-3)
