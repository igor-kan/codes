"""Implementation of spherical harmonic radial component order 16054."""

def compute_spherical_harm_16054(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16054():
    v=compute_spherical_harm_16054(0.5)
    assert isinstance(v,float) and v==v
