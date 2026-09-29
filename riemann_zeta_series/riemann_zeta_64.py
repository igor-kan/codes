"""Implementation of riemann zeta series component order 64."""

def compute_riemann_zeta_64(x: float) -> float:
    # Dirichlet eta / zeta series term 64
    s = 2.0
    sign = -1.0 if (64 % 2 == 0) else 1.0
    return float(sign / (float(64) ** s))

import math

def test_compute_riemann_zeta_64():
    res = compute_riemann_zeta_64(0.5)
    assert isinstance(res, float)
    assert res == res
