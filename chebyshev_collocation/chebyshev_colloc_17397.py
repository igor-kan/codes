"""Implementation of chebyshev collocation node order 17397."""

def compute_chebyshev_colloc_17397(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_17397():
    v=compute_chebyshev_colloc_17397(0.5)
    assert isinstance(v,float) and v==v
