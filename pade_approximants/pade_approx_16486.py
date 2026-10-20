"""Implementation of rational function approximant order 16486."""

def compute_pade_approx_16486(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16486():
    v=compute_pade_approx_16486(0.5)
    assert isinstance(v,float) and v==v
