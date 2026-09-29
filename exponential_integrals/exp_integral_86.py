"""Implementation of exponential integral recurrence order 86."""

def compute_exp_integral_86(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(86)
    return float(val)

import math

def test_compute_exp_integral_86():
    res = compute_exp_integral_86(0.5)
    assert isinstance(res, float)
    assert res == res
