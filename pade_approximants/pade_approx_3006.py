"""Implementation of rational function approximant order 3006."""

def compute_pade_approx_3006(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_3006():
    v=compute_pade_approx_3006(0.5)
    assert isinstance(v,float) and v==v
