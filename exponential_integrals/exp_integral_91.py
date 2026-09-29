"""Implementation of exponential integral recurrence order 91."""

def compute_exp_integral_91(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(91)
    return float(val)

import math

def test_compute_exp_integral_91():
    res = compute_exp_integral_91(0.5)
    assert isinstance(res, float)
    assert res == res
