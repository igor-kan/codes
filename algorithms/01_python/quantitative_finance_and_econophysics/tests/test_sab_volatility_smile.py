import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from sab_volatility_smile import sabr_implied_volatility

def test_sabr_atm():
    # With lognormal SABR (beta = 1.0), alpha = 0.2 is the lognormal ATM vol
    v_atm = sabr_implied_volatility(100.0, 100.0, 1.0, alpha=0.2, beta=1.0, rho=-0.3, nu=0.4)
    assert 0.15 < v_atm < 0.25
