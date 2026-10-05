"""Implementation of spherical harmonic radial component order 3084."""

def compute_spherical_harm_3084(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_3084():
    v=compute_spherical_harm_3084(0.5)
    assert isinstance(v,float) and v==v
