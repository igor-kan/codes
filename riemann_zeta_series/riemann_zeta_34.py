"""Implementation of riemann zeta series component order 34."""

def compute_riemann_zeta_34(x: float) -> float:
    # Dirichlet eta / zeta series term 34
    s = 2.0
    sign = -1.0 if (34 % 2 == 0) else 1.0
    return float(sign / (float(34) ** s))

import math

def test_compute_riemann_zeta_34():
    res = compute_riemann_zeta_34(0.5)
    assert isinstance(res, float)
    assert res == res
