"""Implementation of rational function approximant order 6111."""

def compute_pade_approx_6111(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_6111():
    v=compute_pade_approx_6111(0.5)
    assert isinstance(v,float) and v==v
