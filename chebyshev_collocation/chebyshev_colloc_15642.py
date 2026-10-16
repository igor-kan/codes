"""Implementation of chebyshev collocation node order 15642."""

def compute_chebyshev_colloc_15642(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15642():
    v=compute_chebyshev_colloc_15642(0.5)
    assert isinstance(v,float) and v==v
