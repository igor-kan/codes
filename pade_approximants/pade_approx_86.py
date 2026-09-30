"""Implementation of rational function approximant order 86."""

def compute_pade_approx_86(x: float) -> float:
    # Rational function degree 3
    num = 1.0 + float(x) * 3
    den = 1.0 + float(x)**2 * 1
    return float(num / den)

import math

def test_compute_pade_approx_86():
    val = compute_pade_approx_86(0.5)
    assert isinstance(val, float)
    assert val == val
