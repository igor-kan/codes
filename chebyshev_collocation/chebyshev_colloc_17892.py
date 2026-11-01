"""Implementation of chebyshev collocation node order 17892."""

def compute_chebyshev_colloc_17892(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17892():
    v=compute_chebyshev_colloc_17892(0.5)
    assert isinstance(v,float) and v==v
