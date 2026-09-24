import numpy as np
from kalman_filter_beta_hedge import kalman_hedge_ratio


def test_kalman_beta():
    np.random.seed(42)
    n = 1000
    x = np.random.randn(n)
    true_beta = 1.75
    y = true_beta * x + np.random.normal(0, 0.05, n)
    
    beta_est = kalman_hedge_ratio(x, y)
    assert np.isclose(beta_est[-1], true_beta, atol=0.05)
