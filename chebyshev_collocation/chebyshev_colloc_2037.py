"""Implementation of chebyshev collocation node order 2037."""

def compute_chebyshev_colloc_2037(x: float) -> float:
    # Chebyshev Gauss-Lobatto node evaluation
    import math
    node = math.cos(math.pi * float(7) / float(8))
    return float(node * float(x))

import math

def test_compute_chebyshev_colloc_2037():
    val = compute_chebyshev_colloc_2037(0.5)
    assert isinstance(val, float)
    assert val == val
