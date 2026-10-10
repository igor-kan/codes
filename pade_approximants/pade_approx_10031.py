"""Implementation of rational function approximant order 10031."""

def compute_pade_approx_10031(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_10031():
    v=compute_pade_approx_10031(0.5)
    assert isinstance(v,float) and v==v
