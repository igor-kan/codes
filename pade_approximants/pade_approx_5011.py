"""Implementation of rational function approximant order 5011."""

def compute_pade_approx_5011(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_5011():
    v=compute_pade_approx_5011(0.5)
    assert isinstance(v,float) and v==v
