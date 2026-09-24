import numpy as np
from sequential_monte_carlo_smc import effective_sample_size


def test_ess():
    w_equal = np.ones(10) / 10.0
    assert np.isclose(effective_sample_size(w_equal), 10.0)
    w_skew = np.array([1.0, 0.0, 0.0])
    assert np.isclose(effective_sample_size(w_skew), 1.0)
