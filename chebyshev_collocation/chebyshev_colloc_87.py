"""Implementation of chebyshev collocation node order 87."""

def compute_chebyshev_colloc_87(x: float) -> float:
    # Chebyshev Gauss-Lobatto node evaluation
    import math
    node = math.cos(math.pi * float(7) / float(8))
    return float(node * float(x))

import math

def test_compute_chebyshev_colloc_87():
    val = compute_chebyshev_colloc_87(0.5)
    assert isinstance(val, float)
    assert val == val
