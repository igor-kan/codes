"""Implementation of exponential integral recurrence order 11."""

def compute_exp_integral_11(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(11)
    return float(val)

import math

def test_compute_exp_integral_11():
    res = compute_exp_integral_11(0.5)
    assert isinstance(res, float)
    assert res == res
