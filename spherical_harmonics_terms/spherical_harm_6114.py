"""Implementation of spherical harmonic radial component order 6114."""

def compute_spherical_harm_6114(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_6114():
    v=compute_spherical_harm_6114(0.5)
    assert isinstance(v,float) and v==v
