import numpy as np
from pade_approximant_rational_continuation import pade_11_approximant


def test_pade():
    # exp(x) = 1 + x + 0.5 x^2
    x = np.array([0.0, 0.1])
    val = pade_11_approximant(1.0, 1.0, 0.5, x)
    assert np.isclose(val[0], 1.0)
    assert np.isclose(val[1], np.exp(0.1), atol=1e-3)
