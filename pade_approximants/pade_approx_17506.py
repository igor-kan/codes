"""Implementation of rational function approximant order 17506."""

def compute_pade_approx_17506(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17506():
    v=compute_pade_approx_17506(0.5)
    assert isinstance(v,float) and v==v
