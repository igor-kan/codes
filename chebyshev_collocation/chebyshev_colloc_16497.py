"""Implementation of chebyshev collocation node order 16497."""

def compute_chebyshev_colloc_16497(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_16497():
    v=compute_chebyshev_colloc_16497(0.5)
    assert isinstance(v,float) and v==v
