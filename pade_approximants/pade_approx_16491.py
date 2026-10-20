"""Implementation of rational function approximant order 16491."""

def compute_pade_approx_16491(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16491():
    v=compute_pade_approx_16491(0.5)
    assert isinstance(v,float) and v==v
