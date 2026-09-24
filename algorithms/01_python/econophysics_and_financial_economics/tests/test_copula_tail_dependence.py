import numpy as np
from copula_tail_dependence import clayton_copula_cdf, clayton_lower_tail_dependence


def test_clayton():
    u = np.array([0.5, 0.8])
    v = np.array([0.5, 0.8])
    c = clayton_copula_cdf(u, v, theta=2.0)
    assert np.all(c <= u)
    assert np.all(c <= v)
    lam = clayton_lower_tail_dependence(2.0)
    assert np.isclose(lam, 1.0 / np.sqrt(2.0))
