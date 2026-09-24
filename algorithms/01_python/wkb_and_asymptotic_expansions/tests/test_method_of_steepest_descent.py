import numpy as np
from method_of_steepest_descent import saddle_point_gaussian_integral


def test_saddle():
    res = saddle_point_gaussian_integral(f0=0.0, f_double_prime=2.0, lam=10.0)
    # Integral of exp(-10 * x^2) is sqrt(pi / 10)
    assert np.isclose(res, np.sqrt(np.pi / 10.0))
