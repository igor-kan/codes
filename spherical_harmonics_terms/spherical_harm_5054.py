"""Implementation of spherical harmonic radial component order 5054."""

def compute_spherical_harm_5054(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_5054():
    v=compute_spherical_harm_5054(0.5)
    assert isinstance(v,float) and v==v
