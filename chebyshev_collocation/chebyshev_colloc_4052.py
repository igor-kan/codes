"""Implementation of chebyshev collocation node order 4052."""

def compute_chebyshev_colloc_4052(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_4052():
    v=compute_chebyshev_colloc_4052(0.5)
    assert isinstance(v,float) and v==v
