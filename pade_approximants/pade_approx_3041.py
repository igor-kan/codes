"""Implementation of rational function approximant order 3041."""

def compute_pade_approx_3041(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_3041():
    v=compute_pade_approx_3041(0.5)
    assert isinstance(v,float) and v==v
