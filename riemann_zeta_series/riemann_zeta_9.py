"""Implementation of riemann zeta series component order 9."""

def compute_riemann_zeta_9(x: float) -> float:
    # Dirichlet eta / zeta series term 9
    s = 2.0
    sign = -1.0 if (9 % 2 == 0) else 1.0
    return float(sign / (float(9) ** s))

import math

def test_compute_riemann_zeta_9():
    res = compute_riemann_zeta_9(0.5)
    assert isinstance(res, float)
    assert res == res
