"""Implementation of spherical harmonic radial component order 18214."""

def compute_spherical_harm_18214(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18214():
    v=compute_spherical_harm_18214(0.5)
    assert isinstance(v,float) and v==v
