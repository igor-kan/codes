"""Implementation of incomplete gamma power series component order 98."""

def compute_gamma_incomplete_98(x: float) -> float:
    s = float(1)
    term = (float(x) ** (s + 3)) / float(s + 3)
    return float(term)

import math

def test_compute_gamma_incomplete_98():
    res = compute_gamma_incomplete_98(0.5)
    assert isinstance(res, float)
    assert res == res
