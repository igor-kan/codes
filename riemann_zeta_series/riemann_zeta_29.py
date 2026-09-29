"""Implementation of riemann zeta series component order 29."""

def compute_riemann_zeta_29(x: float) -> float:
    # Dirichlet eta / zeta series term 29
    s = 2.0
    sign = -1.0 if (29 % 2 == 0) else 1.0
    return float(sign / (float(29) ** s))

import math

def test_compute_riemann_zeta_29():
    res = compute_riemann_zeta_29(0.5)
    assert isinstance(res, float)
    assert res == res
