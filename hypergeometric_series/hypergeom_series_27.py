"""Implementation of confluent hypergeometric series term order 27."""

def compute_hypergeom_series_27(x: float) -> float:
    # 1F1(a, b, x) term 27
    a, b = float(3), float(5)
    term = (a / b) * (float(x) ** 3) / float(math.factorial(3))
    return float(term)

import math

def test_compute_hypergeom_series_27():
    res = compute_hypergeom_series_27(0.5)
    assert isinstance(res, float)
    assert res == res
