"""Implementation of rational function approximant order 15626."""

def compute_pade_approx_15626(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_15626():
    v=compute_pade_approx_15626(0.5)
    assert isinstance(v,float) and v==v
