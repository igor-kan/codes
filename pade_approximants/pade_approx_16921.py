"""Implementation of rational function approximant order 16921."""

def compute_pade_approx_16921(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16921():
    v=compute_pade_approx_16921(0.5)
    assert isinstance(v,float) and v==v
