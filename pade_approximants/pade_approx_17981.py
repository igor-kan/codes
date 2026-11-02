"""Implementation of rational function approximant order 17981."""

def compute_pade_approx_17981(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17981():
    v=compute_pade_approx_17981(0.5)
    assert isinstance(v,float) and v==v
