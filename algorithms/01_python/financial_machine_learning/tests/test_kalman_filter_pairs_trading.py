import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from kalman_filter_pairs_trading import kalman_hedge_ratio

def test_kalman():
    x = np.linspace(1, 10, 50)
    # y = 2 * x exactly
    y = 2.0 * x
    beta = kalman_hedge_ratio(y, x)
    assert np.isclose(beta[-1], 2.0, rtol=1e-2)
