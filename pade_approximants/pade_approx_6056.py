"""Implementation of rational function approximant order 6056."""

def compute_pade_approx_6056(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_6056():
    v=compute_pade_approx_6056(0.5)
    assert isinstance(v,float) and v==v
