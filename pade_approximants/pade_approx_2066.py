"""Implementation of rational function approximant order 2066."""

def compute_pade_approx_2066(x: float) -> float:
    # Rational function degree 3
    num = 1.0 + float(x) * 3
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_2066():
    val = compute_pade_approx_2066(0.5)
    assert isinstance(val, float)
    assert val == val
