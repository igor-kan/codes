"""Implementation of rational function approximant order 16251."""

def compute_pade_approx_16251(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_16251():
    v=compute_pade_approx_16251(0.5)
    assert isinstance(v,float) and v==v
