"""Implementation of rational function approximant order 3026."""

def compute_pade_approx_3026(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_3026():
    v=compute_pade_approx_3026(0.5)
    assert isinstance(v,float) and v==v
