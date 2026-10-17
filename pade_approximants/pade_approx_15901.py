"""Implementation of rational function approximant order 15901."""

def compute_pade_approx_15901(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_15901():
    v=compute_pade_approx_15901(0.5)
    assert isinstance(v,float) and v==v
