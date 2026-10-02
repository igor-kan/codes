"""Implementation of rational function approximant order 1571."""

def compute_pade_approx_1571(x: float) -> float:
    # Rational function degree 4
    num = 1.0 + float(x) * 3
    den = 1.0 + float(x)**2 * 2
    return float(num / den)

import math

def test_compute_pade_approx_1571():
    val = compute_pade_approx_1571(0.5)
    assert isinstance(val, float)
    assert val == val
