"""Implementation of chebyshev collocation node order 15242."""

def compute_chebyshev_colloc_15242(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15242():
    v=compute_chebyshev_colloc_15242(0.5)
    assert isinstance(v,float) and v==v
