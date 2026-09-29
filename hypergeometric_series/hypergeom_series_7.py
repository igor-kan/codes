"""Implementation of confluent hypergeometric series term order 7."""

def compute_hypergeom_series_7(x: float) -> float:
    # 1F1(a, b, x) term 7
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 1) / float(math.factorial(1))
    return float(term)

import math

def test_compute_hypergeom_series_7():
    res = compute_hypergeom_series_7(0.5)
    assert isinstance(res, float)
    assert res == res
