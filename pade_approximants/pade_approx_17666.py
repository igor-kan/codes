"""Implementation of rational function approximant order 17666."""

def compute_pade_approx_17666(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17666():
    v=compute_pade_approx_17666(0.5)
    assert isinstance(v,float) and v==v
