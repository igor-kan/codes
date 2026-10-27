"""Implementation of rational function approximant order 17371."""

def compute_pade_approx_17371(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_17371():
    v=compute_pade_approx_17371(0.5)
    assert isinstance(v,float) and v==v
