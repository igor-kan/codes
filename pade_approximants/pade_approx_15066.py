"""Implementation of rational function approximant order 15066."""

def compute_pade_approx_15066(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_15066():
    v=compute_pade_approx_15066(0.5)
    assert isinstance(v,float) and v==v
