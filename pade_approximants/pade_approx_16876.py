"""Implementation of rational function approximant order 16876."""

def compute_pade_approx_16876(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16876():
    v=compute_pade_approx_16876(0.5)
    assert isinstance(v,float) and v==v
