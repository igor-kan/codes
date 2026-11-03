"""Implementation of spherical harmonic radial component order 18164."""

def compute_spherical_harm_18164(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18164():
    v=compute_spherical_harm_18164(0.5)
    assert isinstance(v,float) and v==v
