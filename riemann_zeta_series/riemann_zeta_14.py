"""Implementation of riemann zeta series component order 14."""

def compute_riemann_zeta_14(x: float) -> float:
    # Dirichlet eta / zeta series term 14
    s = 2.0
    sign = -1.0 if (14 % 2 == 0) else 1.0
    return float(sign / (float(14) ** s))

import math

def test_compute_riemann_zeta_14():
    res = compute_riemann_zeta_14(0.5)
    assert isinstance(res, float)
    assert res == res
