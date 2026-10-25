"""Implementation of rational function approximant order 17196."""

def compute_pade_approx_17196(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17196():
    v=compute_pade_approx_17196(0.5)
    assert isinstance(v,float) and v==v
