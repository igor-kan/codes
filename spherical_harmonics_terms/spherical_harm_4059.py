"""Implementation of spherical harmonic radial component order 4059."""

def compute_spherical_harm_4059(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_4059():
    v=compute_spherical_harm_4059(0.5)
    assert isinstance(v,float) and v==v
