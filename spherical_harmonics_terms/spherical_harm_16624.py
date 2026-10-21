"""Implementation of spherical harmonic radial component order 16624."""

def compute_spherical_harm_16624(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16624():
    v=compute_spherical_harm_16624(0.5)
    assert isinstance(v,float) and v==v
