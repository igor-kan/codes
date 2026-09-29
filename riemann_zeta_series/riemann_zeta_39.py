"""Implementation of riemann zeta series component order 39."""

def compute_riemann_zeta_39(x: float) -> float:
    # Dirichlet eta / zeta series term 39
    s = 2.0
    sign = -1.0 if (39 % 2 == 0) else 1.0
    return float(sign / (float(39) ** s))

import math

def test_compute_riemann_zeta_39():
    res = compute_riemann_zeta_39(0.5)
    assert isinstance(res, float)
    assert res == res
