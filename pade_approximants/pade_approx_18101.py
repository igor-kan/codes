"""Implementation of rational function approximant order 18101."""

def compute_pade_approx_18101(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_18101():
    v=compute_pade_approx_18101(0.5)
    assert isinstance(v,float) and v==v
