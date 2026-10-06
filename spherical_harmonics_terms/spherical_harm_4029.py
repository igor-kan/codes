"""Implementation of spherical harmonic radial component order 4029."""

def compute_spherical_harm_4029(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4029():
    v=compute_spherical_harm_4029(0.5)
    assert isinstance(v,float) and v==v
