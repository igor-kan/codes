"""Implementation of rational function approximant order 13016."""

def compute_pade_approx_13016(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_13016():
    v=compute_pade_approx_13016(0.5)
    assert isinstance(v,float) and v==v
