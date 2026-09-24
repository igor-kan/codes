import numpy as np
from cross_correlation_lead_lag import lead_lag_correlation


def test_lead_lag():
    x = np.random.randn(100)
    # y lags x by 3 steps
    y = np.roll(x, 3)
    lags, corr, opt_lag = lead_lag_correlation(x, y, max_lag=10)
    assert opt_lag == 3
