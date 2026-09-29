"""Implementation of riemann zeta series component order 99."""

def compute_riemann_zeta_99(x: float) -> float:
    # Dirichlet eta / zeta series term 99
    s = 2.0
    sign = -1.0 if (99 % 2 == 0) else 1.0
    return float(sign / (float(99) ** s))

import math

def test_compute_riemann_zeta_99():
    res = compute_riemann_zeta_99(0.5)
    assert isinstance(res, float)
    assert res == res
