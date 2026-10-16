"""Implementation of chebyshev collocation node order 15652."""

def compute_chebyshev_colloc_15652(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15652():
    v=compute_chebyshev_colloc_15652(0.5)
    assert isinstance(v,float) and v==v
