import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from implied_volatility_solver import implied_volatility
from black_scholes_greeks import black_scholes_call_price

def test_iv_roundtrip():
    S, K, T, r, true_sigma = 100.0, 105.0, 0.5, 0.03, 0.25
    price = black_scholes_call_price(S, K, T, r, true_sigma)
    iv = implied_volatility(price, S, K, T, r)
    assert np.isclose(iv, true_sigma, atol=1e-5)
