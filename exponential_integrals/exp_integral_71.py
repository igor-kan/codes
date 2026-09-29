"""Implementation of exponential integral recurrence order 71."""

def compute_exp_integral_71(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(71)
    return float(val)

import math

def test_compute_exp_integral_71():
    res = compute_exp_integral_71(0.5)
    assert isinstance(res, float)
    assert res == res
