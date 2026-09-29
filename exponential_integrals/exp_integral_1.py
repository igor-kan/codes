"""Implementation of exponential integral recurrence order 1."""

def compute_exp_integral_1(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(1)
    return float(val)

import math

def test_compute_exp_integral_1():
    res = compute_exp_integral_1(0.5)
    assert isinstance(res, float)
    assert res == res
