import numpy as np
from euler_maclaurin_summation_formula import euler_maclaurin_leading


def test_em():
    f = lambda x: x**2
    fp = lambda x: 2.0 * x
    exact_sum = sum(k**2 for k in range(1, 11))
    approx = euler_maclaurin_leading(f, fp, 1, 10)
    assert np.isclose(exact_sum, approx, atol=1e-5)
