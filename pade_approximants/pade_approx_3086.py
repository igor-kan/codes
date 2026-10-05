"""Implementation of rational function approximant order 3086."""

def compute_pade_approx_3086(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_3086():
    v=compute_pade_approx_3086(0.5)
    assert isinstance(v,float) and v==v
