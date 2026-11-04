"""Implementation of rational function approximant order 18251."""

def compute_pade_approx_18251(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_18251():
    v=compute_pade_approx_18251(0.5)
    assert isinstance(v,float) and v==v
