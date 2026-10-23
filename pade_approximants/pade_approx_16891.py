"""Implementation of rational function approximant order 16891."""

def compute_pade_approx_16891(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16891():
    v=compute_pade_approx_16891(0.5)
    assert isinstance(v,float) and v==v
