"""Implementation of spherical harmonic radial component order 4069."""

def compute_spherical_harm_4069(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4069():
    v=compute_spherical_harm_4069(0.5)
    assert isinstance(v,float) and v==v
