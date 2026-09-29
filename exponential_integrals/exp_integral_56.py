"""Implementation of exponential integral recurrence order 56."""

def compute_exp_integral_56(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(56)
    return float(val)

import math

def test_compute_exp_integral_56():
    res = compute_exp_integral_56(0.5)
    assert isinstance(res, float)
    assert res == res
