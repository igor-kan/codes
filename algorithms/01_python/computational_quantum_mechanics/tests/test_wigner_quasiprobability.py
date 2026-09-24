import numpy as np
from wigner_quasiprobability import harmonic_ground_wigner


def test_wigner_normalization():
    x = np.linspace(-4, 4, 101)
    p = np.linspace(-4, 4, 101)
    dx = x[1] - x[0]
    dp = p[1] - p[0]
    W = harmonic_ground_wigner(x, p)
    total_prob = np.sum(W) * dx * dp
    assert np.isclose(total_prob, 1.0, atol=1e-3)
