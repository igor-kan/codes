import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from black_scholes_greeks import black_scholes_call_price, black_scholes_greeks

def test_bs_greeks():
    S, K, T, r, sigma = 100.0, 100.0, 1.0, 0.05, 0.2
    c = black_scholes_call_price(S, K, T, r, sigma)
    assert c > 0.0
    delta, gamma, vega, theta, rho = black_scholes_greeks(S, K, T, r, sigma)
    assert 0.0 < delta < 1.0
    assert gamma > 0.0
    assert vega > 0.0
