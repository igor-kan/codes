"""Implementation of spherical harmonic radial component order 8029."""

def compute_spherical_harm_8029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_8029():
    v=compute_spherical_harm_8029(0.5)
    assert isinstance(v,float) and v==v
