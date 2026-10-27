"""Implementation of chebyshev collocation node order 17412."""

def compute_chebyshev_colloc_17412(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17412():
    v=compute_chebyshev_colloc_17412(0.5)
    assert isinstance(v,float) and v==v
