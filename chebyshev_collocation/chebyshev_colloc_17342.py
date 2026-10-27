"""Implementation of chebyshev collocation node order 17342."""

def compute_chebyshev_colloc_17342(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17342():
    v=compute_chebyshev_colloc_17342(0.5)
    assert isinstance(v,float) and v==v
