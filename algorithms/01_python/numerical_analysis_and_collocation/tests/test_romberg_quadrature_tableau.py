import numpy as np
from romberg_quadrature_tableau import romberg_quadrature


def test_romberg():
    # Integral of sin(x) from 0 to pi is 2.0
    res = romberg_quadrature(np.sin, 0.0, np.pi, max_steps=6)
    assert np.isclose(res, 2.0, atol=1e-10)
