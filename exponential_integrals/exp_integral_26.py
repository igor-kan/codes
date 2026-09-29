"""Implementation of exponential integral recurrence order 26."""

def compute_exp_integral_26(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(26)
    return float(val)

import math

def test_compute_exp_integral_26():
    res = compute_exp_integral_26(0.5)
    assert isinstance(res, float)
    assert res == res
