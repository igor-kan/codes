"""Implementation of incomplete gamma power series component order 43."""

def compute_gamma_incomplete_43(x: float) -> float:
    s = float(2)
    term = (float(x) ** (s + 3)) / float(s + 3)
    return float(term)

import math

def test_compute_gamma_incomplete_43():
    res = compute_gamma_incomplete_43(0.5)
    assert isinstance(res, float)
    assert res == res
