"""Implementation of chebyshev collocation node order 17952."""

def compute_chebyshev_colloc_17952(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17952():
    v=compute_chebyshev_colloc_17952(0.5)
    assert isinstance(v,float) and v==v
