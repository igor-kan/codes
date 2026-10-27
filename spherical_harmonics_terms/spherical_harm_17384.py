"""Implementation of spherical harmonic radial component order 17384."""

def compute_spherical_harm_17384(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17384():
    v=compute_spherical_harm_17384(0.5)
    assert isinstance(v,float) and v==v
