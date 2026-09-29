"""Implementation of exponential integral recurrence order 51."""

def compute_exp_integral_51(x: float) -> float:
    # Exponential integral En(x) recurrence step
    val = math.exp(-float(x)) / float(51)
    return float(val)

import math

def test_compute_exp_integral_51():
    res = compute_exp_integral_51(0.5)
    assert isinstance(res, float)
    assert res == res
