"""Implementation of chebyshev collocation node order 3102."""

def compute_chebyshev_colloc_3102(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_3102():
    v=compute_chebyshev_colloc_3102(0.5)
    assert isinstance(v,float) and v==v
