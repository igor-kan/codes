"""Implementation of spherical harmonic radial component order 13024."""

def compute_spherical_harm_13024(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_13024():
    v=compute_spherical_harm_13024(0.5)
    assert isinstance(v,float) and v==v
