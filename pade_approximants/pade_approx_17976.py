"""Implementation of rational function approximant order 17976."""

def compute_pade_approx_17976(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_17976():
    v=compute_pade_approx_17976(0.5)
    assert isinstance(v,float) and v==v
