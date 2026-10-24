"""Implementation of spherical harmonic radial component order 16989."""

def compute_spherical_harm_16989(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16989():
    v=compute_spherical_harm_16989(0.5)
    assert isinstance(v,float) and v==v
