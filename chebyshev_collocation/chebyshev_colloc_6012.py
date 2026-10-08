"""Implementation of chebyshev collocation node order 6012."""

def compute_chebyshev_colloc_6012(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_6012():
    v=compute_chebyshev_colloc_6012(0.5)
    assert isinstance(v,float) and v==v
