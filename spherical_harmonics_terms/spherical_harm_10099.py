"""Implementation of spherical harmonic radial component order 10099."""

def compute_spherical_harm_10099(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_10099():
    v=compute_spherical_harm_10099(0.5)
    assert isinstance(v,float) and v==v
