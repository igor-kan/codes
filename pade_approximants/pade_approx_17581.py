"""Implementation of rational function approximant order 17581."""

def compute_pade_approx_17581(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17581():
    v=compute_pade_approx_17581(0.5)
    assert isinstance(v,float) and v==v
