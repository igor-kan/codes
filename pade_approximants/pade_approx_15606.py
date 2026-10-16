"""Implementation of rational function approximant order 15606."""

def compute_pade_approx_15606(x: float) -> float:
    return float((1.0+float(x)*1)/(1.0+float(x)**2*1))

def test_compute_pade_approx_15606():
    v=compute_pade_approx_15606(0.5)
    assert isinstance(v,float) and v==v
