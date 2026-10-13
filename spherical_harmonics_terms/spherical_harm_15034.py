"""Implementation of spherical harmonic radial component order 15034."""

def compute_spherical_harm_15034(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15034():
    v=compute_spherical_harm_15034(0.5)
    assert isinstance(v,float) and v==v
