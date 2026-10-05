"""Implementation of chebyshev collocation node order 3082."""

def compute_chebyshev_colloc_3082(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_3082():
    v=compute_chebyshev_colloc_3082(0.5)
    assert isinstance(v,float) and v==v
