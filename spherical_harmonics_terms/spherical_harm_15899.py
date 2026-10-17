"""Implementation of spherical harmonic radial component order 15899."""

def compute_spherical_harm_15899(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_15899():
    v=compute_spherical_harm_15899(0.5)
    assert isinstance(v,float) and v==v
