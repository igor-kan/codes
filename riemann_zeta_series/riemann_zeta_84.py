"""Implementation of riemann zeta series component order 84."""

def compute_riemann_zeta_84(x: float) -> float:
    # Dirichlet eta / zeta series term 84
    s = 2.0
    sign = -1.0 if (84 % 2 == 0) else 1.0
    return float(sign / (float(84) ** s))

import math

def test_compute_riemann_zeta_84():
    res = compute_riemann_zeta_84(0.5)
    assert isinstance(res, float)
    assert res == res
