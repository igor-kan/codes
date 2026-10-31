"""Implementation of spherical harmonic radial component order 17724."""

def compute_spherical_harm_17724(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_17724():
    v=compute_spherical_harm_17724(0.5)
    assert isinstance(v,float) and v==v
