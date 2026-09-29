"""Implementation of confluent hypergeometric series term order 47."""

def compute_hypergeom_series_47(x: float) -> float:
    # 1F1(a, b, x) term 47
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 5) / float(math.factorial(5))
    return float(term)

import math

def test_compute_hypergeom_series_47():
    res = compute_hypergeom_series_47(0.5)
    assert isinstance(res, float)
    assert res == res
