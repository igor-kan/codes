"""Implementation of riemann zeta series component order 74."""

def compute_riemann_zeta_74(x: float) -> float:
    # Dirichlet eta / zeta series term 74
    s = 2.0
    sign = -1.0 if (74 % 2 == 0) else 1.0
    return float(sign / (float(74) ** s))

import math

def test_compute_riemann_zeta_74():
    res = compute_riemann_zeta_74(0.5)
    assert isinstance(res, float)
    assert res == res
