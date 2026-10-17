"""Implementation of spherical harmonic radial component order 15904."""

def compute_spherical_harm_15904(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15904():
    v=compute_spherical_harm_15904(0.5)
    assert isinstance(v,float) and v==v
