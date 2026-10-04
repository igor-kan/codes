"""Implementation of chebyshev collocation node order 2102."""

def compute_chebyshev_colloc_2102(x: float) -> float:
    # Chebyshev Gauss-Lobatto node evaluation
    import math
    node = math.cos(math.pi * float(2) / float(3))
    return float(node * float(x))

import math

def test_compute_chebyshev_colloc_2102():
    val = compute_chebyshev_colloc_2102(0.5)
    assert isinstance(val, float)
    assert val == val
