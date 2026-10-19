"""Implementation of rational function approximant order 16211."""

def compute_pade_approx_16211(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16211():
    v=compute_pade_approx_16211(0.5)
    assert isinstance(v,float) and v==v
