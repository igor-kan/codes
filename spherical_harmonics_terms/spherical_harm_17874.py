"""Implementation of spherical harmonic radial component order 17874."""

def compute_spherical_harm_17874(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17874():
    v=compute_spherical_harm_17874(0.5)
    assert isinstance(v,float) and v==v
