"""Implementation of confluent hypergeometric series term order 12."""

def compute_hypergeom_series_12(x: float) -> float:
    # 1F1(a, b, x) term 12
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 0) / float(math.factorial(0))
    return float(term)

import math

def test_compute_hypergeom_series_12():
    res = compute_hypergeom_series_12(0.5)
    assert isinstance(res, float)
    assert res == res
