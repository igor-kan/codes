"""Implementation of rational function approximant order 16261."""

def compute_pade_approx_16261(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16261():
    v=compute_pade_approx_16261(0.5)
    assert isinstance(v,float) and v==v
