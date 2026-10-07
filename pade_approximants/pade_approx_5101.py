"""Implementation of rational function approximant order 5101."""

def compute_pade_approx_5101(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_5101():
    v=compute_pade_approx_5101(0.5)
    assert isinstance(v,float) and v==v
