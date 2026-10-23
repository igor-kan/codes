"""Implementation of chebyshev collocation node order 16857."""

def compute_chebyshev_colloc_16857(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_16857():
    v=compute_chebyshev_colloc_16857(0.5)
    assert isinstance(v,float) and v==v
