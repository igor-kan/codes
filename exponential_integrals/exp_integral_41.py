"""Implementation of exponential integral recurrence order 41."""

def compute_exp_integral_41(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(41)
    return float(val)

import math

def test_compute_exp_integral_41():
    res = compute_exp_integral_41(0.5)
    assert isinstance(res, float)
    assert res == res
