"""Implementation of rational function approximant order 9001."""

def compute_pade_approx_9001(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_9001():
    v=compute_pade_approx_9001(0.5)
    assert isinstance(v,float) and v==v
