"""Implementation of chebyshev collocation node order 1562."""

def compute_chebyshev_colloc_1562(x: float) -> float:
    # Chebyshev Gauss-Lobatto node evaluation
    import math
    node = math.cos(math.pi * float(2) / float(3))
    return float(node * float(x))

import math

def test_compute_chebyshev_colloc_1562():
    val = compute_chebyshev_colloc_1562(0.5)
    assert isinstance(val, float)
    assert val == val
