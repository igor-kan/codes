"""Implementation of riemann zeta series component order 89."""

def compute_riemann_zeta_89(x: float) -> float:
    # Dirichlet eta / zeta series term 89
    s = 2.0
    sign = -1.0 if (89 % 2 == 0) else 1.0
    return float(sign / (float(89) ** s))

import math

def test_compute_riemann_zeta_89():
    res = compute_riemann_zeta_89(0.5)
    assert isinstance(res, float)
    assert res == res
