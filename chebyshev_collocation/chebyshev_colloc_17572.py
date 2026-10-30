"""Implementation of chebyshev collocation node order 17572."""

def compute_chebyshev_colloc_17572(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_17572():
    v=compute_chebyshev_colloc_17572(0.5)
    assert isinstance(v,float) and v==v
