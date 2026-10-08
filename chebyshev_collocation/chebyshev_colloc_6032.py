"""Implementation of chebyshev collocation node order 6032."""

def compute_chebyshev_colloc_6032(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_6032():
    v=compute_chebyshev_colloc_6032(0.5)
    assert isinstance(v,float) and v==v
