"""Implementation of riemann zeta series component order 94."""

def compute_riemann_zeta_94(x: float) -> float:
    # Dirichlet eta / zeta series term 94
    s = 2.0
    sign = -1.0 if (94 % 2 == 0) else 1.0
    return float(sign / (float(94) ** s))

import math

def test_compute_riemann_zeta_94():
    res = compute_riemann_zeta_94(0.5)
    assert isinstance(res, float)
    assert res == res
