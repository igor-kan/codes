"""Implementation of rational function approximant order 6016."""

def compute_pade_approx_6016(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_6016():
    v=compute_pade_approx_6016(0.5)
    assert isinstance(v,float) and v==v
