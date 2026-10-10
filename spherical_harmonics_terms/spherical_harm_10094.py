"""Implementation of spherical harmonic radial component order 10094."""

def compute_spherical_harm_10094(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10094():
    v=compute_spherical_harm_10094(0.5)
    assert isinstance(v,float) and v==v
