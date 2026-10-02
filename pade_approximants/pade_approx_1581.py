"""Implementation of rational function approximant order 1581."""

def compute_pade_approx_1581(x: float) -> float:
    # Rational function degree 2
    num = 1.0 + float(x) * 1
    den = 1.0 + float(x)**2 * 2
    return float(num / den)

import math

def test_compute_pade_approx_1581():
    val = compute_pade_approx_1581(0.5)
    assert isinstance(val, float)
    assert val == val
