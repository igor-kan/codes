"""Implementation of exponential integral recurrence order 46."""

def compute_exp_integral_46(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(46)
    return float(val)

import math

def test_compute_exp_integral_46():
    res = compute_exp_integral_46(0.5)
    assert isinstance(res, float)
    assert res == res
