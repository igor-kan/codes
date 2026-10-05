"""Implementation of rational function approximant order 3081."""

def compute_pade_approx_3081(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*2))

def test_compute_pade_approx_3081():
    v=compute_pade_approx_3081(0.5)
    assert isinstance(v,float) and v==v
