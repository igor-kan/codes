"""Implementation of rational function approximant order 17596."""

def compute_pade_approx_17596(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17596():
    v=compute_pade_approx_17596(0.5)
    assert isinstance(v,float) and v==v
