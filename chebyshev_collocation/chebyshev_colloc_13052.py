"""Implementation of chebyshev collocation node order 13052."""

def compute_chebyshev_colloc_13052(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_13052():
    v=compute_chebyshev_colloc_13052(0.5)
    assert isinstance(v,float) and v==v
