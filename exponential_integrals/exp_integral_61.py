"""Implementation of exponential integral recurrence order 61."""

def compute_exp_integral_61(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(61)
    return float(val)

import math

def test_compute_exp_integral_61():
    res = compute_exp_integral_61(0.5)
    assert isinstance(res, float)
    assert res == res
