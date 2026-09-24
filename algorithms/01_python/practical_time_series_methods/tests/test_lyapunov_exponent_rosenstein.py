import numpy as np
from lyapunov_exponent_rosenstein import estimate_max_lyapunov_divergence


def test_lyapunov():
    x = np.random.randn(100, 2)
    div = estimate_max_lyapunov_divergence(x, max_t=5)
    assert len(div) == 5
