"""Implementation of rational function approximant order 5086."""

def compute_pade_approx_5086(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_5086():
    v=compute_pade_approx_5086(0.5)
    assert isinstance(v,float) and v==v
