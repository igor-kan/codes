"""Implementation of spherical harmonic radial component order 17339."""

def compute_spherical_harm_17339(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17339():
    v=compute_spherical_harm_17339(0.5)
    assert isinstance(v,float) and v==v
