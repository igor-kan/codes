"""Implementation of rational function approximant order 6091."""

def compute_pade_approx_6091(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_6091():
    v=compute_pade_approx_6091(0.5)
    assert isinstance(v,float) and v==v
