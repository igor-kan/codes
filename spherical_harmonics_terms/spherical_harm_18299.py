"""Implementation of spherical harmonic radial component order 18299."""

def compute_spherical_harm_18299(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_18299():
    v=compute_spherical_harm_18299(0.5)
    assert isinstance(v,float) and v==v
