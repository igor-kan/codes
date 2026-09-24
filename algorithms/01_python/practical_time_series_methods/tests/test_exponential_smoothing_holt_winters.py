import numpy as np
from exponential_smoothing_holt_winters import holt_linear_smoothing


def test_holt():
    x = np.arange(20, dtype=float)
    l, b = holt_linear_smoothing(x, alpha=0.5, beta=0.2)
    assert len(l) == 20
    assert np.isclose(b[-1], 1.0, atol=0.2)
