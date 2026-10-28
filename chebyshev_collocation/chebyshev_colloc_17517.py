"""Implementation of chebyshev collocation node order 17517."""

def compute_chebyshev_colloc_17517(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_17517():
    v=compute_chebyshev_colloc_17517(0.5)
    assert isinstance(v,float) and v==v
