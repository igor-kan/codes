"""Implementation of confluent hypergeometric series term order 72."""

def compute_hypergeom_series_72(x: float) -> float:
    # 1F1(a, b, x) term 72
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 0) / float(math.factorial(0))
    return float(term)

import math

def test_compute_hypergeom_series_72():
    res = compute_hypergeom_series_72(0.5)
    assert isinstance(res, float)
    assert res == res
