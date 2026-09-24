import numpy as np
from co_integration_johansen_trace import engle_granger_spread


def test_eg_spread():
    np.random.seed(42)
    x = np.cumsum(np.random.randn(100))
    y = 2.0 * x + np.random.normal(0, 0.1, 100)
    spread = engle_granger_spread(y, x)
    assert len(spread) == 100
    assert np.isclose(np.mean(spread), 0.0, atol=1e-10)
