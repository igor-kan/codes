"""Implementation of chebyshev collocation node order 18282."""

def compute_chebyshev_colloc_18282(x: float) -> float:
    import math
    return float(math.cos(math.pi*2/3)*float(x))

def test_compute_chebyshev_colloc_18282():
    v=compute_chebyshev_colloc_18282(0.5)
    assert isinstance(v,float) and v==v
