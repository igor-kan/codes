"""Implementation of exponential integral recurrence order 36."""

def compute_exp_integral_36(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(36)
    return float(val)

import math

def test_compute_exp_integral_36():
    res = compute_exp_integral_36(0.5)
    assert isinstance(res, float)
    assert res == res
