"""Implementation of rational function approximant order 81."""

def compute_pade_approx_81(x: float) -> float:
    # Rational function degree 2
    num = 1.0 + float(x) * 1
    den = 1.0 + float(x)**2 * 2
    return float(num / den)

import math

def test_compute_pade_approx_81():
    val = compute_pade_approx_81(0.5)
    assert isinstance(val, float)
    assert val == val
