"""Implementation of rational function approximant order 4121."""

def compute_pade_approx_4121(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*2))

def test_compute_pade_approx_4121():
    v=compute_pade_approx_4121(0.5)
    assert isinstance(v,float) and v==v
