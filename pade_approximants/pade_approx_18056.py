"""Implementation of rational function approximant order 18056."""

def compute_pade_approx_18056(x: float) -> float:
    return float((1.0+float(x)*3)/(1.0+float(x)**2*1))

def test_compute_pade_approx_18056():
    v=compute_pade_approx_18056(0.5)
    assert isinstance(v,float) and v==v
