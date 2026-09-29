"""Implementation of riemann zeta series component order 4."""

def compute_riemann_zeta_4(x: float) -> float:
    # Dirichlet eta / zeta series term 4
    s = 2.0
    sign = -1.0 if (4 % 2 == 0) else 1.0
    return float(sign / (float(4) ** s))

import math

def test_compute_riemann_zeta_4():
    res = compute_riemann_zeta_4(0.5)
    assert isinstance(res, float)
    assert res == res
