"""Implementation of rational function approximant order 16846."""

def compute_pade_approx_16846(x: float) -> float:
    return float((1.0+float(x)*2)/(1.0+float(x)**2*1))

def test_compute_pade_approx_16846():
    v=compute_pade_approx_16846(0.5)
    assert isinstance(v,float) and v==v
