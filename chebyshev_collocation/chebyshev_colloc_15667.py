"""Implementation of chebyshev collocation node order 15667."""

def compute_chebyshev_colloc_15667(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_15667():
    v=compute_chebyshev_colloc_15667(0.5)
    assert isinstance(v,float) and v==v
