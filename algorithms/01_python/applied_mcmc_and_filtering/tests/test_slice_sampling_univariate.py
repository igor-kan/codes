import numpy as np
from slice_sampling_univariate import slice_sample_1d


def test_slice():
    log_std_norm = lambda x: -0.5 * x**2
    samples = slice_sample_1d(log_std_norm, 0.0, 500)
    assert np.isclose(np.mean(samples), 0.0, atol=0.2)
