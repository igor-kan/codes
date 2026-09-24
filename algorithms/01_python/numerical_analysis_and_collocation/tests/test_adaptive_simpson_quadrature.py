import numpy as np
from adaptive_simpson_quadrature import adaptive_simpson


def test_adaptive_simpson():
    res = adaptive_simpson(lambda x: np.exp(-x**2), -2.0, 2.0, tol=1e-7)
    # Exact integral of exp(-x^2) over [-2, 2] is approx sqrt(pi)*erf(2) = 1.76416278
    assert np.isclose(res, 1.76416278, atol=1e-5)
