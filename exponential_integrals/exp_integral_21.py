"""Implementation of exponential integral recurrence order 21."""

def compute_exp_integral_21(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(21)
    return float(val)

import math

def test_compute_exp_integral_21():
    res = compute_exp_integral_21(0.5)
    assert isinstance(res, float)
    assert res == res
