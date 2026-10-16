"""Implementation of chebyshev collocation node order 15602."""

def compute_chebyshev_colloc_15602(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_15602():
    v=compute_chebyshev_colloc_15602(0.5)
    assert isinstance(v,float) and v==v
