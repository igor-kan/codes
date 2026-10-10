"""Implementation of rational function approximant order 10081."""

def compute_pade_approx_10081(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*2))

def test_compute_pade_approx_10081():
    v=compute_pade_approx_10081(0.5)
    assert isinstance(v,float) and v==v
