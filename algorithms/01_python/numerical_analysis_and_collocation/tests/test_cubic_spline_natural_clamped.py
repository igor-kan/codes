import numpy as np
from cubic_spline_natural_clamped import natural_cubic_spline_coefficients


def test_spline():
    x = np.array([0.0, 1.0, 2.0, 3.0])
    y = np.array([1.0, 2.0, 0.0, 2.0])
    M = natural_cubic_spline_coefficients(x, y)
    assert len(M) == 4
    assert np.isclose(M[0], 0.0)  # Natural boundary condition
    assert np.isclose(M[-1], 0.0)
