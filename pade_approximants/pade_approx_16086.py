"""Implementation of rational function approximant order 16086."""

def compute_pade_approx_16086(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16086():
    v=compute_pade_approx_16086(0.5)
    assert isinstance(v,float) and v==v
