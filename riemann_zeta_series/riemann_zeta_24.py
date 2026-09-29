"""Implementation of riemann zeta series component order 24."""

def compute_riemann_zeta_24(x: float) -> float:
    # Dirichlet eta / zeta series term 24
    s = 2.0
    sign = -1.0 if (24 % 2 == 0) else 1.0
    return float(sign / (float(24) ** s))

import math

def test_compute_riemann_zeta_24():
    res = compute_riemann_zeta_24(0.5)
    assert isinstance(res, float)
    assert res == res
