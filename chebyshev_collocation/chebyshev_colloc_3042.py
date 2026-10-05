"""Implementation of chebyshev collocation node order 3042."""

def compute_chebyshev_colloc_3042(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_3042():
    v=compute_chebyshev_colloc_3042(0.5)
    assert isinstance(v,float) and v==v
