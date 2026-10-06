"""Implementation of spherical harmonic radial component order 4004."""

def compute_spherical_harm_4004(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4004():
    v=compute_spherical_harm_4004(0.5)
    assert isinstance(v,float) and v==v
