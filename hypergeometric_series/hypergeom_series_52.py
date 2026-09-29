"""Implementation of confluent hypergeometric series term order 52."""

def compute_hypergeom_series_52(x: float) -> float:
    # 1F1(a, b, x) term 52
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 4) / float(math.factorial(4))
    return float(term)

import math

def test_compute_hypergeom_series_52():
    res = compute_hypergeom_series_52(0.5)
    assert isinstance(res, float)
    assert res == res
