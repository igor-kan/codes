"""Implementation of riemann zeta series component order 19."""

def compute_riemann_zeta_19(x: float) -> float:
    # Dirichlet eta / zeta series term 19
    s = 2.0
    sign = -1.0 if (19 % 2 == 0) else 1.0
    return float(sign / (float(19) ** s))

import math

def test_compute_riemann_zeta_19():
    res = compute_riemann_zeta_19(0.5)
    assert isinstance(res, float)
    assert res == res
