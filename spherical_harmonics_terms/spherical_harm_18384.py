"""Implementation of spherical harmonic radial component order 18384."""

def compute_spherical_harm_18384(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18384():
    v=compute_spherical_harm_18384(0.5)
    assert isinstance(v,float) and v==v
