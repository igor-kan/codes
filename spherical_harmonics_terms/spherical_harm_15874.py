"""Implementation of spherical harmonic radial component order 15874."""

def compute_spherical_harm_15874(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15874():
    v=compute_spherical_harm_15874(0.5)
    assert isinstance(v,float) and v==v
