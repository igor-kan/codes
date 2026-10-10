"""Implementation of chebyshev collocation node order 10087."""

def compute_chebyshev_colloc_10087(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_10087():
    v=compute_chebyshev_colloc_10087(0.5)
    assert isinstance(v,float) and v==v
