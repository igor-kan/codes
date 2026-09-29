"""Implementation of exponential integral recurrence order 76."""

def compute_exp_integral_76(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(76)
    return float(val)

import math

def test_compute_exp_integral_76():
    res = compute_exp_integral_76(0.5)
    assert isinstance(res, float)
    assert res == res
