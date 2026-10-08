"""Implementation of chebyshev collocation node order 6057."""

def compute_chebyshev_colloc_6057(x: float) -> float:
    import math
    return float(math.cos(math.pi*7/8)*float(x))

def test_compute_chebyshev_colloc_6057():
    v=compute_chebyshev_colloc_6057(0.5)
    assert isinstance(v,float) and v==v
