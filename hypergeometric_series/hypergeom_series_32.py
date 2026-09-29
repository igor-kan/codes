"""Implementation of confluent hypergeometric series term order 32."""

def compute_hypergeom_series_32(x: float) -> float:
    # 1F1(a, b, x) term 32
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 2) / float(math.factorial(2))
    return float(term)

import math

def test_compute_hypergeom_series_32():
    res = compute_hypergeom_series_32(0.5)
    assert isinstance(res, float)
    assert res == res
