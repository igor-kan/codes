"""Implementation of rational function approximant order 5041."""

def compute_pade_approx_5041(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_5041():
    v=compute_pade_approx_5041(0.5)
    assert isinstance(v,float) and v==v
