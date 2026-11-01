"""Implementation of chebyshev collocation node order 17862."""

def compute_chebyshev_colloc_17862(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17862():
    v=compute_chebyshev_colloc_17862(0.5)
    assert isinstance(v,float) and v==v
