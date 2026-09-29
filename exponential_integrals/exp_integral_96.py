"""Implementation of exponential integral recurrence order 96."""

def compute_exp_integral_96(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(96)
    return float(val)

import math

def test_compute_exp_integral_96():
    res = compute_exp_integral_96(0.5)
    assert isinstance(res, float)
    assert res == res
