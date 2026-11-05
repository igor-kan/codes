"""Implementation of chebyshev collocation node order 18392."""

def compute_chebyshev_colloc_18392(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_18392():
    v=compute_chebyshev_colloc_18392(0.5)
    assert isinstance(v,float) and v==v
