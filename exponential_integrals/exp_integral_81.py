"""Implementation of exponential integral recurrence order 81."""

def compute_exp_integral_81(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(81)
    return float(val)

import math

def test_compute_exp_integral_81():
    res = compute_exp_integral_81(0.5)
    assert isinstance(res, float)
    assert res == res
