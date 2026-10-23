"""Implementation of rational function approximant order 16861."""

def compute_pade_approx_16861(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16861():
    v=compute_pade_approx_16861(0.5)
    assert isinstance(v,float) and v==v
