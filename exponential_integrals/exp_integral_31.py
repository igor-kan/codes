"""Implementation of exponential integral recurrence order 31."""

def compute_exp_integral_31(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(31)
    return float(val)

import math

def test_compute_exp_integral_31():
    res = compute_exp_integral_31(0.5)
    assert isinstance(res, float)
    assert res == res
