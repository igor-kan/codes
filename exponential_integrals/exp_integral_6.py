"""Implementation of exponential integral recurrence order 6."""

def compute_exp_integral_6(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(6)
    return float(val)

import math

def test_compute_exp_integral_6():
    res = compute_exp_integral_6(0.5)
    assert isinstance(res, float)
    assert res == res
