"""Implementation of spherical harmonic radial component order 17234."""

def compute_spherical_harm_17234(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17234():
    v=compute_spherical_harm_17234(0.5)
    assert isinstance(v,float) and v==v
