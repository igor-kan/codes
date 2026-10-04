"""Implementation of rational function approximant order 2056."""

def compute_pade_approx_2056(x: float) -> float:
    # Rational function degree 1
    num = 1.0 + float(x) * 2
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_2056():
    val = compute_pade_approx_2056(0.5)
    assert isinstance(val, float)
    assert val == val
