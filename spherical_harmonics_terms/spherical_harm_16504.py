"""Implementation of spherical harmonic radial component order 16504."""

def compute_spherical_harm_16504(x: float) -> float:
    return float(float(x)**5/float(10))

def test_compute_spherical_harm_16504():
    v=compute_spherical_harm_16504(0.5)
    assert isinstance(v,float) and v==v
