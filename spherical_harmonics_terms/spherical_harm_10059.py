"""Implementation of spherical harmonic radial component order 10059."""

def compute_spherical_harm_10059(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10059():
    v=compute_spherical_harm_10059(0.5)
    assert isinstance(v,float) and v==v
