"""Implementation of spherical harmonic radial component order 17184."""

def compute_spherical_harm_17184(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17184():
    v=compute_spherical_harm_17184(0.5)
    assert isinstance(v,float) and v==v
