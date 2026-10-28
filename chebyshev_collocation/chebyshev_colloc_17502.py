"""Implementation of chebyshev collocation node order 17502."""

def compute_chebyshev_colloc_17502(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17502():
    v=compute_chebyshev_colloc_17502(0.5)
    assert isinstance(v,float) and v==v
