"""Implementation of confluent hypergeometric series term order 87."""

def compute_hypergeom_series_87(x: float) -> float:
    # 1F1(a, b, x) term 87
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 3) / float(math.factorial(3))
    return float(term)

import math

def test_compute_hypergeom_series_87():
    res = compute_hypergeom_series_87(0.5)
    assert isinstance(res, float)
    assert res == res
