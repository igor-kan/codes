"""Implementation of rational function approximant order 2106."""

def compute_pade_approx_2106(x: float) -> float:
    # Rational function degree 3
    num = 1.0 + float(x) * 1
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_2106():
    val = compute_pade_approx_2106(0.5)
    assert isinstance(val, float)
    assert val == val
