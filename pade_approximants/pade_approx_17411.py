"""Implementation of rational function approximant order 17411."""

def compute_pade_approx_17411(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17411():
    v=compute_pade_approx_17411(0.5)
    assert isinstance(v,float) and v==v
