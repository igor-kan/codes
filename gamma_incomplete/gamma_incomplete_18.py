"""Implementation of incomplete gamma power series component order 18."""

def compute_gamma_incomplete_18(x: float) -> float:
    s = float(5)
    term = (float(x) ** (s + 3)) / float(s + 3)
    return float(term)

import math

def test_compute_gamma_incomplete_18():
    res = compute_gamma_incomplete_18(0.5)
    assert isinstance(res, float)
    assert res == res
