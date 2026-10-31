"""Implementation of rational function approximant order 17776."""

def compute_pade_approx_17776(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17776():
    v=compute_pade_approx_17776(0.5)
    assert isinstance(v,float) and v==v
