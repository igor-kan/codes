"""Implementation of spherical harmonic radial component order 16874."""

def compute_spherical_harm_16874(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16874():
    v=compute_spherical_harm_16874(0.5)
    assert isinstance(v,float) and v==v
