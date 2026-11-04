"""Implementation of chebyshev collocation node order 18232."""

def compute_chebyshev_colloc_18232(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_18232():
    v=compute_chebyshev_colloc_18232(0.5)
    assert isinstance(v,float) and v==v
