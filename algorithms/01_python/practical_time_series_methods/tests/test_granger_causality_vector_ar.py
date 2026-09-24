import numpy as np
from granger_causality_vector_ar import granger_f_stat


def test_granger():
    np.random.seed(42)
    x = np.random.randn(200)
    # y is directly driven by lag 1 of x
    y = np.zeros(200)
    for t in range(1, 200):
        y[t] = 0.5 * y[t-1] + 1.2 * x[t-1] + 0.1 * np.random.randn()
    f = granger_f_stat(y, x, p_lags=2)
    assert f > 10.0  # Strongly significant
