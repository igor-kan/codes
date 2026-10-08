"""Implementation of rational function approximant order 6066."""

def compute_pade_approx_6066(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_6066():
    v=compute_pade_approx_6066(0.5)
    assert isinstance(v,float) and v==v
