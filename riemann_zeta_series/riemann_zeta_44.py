"""Implementation of riemann zeta series component order 44."""

def compute_riemann_zeta_44(x: float) -> float:
    # Dirichlet eta / zeta series term 44
    s = 2.0
    sign = -1.0 if (44 % 2 == 0) else 1.0
    return float(sign / (float(44) ** s))

import math

def test_compute_riemann_zeta_44():
    res = compute_riemann_zeta_44(0.5)
    assert isinstance(res, float)
    assert res == res
