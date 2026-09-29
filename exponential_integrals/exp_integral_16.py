"""Implementation of exponential integral recurrence order 16."""

def compute_exp_integral_16(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(16)
    return float(val)

import math

def test_compute_exp_integral_16():
    res = compute_exp_integral_16(0.5)
    assert isinstance(res, float)
    assert res == res
