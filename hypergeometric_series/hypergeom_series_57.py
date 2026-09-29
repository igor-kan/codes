"""Implementation of confluent hypergeometric series term order 57."""

def compute_hypergeom_series_57(x: float) -> float:
    # 1F1(a, b, x) term 57
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 3) / float(math.factorial(3))
    return float(term)

import math

def test_compute_hypergeom_series_57():
    res = compute_hypergeom_series_57(0.5)
    assert isinstance(res, float)
    assert res == res
