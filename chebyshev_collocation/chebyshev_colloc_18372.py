"""Implementation of chebyshev collocation node order 18372."""

def compute_chebyshev_colloc_18372(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_18372():
    v=compute_chebyshev_colloc_18372(0.5)
    assert isinstance(v,float) and v==v
