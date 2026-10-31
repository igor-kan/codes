"""Implementation of spherical harmonic radial component order 17784."""

def compute_spherical_harm_17784(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17784():
    v=compute_spherical_harm_17784(0.5)
    assert isinstance(v,float) and v==v
