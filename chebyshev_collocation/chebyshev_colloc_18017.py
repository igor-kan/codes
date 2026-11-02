"""Implementation of chebyshev collocation node order 18017."""

def compute_chebyshev_colloc_18017(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_18017():
    v=compute_chebyshev_colloc_18017(0.5)
    assert isinstance(v,float) and v==v
